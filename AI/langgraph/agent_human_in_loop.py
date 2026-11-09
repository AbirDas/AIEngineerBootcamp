import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages

from langgraph.graph import StateGraph, END

from langchain_core.tools import tool
from langchain_tavily import TavilySearch

import json
from langchain_core.messages import ToolMessage
from langgraph.prebuilt import ToolNode, tools_condition

from langgraph.checkpoint.memory import MemorySaver


path_root = str(Path(__file__).resolve().parent.parent.parent)
path_env = path_root + "\\.venv\\.env"

load_dotenv(path_env)
tavily_api_key = os.getenv("TAVILY_API_KEY")

model_name = "llama3.2"
model = ChatOllama(model=model_name)

class State(TypedDict):
    # Messages have the type "list". The `add_messages` function
    # in the annotation defines how this state key should be updated
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages : Annotated[list, add_messages]
    

graph_builder = StateGraph(State)


# Create tools
# 1. Initialize the underlying base tool with your configurations
tavily_tool = TavilySearch(
    max_results=2,
    topic="general"
    )

# 2. Create a wrapper tool that filters out empty strings and invalid formats
@tool
def safe_tavily_search(query: str, **kwargs) -> str:
    """Search the web for up-to-date information, news, and research data."""
    
    # Clean the arguments: Remove anything that is an empty string ('') or 'null'
    sanitized_kwargs = {
        k: v for k, v in kwargs.items()
        if v not in ["", "null", None]
    }
    
    # Handle LLMs passing booleans as strings (e.g., 'false' -> False)
    if "include_images" in sanitized_kwargs:
        val = str(sanitized_kwargs["include_images"]).lower()
        sanitized_kwargs["include_images"] = val == "true"
        
    # Re-inject the query along with the safe, filtered keyword arguments
    sanitized_kwargs["query"] = query
    
    return tavily_tool.invoke(sanitized_kwargs)

tools = [safe_tavily_search]

model_with_tools = model.bind_tools(tools=tools)

# Below, implement a BasicToolNode that checks the most recent
# message in the state and calls tools if the message contains tool_calls

def bot(state: State):
    print(state["messages"])
    return {"messages" : [model_with_tools.invoke(state["messages"])]}

# instantiate the ToolNode with the tools
tool_node = ToolNode(tools=tools)
graph_builder.add_node("tools", tool_node) # Add the node to the graph

# The `tools_condition` function returns "tools" if the chatbot asks to use a tool, and "__end__" if
# it is fine directly responding. This conditional routing defines the main agent loop.
graph_builder.add_conditional_edges(
    "bot",
    tools_condition
)

# The first argument is the unique node name
# The second argument is the function or object that will be called whenever
# the node is used.
graph_builder.add_node("bot", bot)

# STEP 3: Add an entry point to the graph
graph_builder.set_entry_point("bot")

# ADD MEMORY NODE
memory = MemorySaver()

# STEP 5: Compile the graph
graph = graph_builder.compile(
    checkpointer=memory,
    interrupt_before=["tools"]
)

# MEMORY CODE CONTINUES ===
# Now we can run the chatbot and see how it behaves
# PICK A TRHEAD FIRST
config = {
    "configurable" : {"thread_id" : 1}
} # a thread where the agent will dump its memory to

user_input = "I'm learning about astrology. Could you do some research on it for me?"

# The config is the **second positional argument** to stream() or invoke()!
events = graph.stream(
    {"messages":[("user", user_input)]},
    config=config,
    stream_mode="values"
)

for event in events:
    event["messages"][-1].pretty_print()
    
# inspect the state
print("*" * 10)
snapshot = graph.get_state(config=config)
next_step = snapshot.next

# this will show "action", because we've interrupted the flow before the tools node
print(
    "===>>>", next_step
)  # this will show "action", because we've interrupted the flow before the tools node

existing_message = snapshot.values["messages"][-1]
all_tools = existing_message.tool_calls

print()
print("tools to be called::", all_tools)

# Continue the conversation passing None to say continue - all is good
# `None` will append nothing new to the current state, letting it resume as if it had never been interrupted
events = graph.stream(
    None,
    config=config,
    stream_mode="values"
)
for event in events:
    if "messages" in event:
        event["messages"][-1].pretty_print()
        print("****End****\n")
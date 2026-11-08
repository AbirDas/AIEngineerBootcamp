import os
from dotenv import load_dotenv
from pathlib import Path
from langchain_ollama import ChatOllama
from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, END
from langchain_community.tools.tavily_search import TavilySearchResults

import json
from langchain_core.messages import ToolMessage
from langgraph.prebuilt import ToolNode, tools_condition

from langgraph.checkpoint.memory import MemorySaver


path_root = str(Path(__file__).resolve().parent.parent.parent)
path_env = path_root + "\\.venv\\.env"
# Load environment variables from .env file
load_dotenv(path_env)

tavily_api_key = os.getenv("TAVILY_API_KEY")

llm_name = "llama3.2"
model = ChatOllama(model=llm_name)

class State(TypedDict):
    # Messages have the type "list". The `add_messages` function
    # in the annotation defines how this state key should be updated
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages : Annotated[list, add_messages]
    

graph_builder = StateGraph(State)

#Create Tools
tool = TavilySearchResults(max_results=2)
tools = [tool]

model_with_tools = model.bind_tools(tools)

# Below, implement a BasicToolNode that checks the most recent
# message in the state and calls tools if the message contains tool_calls

def bot(state: State):
    print(state["messages"])
    return {"messages" : [model_with_tools.invoke(state["messages"])]}


# instantiate the ToolNode with the tools
tool_node = ToolNode(tools=[tool])
graph_builder.add_node("tools", tool_node) # Add the node to the graph

# The `tools_condition` function returns "tools" if the chatbot asks to use a tool, and "__end__" if
# it is fine directly responding. This conditional routing defines the main agent loop.
graph_builder.add_conditional_edges(
    "bot",
    tools_condition,
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
    checkpointer=memory
)

# MEMORY CODE CONTINUES ===
# Now we can run the chatbot and see how it behaves
# PICK A TRHEAD FIRST

config = {
    "configurable": {"thread_id": 1}
} # a thread where the agent will dump its memory to

user_input = "Hi there! My name is Bond. and I have been happy for 100 years"

# The config is the **second positional argument** to stream() or invoke()!
events = graph.stream(
    {"messages": [("user", user_input)]},
    config=config,
    stream_mode="values"
)

for event in events:
    event["messages"][-1].pretty_print()
    
#second input from user to check memory
user_input = "do you remember my name, and how long have I been happy for?"

# The config is the **second positional argument** to stream() or invoke()!
events = graph.stream(
    {"messages": [("user", user_input)]}, config, stream_mode="values"
)

for event in events:
    event["messages"][-1].pretty_print()


snapshot = graph.get_state(config)
print(snapshot)
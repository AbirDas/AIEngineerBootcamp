import json
from typing import Dict, List
from openai import OpenAI
import sys
from dotenv import load_dotenv

# Add path to get the .env file inside virtual-environment .venv
load_dotenv()

def initialize_client(use_ollama: bool = True) -> OpenAI:
    """Initialize the OpenAI client for either OpenAI or OLLAMA."""
    if use_ollama:
        return OpenAI(
            base_url="http://localhost:11434/v1/",
            api_key="ollama"
        )
    # load api key from .env file and pass here to use openai. check no_memory.py file for more detail info
    return OpenAI()


def create_initial_message() -> List[Dict[str, str]]:
    """Create the initial messages for the context memory."""
    return [
        {"role" : "system",
         "content" : "you are a helpful assistant."}
    ]

    
def chat(
    user_input: str,
    message: List[Dict[str, str]],
    client: OpenAI,
    model_name: str
) -> str:
    """Handle user input and generate responses"""
    # Append user message to the conversation
    message.append({"role":"user",
                    "content": user_input})
    
    try:
        # Generate a response using the API
        response = client.chat.completions.create(
            model=model_name,
            messages=message
        )
        
        # Append assistant's response to the conversation
        assistant_response = response.choices[0].message.content
        message.append({"role":"system",
                        "content" : assistant_response})
        
        return assistant_response
    except Exception as e:
        return f"Error with API: {str(e)}"

  
def summarize_message(message: List[Dict[str, str]]) -> List[Dict[str,str]]:
    """ Summarize older message to save tokens """
    summary = "Previous conversation summarized: " + " ".join(
        [m["content"][:50] + "..." for m in message[-5:]]
    )
    
    return [{"role":"system", "content" : summary}] + message[-5:]


def  save_conversation(
    messages: List[Dict[str,str]],
    file_name: str = "context_memory.json"
):
    """ Save conversation to a file """
    with open(file_name,"w") as file:
        json.dump(messages, file)
        

def load_conversation(file_name: str = "context_memory.json") -> List[Dict[str,str]]:
    """ Load conversation from a file """
    try:
        with open(file_name, "r") as file:
            return json.load(file)
        
    except Exception as e:
        print(f"Error encounter during loading conversation : {str(e)}")
        return create_initial_message()
    
def main():
    # MOdel selection
    print("Select model typer:")
    print("1. OpenAI GPT-5 (cost to token)")
    print("2. Ollama llama3.2 (local)")
    
    choice = input("Enter choice (1 & 2): ").strip()
    if choice not in ["1", "2"]:
        while True:
            print("Wrong choice input can only be either '1' or '2'")
            choice = input("Enter choice (1 & 2): ").strip()
            if choice in ['1','2']:
                break
            
    use_ollama = (choice == "2")
    
    # Initialize client and model name
    client = initialize_client(use_ollama=use_ollama)
    model_name = "llama3.2" if use_ollama else "gpt-5-nano"
    
    # Initialize or load conversation
    message = create_initial_message()
    
    print(f"\nUsing {'Ollama' if use_ollama else 'OpenAI'} LLM.")
    print("Type 'quit' or 'exit' to come out")
    print("Available commands:")
    print("- 'save': Save conversation")
    print("- 'load': Load conversation")
    print("- 'summary': Summarize conversation")
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ['quit','exit','stop']:
            break
        elif user_input.lower() == "save":
            save_conversation(messages=message)
            print("Conversation saved!")
            continue
        elif user_input.lower() == "load":
            message = load_conversation()
            print("Conversation loaded!")
            continue
        elif user_input.lower() == "summary":
            message = summarize_message(message=message)
            print("\n(Conversation automatically summarized)")
            continue
        
        response = chat(user_input, message, client, model_name)
        print(f"\nAssistant: {response}")
        
        # Automatically summarize if conversation gets too long
        if len(message) > 10:
            message = summarize_message(message)
            print(f"\n (Conversation automatically summarized): {message}")
            

# Example usage
if __name__ == "__main__":
    print("going to call main method")
    main()
    
print(__name__)
            
from transformers import pipeline, AutoTokenizer

def create_simple_llm(model_name = "distilgpt2"):
    """
    Creates a simple LLM using a small GPT-2 model.
    GPT-2 (smallest version) is perfect for demonstrations as it's:
    - Relatively small (124M parameters)
    - Fast enough to run on CPU
    - Good for understanding basic concepts
    """
    
    #Initialize the model and tokenizer
    #model_name = "distilgpt2" #using DistilGPT-2 (Smaller version od GPT-2)
    
    #Create the generator pipeline
    generator = pipeline('text-generation',
                         model=model_name,
                         pad_token_id=50256)
    
    return generator

# for default model calling
#generator = create_simple_llm()
#To swap DistilGPT-2 for the modern Qwen2.5-0.5B model
generator = create_simple_llm(model_name="Qwen/Qwen2.5-0.5B-Instruct")

prompt = "I am learning GenAI and python, this is my first GenAI project suggest next"

# Generate text
generated_text = generator(prompt, max_length=200, num_return_sequences=1)

print(generated_text[0]['generated_text'])


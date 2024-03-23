from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def chatbot(input_text):
    # Load pre-trained model and tokenizer
    model_name = "HuggingFaceH4/zephyr-7b-beta"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Encode user input and generate response
    input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors="pt")
    bot_input_ids = torch.cat([input_ids, torch.zeros_like(input_ids)], dim=-1)
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    # Decode and return the bot's response
    bot_response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return bot_response

# Example usage
user_input = input("You: ")
while user_input.lower() != 'exit':
    bot_response = chatbot(user_input)
    print("Bot:", bot_response)
    user_input = input("You: ")

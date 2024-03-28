from transformers import BartTokenizer, BartForConditionalGeneration
import logging

logging.getLogger("transformers").setLevel(logging.ERROR)
# Load the pre-trained BART model and tokenizer
model_name = "facebook/bart-base"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

# Simulated chat between the user and the assistant
chat_history = [
    "User: Hey, can you help me with something?",
    "Assistant: Of course! What can I assist you with?",
    "User: I'm trying to understand how to use the BART model for text summarization.",
    "Assistant: Great! BART is a powerful model for text summarization. It's based on a transformer architecture and can generate high-quality summaries of long text passages.",
    "User: That sounds interesting. How can I get started with using BART?",
    "Assistant: To get started with BART, you can use the Hugging Face Transformers library in Python. It provides an easy-to-use interface for loading pre-trained BART models and applying them to your own text data.",
    "User: Can you show me a quick example of how to use BART for summarization?",
    "Assistant: Certainly! Here's a simple example of how to use BART for summarization using the Transformers library:",
    "```python",
    "from transformers import BartTokenizer, BartForConditionalGeneration",
    "tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')",
    "model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')",
    "text = 'Your long text passage goes here.'",
    "inputs = tokenizer(text, return_tensors='pt', max_length=1024, truncation=True)",
    "summary_ids = model.generate(inputs['input_ids'], num_beams=4, max_length=100, early_stopping=True)",
    "summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)",
    "print(summary)",
    "```",
    "User: That's really helpful! Thanks for the explanation and example.",
    "Assistant: You're welcome! Let me know if you have any more questions while working with BART. I'm here to help!"
]

# Convert the chat history into a single string
chat_text = "\n".join(chat_history)

# Tokenize the chat text
inputs = tokenizer(chat_text, return_tensors="pt", max_length=1024, truncation=True)

# Generate the summary
summary_ids = model.generate(inputs["input_ids"], num_beams=4, max_length=100, early_stopping=True)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print("Chat Summary:")
print(summary)

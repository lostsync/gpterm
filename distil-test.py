from transformers import BartTokenizer, BartForConditionalGeneration
import logging

logging.getLogger("transformers").setLevel(logging.ERROR)
model_name = "sshleifer/distilbart-cnn-12-6"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

chat_history = [
    "User: Hey, can you help me with something?",
    "Assistant: Of course! What can I assist you with?",
    "User: I'm trying to understand how to use the T5 model for text summarization.",
    "Assistant: Great! T5 is a versatile model that can be used for various natural language processing tasks, including text summarization. It's known for its efficiency and good performance.",
    "User: That sounds interesting. How can I get started with using T5?",
    "Assistant: To get started with T5, you can use the Hugging Face Transformers library in Python. It provides an easy-to-use interface for loading pre-trained T5 models and applying them to your own text data.",
    "User: Can you show me a quick example of how to use T5 for summarization?",
    "Assistant: Certainly! Here's a simple example of how to use T5 for summarization using the Transformers library:",
    "```python",
    "from transformers import T5Tokenizer, T5ForConditionalGeneration",
    "tokenizer = T5Tokenizer.from_pretrained('t5-small')",
    "model = T5ForConditionalGeneration.from_pretrained('t5-small')",
    "text = 'Your long text passage goes here.'",
    "inputs = tokenizer.encode('summarize: ' + text, return_tensors='pt', max_length=512, truncation=True)",
    "summary_ids = model.generate(inputs, max_length=150, num_beams=4, early_stopping=True)",
    "summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)",
    "print(summary)",
    "```",
    "User: That's really helpful! Thanks for the explanation and example.",
    "Assistant: You're welcome! Let me know if you have any more questions while working with T5. I'm here to help!"
]

# Concatenate the chat history into a single string
conversation = " ".join(chat_history)

# Encode the conversation and generate the summary
inputs = tokenizer.encode("summarize: " + conversation, return_tensors="pt", max_length=1024, truncation=True)
summary_ids = model.generate(inputs, max_length=150, num_beams=4, early_stopping=True)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print("Conversation Summary:")
print(summary)

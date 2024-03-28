from transformers import T5Tokenizer, T5ForConditionalGeneration
import logging

logging.getLogger("transformers").setLevel(logging.ERROR)

model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name, legacy=False)
model = T5ForConditionalGeneration.from_pretrained(model_name)

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

# Summarize the conversation parts separately
summary_prompts = [
    "summarize the main points discussed about project updates: ",
    "provide a brief overview of the key topics covered in the budget review: ",
    "summarize the discussion on team assignments: "
]

summaries = []
for prompt in summary_prompts:
    conversation_part = " ".join(chat_history[summary_prompts.index(prompt)*2 : (summary_prompts.index(prompt)+1)*2 + 1])
    inputs = tokenizer.encode(prompt + conversation_part, return_tensors="pt", max_length=256, truncation=False)
    summary_ids = model.generate(inputs, max_length=100, num_beams=2, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    summaries.append(summary)

# Combine the individual summaries
overall_summary = "\n\n".join(summaries)

print("Conversation Summary:")
print(overall_summary)

import os
from openai import OpenAI 

api_key = os.gateway("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

MODEL =
MAX_TOKENS = 100

def chat(user_input):
    response = client.chat.completions.create(
        model="gpt-4o",    model= MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hey there boss! How can I hep?"}
        ],

        max_tokens=MAX_TOKENS
    )
    reply = response.choices[0].message.content

    return reply

#print(chat("Hello, how are you?"))
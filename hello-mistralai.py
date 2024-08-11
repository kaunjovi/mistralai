import os
from mistralai import Mistral

api_key = "ncWiVFAsjhAs7UD5USXp2eI4KuhooONj"
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "user",
            "content": "Is AI any good?",
        },
    ]
)
print(chat_response.choices[0].message.content)
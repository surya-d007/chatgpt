

!pip install openai

from openai import OpenAI

api_key = "key"  # Replace "your_api_key_here" with your actual API key
client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "give me python code foe running in google colab for the desition trees and visualize the trees "}
    ]
)

print(completion.choices[0].message.content)


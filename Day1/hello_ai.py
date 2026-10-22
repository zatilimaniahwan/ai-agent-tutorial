from openai import OpenAI
from constant import BASE_URL,API_KEY,MODEL

client = OpenAI(base_url=BASE_URL,api_key=API_KEY)
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": "What is machine learning?"
        }
    ]
)
print(response.choices[0].message.content)
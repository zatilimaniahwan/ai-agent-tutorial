from openai import OpenAI
from utils.constant import BASE_URL,API_KEY,MODEL

def main() -> None:
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

if __name__ == "__main__":
    main()

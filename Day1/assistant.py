from openai import OpenAI
from constant import MODEL,BASE_URL,API_KEY

print("=" *40)
print("My AI Assistant")
print("=" *40)

while True:
    user_input = input("\nYou:")
    if user_input.lower() == "quit" or user_input.lower() == "exit":
        print("\nAI:Goodbye! Have a great day.")
        break
    client = OpenAI(base_url=BASE_URL,api_key=API_KEY)
    response = client.chat.completions.create(
    model=MODEL,
    messages =[
        {
            "role": "user",
            "content": user_input
        }
    ]
    )
    print("\nAI:", response.choices[0].message.content)
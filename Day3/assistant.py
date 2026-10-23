from openai import OpenAI
from utils.constant import MODEL,BASE_URL,API_KEY
from typing import List

def get_role():
    roles = ["1. Teacher", "2. Python Expert", "3. Travel Guider"]
    for role in roles:
        print(f"{role}\n")

def main()->None:
    print("=" *40)
    print("My AI Assistant")
    print("=" *40)
    get_role()
    choice = input("\nEnter your choice: ")
    roles={
        "1":"You are a friendly school teacher. Explain every concept using simple language and real life examples.",
        "2":"You are a senior Python developer. Explain programming concepts clearly and always include python examples.",
        "3": "You are an experienced travel guide. Recommend places, food, transportation and travel tips."
    }

    messages = [
        {
            "role": "system",
            "content": roles.get(choice, "You are a helpful AI Assistant!")
        }
    ]

    while True:
        user_input = input("\nYou: ")
        messages.append({
            "role": "user",
            "content": user_input
        })
        if user_input.lower() == "quit" or user_input.lower() == "exit":
            print("\nAI: Goodbye! Have a great day.")
            break
        client = OpenAI(base_url=BASE_URL,api_key=API_KEY)
        response = client.chat.completions.create(
            model=MODEL,
            messages =messages
        )
        assistant_response = response.choices[0].message.content
        print("\nAI:", assistant_response)
        messages.append({
            "role": "assistant",
            "content": assistant_response
        })


if __name__ == "__main__":
    main()
from openai import OpenAI
from utils.constant import MODEL,BASE_URL,API_KEY
from typing import List

def retrieve_conversation_history(messages:List):
    for message in messages:
        print(f"{message['role'].title()}:{message['content']}")
    return None


def main()->None:
    print("=" *40)
    print("My AI Assistant")
    print("=" *40)
    messages = []

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

        print("=" *40)
        print("Conversation History")
        print("=" *40)
        retrieve_conversation_history(messages)

if __name__ == "__main__":
    main()
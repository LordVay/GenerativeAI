import os
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.llms.google_genai import GoogleGenAI

llm = GoogleGenAI(
    model="gemini-2.5-flash",
    google_api_key= os.environ["GEMINI_API_KEY"],
    temperature = 0.1
)

def chat():
    chat_history = [
        ChatMessage(role=MessageRole.SYSTEM, content="You are a helpful assistant. Be concise and accurate")
    ]

    print("Llamaindex Chatbot. Type Exit to quit")

    while True:
        user = input("You: ").strip()

        if user .lower() == "exit":
            break

        chat_history.append(ChatMessage(role=MessageRole.USER, content=user))

        response = llm.chat(messages=chat_history)
        answer = response.message.content

        print(f"Bot: {answer}\n")

        chat_history.append(ChatMessage(role=MessageRole.ASSISTANT, content = answer))     

        print("-"*80)

chat()                       
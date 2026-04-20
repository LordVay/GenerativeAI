import os 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key= os.environ["GEMINI_API_KEY"],
    temperature = 0.1
)

parser = StrOutputParser()

def chat():
    chat_history = [
        ("system","You are a helpful chatbot. Be concise and accurate")
    ]

    print("Welcome to LangChain Chatbot. Type Exit to quit")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            break
        
        chat_history.append(("user", user_input))

        prompt = ChatPromptTemplate.from_messages(chat_history)
        chain = prompt | llm | parser

        response = chain.invoke({})

        print(f"Bot: {response}\n")

        chat_history.append(("assistant", response))

        print("-"*80)


chat()
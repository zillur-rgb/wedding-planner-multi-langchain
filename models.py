
from langchain_ollama import ChatOllama

openai_model = ChatOllama(
    model="llama3.2:3b",
    temperature=0,
)

response = openai_model.invoke("What is the color of the sky?")

print(response.content)
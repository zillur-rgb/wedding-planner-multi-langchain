
from langchain_ollama import ChatOllama

ollama_model = ChatOllama(
    model="llama3.2:3b",
    temperature=0,
)

response = ollama_model.invoke("What is the color of the sky?")

print(response.content)
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage
from models import ollama_model
from tools import search_web
import logging

#configure logging
logging.basicConfig(
    level=logging.INFO
)


#creating subagents
logging.info("Initializing Subagent1...")
subagent1 = create_agent(model=ollama_model, tools=[search_web], name="SubAgent1")
logging.info("Initializing Subagent2...")
subagent2 = create_agent(model=ollama_model, tools=[search_web], name="SubAgent2")

@tool
def delegate_to_subagent1(query: str) -> str:
    """Search the web for a given topic by delegating the task to SubAgent1 to do so"""
    logging.info(f"delegating query to Subagent 1: {query}")
    response = subagent1.invoke({"messages": [HumanMessage(content=query)]})
    return response["message"][-1].content

@tool
def delegate_to_subagent2(query: str) -> str:
    """Search the web for a given topic by delegating the task to SubAgent1 to do so"""
    logging.info(f"delegating query to Subagent 2: {query}")
    response = subagent2.invoke({"messages": [HumanMessage(content=query)]})
    return response["message"][-1].content
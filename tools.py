from langchain.tools import tool
from dotenv import load_dotenv
from tavily import TavilyClient
import logging

#configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

load_dotenv()
tavily_client = TavilyClient()

@tool
def search_web(topic: str) -> str:
    """Search the web for a give topic and return the results"""
    logging.info(f"Searching the web for topic: {topic}")
    return tavily_client.search(topic)
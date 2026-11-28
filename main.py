from dotenv import load_dotenv


load_dotenv()
#from typing import List
#from pydantic import BaseModel, Field

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from tavily import TavilyClient


tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Tool that searches over internet 
        Args: 
            query: The query to search for
        Return: 
            The search result
    """
    print(f"search for {query}")

    response = tavily.search(query=query)
    return str(response) 


llm = ChatOllama(temperature=0, model="gemma4:e2b")
#llm = ChatOpenAI(    model="gpt-5.6-terra",temperature=0)
tools = [search]
agent = create_agent(model=llm,tools=tools)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="What is the weather in Tokyo")})
    print(result)


if __name__ == "__main__":
    main()
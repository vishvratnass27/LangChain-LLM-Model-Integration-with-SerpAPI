# LangChain LLM Model Integration with SerpAPI

This repository demonstrates how to set up and use LangChain with OpenAI's LLM, SerpAPI for real-time search, and various tools and agents. It also explains the use of environment variables to securely manage API keys

# Features
Use OpenAI LLMs with LangChain.
Implement agents for planning and execution.
Integrate SerpAPI for real-time search capabilities.
Securely manage API keys using environment variables.
Create a functional chain with models, tools, and agents.

# Prerequisites
Python 3.8 or higher installed.
An OpenAI API Key and SerpAPI Key (sign up at OpenAI and SerpAPI).

# Install Dependencies
Run the following commands in your terminal:

pip install langchain
pip install langchain-openai
pip install langchain-community
pip install langchain-core
pip install langsmith
pip install langchain-text-splitters
pip install python-dotenv

# Create an .env File
To manage your secret keys securely, create a .env file in the project directory and add the following

llm_api_key=sk-your-openai-api-key
serpapi_api_key=your-serpapi-api-key

# Code Explanation
# Step 1: Load Environment Variables
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch OpenAI API Key securely
OpenAiApi_key = os.getenv("llm_api_key")

The dotenv library securely loads API keys from the .env file, preventing exposure of sensitive credentials

----------------------

# Step 2: Initialize OpenAI LLM

from langchain.llms import OpenAI

# Initialize the OpenAI LLM
model = OpenAI(openai_api_key=OpenAiApi_key)

# Test the model with a prompt
output = model(prompt="Tell me about India in 1 sentence", temperature=1)
print(output)

The OpenAI class from LangChain is used to create an instance of the model with the API key. You can modify the prompt and parameters like temperature for creativity

--------------------

# Step 3: Set Up an Agent
Agents in LangChain handle decision-making tasks like planning and executing actions.

from langchain.agents import AgentType

# Initialize an agent
myagent = AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION

The CHAT_ZERO_SHOT_REACT_DESCRIPTION agent type uses a reactive approach to execute tasks based on descriptions.

---------------------

# Step 4: Integrate SerpAPI for Real-Time Search
LangChain's SerpAPIWrapper allows the model to fetch real-time search results.

from langchain_community.utilities import SerpAPIWrapper

# Initialize the SerpAPI wrapper
Search = SerpAPIWrapper()

# Test the search functionality
Search.run("Who is Tony Stark in Marvel?")

This code integrates SerpAPI, which retrieves information unavailable to the LLM due to lack of web access.

-------------------

# Step 5: Load Tools
Tools are utilities for performing actions. Here, the serpapi tool is loaded.

from langchain.agents import load_tools

# Load tools including SerpAPI
mytools = load_tools(["serpapi"])


-------------------

# Step 6: Create a Chain
Chains combine models, agents, and tools to perform tasks cohesively.

from langchain.agents import initialize_agent

# Initialize the chain with a model, tools, and agent
google_search_chain = initialize_agent(
    agent="zero-shot-react-description", 
    tools=mytools, 
    llm=model, 
    verbose=True
)

# Run the chain with a prompt
output = google_search_chain.run("Who is Tony Stark in Marvel?")
print(output)

The initialize_agent function creates a seamless pipeline for combining the model, tools, and agent.

------------------


# Note
# Chain Composition
Model: Generates responses using OpenAI LLM.
Agent: Plans and manages execution of tasks.
Tools: Execute specific actions (e.g., SerpAPI for real-time search).

Chain = Model + Agent + Tools







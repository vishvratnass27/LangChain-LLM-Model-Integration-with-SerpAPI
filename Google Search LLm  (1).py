#!/usr/bin/env python
# coding: utf-8

# # LangChain-Based LLM Implementation with Tools and Search Capabilities

# Install these libraries using pip

# In[ ]:


pip install langchain


# In[ ]:


pip install langchain-openai


# In[ ]:


pip install langchain-community


# In[ ]:


pip install langchain-core


# In[ ]:


pip install langsmith


# In[ ]:


pip install langchain-text-splitters


# Setting Up API Keys
# 
# Using API keys in your code directly is not secure. Instead, we'll use a .env file to store sensitive data like the OpenAI API key.

# In[ ]:





# In[ ]:


OpenAiApi_key = "sk-xN_j5bJBwQw6EsTnMpB0xccEMLwsB3UqwkLlxpzGq1T3BlbkFJCKWG2SV009GUXwujq5DVR0IllVH38JulDEqtthFzkA"


# In[ ]:


#OpenAiApi_key ="sk-3wf2b9axht5Ec0fdDrliqRxi8mvVbKgnegclmiD4RCT3BlbkfJPQGdSl-0Awn1WzJT3No2aHVYHncj8lNK5ozzYCkbUA"


# create env file for that all secret keys because we need to use all the time this keys this not a good practice you show your secret keys 

# 1. Environment Setup and API Key Management
# 
# 

# In[ ]:


from dotenv import load_dotenv


# In[ ]:


load_dotenv()


# In[ ]:


import os 


# In[ ]:


OpenAiApi_key = os.getenv("llm_api_key")


# In[ ]:





# 2. Using LangChain's OpenAI LLM
# 
# The OpenAI class from LangChain is used to create a Language Model (LLM) with the OpenAI API key

# In[ ]:


from langchain.llms import OpenAI


# In[ ]:


model = OpenAI(openai_api_key=OpenAiApi_key)


# In[ ]:


output = model(prompt="tell me about india in 1 ",temperature=1 )


# In[ ]:


print(output)


# 3. Understanding Agents
# 
# Agents are responsible for thinking, planning, and executing tasks. Here, we use the CHAT_ZERO_SHOT_REACT_DESCRIPTION agent type.

# agent is use for that think and plan the all the thinks 

# In[ ]:


from langchain.agents import AgentType


# In[ ]:


myagent = AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION


# 4. Integrating SerpAPI for Real-Time Search
# 
# Since LLMs cannot fetch real-time data, we integrate SerpAPI to query a search engine.

# serpAPi is use for the real search engine because any llm model is not abole to take data from the serach engine thats way we need a SerpAPIWrapper

# In[ ]:


from langchain_community.utilities import SerpAPIWrapper


# In[ ]:


Search = SerpAPIWrapper()


# In[ ]:


Search.run("tell me who is tony stark in marvel")


# 5. Creating Tools
# 
# Tools are components that execute specific actions. In this case, we use SerpAPI as a tool.

# tools is use to execut or run the actions 

# In[ ]:


from langchain.agents import load_tools


# In[ ]:


mytools = load_tools(["serpapi"])


# 6. Combining Everything: Chains
#     
# A Chain is a combination of an LLM, an agent, and tools.

# Note :- Chain = Model + Agent + Tools

# In[ ]:


from langchain.agents import initialize_agent


# In[ ]:


google_search_chain = initialize_agent(agent= "zero-shot-react-description" , tools=mytools , llm=model , verbose=True)


# In[ ]:


google_search_chain


# In[ ]:


output = google_search_chain.run("tell me who is tony stark in marvel")


# In[ ]:


output 


# In[ ]:





# Key Components:
#     
# Model: Represents the Language Model (LLM) used for generating responses.
#     
# Agent: Thinks and plans actions based on input queries.
#     
# Tools: Executes actions (e.g., performing a search).
#     
# Chain: Combines the model, agent, and tools into a unified workflow.
# 

# In[ ]:





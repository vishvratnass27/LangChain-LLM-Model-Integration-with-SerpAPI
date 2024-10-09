#!/usr/bin/env python
# coding: utf-8

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


# In[ ]:


#OpenAiApi_key = "sk-xN_j5bJBwQw6EsTnMpB0xccEMLwsB3UqwkLlxpzGq1T3BlbkFJCKWG2SV009GUXwujq5DVR0IllVH38JulDEqtthFzkA"


# create env file for that all secret keys because we need to use all the time this keys this not a good practice you show your secret keys 

# In[ ]:


from dotenv import load_dotenv


# In[ ]:


load_dotenv()


# In[ ]:


import os 


# In[ ]:


OpenAiApi_key = os.getenv("llm_api_key")


# In[ ]:





# In[ ]:





# In[ ]:


from langchain.llms import OpenAI


# In[ ]:


model = OpenAI(openai_api_key=OpenAiApi_key)


# In[ ]:


output = model(prompt="tell me about india in 1 lines" , tempreture=1)


# In[ ]:


print(output)


# In[ ]:





# agent is use for that thik and plan the all the thinks 

# In[ ]:


from langchain.agents import AgentType


# In[ ]:


myagent = AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION


# In[ ]:





# serpAPi is use for the real search engine because any llm model is not abole to take data from the serach engine thats way we need a SerpAPIWrapper

# In[ ]:


from langchain_community.utilities import SerpAPIWrapper


# In[ ]:


Search = SerpAPIWrapper()


# In[ ]:


Search.run("tell me who is tony stark in marvel")


# In[ ]:





# tools is use to execut or run the actions 

# In[ ]:


from langchain.agents import load_tools


# In[ ]:


mytools = load_tools(["serpapi"])


# In[ ]:





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


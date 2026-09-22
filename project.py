import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI Assistant."),
    ("human", "Question: {Question}")
])

def generate_response(query,llm,temperature,max_tokens,api_key):
  model=ChatOpenAI(model_name=llm,temperature=temperature,openai_api_key=api_key,max_tokens=max_tokens)
  parser=StrOutputParser()
  chain= prompt| model|parser
  result=chain.invoke({'Question':query})
  return result

st.title("Q And A ChatBot with OpenAI")  
query=st.text_input("What's Your Query")
st.sidebar.title("Settings")

api=st.sidebar.text_input("Provide the API key ",type='password')

llm=st.sidebar.selectbox('Select the LLM:',['gpt-4-turbo','gpt-4o','o3'])

temperature=st.sidebar.slider("Select Temperature:",min_value=0.0,max_value=2.0,value=0.8)

max_tokens=st.sidebar.slider("Select Max Tokens:",min_value=50,max_value=200,value=100)

if st.button("Answer"):
  if query and api:
    response=generate_response(query,llm,temperature,max_tokens,api)
    st.write(response)
  else:
    st.warning("please Enter some query")
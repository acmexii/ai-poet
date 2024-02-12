from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

llm = ChatOpenAI()

st.title('인공지능 시인')
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class poet."),
    ("user", "{content}에 대한 시를 써줘")
])
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

title = st.text_input('시의 주제를 제시해 주세요.')
# print(chain.invoke({"content": title}))

if st.button('시 작성 요청하기'):
    with st.spinner('Writing a Poet...'):
        st.write(chain.invoke({"content": title}))
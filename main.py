import streamlit as st
# from langchain_helper import get_qa_chain, create_vector_db
import langchain_helper

st.title("AR-4U Q&A 💬")
btn = st.button("Create Knowledgebase")
if btn:
    langchain_helper.create_vector_db()

question = st.text_input("Question: ")

if question:
    chain = langchain_helper.get_qa_chain()
    response = chain(question)

    st.header("Answer")
    st.write(response["result"])







import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image(r"D:\Udemy\Python Mega Course Learn Python in 60 Days, Build 20 Apps\App2-portfolio\images\Photo.jpg")

with col2:
    st.title("Phan Hoang")
    content = """
    Xin chao moi nguoi toi la Hoang
    """
    st.info(content)

content2 = """
Contact me
"""
st.write(content2)

col3,col4 = st.columns(2)

df = pandas.read_csv('data.csv',sep=";")
with col3:
    for index, row in df.iterrows():
        st.header(row['title'])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
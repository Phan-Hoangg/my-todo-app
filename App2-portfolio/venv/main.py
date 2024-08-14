import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image(r"D:\Udemy\Python Mega Course Learn Python in 60 Days, Build 20 Apps\App2-portfolio\images\Photo.jpg",width=300)

with col2:
    st.title("Phan Hoang")
    content = """
    Xin chao moi nguoi toi la Hoang
    """
    st.info(content)
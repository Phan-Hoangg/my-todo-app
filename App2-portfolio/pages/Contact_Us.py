import streamlit as st

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")

    # Check if the button was pressed
    if button:
        st.write("I was pressed!")
        print("I was pressed!")
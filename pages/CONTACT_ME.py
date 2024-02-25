import streamlit as st
from send_email import send_message

st.title("Contact me")

with st.form(key='email_form',clear_on_submit=True):
    user_email=st.text_input(label='Enter Your Email Address :- ',placeholder="Type Your email here......",key='email')

    user_message=st.text_area(label='Enter Your message :- ',placeholder='Type Your message here.....',key='message')

    message=f'''\
Subject : BOOTCAMP QUERY email from {user_email}

From : {user_email}
{user_message}
'''
    button=st.form_submit_button()

    if button:
        send_message(message)
        st.info("EMAIL SENT SUCCESSFULLY !!!")



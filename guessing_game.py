import streamlit as st
import random


st.set_page_config(page_title="guess", page_icon="🐬")
st.header("Guessing Game")
st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .stNumberInput:first-child input {
        background-color:white;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if 'num' not in st.session_state:
    st.session_state.num = random.randint(1, 10)

count = 3
attempts = 0

for i in range(count):
    guess_num = st.number_input("Enter a number between 1 and 10", step=1, key=f"guess_{i}")
    
    if guess_num != 0 and guess_num is not None:
        attempts += 1
        
        if st.session_state.num == guess_num:
            st.write("You are right!")
            break
        elif guess_num < st.session_state.num:
            st.write("Too low!")
        else:
            st.write("Too high!")

if attempts == count and guess_num:
    st.write("The correct answer is: {}".format(st.session_state.num))
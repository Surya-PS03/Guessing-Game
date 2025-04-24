import streamlit as st
import requests

st.title("Guessing Game 🎮")
url = "http://backend:8000"
check = st.sidebar.selectbox("Menu",["Register","Play"])

if check=="Register":
    st.subheader("Register!!!")
    username = st.text_input("Username")
    email = st.text_input("xyz@hotmail.com")
    password = st.text_input("Password",type = "password")
    
    if(st.button("Register")):
        res = requests.post(url+'/register', json = {"username":username,"password":password,"email":email})
        try:
            if(res.status_code ==200):
                st.success("Player Registered, You have 5 free chances")
            else:
                st.error(res.json()["detail"])
        except requests.exceptions.JSONDecodeError:
            st.error(f"Server returned a non-JSON response. Status: {res.status_code}, content: {res.text}")
elif check=="Play":
    st.subheader("Play")
    username = st.text_input("Username")
    guess = st.number_input("From 1 to 10")

    if(st.button("Play")):
        res = requests.post(url+'/play',json = {"username":username,"guess":guess})

        if(res.status_code == 200):
            
            data = res.json()

            if data["status"]:
                st.success("Congratulation You Won!!!")
            else:
                st.write(f"Sorry You lost!!! Correct guess was {data['correct']}")
            
            st.write(f"You have {data['games left']} games left")
        else:
            st.error(res.json()["detail"])





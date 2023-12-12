import streamlit as st

st.write("""
# Largest number

This app tells the largest number
""")
#Get Input

st.header('Enter the numbers')

def user_input_features():
    first_number = st.number_input("First number")
    second_number = st.number_input("Second number")
    third_number = st.number_input("Third number")
    return max(first_number,second_number,third_number)

x=user_input_features()
st.subheader('The maximum among three numbers is:')
st.write(x)

import streamlit as st
import random  # for generating random char
import string   # for generating string char


# function to generate a password based on user's preferences
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters +=string.digits  # adds number (if selected) (0-9)


    if use_special:
        characters +=string.punctuation    # adds special digits (if selected) (! @ # $ % ^ & * )
       
    # Generate a password by randomly selecting characters from the allowed set
    # Join them together into a string of the requested length
    return ''.join(random.choice(characters) for _ in range(length))


st.title("Password Generator")

length = st.slider("Select Password Length", min_value=6 , max_value=32 , value=12)

use_digits = st.checkbox("Include Digits")

use_special =st.checkbox("Include Special Characters")


if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generate Password: `{password}")

st.write("---------------------------------")

st.write("Build with ❤️ by [Ahmer Abbasi]")










# st.title("hello this is my first project")



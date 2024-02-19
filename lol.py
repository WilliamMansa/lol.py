import streamlit as st
from PIL import Image

def check_eligible(age, income):
    if age >= 18 and income >= 100000:
        return True
    else:
        return False

def Interest(age, income):
    if age < 25:
        if income < 100000:
            return 55.0
        else:
            return 7.5
    elif age >= 25 and age < 50:
        if income < 100000:
            return 80.5
        else:
            return 6.5
    else:
        return 1.0

def bank_management():
    st.title("All India Loan Management System")
    st.write("Fill in the following details to check your loan eligibility and interest rate:")
    st.image("bank.jfif")

    age = st.slider("Your Age:", 18, 100)
    income = st.number_input("saal ka kitna kamate ho:", min_value=0)

    if st.button("Check Eligibility"):
        if check_eligible(age, income):
            st.success("Congratulations! You are eligible for a loan. and bhut paise denge")
            interest_rate = Interest(age, income)
            st.write("Based on your details, the interest rate for your loan is:", interest_rate, "%")
            st.write("apke sath jldi baat hogi dhanyawad.")
        else:
            st.error("Sorry, agli baar aye.")

if __name__ == "__main__":
    bank_management()

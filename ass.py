import streamlit as st

# App title and header
st.title("📱 Streamlit App")
st.header("🔐 Information Form")

# Input fields with additional fields for Name, Phone Number, and Age
with st.form("user_form"):
    name = st.text_input("📝 Enter your full name")
    email = st.text_input("📧 Enter your email address")
    phone_number = st.text_input("📱 Enter your phone number")
    age = st.number_input("🎂 Enter your age", min_value=0)
    pin = st.text_input("🔢 Enter your 4-digit PIN", type="password")
    submitted = st.form_submit_button("Submit")

# Display results after form submission
if submitted:
    st.success("✅ Submission received!")
    st.write("You entered the following information:")
    st.write(f"📝 Full Name: {name}")
    st.write(f"📧 Email: {email}")
    st.write(f"📱 Phone Number: {phone_number}")
    st.write(f"🎂 Age: {age} years old")
    st.write(f"🔒 PIN: {'*' * len(pin)} (hidden for privacy)")

import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# --------------------------
# Database Configuration
# --------------------------
DB_USER = 'root'
DB_PASSWORD = None  # or your actual password as a string
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'hospital'  # Changed DB name to 'hospital' for doctors and patients

@st.cache_resource
def get_connection():
    if DB_PASSWORD is None:
        connection_url = f"mysql+pymysql://{DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    else:
        connection_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    return create_engine(connection_url)

engine = get_connection()

# --------------------------
# Authentication
# --------------------------
st.sidebar.header("🔐 Login")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

def authenticate(user, pwd):
    return user == "admin" and pwd == "hospital123"

if authenticate(username, password):
    st.success(f"Welcome, {username} 👋")
    st.title("🏥 Hospital Management Dashboard")

    # --------------------------
    # Table Selector
    # --------------------------
    table = st.selectbox("Select Table", ["doctors", "patients"])

    # --------------------------
    # Table Viewer with Filter
    # --------------------------
    st.subheader("📄 Table Viewer")
    filter_query = st.text_input("Optional SQL Filter (e.g., specialty = 'Cardiology')")

    view_query = f"SELECT * FROM {table}"
    if filter_query.strip():
        view_query += f" WHERE {filter_query}"

    with engine.connect() as conn:
        df = pd.read_sql(text(view_query), conn)
    st.dataframe(df)

    # --------------------------
    # Insert New Record
    # --------------------------
    st.subheader(f"➕ Add New Record to `{table}`")
    with st.form(key="insert_form"):
        with engine.connect() as conn:

            if table == "doctors":
                full_name = st.text_input("Full Name")
                specialty = st.text_input("Specialty")
                email = st.text_input("Email")
                contact_number = st.text_input("Contact Number")
                submit = st.form_submit_button("Insert Doctor")
                if submit:
                    conn.execute(text("""
                        INSERT INTO doctors (full_name, specialty, email, contact_number)
                        VALUES (:name, :specialty, :email, :contact)
                    """), {"name": full_name, "specialty": specialty, "email": email, "contact": contact_number})
                    conn.commit()
                    st.success("✅ Doctor record inserted!")

            elif table == "patients":
                full_name = st.text_input("Full Name")
                age = st.number_input("Age", min_value=0)
                gender = st.selectbox("Gender", ["Male", "Female", "Other"])
                contact_number = st.text_input("Contact Number")
                doctor_id = st.number_input("Assigned Doctor ID", min_value=1)
                submit = st.form_submit_button("Insert Patient")
                if submit:
                    conn.execute(text("""
                        INSERT INTO patients (full_name, age, gender, contact_number, doctor_id)
                        VALUES (:name, :age, :gender, :contact, :doctor_id)
                    """), {"name": full_name, "age": age, "gender": gender, "contact": contact_number, "doctor_id": doctor_id})
                    conn.commit()
                    st.success("✅ Patient record inserted!")

else:
    st.warning("🔐 Please log in with valid credentials.")

import streamlit as st
import pandas as pd
import plotly.express as px
from matplotlib_venn import venn2
import matplotlib.pyplot as plt
from io import BytesIO

# ----- Simple Login -----
def login():
    st.title("🔐 Advaitverse Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.success("Login successful! Redirecting...")
        else:
            st.error("Invalid credentials")

# ----- Dummy Healthcare Data -----
def get_dummy_data():
    data = {
        'Patient ID': [101, 102, 103, 104],
        'Glucose': [85, 140, 160, 110],
        'Cholesterol': [190, 220, 250, 200],
        'Status': ['Normal', 'High', 'High', 'Borderline']
    }
    return pd.DataFrame(data)

# ----- Dashboard -----
def dashboard():
    st.title("📊 Advaitverse Healthcare Dashboard")

    # Table
    df = get_dummy_data()
    st.subheader("📋 Patient Data Table")
    st.dataframe(df, use_container_width=True)

    # Plot
    st.subheader("📈 Glucose Level Chart")
    fig = px.bar(df, x='Patient ID', y='Glucose', color='Status', title='Glucose Levels by Patient')
    st.plotly_chart(fig, use_container_width=True)

    # Venn Diagram
    st.subheader("🧬 Venn Diagram - Glucose vs Cholesterol")
    set1 = set([101, 102])  # High Glucose
    set2 = set([102, 103])  # High Cholesterol
    
    fig_venn, ax = plt.subplots()
    venn2([set1, set2], set_labels=('High Glucose', 'High Cholesterol'))
    
    buf = BytesIO()
    fig_venn.savefig(buf, format="png")
    st.image(buf)

# ----- Main App Flow -----
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
else:
    dashboard()

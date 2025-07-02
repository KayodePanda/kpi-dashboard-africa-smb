import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="KPI Dashboard", layout="wide")
st.title("KPI Dashboard for Small African Businesses")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/financial_data.csv")
    df['Month'] = pd.to_datetime(df['Month'])
    df['Profit'] = df['Revenue'] - df['Expenses']
    df['Total_Customers'] = df['New_Customers'] + df['Existing_Customers']
    df['CAC'] = df['Expenses'] / df['New_Customers'].replace(0, pd.NA)
    df['Revenue_per_Customer'] = df['Revenue'] / df['Total_Customers'].replace(0, pd.NA)
    df['LTV'] = df['Revenue_per_Customer'] * 12
    df['Churn Rate (%)'] = (df['Churned_Customers'] / df['Total_Customers'].replace(0, pd.NA)) * 100
    return df

df = load_data()

# =============================
# Data Preview + KPI Metrics
# =============================
st.subheader("Data Preview")
st.dataframe(df.head())

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${df['Revenue'].sum():,.0f}")
col2.metric("Total Expenses", f"${df['Expenses'].sum():,.0f}")
col3.metric("Average CAC", f"${df['CAC'].mean():.2f}")
col4.metric("Average LTV", f"${df['LTV'].mean():.2f}")

# =============================
# Helper function to rotate x-axis labels
# =============================
def rotate_labels(ax):
    ax.tick_params(axis='x', rotation=45)

# =============================
# Charts
# =============================

# Revenue vs Expenses
st.subheader("Revenue vs Expenses Over Time")
fig1, ax1 = plt.subplots()
ax1.plot(df['Month'], df['Revenue'], label='Revenue', marker='o', color='green')
ax1.plot(df['Month'], df['Expenses'], label='Expenses', marker='x', color='red')
ax1.set_ylabel("Amount")
rotate_labels(ax1)
ax1.legend()
st.pyplot(fig1)

# CAC vs LTV
st.subheader("CAC vs LTV Over Time")
fig2, ax2 = plt.subplots()
ax2.plot(df['Month'], df['CAC'], label='CAC', marker='o', color='orange')
ax2.plot(df['Month'], df['LTV'], label='LTV', marker='x', color='blue')
ax2.set_ylabel("Cost / Value")
rotate_labels(ax2)
ax2.legend()
st.pyplot(fig2)

# Profit Trend
st.subheader("Profit Trend by Month")
fig3, ax3 = plt.subplots()
ax3.plot(df['Month'], df['Profit'], marker='o', color='purple')
ax3.set_ylabel("Profit")
rotate_labels(ax3)
st.pyplot(fig3)

# Customer Growth
st.subheader("Customer Growth Over Time")
fig4, ax4 = plt.subplots()
ax4.plot(df['Month'], df['Total_Customers'], marker='o', color='dodgerblue')
ax4.set_ylabel("Total Customers")
rotate_labels(ax4)
st.pyplot(fig4)

# Churn Rate
st.subheader("Customer Churn Rate Over Time")
fig5, ax5 = plt.subplots()
ax5.plot(df['Month'], df['Churn Rate (%)'], marker='x', color='crimson')
ax5.set_ylabel("Churn Rate (%)")
rotate_labels(ax5)
st.pyplot(fig5)

# Footer
st.markdown("---")
st.markdown("Built by Kayode Olorunmaiye | GitHub: [KayodePanda](https://github.com/KayodePanda)")
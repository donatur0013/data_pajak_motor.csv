import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Pajak Motor", layout="wide")

st.title("🚗 Dashboard Pajak Motor")

# Load data
data = pd.read_csv("data_pajak_motor.csv")

# Statistik ringkas
col1, col2 = st.columns(2)
col1.metric("Total Transaksi", int(data["transaksi"].sum()))
col2.metric("Total Pendapatan (Rp)", f"{data['pendapatan'].sum():,}")

st.subheader("Grafik Transaksi Pajak Motor")
st.bar_chart(data.set_index("bulan")["transaksi"])

st.subheader("Grafik Pendapatan Pajak Motor")
st.bar_chart(data.set_index("bulan")["pendapatan"])

st.caption("Data bersifat simulasi (dummy)")

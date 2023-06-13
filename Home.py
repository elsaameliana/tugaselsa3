import streamlit as st

col1, col2, col3 = st.columns([1,2,1])
col1.markdown(" # Uji Hipotesis Satu Populasi")
col1.markdown("App Uji Hipotesis Satu Populasi merupakan aplikasi sederhana untuk mempermudah perhitungan statistik")
col3.metric(label="Temperatur", value="32 C", delta="1,4 C")



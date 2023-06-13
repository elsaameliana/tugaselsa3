import streamlit as st
import numpy as np
from scipy import stats 
import matplotlib.pyplot as plt

# Menampilkan judul halaman
st.title("Statistik dan Visualisasi Data")

st.write('#### Ayo kita hitung!')

# Memasukkan data
data = st.text_area("Masukkan data (pisahkan dengan spasi)", value="1 1 1 5 3 2 4")

# Mengubah data menjadi array numpy
data = np.array([float(x) for x in data.split()])

# Menampilkan data
st.subheader("Data")
st.write("Data:", data)

#Menampilkan n
n = len(data)
st.write("##### Jumlah sampel")
st.write("n:", n)

# Menghitung mean
mean = np.mean(data)
st.write("##### Mean")
st.write("Mean:", mean)

# Menghitung median
median = np.median(data)
st.write("##### Median")
st.write("Median:", median)

# Menghitung varians
variance = np.var(data, ddof=1)
st.write("##### Varians")
st.write("Varians:", variance)

# Menghitung standar deviasi
std_dev = np.std(data, ddof=1)
st.write("##### Standar Deviasi")
st.write("Standar Deviasi:", std_dev)





# Diagram Batang (Bar Chart)
st.subheader("Diagram Batang")
fig, ax = plt.subplots()
ax.bar(range(len(data)), data)
ax.set_xlabel("Index")
ax.set_ylabel("Value")
st.pyplot(fig)

# Diagram Garis
st.subheader("Diagram Garis")
fig, ax = plt.subplots()
ax.plot(range(len(data)), data)
ax.set_xlabel("Index")
ax.set_ylabel("Value")
st.pyplot(fig)

# Diagram Lingkaran 
st.subheader("Diagram Lingkaran")
labels = [f"Data {i+1}" for i in range(len(data))]
fig, ax = plt.subplots()
ax.pie(data, labels=labels, autopct='%1.1f%%')
st.pyplot(fig)

# Boxplot
st.subheader("Boxplot")
fig, ax = plt.subplots()
ax.boxplot(data)
ax.set_ylabel("Value")
st.pyplot(fig)

# Scatter Plot
st.subheader("Scatter Plot")
x = range(len(data))
y = data
fig, ax = plt.subplots()
ax.scatter(x, y)
ax.set_xlabel("Index")
ax.set_ylabel("Value")
st.pyplot(fig)

# Diagram Pareto
st.subheader("Diagram Pareto")
sorted_data = sorted(data, reverse=True)
cumulative_sum = [sum(sorted_data[:i+1]) for i in range(len(sorted_data))]
cumulative_percentage = [cumulative_sum[i] / sum(sorted_data) * 100 for i in range(len(sorted_data))]
fig, ax = plt.subplots()
ax.plot(range(1, len(sorted_data) + 1), cumulative_percentage, marker='o')
ax.set_xlabel("Data")
ax.set_ylabel("Cumulative Percentage")
ax.set_title("Pareto Chart")
st.pyplot(fig)

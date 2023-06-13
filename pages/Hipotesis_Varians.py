import streamlit as st
import numpy as np
from scipy import stats

# judul
st.title("Uji Hipotesis Varians Satu Populasi")

# Memasukkan data sampel
st.write('##### Ayo kita hitung!')
sample_data = st.text_area("Masukkan data sampel (pisahkan dengan spasi)", value="1 2 3 4 5")

# Mengubah data sampel menjadi array numpy
sample = np.array([float(x) for x in sample_data.split()])
n = len(sample)

# Menampilkan data sampel
st.subheader("Data Sampel")
st.write(sample)
st.write("Jumlah Sampel (n):", n)

#Menampilkan hipotesis uji
st.write('### Hipotesis')
st.latex('H_{0}: \sigma^2 = \sigma_0^2')
st.latex('H_{1} : \sigma^2 \neq \sigma_0^2')

# Menentukan hipotesis nol
h0 = st.number_input("Masukkan nilai hipotesis nol (H0) untuk varians", value=1.0)

# Menghitung statistik uji chi-square dan p-value
chi2_statistic = sum((x - np.mean(sample))**2 / h0 for x in sample)
p_value = 1 - stats.chi2.cdf(chi2_statistic, len(sample) - 1)

# Menampilkan hasil uji hipotesis
st.subheader("Hasil Uji Hipotesis")
st.write("Chi-square Hitung:", chi2_statistic)
st.write("P-Value:", p_value)

# Menentukan keputusan berdasarkan hasil uji hipotesis
alpha = st.number_input("Masukkan tingkat signifikansi (alpha)", value=0.01)
if p_value < alpha:
    st.write("Keputusan: Tolak (H0)")
    st.write("Kesimpulan: Varians dari data memiliki nilai yang berbeda dengan H0 ")
else:
    st.write("Keputusan : Gagal Tolak (H0)")
    st.write("Kesimpulan : Nilai varians dari data memiliki nilai sama dengan H0")

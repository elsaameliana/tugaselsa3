import streamlit as st
import numpy as np
from scipy import stats

# Menampilkan judul halaman
st.title("Uji Hipotesis Rata-Rata Satu Populasi (z-test)")

#menampilkan peringatan
st.write('#### *Reminder')
st.write('Uji hipotesis rata-rata dengan uji z digunakan ketika : ')
st.write('1. Ukuran sampel besar ( n>30 )')
st.write('2. Nilai dari standar deviasi atau varians dari populasi diketahui')

# Memasukkan data sampel
st.write('##### Ayo kita hitung!')
sample_data = st.text_area("Masukkan data sampel (pisahkan dengan spasi)", value="1 2 3 4 5 1 5 2 6 9 8 4 7 5 3 8 2 4 5 6 7 1 3 3 3 1 2 1 2 4 5 7 6 2 1 3 4 5 8 7 2 1 5 6")

# Mengubah data sampel menjadi array numpy
sample = np.array([float(x) for x in sample_data.split()])
n = len(sample)

# Menampilkan data sampel
st.subheader("Data Sampel")
st.write("Sampel:", sample)
st.write("Jumlah Sampel (n):", n)

# Menghitung mean dan standar deviasi sampel
mean = np.mean(sample)
std_dev = np.std(sample, ddof=1)

# Menampilkan nilai mean dan standar deviasi sampel
st.subheader("Statistik Sampel")
st.write("Mean:", mean)
st.write("Standar Deviasi:", std_dev)

#menampilkan hipotesis
st.write('### Hipotesis')
st.latex('H_0: \mu = \mu_0')
st.latex('H_1: \mu \neq \mu_0')

# Memasukkan nilai hipotesis nol
null_hypothesis = st.number_input("Masukkan nilai hipotesis nol", value=0.0)

# Menentukan tingkat signifikansi (alpha)
alpha = st.number_input("Masukkan tingkat signifikansi (alpha)", value=0.01)

# Menghitung z-score dan p-value
z_score = (mean - null_hypothesis) / (std_dev / np.sqrt(len(sample)))
p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))

# Menampilkan hasil uji hipotesis
st.subheader("Hasil Uji Hipotesis")
st.write("Z-Score:", z_score)
st.write("P-Value:", p_value)

# Menentukan keputusan berdasarkan hasil uji hipotesis
if p_value < alpha:
    st.write("Keputusan : Tolak H0")
    st.write("Kesimpulan : Rata-rata dari data memiliki nilai yang berbeda dengan H0")
else:
    st.write("Keputusan : Gagal Tolak H0")
    st.write("Kesimpulan : Rata-rata dari data memiliki nilai sama dengan H0")
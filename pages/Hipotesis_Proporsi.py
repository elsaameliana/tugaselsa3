import streamlit as st
import numpy as np
from scipy import stats

# Menampilkan judul halaman
st.title("Uji Hipotesis Proporsi Satu Populasi")

st.write('#### Ayo kita hitung!')

# Memasukkan data
success_count = st.number_input("Masukkan jumlah kejadian berhasil (k)", value=50)
sample_size = st.number_input("Masukkan ukuran sampel (n)", value=100)
null_hypothesis = st.number_input("Masukkan nilai hipotesis nol (p0)", min_value=0.0, max_value=1.0, value=0.5)
alpha = st.number_input("Masukkan tingkat signifikansi (alpha)", value=0.01)

# Menghitung proporsi sampel
sample_proportion = success_count / sample_size

#menampilkan hipotesis
st.write('### Hipotesis')
st.latex('H_0: p = p_0')
st.latex('H_1: p \neq p_0')

# Menampilkan hasil proporsi sampel
st.subheader("Proporsi Sampel")
st.write("Proporsi Sampel (p-hat):", sample_proportion)

# Menghitung z-score dan p-value
z_score = (sample_proportion - null_hypothesis) / np.sqrt(null_hypothesis * (1 - null_hypothesis) / sample_size)
p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))

# Menampilkan hasil uji hipotesis
st.subheader("Hasil Uji Hipotesis")
st.write("Z-Score:", z_score)
st.write("P-Value:", p_value)

# Menentukan keputusan berdasarkan hasil uji hipotesis
if p_value < alpha:
    st.write("Keputusan : Tolak H0")
    st.write("Kesimpulan : Proporsi dari data memiliki nilai yang berbeda dengan H0")
else:
    st.write("Keputusan : Gagal Tolak H0")
    st.write("Kesimpulan : Proporsi dari data memiliki nilai sama dengan H0")
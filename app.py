import streamlit as st
import pandas as pd
import os


# Judul aplikasi
st.title("Soal Statistik dan Probabilitas Berdasarkan Data Saham Amazon (1997-2025)")

# Instruksi soal
st.markdown("""
---

1. Hitung nilai rata-rata (mean), median, dan simpangan baku (standard deviation) dari harga penutupan (close price) saham Amazon selama tahun 2024.

2. Hitung range, variansi, dan standar deviasi dari volume transaksi saham Amazon pada tahun 2024. Apa yang dapat disimpulkan dari hasil tersebut ?

---

3. Kategorikan harga penutupan saham Amazon pada tahun 2024 ke dalam tiga kelompok:  
   - **Rendah:** Harga penutupan < Kuartil 1 (Q1)  
   - **Sedang:** Harga penutupan antara Kuartil 1 (Q1) dan Kuartil 3 (Q3)  
   - **Tinggi:** Harga penutupan > Kuartil 3 (Q3)  
Tentukan probabilitas empiris dari masing-masing kategori berdasarkan data tahun 2024.

4. Buat distribusi probabilitas untuk volume transaksi (volume) dari data tahun 2024 dengan membaginya menjadi beberapa interval diskrit (misalnya: rendah, sedang, tinggi). Pastikan total probabilitas bernilai 1.

---

5. Buatlah:
   - Histogram dari harga penutupan Amazon pada tahun 2024.
   - Boxplot untuk melihat distribusi harga penutupan pada tahun 2024.
   - Time Series Plot yang menunjukkan tren harga penutupan dari Januari 2024 hingga Desember 2024.

---

6. Gunakan data harga penutupan saham Amazon dari Januari hingga Desember 2024 untuk menguji apakah data tersebut mengikuti distribusi normal dengan menggunakan:
   - Q-Q Plot
   - Uji Normalitas (misalnya: Shapiro-Wilk test)

7. Berikan kesimpulan berdasarkan hasil uji normalitas.

---

**Data:**  
Gunakan data saham Amazon yang dapat diunduh dari:  
[Amazon Stock Data 2025 (Kaggle)](https://www.kaggle.com/datasets/umerhaddii/amazon-stock-data-2025/data)
""")

file_path = "AMZN_1997-05-15_2025-02-21.csv"

if os.path.exists(file_path):
    # Atur presisi tampilan angka di pandas
    pd.set_option('display.precision', 20)
    
    # Membaca file CSV
    df = pd.read_csv(file_path)
    
    st.subheader("Seluruh Data")
    st.dataframe(df)  # Tabel interaktif dengan scrollbar
    
    st.write(f"**Dimensi Data:** {df.shape[0]} baris x {df.shape[1]} kolom")
else:
    st.error(f"File '{file_path}' tidak ditemukan di direktori yang sama.")
    
st.markdown("""
### Deskripsi Kolom Data

- **date**  
  Date
  
- **open**  
  The price at market open
  
- **high**  
  The highest price for that day
  
- **low**  
  The lowest price for that day
  
- **close**  
  The price at market close, adjusted for splits
  
- **adj_close**  
  The closing price after adjustments for all applicable splits and dividend distributions. Data is adjusted using appropriate split and dividend multipliers, adhering to Center for Research in Security Prices (CRSP) standards.
  
- **volume**  
  The number of shares traded on that day
""")


st.title("Jawaban dari Perhitungan Statistik Saham Amazon Tahun 2024")

st.markdown("""
### Nomor 1. Statistik Harga Penutupan (Close Price)
- **Mean (Rata-rata):** 184.63  
- **Median:** 183.43  
- **Standar Deviasi:** 17.43  

### Nomor 2. Statistik Volume Transaksi
- **Range (Jangkauan):** 126,440,900  
- **Variansi:** 2.64 × 10¹⁴  
- **Standar Deviasi:** 16,254,293.29  

### Kesimpulan

**Harga Penutupan:**
- Rata-rata harga penutupan saham Amazon selama tahun 2024 adalah \$184.63.
- Median \$183.43, yang hampir sama dengan mean, menunjukkan bahwa distribusi harga saham cukup simetris.
- Standar deviasi \$17.43 menunjukkan adanya fluktuasi harga yang cukup besar.

**Volume Transaksi:**
- Volume transaksi memiliki rentang yang sangat besar, dari nilai minimum ke maksimum sebesar 126 juta.
- Variansi dan standar deviasi yang tinggi menunjukkan bahwa jumlah saham yang diperdagangkan per hari sangat bervariasi.
- Hal ini mengindikasikan adanya volatilitas yang tinggi dalam aktivitas perdagangan saham Amazon pada tahun 2024.
---
""")

st.markdown("""
### Nomor 3: Kategorisasi Harga Penutupan (Close Price)

Berdasarkan data saham Amazon tahun 2024, diperoleh nilai kuartil sebagai berikut:
- **Kuartil 1 (Q1):** Nilai harga penutupan pada persentil ke-25.
- **Kuartil 3 (Q3):** Nilai harga penutupan pada persentil ke-75.

**Kategori Harga Penutupan:**
- **Rendah:** Harga penutupan < Q1  
- **Sedang:** Harga penutupan antara Q1 dan Q3  
- **Tinggi:** Harga penutupan > Q3  

**Hasil Perhitungan:**
- **Rendah:** 63 hari (25% dari total hari perdagangan)  
- **Sedang:** 126 hari (50% dari total hari perdagangan)  
- **Tinggi:** 63 hari (25% dari total hari perdagangan)  

**Kesimpulan:**  
Mayoritas (50%) hari perdagangan saham Amazon pada tahun 2024 menunjukkan harga penutupan berada dalam kategori *Sedang*, sedangkan hanya 25% hari perdagangan berada di masing-masing kategori *Rendah* dan *Tinggi*. Total probabilitas adalah 1 (100%), yang memenuhi syarat distribusi probabilitas.

---

### Nomor 4: Distribusi Probabilitas Volume Transaksi

Analisis distribusi volume transaksi saham Amazon tahun 2024 dengan pembagian ke dalam beberapa interval (misalnya: Rendah, Sedang, Tinggi) menunjukkan:
- **Volume Transaksi Sedang:** 50%
- **Volume Transaksi Rendah:** 25%
- **Volume Transaksi Tinggi:** 25%

**Kesimpulan:**  
Meskipun volume transaksi cenderung berada di kategori *Sedang*, terdapat fluktuasi signifikan dengan peluang yang sama (25%) untuk volume transaksi yang berada di kategori *Rendah* dan *Tinggi*.

---

### Nomor 5: Buatlah visualisasi data sebagai berikut:
- **Histogram** dari harga penutupan saham Amazon pada tahun 2024.
- **Boxplot** untuk melihat distribusi harga penutupan pada tahun 2024.
- **Time Series Plot** yang menunjukkan tren harga penutupan dari Januari hingga Desember 2024.
""")

# Asumsikan gambar hasil visualisasi disimpan dengan nama file berikut
image_path = "histo.png"

# Cek apakah file gambar tersedia
if os.path.exists(image_path):
    st.image(image_path, caption="Visualisasi Nomor 5: Histogram, Boxplot, dan Time Series Plot",  use_container_width=True)
else:
    st.error(f"File gambar '{image_path}' tidak ditemukan di direktori yang sama.")
    
image_path = "boxplot.png"

# Cek apakah file gambar tersedia
if os.path.exists(image_path):
    st.image(image_path, caption="Visualisasi Nomor 5: Histogram, Boxplot, dan Time Series Plot",  use_container_width=True)
else:
    st.error(f"File gambar '{image_path}' tidak ditemukan di direktori yang sama.")
    
image_path = "time.png"

# Cek apakah file gambar tersedia
if os.path.exists(image_path):
    st.image(image_path, caption="Visualisasi Nomor 5: Histogram, Boxplot, dan Time Series Plot",  use_container_width=True)
else:
    st.error(f"File gambar '{image_path}' tidak ditemukan di direktori yang sama.")
    
st.markdown("""
**Histogram Harga Penutupan:**  
- Menunjukkan distribusi frekuensi harga penutupan selama tahun 2024.  
- Terlihat bagaimana harga saham tersebar dalam berbagai rentang nilai.

**Boxplot Harga Penutupan:**  
- Memberikan gambaran tentang distribusi harga saham, median, dan kemungkinan outlier.  
- Membantu melihat persebaran dan adanya fluktuasi yang ekstrem.

**Time Series Plot Harga Penutupan:**  
- Menampilkan tren harga saham dari Januari hingga Desember 2024.  
- Memudahkan dalam mengidentifikasi pola naik/turun sepanjang tahun.
""")


st.markdown("""
---
### Nomor 6: Uji Normalitas Harga Penutupan Saham Amazon Tahun 2024 """)

image_path = "qq.png"

# Cek apakah file gambar tersedia
if os.path.exists(image_path):
    st.image(image_path, caption="Visualisasi Nomor 5: Histogram, Boxplot, dan Time Series Plot",  use_container_width=True)
else:
    st.error(f"File gambar '{image_path}' tidak ditemukan di direktori yang sama.")
  

st.markdown("""
📌 **Interpretasi Q-Q Plot**  
Titik-titik data berada di sekitar garis merah di bagian tengah, menunjukkan bahwa sebagian besar data mendekati distribusi normal.  
Ekor bawah (kiri) dan ekor atas (kanan) menyimpang dari garis merah, yang mengindikasikan adanya skewness (ketidakseimbangan distribusi) atau outlier.  
Penyimpangan di ekor bawah menunjukkan bahwa harga saham memiliki beberapa nilai yang lebih kecil dari yang diharapkan.  
Penyimpangan di ekor atas menunjukkan bahwa ada beberapa hari dengan harga saham yang jauh lebih tinggi dari yang diprediksi oleh distribusi normal.

**Shapiro-Wilk normality test**  
data:  amazon_2024$close  
W = 0.94885, p-value = 9.915e-08

📌 **Interpretasi Hasil**  
p-value = 9.915e-08 (~0.00000009915) sangat kecil (p < 0.05),  
❌ **Kesimpulan:** Data tidak berdistribusi normal.  
Nilai W = 0.94885 menunjukkan bahwa data mendekati normal, tetapi tidak sepenuhnya.  
Dikombinasikan dengan Q-Q Plot, terlihat bahwa data memiliki penyimpangan di ekor bawah dan atas.""")

st.markdown("""
---
### Nomor 7: Kesimpulan Berdasarkan Hasil Uji Normalitas Harga Penutupan Saham Amazon Tahun 2024

erdasarkan hasil uji normalitas Shapiro-Wilk dan Q-Q Plot, dapat disimpulkan bahwa:  
1. **Hasil Uji Normalitas Shapiro-Wilk**  
   Shapiro-Wilk normality test  
   data:  amazon_2024$close  
   W = 0.94885, p-value = 9.915e-08  
   p-value = 9.915e-08 (< 0.05) → ❌ Data tidak mengikuti distribusi normal.  
   Nilai W = 0.94885 menunjukkan bahwa data agak mendekati normal, tetapi masih memiliki penyimpangan.  
2. **Hasil Q-Q Plot**  
   Titik-titik menyimpang dari garis merah di ekor bawah dan atas, menunjukkan skewness atau outlier.  
   Bagian tengah data sejajar dengan garis normal, tetapi ekor bawah lebih rendah dan ekor atas lebih tinggi, menunjukkan adanya distribusi yang lebih miring.

📌 **Kesimpulan Akhir**  
Harga penutupan saham Amazon tahun 2024 tidak berdistribusi normal (p-value < 0.05 dari uji Shapiro-Wilk).  
Q-Q Plot menunjukkan penyimpangan di ekor bawah dan atas, yang menunjukkan adanya outlier atau distribusi skewed.
""")
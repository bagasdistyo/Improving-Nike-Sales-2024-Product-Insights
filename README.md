# 👟 Nike Product Sales Analysis

![Nike Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Logo_NIKE.svg/1280px-Logo_NIKE.svg.png)

📊 **Analisis penjualan produk Nike untuk mengidentifikasi penyebab performa rendah dan memberikan rekomendasi strategis berbasis data.**

---

## 📁 Repository Outline

| File/Folder                           | Deskripsi                                                                 |
|--------------------------------------|---------------------------------------------------------------------------|
| `README.md`                          | Penjelasan umum project                                                  |
| `notebook.ipynb`                     | Notebook utama untuk EDA dan analisis data                               |
| `images/`                            | Folder berisi screenshot visualisasi hasil analisis dan insight          |
| `P2M3_bagas_distyo_data_raw.csv`     | Dataset mentah sebelum diproses                                          |
| `P2M3_bagas_distyo_data_clean.csv`   | Dataset hasil pembersihan dan pengolahan data                            |
| `P2M3_bagas_distyo_GX.ipynb`         | Validasi data menggunakan Great Expectations                             |
| `P2M3_bagas_distyo_DAG.py`           | Pipeline automasi menggunakan Apache Airflow                             |

---

## 🧩 Problem Background

Nike adalah salah satu brand olahraga global terbesar. Di tengah persaingan ketat, penting bagi perusahaan untuk memahami:
- Produk mana yang **tidak laku** (underperforming),
- Faktor-faktor yang memengaruhi rendahnya penjualan, dan
- Strategi yang dapat digunakan untuk memperbaiki performa tersebut.

📌 **Tujuan**: Memberikan insight berbasis data untuk mendukung keputusan strategis dalam hal **harga, promosi, dan distribusi produk**.

---

## 🎯 Project Output

✅ Hasil akhir dari project ini meliputi:

- 📈 **Laporan EDA**: Analisis performa produk berdasarkan kategori, wilayah, harga, dan waktu penjualan.
- 🧠 **Rekomendasi**: Strategi harga & distribusi untuk produk dengan performa rendah.
- ⚙️ **Pipeline Automasi**: Dengan Apache Airflow, dari ekstraksi hingga pembersihan data.
- 📋 **Validasi Data**: Menggunakan Great Expectations untuk menjamin kualitas data.
- 📊 **Dashboard**: Visualisasi insight melalui Kibana.

---

## 📊 Dataset Description

- **Sumber**: Database PostgreSQL  
- **Format**: `.csv` hasil ekstraksi & pembersihan
- **Kolom utama**:
  - `product_category`, `sub_category`, `retail_price`
  - `region`, `sales_channel`, `units_sold`, `month`

🧹 Data telah melalui:
- Penghapusan duplikasi
- Penanganan nilai null
- Validasi dengan rule-based expectations (Great Expectations)

---

## 🔍 Methodology

### 🔧 1. Data Cleaning
- Menghapus duplikasi
- Normalisasi kolom
- Imputasi nilai hilang

### 📊 2. Exploratory Data Analysis (EDA)
- Identifikasi tren penjualan per produk & wilayah
- Analisis outlier harga dan performa musiman

### ✅ 3. Data Validation
- Menggunakan **Great Expectations**
- Menetapkan dan mengevaluasi data quality checks

### ⛓️ 4. Pipeline Automation
- Automasi proses ETL dengan **Apache Airflow**
- Eksekusi rutin dan replikasi pipeline

### 📈 5. Visualization
- Visualisasi data menggunakan **matplotlib** dan **seaborn**
- Dashboard interaktif dengan **Kibana**

---

## 🛠️ Tech Stack

### 🔤 Bahasa Pemrograman
- Python

### 🧰 Tools & Platform
- **Apache Airflow** – Automasi pipeline
- **PostgreSQL** – Sumber data utama
- **Elasticsearch & Kibana** – Visualisasi dan dashboard

### 📦 Libraries Python
- `pandas`, `numpy`
- `matplotlib`, `seaborn`
- `great_expectations`
- `psycopg2`, `elasticsearch-py`

---

## 📌 Catatan

Project ini tidak hanya bertujuan memberikan insight tentang penjualan produk Nike, tetapi juga menerapkan praktik rekayasa data modern:
- Validasi data otomatis
- Pipeline data yang dapat diulang dan diskalakan
- Visualisasi interaktif untuk membantu pengambilan keputusan berbasis data

---

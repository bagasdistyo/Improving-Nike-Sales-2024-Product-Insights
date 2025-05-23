'''
=================================================
Milestone 3

Nama  : Bagas Distyo Utomo
Batch : RMT-41

Program ini dibuat untuk melakukan automatisasi load data dan cleaning dari PostgreSQL ke ElasticSearch. Dataset yang digunakan adalah penjualan sepatu Nike tahun 2024.
=================================================
'''

import datetime as dt
from datetime import timedelta
import hashlib

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

import pandas as pd
import psycopg2 as db
from elasticsearch import Elasticsearch

# ------------------ FUNCTION DEFINITIONS ------------------

def fetch_data_from_postgresql():
    '''
    Fungsi ini mengambil data dari PostgreSQL dan menyimpannya sebagai CSV
    untuk keperluan data cleaning selanjutnya.
    '''
    conn_string = "dbname='airflow' host='postgres' user='airflow' password='airflow' port=5432"
    conn = db.connect(conn_string)
    df = pd.read_sql("SELECT * FROM sales", conn)
    df.to_csv('/opt/airflow/dags/P2M3_bagas_distyo_data_raw.csv', index=False)
    print("Data fetched from PostgreSQL and saved to CSV.")


def clean_and_save_data():
    '''
    Fungsi ini membersihkan data:
    - Menghapus duplikat
    - Menghapus baris yang mengandung missing value
    - Normalisasi nama kolom:
        * lowercase
        * ganti spasi dengan underscore
        * hapus simbol

    Hasilnya disimpan ke CSV clean.
    '''
    df = pd.read_csv('/opt/airflow/dags/P2M3_bagas_distyo_data_raw.csv')

    # Hapus duplikat
    df.drop_duplicates(inplace=True)

    # Hapus baris yang memiliki missing values
    df.dropna(inplace=True)

    # Normalisasi nama kolom
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace(r'[^a-zA-Z0-9_]', '', regex=True)
    )

    # Simpan data yang telah dibersihkan
    df.to_csv('/opt/airflow/dags/P2M3_bagas_distyo_data_clean.csv', index=False)
    print("Data cleaned (duplicates and missing rows removed) and saved.")



def post_data_to_elasticsearch():
    '''
    Mengirim data hasil cleaning ke Elasticsearch.
    Setiap baris dikirim sebagai dokumen individual tanpa duplikat, 
    menggunakan hash dari isi data sebagai _id.
    '''
    es = Elasticsearch(hosts=["http://elasticsearch:9200"])
    df = pd.read_csv('/opt/airflow/dags/P2M3_bagas_distyo_data_clean.csv')

    for _, row in df.iterrows():
        doc = row.to_dict()
        # Buat ID unik berdasarkan isi baris (hash MD5 dari string isi row)
        doc_id = hashlib.md5(str(doc).encode()).hexdigest()
        
        es.index(index="data_sales", id=doc_id, body=doc)

    print("Cleaned data posted to Elasticsearch (without duplicates).")


# ------------------ DAG CONFIGURATION ------------------

default_args = {
    'owner': 'bagas',
    'start_date': dt.datetime(2024, 11, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='milestone_DAG1',
    default_args=default_args,
    schedule_interval='10-30/10 9 * * 6',  # Tiap Sabtu 09:10, 09:20, 09:30
    catchup=True,
    description='Pipeline: PostgreSQL ➜ Clean ➜ Elasticsearch'
) as dag:

    task_fetch = PythonOperator(
        task_id='fetch_from_postgresql',
        python_callable=fetch_data_from_postgresql
    )

    task_clean = PythonOperator(
        task_id='clean_data',
        python_callable=clean_and_save_data
    )

    task_post = PythonOperator(
        task_id='post_to_elasticsearch',
        python_callable=post_data_to_elasticsearch
    )

    # Urutan tugas
    task_fetch >> task_clean >> task_post
import mysql.connector

def koneksi():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="koperasi_simpan_pinjam"
    )
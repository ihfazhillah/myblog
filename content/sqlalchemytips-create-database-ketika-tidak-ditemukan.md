Title: #sqlalchemytips - Create Database Ketika Tidak Ditemukan
Slug: sqlalchemytips-create-database-ketika-tidak-ditemukan
Date: 2017-05-21 20:47
Category: Tips
Tags: sqlalchemy, sqlalchemy_utils, create_database, sqlalchemy create database if not exists
Authors: Ihfazhillah
Summary: Membuat database ketika database tidak ditemukan


# Bismillah,

Saat saya bekerja menggunakan `sqlalchemy`dan `mysql`, kemudian database belum
dibuat, maka saya harus masuk ke mysql console dan mengetikkan perintah `CREATE
DATABASE inidatabase`. Setelah itu baru bisa menggunakannya lewat `sqlalchemy`

Namun, masalahnya ketika saya ingin mengubah database url, saya harus
*re-create* lagi dong? 

## Tipsnya

Gunakan kombinasi `database_exists` dan `create_database` dari
`sqlalchemy_utils` package.

Berikut langkahnya :

1. Install `sqlalchemy_utils`
2. check kalau database sudah ada atau tidak menggunakan `database_exists`
3. buat database kalau tidak ada menggunakan `create_database`

Lihat kode berikut

```python
from sqlalchemy_utils.functions import database_exists, create_database

db.init_app(app)
engine = db.engine

if not database_exists(engine.url):
    create_database(engine.url)
```

Perhatikan, contoh diatas saya menggunakan `flask_sqlalchemy`. Saya dapatkan
url database menggunakan `engine.url`.

## Kesimpulan

Dengan `sqlalchemy_utils` ini, saya menjadi sangat terbantu. Sehingga saya
tidak perlu *re-create* database secara manual lagi setiap **harus** pindah
database/ pindah tempat.

Semoga bermanfaat.

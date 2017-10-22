Title: Pymysql Internal Error Incorrect String Value
Slug: pymysql-internal-error-incorrect-string-value
Date: 2017-05-21 21:03
Category: Error
Tags: pymysql error, pymysql error encoding, mysql arabic, mysql insert arabic value
Authors: Ihfazhillah
Summary: tips sederhana mengatasi internal error incorrect string value ketika memasukkan arabic value ke table dalam mysql


# Bismillah

Baru kali ini saya menyentuh mysql, dan ingin membuat table yang berisi kolom
diantaranya adalah `post`. Kolom `post` ini harus bisa menyimpan unicode value,
diantaranya adalah arabic.

Ketika *testing* sampai ke table `post` untuk blog, masalah ini bermula. Saya
test menggunakan kata مقدمة dan... 

```python
InternalError: (1366, "Incorrect string value:
```

## Solusi

Ini solusi saya, buat ulang databasenya dengan *menge-set* encoding yang
sesuai. Karena saya masih dalam tahap testing. Hehe.

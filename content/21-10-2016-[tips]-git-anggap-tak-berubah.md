Title: [Tips] Git Anggap Tak Berubah
Date: 2016-10-21 23:02
Category: Tips
Tags: git, credentials, assume-unchanged
Slug: [tips]-git-anggap-tak-berubah
Authors: Ihfazhillah
Summary: dengan tips ini, anda dapat menulis kode yang butuh credentials tanpa harus membaginya ke publik


Misalkan anda ingin menulis kode dan menyimpannya di [github]('https://github.com'). Namun, di kode anda terdapat credentials, yang anda perlukan untuk **testing**. Jangan sampai anda ikut bagikan **kode rahasia** anda ini.

Ada beberapa langkah untuk mengantisipasinya:

- Buat file terpisah untuk credentials.py, isi dengan dummy credential. misal 
```python
username = 'fakeusername'
password = 'fakepassword'
```
- Add and Commit 
- Ketikkan perintah `git update-index --assume-unchanged credentials.py`

Setelah ini, isi `username` dan `password` dengan yang asli. Check `git status`, apakah ada perubahan? Kalau tidak ada, maka langkah anda berhasil. Selamat.
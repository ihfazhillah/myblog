Title: Kill Uwsgi Process
Slug: kill-stop-uwsgi-process-how-to
Date: 2017-12-13 23:16
Category: Error
Tags: uwsgi, kill, process, python, flask
Authors: Ihfazhillah
Summary: Uwsgi process sudah dimatikan, tapi port masih ter-pakai????


# Bismillah

Saya akhir akhir ini, ada projek dan mencoba untuk menggunakan uwsgi daripada gunicorn. Semua berjalan baik sampai ketika kita butuh `supervisorctl restart namaapp`. 

Taraa... Error ketika proses start kembali. Kenapa? 

Setelah dilihat, ternyata port-nya belum mati, masih terpakai.

Habis research, maka lakukan

```
fuser -k nomorport/tcp
# contoh, port yang digunakan 1234
fuser -k 1234/tcp
```

Sumber: https://askubuntu.com/questions/592261/how-to-exit-from-uwsgi-server-process

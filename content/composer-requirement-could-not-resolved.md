Title: Composer - Requirements could not be resolved
Slug: composer-requirements-could-not-be-resolved
Date: 2018-02-02 20:41
Category: Error
Tags: composer, installation failed, requirements not be resolved, requirements error, composer install
Authors: Ihfazhillah
Summary: instalasi composer gagal karena requirements tidak didapatkan? Bila anda menggunakan linux (debian), ada kabar gembira untuk kamu.

# Bismillah

Suatu ketika, kamu mengetikkan `composer install`. Kamu sudah menunggu lama, tidak ada kembalian, seakan - akan `composer` sedang *freeze*. Tiba tiba, installasi gagal, dan kamu mendapatkan keluaran kira kira begini: 

```
Problem 1:
- Installation request for .... 
- ..... requires xxxx
```

## Tentang Error

untuk menggunakan package yang akan di install, anda butuh menginstall package `xxx` tersebut.

## Solusi

Perhatikan versi php anda. Saya ambil contoh disini dengan php versi 7. dan `xxx` disini adalah `ext-curl`. 
Jadi, package yang perlu kamu install adalah **hilangkan kata `ext` bila ada** menjadi `php7.0-curl`.

kalau `xxx` adalah `ext-gd`, maka package yang kamu install adalah `php7.0-gd`.

# Penutup

Dalam dunia per-codingan / software development, ketika kamu dapat pesan error dari aplikasi yang kamu tulis / tools yang kamu gunakan, jangan anggap kiamat datang yah. Perhatikan baik baik pesan error yang disampaikan. Bila belum dapat, tinggal *copas* kan line demi line error ke google search.




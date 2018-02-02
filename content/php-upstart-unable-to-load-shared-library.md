Title: PHP Unable To Load Shared Library 
Slug: php-unable-to-load-shared-library
Date: 2018-02-02 21:30
Category: Error
Tags: php error, php unable to load shared library, php cannot start
Authors: Ihfazhillah
Summary: Mungkin kamu habis upgrade php kamu dari 5 ke 7. Ketika mau cek versi, eeh, keluar banyak warning. Bisa di coba nih solusinya...

# Bismillah

Kemarin, teman kerja setelah upgrade php, dia mendapatkan error / warning lah pasnya sebagai berikut: 

```
PHP Warning: PHP Startup : Unable to load shared library xxxx.so .....
```

## Solusi
Setelah melakukan pencarian, ternyata solusi gampang. Anda hanya perlu menginstall package tersebut. Lagi lagi, saya akan mencontohkan dengan debian - ini karena saya menggunakan debian (okay, hehe) -.

contoh: 
```
.... /usr/lib/xxxx/xml.so
.... /usr/lib/xxxx/simplexml.so
```

maka yang perlu anda install, nama file tanpa `.so`.

jadi install `php7.0-xml` dan `php7.0-simplexml`

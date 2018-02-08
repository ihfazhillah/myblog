Title: PHP Perbedaan Antara php://input dan $_POST
Slug: php-perbedaan-antara-php-input-dan-post
Date: 2018-02-05 22:21
Category: PHP
Tags: perbedaan, php://input, php, post, $_post, laravel, request
Authors: Ihfazhillah
Summary: Memahami perbedaan antara php://input dan $_POST
Status: Draft

# Bismillah

Dalam verifikasi signature di stripe menggunakan library, kita diminta untuk memasukkan payload dari stripe sebagai parameter pertama dalam fungsi yang disediakan. Saat itu, saya menggunakan framework herbert, yang notabene variable `$http` menggunakan object `Request` miliknya Laravel. Content-type request dari stripe adalah json. Jadi, saya ambil kesimpulan untuk mengambil data dengan `$http->json()`, kemudian saya jadikan json string lagi. Akan tetapi, signature selalu salah. Heran, dan tidak dapat jawabannya.

Didalam contoh, untuk mendapatkan `$payload`, menggunakan `@file_get_contents("php://input");`. Hmmt, berarti saya harus ambil raw data dari request tepat setelah header selesai, sampaii akhir. 

Setelah cari cari, ternyata menggunakan `$http->getContent()`.

Rasa penasaran saya masih ada, apa sih perbedaan antara `$_post` dengan `php://input` ?

https://stackoverflow.com/questions/8893574/php-php-input-vs-post

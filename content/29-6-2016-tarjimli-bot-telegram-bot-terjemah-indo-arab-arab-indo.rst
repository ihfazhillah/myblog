TarjimLi bot Telegram Bot Terjemah Indo Arab Arab Indo
#######################################################

:date: 2016-6-29 20:11
:tags: qaamus, telegram, terjemah
:category: Project
:slug: tarjimli-bot-telegram-bot-terjemah-indo-arab-arab-indo
:authors: Ihfazhillah
:summary: Bot untuk terjemah indo arab dan sebaliknya (versi yang akan datang)

Bismillah,
**TarjimLi** bot adalah telegram bot yang memberikan layanan berupa terjemah indonesia arab dan juga sebaliknya (akan ada pada versi berikutnya). Bot ini beralamat di `@tarjimli_bot <http://telegram.me/tarjimli_bot>`_. 

Adapun terjemah indonesia arab, maka saya menggunakan modul yang telah saya buat sebelumnya yaitu `qaamus-python <https://github.com/ihfazhillah/qaamus-python>`_ (atau `disini <{static}26-6-2016-[project]-qaamus-python-tool-untuk-terjemah-indo-arab.md>`_ untuk review dari blog ini) dengan mengubah controllernya (ini akan menjadi perubahan juga untuk ``qaamus-python`` nya.

Daftar Perintah
=========================
    Didalam telegram bot, yang namanya *command* atau perintah, itu adalah kata yang di awali dengan *garing* `/`.

Untuk saat ini, daftar perintah yang ada adalah sebagai berikut:

#. `/start` Untuk menampilkan pesan intro. Ini biasanya ada tombol bertuliskan start dibawah ketika anda baru masuk ke bot.
#. `/help` Untuk menampilkan daftar perintah .
#. `/idar` Untuk terjemahan indonesia arab. Setelah perintah ini harus ada query. Bila tidak ada, maka bot tidak akan memberikan balasan. 
      misal: `/idar mobil pickup`
#. `/angka` Untuk terjemahan angka. Setelah perintah ini harus ada query. Dan bila tidak diberikan, maka tidak akan ada balasan.
    misal: `/angka 1234`
#. `/pegon` Untuk meng-*arab*-kan tulisan latin. Setelah perintah ini harus juga ada query. Kalau tidak ada, maka tidak akan memberikan balasan.
     misal: `/pegon surabaya`

Daftar Layanan
===========================
Dari daftar perintah diatas, kita bisa tahu -untuk saat ini- layanan yang tersedia di dalam tarjimli bot hanya ada 3:

1. Terjemah Indonesia Arab
2. Terjemah angka numerik, misal 123
3. Mengarabkan tulisan latin

Kenapa Menggunakan Telegram ?
===================================
Di tahun kemarin, saya sempat membuat bot serupa, namun menggunakan whatsapp. Akan tetapi, karena dari whatsapp sendiri tidak mengijinkan penggunaan bot, dan mereka serius akan hal ini, banyak terjadi nomor yang ter-block. Daan, setelah berjalan hampir 6 bulan, nomor bot ini ter-block oleh whatsapp.
Kalau masih ingat, beberapa layanan yang ada kemarin adalah:

1. terjemah arab indo dan sebaliknya
2. hadith, pengecekan keabsahan hadith lewat `dorar.net <http://dorar.net>`_ 
3. cek ongkir **jne**, **tiki**, dan **pos** menggunakan API gratis dari RajaOngkir.

Inilah, diantara alasan saya menggunakan telegram untuk pembuatan bot.

Dimana Bot ini Hidup?
=============================
Sampai saat ini, bot ini hidup di Samsung Galaxy S3 saya dikarenakan keterbatasan dana. Rencananya, saya ingin menyewa vps untuk beberapa bot yang akan saya buat nanti InsyaAlloh. Dan anda bisa ikut support untuk ini.

Support
=============
Bila anda merasa mendapatkan manfaat dengan bot ini, anda bisa me-rate bot ini di `@storebot <tg://resolve?domain=storebot&start=tarjimli_bot>`_ dan memberikan komentar disana.
Anda juga bisa ikut me-like `mading bengkelku fanspage <https://www.facebook.com/madingbengkelku>`_ dan mendapatkan berita terbaru tentang bot ini, dan juga hal hal lain yang berkaitan dengan program/modul/bot yang saya buat.
Di fanspage tsb, anda juga memberikan saran dan kritik tentang bot ini. 
Dan jangan lupa, ikut men-share bot ini dengan harapan banyak orang juga dapat merasakan manfaatnya.

Beberapa Tangkapan Layar
===========================
..  figure:: {static}images/start.png
    :align: center
    :width: 500
    :height: 800
    :alt: start command
    :scale: 50

Perintah Start

..  figure:: {static}images/server_sedang_jalan.png
    :align: center
    :width: 500
    :height: 800
    :alt: start command
    :scale: 50

server sedang jalan

..  figure:: {static}images/pegon_selendangsutra.png
    :align: center
    :width: 500
    :height: 800
    :alt: start command
    :scale: 50

Perintah pegon

..  figure:: {static}images/angka.png
    :align: center
    :width: 500
    :height: 800
    :alt: start command
    :scale: 50

Perintah angka

..  figure:: {static}images/idar_gratis.png
    :align: center
    :width: 500
    :height: 800
    :alt: start command
    :scale: 50

Perintah idar
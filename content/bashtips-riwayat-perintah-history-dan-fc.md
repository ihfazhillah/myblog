Title: #bashtips - Riwayat Perintah (History Dan Fc)
Slug: bashtips-riwayat-perintah-history-dan-fc
Date: 2017-05-07 20:16
Category: Tips
Tags: history, fc, riwayat perintah command line, command line indonesia, menjalankan perintah lama, menjalankan command lama
Authors: Ihfazhillah
Summary: Mengatasi *lupa* perintah yang pernah kita jalankan di linux.

# Bismillah

Seringkali saya tidak ingat, alamat IP server yang saya gunakan untuk bekerja. Sehingga, sering kali saya harus menekan tombol panah atas berkali kali sampai saya dapatkan perintah yang pernah saya jalankan.

Di terminal linux sendiri, ada fasilitas penyimpanan riwayat perintah yang kita pernah jalankan. Diantaranya tadi, dengan menekan panah atas beberapa kali.

Akan tetapi, cara ini kurang efisien. Terlebih ketika perintah ini sudah kita jalankan setelah waktu berselang lama. 

## Perintah `history`

Perintah `history` memungkinkan anda untuk melihat riwayat perintah yang pernah anda tuliskan. Anda juga dapat menghapus riwayat anda, baik keseluruhan maupun pada baris tertentu.

```bash
$ history # ini me-list semua riwayat
$ history 10 # me-list 10 riwayat terakhir
$ history -d 10 # menghapus riwayat baris ke sepuluh
$ history -c # menghapus semua riwayat
```

Untuk perintah lainnya, anda dapat melihatnya di `man history` atau `history --help`

## Perintah `fc`

Ada lagi perintah lain yang berkaitan dengan riwayat perintah yang pernah kita jalankan. Yaitu `fc`. Berangkat dari rasa penasaran saya ketika mengetikkan `fc` kemudian tab (saya waktu itu sedang berurusan dengan font, karena font commandnya didahului dengan `fc-`), maka saya cari dengan `man fc`. Tidak ada. Oke, `fc --help`. Nah, akhirnya sangat berguna juga perintah ini.

Oke, balik lagi.

Perintah `fc` ini digunakan untuk melist atau mengedit, atau malah menjalankan ulang perintah yang pernah kita lakukan.

Bagaimana? Misal kita lupa nomor IP, dan butuh ssh ulang. Maka kita lihat list riwayat, kemudian kita jalankan ulang lagi tanpa menulis / copas perintah itu. 

Perhatikan perintah - perintah berikut

```bash
$ fc -l # untuk menampilkan riwayat default 17 baris
$ fc -l 100 # untuk menampilkan 100 baris riwayat 
$ fc 100 # meng-edit baris ke 100, dan ketika kita tutup akan kita akan menjalankan perintah tersebut
$ fc -s 100 # jalankan kembali perintah di baris ke 100 tanpa harus mengedit
```

Asyik bukan?

## Kesimpulan

Dua perintah diatas, kurang lebih sama fungsinya. Akan tetapi, perintah `fc` mempunyai kelebihan yaitu **manipulasi perintah**

Namun, yang saya lakukan untuk masalah diatas adalah:

1. Cari perintah yang kurang lebih sama dengan yang dahulu saya jalankan. Dalam hal ini ssh.
2. Jalankan line tersebut dengan `fc -s n` dimana `n` adalah baris perintah itu bersemayam.

```bash
$ history | grep ssh --> output: 100 ssh root@nomorIP, misalnya
$ fc -s 100
```

bagaimana? Membantu bukan ? 

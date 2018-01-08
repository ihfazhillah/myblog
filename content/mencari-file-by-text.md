Title: [command-line] Mencari File Sesuai Text Pattern
Slug: command-line-mencari-file-sesuai-text-pattern
Date: 2018-01-18 16:44
Category: Tips
Tags: tips, cmd, bash, command-line, linux, grep, pattern
Authors: Ihfazhillah
Summary: Tips untuk cari file sesuai text pattern yang ada di dalamnya. Check this out..!!

# Bismillah,

Ketika itu, saya harus mengubah beberapa file, karena perubahan *constant* menjadi *function*. Yang saya ingat, file yang perlu saya ubah ini banyak, tapi saya lupa dimana saja. Kalau saya harus buka satu persatu, ini akan memakan banyak waktu. Dan mungkin ada yang terluput. Jurus sakti pun keluar. Googling.

## Solusi

Gunakan perintah berikut : 

```
grep -rnw "/path" -e "pattern"
```

## Penjelasan

`grep` sendiri adalah utilitas yang dapat digunakan untuk melakukan **pencarian pattern** di **setiap file**.

`-e` adalah flag untuk **matching control**. Gunakan string pattern sebagai pattern. Lawannya adalah `-f`. Yaitu, gunakan file sebagai source pattern, baca *line by line*

`-r` recursive, terus ikuti pohon file kebawah (atau keatas?)

`-n` tampilkan nomor baris.

`-w` cocokkan satu kata.

## Contoh

`grep -rnw "src/scenes" -e "myUserId"` : cari semua file, dibawah `src/scenes` folder dan turunannya, yang cocok dengan kata `myUserId` dan tampilkan nomor baris.

[Sumber](https://stackoverflow.com/questions/16956810/how-do-i-find-all-files-containing-specific-text-on-linux)

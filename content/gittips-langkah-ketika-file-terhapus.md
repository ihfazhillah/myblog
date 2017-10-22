Title: #GitTips - Langkah Ketika File Terhapus
Slug: gittips-langkah-ketika-file-terhapus
Date: 2017-05-07 11:26
Category: Tips
Tags: git-tips, git, lupa hapus, lupa terhapus, lupa diubah, branch baru, menghapus branch
Authors: Ihfazhillah
Summary: Kamu lupa menghapus file, padahal file tersebut sangat penting. Bila kamu pakai git, maka ada kabar gembira untukmu.

# Bismillah

Dhuarr !!

Tiba tiba kamu tersadar, ternyata kamu tidak sengaja *ngetikkan* perintah `rm *`. Dan apa yang terjadi? Kamu sudah menghapus semua file yang ada di folder kamu bekerja. Padahal, pekerjaan-mu sudah hampir selesai.

Pernahkah kamu pusing karena kejadian ini?

Bila kamu menggunakan `git`, maka kamu punya kabar gembira.

## Langkah

1. Buat `branch` baru
2. `commit`-kan perubahan yang tidak diinginkan tersebut
3. pindah ke `branch` master/yang kamu sedang bekerja
4. hapus `branch` baru tersebut

## Ilustrasi

Misalkan, kamu sedang bekerja di *branch* `master`, dan tidak sengaja kamu mengetikkan perintah diatas. Maka, 

```python
$ git checkout -b tidak_diinginkan
$ git commit -am "ini commit penghapusan yang tidak diinginkan"
$ git checkout master
$ git branch -D tidak_diinginkan
```

nah, akhirnya kamu sudah kembali ke *stage* dimana kamu belum menghapus file tersebut.

## Kesimpulan

Ini, adalah langkah sederhana yang bisa kamu lakukan ketika kamu kelupaan menghapus atau mengedit file dan ingin mengembalikan seperti sedia kala sebelum perubahan tersebut.


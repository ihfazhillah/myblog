Title: Generate File Patch Dari Github Dan Apply Patch
Slug: generate-file-patch-dari-github-dan-apply-patch
Date: 2017-04-30 16:44
Category: Tips
Tags: cookiecutter, git-patch, buat patch file, apply patch file, jinja2 extension cookiecutter
Authors: Ihfazhillah
Summary: Tips add buat file patch dari github dan apply


# **Bismillah**

## Pendahuluan
Dengan [github](http://github.com), dengan mudah kita bisa membuat file `patch` dari sebuah `pull requests`. Terlebih, ketika si-*empunya* repository belum menyetujui `PR` ini, tapi kamu sudah *kesusu* untuk memakai fitur yang ada di `PR` ini.

Sebagai contoh, pada projek [cookiecutter](https://github.com/audreyr/cookiecutter), ada fitur yang ditawarkan di versi terakhir (`1.5.x`), yaitu **kita dapat menambahkan `jinja2` extensions dengan mengkonfigurasikan di `cookiecutter.json`**. Namun sayangnya, `jinja2` extension ini harus terinstall pada *system-wide*. Kalau kita buat sendiri, taruh di direktori template, maka akan ada pesan `ImportError`. *Alhamdulillah*, ada yang mengirimkan `PR` [ini](https://github.com/audreyr/cookiecutter/pull/892). Nah, `PR` ini belum di setujui oleh bu audreyr, tapi saya harus pakai pr ini. 

## How To ?

Caranya: 

1. tambahkan `.patch` ke akhir alamat `PR` tadi. 
2. kemudian **unduh** file tersebut. 
3. Dan Jalankan perintah berikut `git am patchfile`

Mudah bukan?

## Akhirnya

Pada akhirnya, untuk menggunakannya saya install aplikasi ini dengan cara:

1. clone git repo tersebut
2. patch dengan file tadi
3. install dengan pip ke virtual environment project kita tadi

Sedikit membantu bukan ? 

Title: [Project] Qaamus-python Tool untuk Terjemah Indo Arab
Date: 2016-6-26 10:22
Category: Project
Tags: tool, qaamus, terjemah cli, modul terjemah, indo-arab, indonesia, arab
Slug: [project]-qaamus-python-tool-untuk-terjemah-indo-arab
Authors: Ihfazhillah
Summary: Tool / Modul sederhana untuk terjemah indonesia arab.

Bismillah,

[qaamus](http://qaamus.com) adalah website yang memberikan layanan penterjemahan dari indonesia ke
arab. Saat ini, [qaamus](http://qaamus.com) memiliki beberapa layanan:

- terjemah indonesia arab : dengan gabungan antara bing translator dengan *ketikan* ulang kamus munawwir, memberikan hasil yang *hampir* mendekati hasil yang pas.
-  pegon : layanan ini, mengubah kata kata kedalam tulisan arab. Tanpa menterjemahkannya
-  angka : adapun layanan ini, dia memberikan terjemahan angka dengan query angka yang anda berikan

disitu, juga ada tab yang berisi kata kata bijak. Ter-list-kan disitu, dan andapun dapat *mengontak* admin untuk memberikan saran kata kata bijak yang ingin anda masukkan.

## qaamus-python

Adapun `qaamus-python`, maka ini adalah script untuk query ke website diatas. Memiliki ke-3 layanan dasar diatas. 
Saat ini, per-rilis 2.0.1 script ini sudah di*test* di python 2.7 dan 3.5 di linux ubuntu versi .... (lupa saya, bukan penghafal seri).

### Beberapa yang mungkin membuat anda tertarik:
- Kemudahan syntax
- cli-tool
- template dapat dimodifikasi (untuk rilis mendatang bisa lebih mudah, tanpa mengubah controller)
- gampang dimodifikasi (opensource, anda dapat melihat, membaca, menuliskan ulang source code), dengna lisensi MIT
- tested di python versi 2.7 dan 3.5 

### Installasi
Ada beberapa cara untuk menginstall modul ini:

1. installasi dari pypi
cukup mudah, karena hanya dengan mengetikkan
`pip install qaamus`
atau kalau anda ingin meng-upgrade
`pip install -U qaamus`

2. installasi dari github (masih menggunakan pip installer)
`pip install git+https://github.com/ihfazhillah/qaamus-python`

3. installasi dari github (dengan meng-clone or download zip)
```bash
git clone https://github.com/ihfazhillah/qaamus-python
cd qaamus-python
python setup.py install
```

### ScreenShot
![Tangkapan Layar qaamus](https://raw.githubusercontent.com/ihfazhillah/qaamus-python/master/screenshot/qaamus1.gif)


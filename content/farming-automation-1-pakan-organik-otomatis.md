Title: Pakan Lele Organik Otomatis
Slug: pakan-lele-organik-otomatis
Date: 2023-09-10 09:12
Tags: farming automation, raspberry pi pico, lele organik
Category: Farming Automation
Summary: Cerita tentang otomatisasi pemberian pakan lele organik

# Bismillah

Beberapa bulan ini, saya sedang explore berkaitan dengan otomatisasi pemberian pakan ikan. Karena yang terbiasa adalah pakan berbentuk pelet, hint pertama yang ada dikepala saya adalah, mencari auto fish feeder dan mempelajari alurnya.

Okay, sudah banyak tutorial baik yang sederhana menggunakan servo murah dan botol bekas, atau pakai gentong pakai dinamo dan pelempar pakan, atau bahkan 3d printing. Banyak.

Setelah cerita dan berkonsultasi sama tetangga, dapat konsep yang bernama Taga, kepanjangan dari Tanpa airator dan ganti air dari [Joyo Farm](https://www.indonetwork.co.id/product/joyo-farm-probiotik-7098105). 

Inti dari konsepnya adalah untuk meminimalisir pergantian air (zero water excange), mengurangi jumlah penggunaan pelet (kalau mau hybrid yah), dan mengurangi penggunaan airator.

Btw, saya disini tidak banyak bahas masalah konsep ini yah. Karena basic saya di software yang nyemplung dikit dikit di hardware (bisa jadi nantinya nyemplung banyak), maka saya fokus di "otomatisasi". Kalau mau tanya tanya lebih lanjut, silahkan hubungi [Joyo Farm](https://www.indonetwork.co.id/product/joyo-farm-probiotik-7098105) secara langsung.

### Pemberian pakan

Setelah saya konsultasi, ternyata pemberian pakannya bukan pakan apung. Sehingga pencarian saya sebelumnya tidak terpakai disini.

Pakan berbentuk semacam lumpur, kita aduk dahulu, kemudian kita berikan ke kolam, dan masukkan air lagi ke lumbung pakannya.

Pemberian pakan adalah 3 kali sehari, jam 8, jam 16 dan jam 22. 

Kita akan otomatisasi itu semua. 

### Solusi

Setelah melakukan "experiment" kecil kecilan, akhirnya saya membuat alur versi pertama seperti ini:

1. alat mengaduk pakan dalam gentong
2. air masuk kedalam gentong dengan bantuan pompa, sehingga membuat dorongan untuk mengeluarkan air melalui lobang yang dipersiapkan.

Air yang keluar tersebut sudah tercampur dengan pakan yang sudah kita aduk tadi.

Berikut hasilnya

<iframe width="560" height="315" src="https://www.youtube.com/embed/lojRU8Jl6Eg?si=ftF74Oy2zYEWHi8q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Kesimpulan

Banyak kekurangan? Ya betul. Tapi dengan menjalaninya, hampir tiap hari saya dan istri mendapatkan ide ide baru, untuk menjadikan alat ini lebih efisien dan benar benar mentransfer pakan ke lele, tidak hanya air yang bersirkulasi.

Beberapa hal yang akan kami update untuk versi kedua:

1. Mixer dan Dinamo yang akan kita update
2. Daripada harus membuat tekanan, kenapa tidak kita keluarkan dari samping gentong? Sehingga tidak ada tekanan air ketutupnya dan meminimalisir air keluar sia sia.

2 hal ini adalah mayor manurut saya untuk dilakukan explorasi, terutama yang pertama. Sehingga pakan itu bener bener sampai ke lele, dan tidak mengendap di bawah dan mengeras.

Saat ini fokusnya adalah otomatisasi, jadi jangan tanya dulu perkembangannya.

### Apa yang kita pelajari?

Banyak, diantaranya:

1. Raspberry pi pico dan micropython. Oleh sebab inilah saya menulis seri berkaitan micropython dan raspberry pi pico. 
2. Elektronika. Ya saya belajar solder menyolder, memahami alur tiap komponen, melakukan perhitungan, dan juga pembuatan PCB. Kamu tahu, v1 pertama ini saya menggunakan PCB lobang satu sisi dan banyak kabel yang lalu lalang :D. 
3. Konsep Dinamo dan hubungan antara torsi dan rpm.
4. Konsep pergiran. Bagaimana membagi beban sehingga dengan dinamo tamiya bisa mengangkat beban lebih dari 30kg.
5. Pertukangan, design 3d, bubut dsb...

Kita pelajari apa yang kita butuhkan saja, belum tentu saya bisa menjelaskan semua tentang itu semua

### Barang yang saya pergunakan?

1. [Raspberry pi pico wifi](https://tokopedia.link/TC3ORrV8XCb)
2. [PCB bolong satu sisi](https://tokopedia.link/1y64Xc58XCb)
3. [Relay 8 channel](https://tokopedia.link/MjyrNL88XCb) (kebanyakan untuk versi ini)
4. [Motor DC 12v 200RPM 1.2KGfCM](https://tokopedia.link/a6UZVNy9XCb)
4. [Pompa DC](https://www.tokopedia.com/mollarofficial/mollar-pp25w-pompa-air-dc-12-volt-push-pump-12v-25-watt?extParam=ivf%3Dfalse%26whid%3D8985&src=topads)
5. Perselangan
6. [Step Down](https://tokopedia.link/uFXohPQ9XCb): Saya gunakan untuk menurunkan tegangan baterai dari 12v ke 5v. Untuk power raspberry pi dan relaynya.
7. [Aki atau baterai 12v](https://tokopedia.link/Rns3zwA9XCb)
8. Resistor. Saya gunakan ini untuk membagi tegangan aki 12v supaya bisa saya baca tegangan akinya dari raspberry pi pico
9. [Solar Panel](https://tokopedia.link/LKS5m6C9XCb). Saran saya, jangan lupa beli SCC dan juga kabel konektornya juga di [toko yang sama](https://tokopedia.link/h1VsQmG9XCb). Supaya tidak bolak balik pesen dan double ongkir jadinya selain harus menunggu lebih lama.
10. [Gentong bekas 30L beserta klemnya](https://www.tokopedia.com/tokohoki7/drum-plastik-ember-plastik-tong-plastik-tong-hdpe-kap-30l-tebal-kuat?extParam=ivf%3Dfalse%26src%3Dsearch&refined=true)
11. Potongan kawat 2mm dari mixer dapur.
12. Tidak lupa kolam 1mx1mx1m (bisa check check [di sini](https://tokopedia.link/GNXyVkaaYCb) atau cari di kota kamu) dan lele serta pakan organiknya.

### Kode?

Adapun kodenya, untuk versi sekarang ada 2 layer:
1. [backend](https://github.com/ihfazhillah/ksatriamuslim_backend/tree/main/ksatria_muslim/irrigation), dan saya tumpangkan di web ksatriamuslim, kode bisa dilihat [di folder ini](https://github.com/ihfazhillah/ksatriamuslim_backend/tree/main/ksatria_muslim/irrigation)
2. [micropython](https://github.com/ihfazhillah/irigation-system/blob/main/irrigation_new_main.py), program untuk otomatisasi di [board raspberrypi pico](https://tokopedia.link/JC2CFLDaYCb) nya.




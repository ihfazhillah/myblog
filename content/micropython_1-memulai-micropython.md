Title: [Micropython 1] Memulai Micropython Menggunakan Raspberry Pi Pico
Slug: micropython-1-memulai-micropython-menggunakan-raspberrypi-pico
Date: 2023-08-10 21:45
Tags: raspberrypi pico, micropython
Category: Micropython
Summary: Microcontroller membuka ruang untuk programmer untuk bisa memprogram almost anything. Raspberry pi pico adalah salah satunya. Kamu bisa memprogramnya menggunakan python. Yuk check bagaimana cara memulainya.

![Raspberry Pi Pico]({filename}images/raspberry_pi_pico_tangan.jpeg)

# Bismillah

Microcontroller adalah semisal komputer kecil yang didesain khusus untuk keperluan tertentu. Semisal untuk mengkontrol led, dinamo, membaca sensor dan sebagainya.

Microcontroller ini membuka ruang untuk para programmer untuk bisa mengatur alat alat elektronik dan mengotomatisasinya. 

Raspberry pi pico adalah salah satunya. Dia bukan "mini komputer" yang lengkap. Memiliki bentuk kecil, memori kecil, prosesor kecil. Beruntungnya, barang ini sudah masuk indonesia. Mau kloningan atau asli, kamu bisa dapatkan.

Untuk memprogram raspberry pi pico, kamu bisa menggunakan bahasa python. Yaitu dengan menggunakan Micropython. Perlu diingat, karena dia bukan komputer lengkap seperti raspberry pi type b, atau yang lainnya, maka tidak semua fitur python tersedia.

### Installasi

Raspberry pi pico punya 3 varian, firmware tiap firmware berbeda:

1. Biasa (tanpa wifi dan bluetooth) : https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2
2. Raspberry pi pico W (dengan wifi) : https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2
3. Raspberry pi pico W (dengan wifi dan bluetooth) : https://datasheets.raspberrypi.com/soft/micropython-firmware-pico-w-130623.uf2?_gl=1*13lvwpj*_ga*MTE4NzE0NzU0Ni4xNjg4Mjk5MDUz*_ga_22FD70LWDS*MTY5MTYyMTU3My43LjAuMTY5MTYyMTU3My4wLjAuMA..

Unduh salah satu sesuai barang yang kamu miliki. Konsultasikan sama penjual dimana kamu beli barang tersebut.

Kemudian, raspberry pi pico kamu ke komputer. 

Secara default, mode pico kamu akan menjadi Mass Storage dengan nama RPI-RP2. 

Drag dan Drop uf2 file yang kamu unduh tadi kedalam root dari folder RPI-RP2 tadi.

Setelah selesai proses copy, pico kamu akan reboot, dan akan berubah mode untuk menjalankan micropython yang bisa kamu akses dengan mode serial.

### Hello world

Install mpremote. 

```pip install mpremote```

Library ini kita gunakan sebagai alat untuk akses REPL-nya micropython, lihat atau ubah file yang ada di device yang menjalankan pico, atau bisa kita pakai untuk mengecek memory daripada pico kamu.

Setelah selesai, jalankan perintah berikut

```mpremote```

Bila `mpremote` kamu jalankan tanpa argument sama sekali, dia akan menjalankan REPL dari raspberry pi pico pertama yang ditemukan oleh aplikasi ini.

Ketikkan

```python
print("hello world dari micropython")
```

Selamat, ini adalah langkah awal kamu bisa memprogram barang kecil tapi powerfull ini.

### Menyala matikan led

Raspberry Pi Pico ini memiliki LED bawaan yang bisa kita program nyala matinya. Tidak seperti seri lainnya, yang mana led digunakan untuk indikator nyala atau tidak, ada proses atau tidak. Di Pico, Led ini mati, dan mereka membiarkan kita untuk memprogramnya.

Tulis ini di REPL

```python
from machine import Pin

onboard_led = Pin(25, Pin.OUT)
onboard_led.value(1)
```

Module `machine` memungkinkan kamu untuk mengatur hardware yang terintegrasi sama chip pico. Class `Pin` sendiri adalah class untuk mengontrol pin pin yang terkoneksi dengan dunia luar.

Adapun angka `25` adalah nomor pin dimana bawaan led pico terkoneksi.

Perlu diperhatikan, Pico seri W menggunakan `LED` daripada `25` sebagai argument pertama.

Argument kedua `Pin.OUT` adalah tanda bahwa kamu yang mengatur hardware tersebut. Misal dalam hal ini menyala matikan LED.

Baris berikutnya, `onboard_led.value(1)`, kamu menginstruksikan pin 25 untuk mendapatkan arus listrik, sehingga led menyala. 

Lalu, bagaimana kamu bisa mematikannya? Mudah, ganti angka value menjadi `0`

```python
onboard_led.toggle()
```

Selain kamu dapat mengontrol secara manual, menyala matikan led dengan memberikan value `0` atau `1`. Micropython juga memberikan shortcut untuk melakukan `toggle`.


### Penutup

Nah, itu dia perkenalan dengan micropython dan juga raspberry pi pico. Kamu bisa membeli barang tersebut di marketplace.

|Type|Link Toko|Harga|
|---|---|---|
|Biasa|[Tokopedia](https://tokopedia.link/DKzqu8Os8Bb)|Rp 139.000|
|Wifi| [Tokopedia](https://tokopedia.link/AddaP58r8Bb)|Rp 170.000|
|Paket Biasa dan paket Getting Started with micropython| [Tokopedia](https://tokopedia.link/C5tY9OGs8Bb)| Rp 265.000|
--------------------------------------------

Nah, untuk belajar, paling cocok kita beli yang langsung paket seperti dalam item yang ke 3, atau [disini](https://tokopedia.link/C5tY9OGs8Bb). Piconya sudah siap pasang di breadboard, dan sudah include beberapa sensor, led, saklar yang siap kamu pakai untuk belajar.

Diseri berikutnya, insyaAlloh kita akan belajar bagaimana mendapatkan data dari dunia luar.

Untuk mematikan pico kamu, tinggal cabut saja dari USB port dan matikan pico kamu.

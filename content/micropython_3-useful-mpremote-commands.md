Title: [Micropython 3] 5 Useful Mpremote Commands
Slug: micropython-3-5-useful-mpremote-commands
Date: 2023-08-26 23:43
Tags: raspberrypi pico, micropython, mpremote, mip
Category: Micropython
Summary: Sebelum mempelajari micropython lebih lanjut, alangkah baiknya untuk mengetahui beberapa perintah dari mpremote untuk mempermudah development dan juga deployment aplikasi kita ke micropython.

# Bismillah

Pada dua seri sebelumnya, kita menuliskan dan menjalankan program kita dari REPLnya micropython. Tidak masalah sih, tapi repot. Iya kan?

Maka dari itu, sebelum kita melanjutkan petualangan dengan micropython, kita akan menelisik lebih lanjut mengenai perintah perintah dari tool `mpremote`. Tidak semua, tapi beberapa yang dapat mempermudah kita melakukan development maupun deployment nantinya.

Di artikel kali ini, saya akan sampaikan beberapa perintah:

1. Masuk REPL (seperti yang lalu)
2. Membaca file yang sudah ada di [raspberry pi pico](https://tokopedia.link/Ppgxp55eACb)
3. Menjalankan script tanpa harus mencopy script ke [raspberry pi pico](https://tokopedia.link/hIQefkKeACb)
4. Menginstall script supaya bisa dijalankan tanpa sambungan komputer
5. Install library


### 1. Masuk REPL

Secara default, memanggil `mpremote` tanpa tambahan apa apa akan memasukkan kamu ke REPL milik micropython. Atau kalau mau lebih spesifik jalankan

```shell
mpremote repl
```

Ada beberapa mode dalam micropython REPL:
1. Normal: Yaitu seperti ketika kamu masuk pertama kali
2. Paste: Tekan `ctrl+e`. Kalau sudah selesai tekan `ctrl+d`

### 2. Membaca file

Terkadang kamu ingin lihat file yang sudah ada di [raspberry pi pico](https://tokopedia.link/5uvJcQLeACb) kamu. Kamu bisa jalankan

```shell
mpremote fs cat main.py
```

Artinya, kamu ingin membaca file `main.py` yang ada di [raspberry pi pico](https://tokopedia.link/5uvJcQLeACb).

atau, kalau mau check directory

```shell
mpremote fs ls
```

### 3. Jalankan Script tanpa install

```shell
mpremote run file_kamu.py
```

`file_kamu.py` adalah file python yang kamu tuliskan di komputer kamu. `mpremote` akan menjalankan file tersebut di micropython intrepeter tanpa melakukan copy file tersebut kedalam device.

Contoh saja, buat file baru `push_button.py` dan isi dengan perintah seperti berikut

```python
from machine import Pin
import time

button = Pin(15, Pin.IN, Pin.PULL_DOWN)
led = Pin("LED", Pin.OUT) # atau ganti "LED" dengan 25 kalau menggunakan pico biasa

while True:
    if button.value() == 1:
        led.toggle()
    time.sleep(0.5)
```

kemudian jalankan

```shell
mpremote run push_button.py
```

Untuk skema bisa lihat ke [artikel yang lalu berikut ini](https://blog.ihfazh.com/micropython-2-control-device-dari-luar-menggunakan-push-button)

### 4. Install Script Agar bisa dijalankan tanpa komputer

Microcontroller kurang lengkap kalau harus selalu menancap dengan komputer. Untuk bisa menjalankan program setiap kali microcontroller nyala, maka buat file bernama `main.py`.
Micropython ketika menyala, akan otomatis menjalankan file tersebut.

Lalu, bagaimana menginstall nya? Mudah

```shell
mpremote cp push_button.py :main.py + reset 0
```

Tenang, mudah saja. `cp push_button.py :main.py`. Kopi file `push_button.py` ke device dan ubah menjadi file yang bernama `main.py`. Untuk perintah copy,  awalan `:` berarti alamat dalam device.

`+` adalah pemisah antar satu perintah dengan perintah yang lainnya. 

`reset 0` artinya restart device.

### 5. Install Library

Terkadang kita butuh library tambahan selain yang kita tuliskan. Misal `urequests` adalah library untuk mudahkan komunikasi API dengan interface seperti package `requests`. Atau `umqtt.simple` untuk interaksi dengan protokol `mqtt`. Bagaimana installnya?

```shell
mpremote mip urequests
```

## Penutup

Nah, itu dia 5 command yang berguna untuk mempermudah kamu melakukan development dan deployment aplikasi pada micropython. Untuk perintah perintah lainnya, kamu bisa konsultasi lebih lanjut ke [dokumentasi intinya](https://docs.micropython.org/en/latest/reference/mpremote.html). 

Tentunya kurang lengkap bila hanya membaca, jangan lupa praktek. Kamu bisa membeli [raspberry pi pico dengan paket yang cukup untuk explore seri seri saya ini di sini](https://tokopedia.link/5uvJcQLeACb). [Toko tersebut](https://tokopedia.link/Ppgxp55eACb) menjual raspberry pi pico original dan bukan imitasi. Happy Hacking !!

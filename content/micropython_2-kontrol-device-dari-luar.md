Title: [Micropython 2] Kontrol Device Dari Luar Menggunakan Push Button
Slug: micropython-2-control-device-dari-luar-menggunakan-push-button
Date: 2023-08-17 07:30
Tags: raspberrypi pico, micropython, saklar, push button
Category: Micropython
Summary: Kali ini kita akan belajar bagaimana menggunakan push button untuk mengontrol internal led dari raspberry pi pico. Kamu akan memhami perbedaan antara Pin.IN dan Pin.OUT disini.

![Contoh Sambungan]({filename}images/push_button_breadboard.png)

# Bismillah

Pada [seri yang telah lalu](https://blog.ihfazh.com/micropython-1-memulai-micropython-menggunakan-raspberrypi-pico), kita dapat mengontrol internal led menggunakan program. Untuk mendefinisikan bahwa **kita yang akan mengontrol** maka kita menggunakan `Pin.OUT`. Sehingga, kita dapat mengubah value menjadi 1 dan led akan menyala, ketika kita ubah menjadi 0, led akan mati.

Lalu, bagaimana caranya kita menerima perintah dari dunia luar? Sebagai contoh dengan menggunakan push button? Ketika kita tekan push button, maka led akan menyala. Ketika kita lepas push buttonnya led akan mati?

Micropython punya konstanta `Pin.IN`. Dengan memasukkannya sebagai argumen kedua sebagain ganti dari `Pin.OUT`, kita dapat mendapatkan value dari push button tersebut, apakah value nya adalah 1 atau 0.

## Parts

Saya asumsikan bahwa kamu punya raspberry pi pico dan membeli paket [getting started with raspberry pi pico](https://tokopedia.link/SjEhbNpckCb). Sehingga kamu sudah punya pico, breadboard, beberapa kabel jumper dan juga push button.

Kalau belum, ini yang kamu butuhkan

|Part| toko                                                                                                                                                    | rentang harga |
|:---|---------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
|Raspberry pi pico w| [Tokopedia 1](https://tokopedia.link/nelKTdtbkCb), [Tokopedia 2](https://tokopedia.link/pqUQk4vbkCb), [Tokopedia 3](https://tokopedia.link/dTYcQZybkCb) | Rp 180.000,-  |
|Breadbord| [Tokopedia 1](https://tokopedia.link/eIAbJEFbkCb), [Tokopedia 2](https://tokopedia.link/dpyJGBJbkCb)                                                    | Rp 10.000,-   |
|Push button| [Tokopedia 1](https://tokopedia.link/WvKOYMQbkCb), [Tokopedia 2](https://tokopedia.link/IxtJRpTbkCb), [Tokopedia 3](https://tokopedia.link/HM2G8sXbkCb) | Rp 1.000,-    |
|kabel jumper male to male| [Tokopedia 1](https://tokopedia.link/BcRNMy4bkCb), [Tokopedia 2](https://tokopedia.link/N2427F9bkCb)                                  | Rp 12.000,-   |

## Skema

Perhatikan, push button memiliki 4 kaki. Bagian yang saya beri tanda saling terkoneksi. Jadi, kita butuh sambungkan salah satu, dari yang depan ke pin `3v3` (Power). Dan salah satu dari yang belakang ke Pin 15.

![Push Button]({filename}images/push_button.jpeg)

Pin yang perlu disambung

![Pin yang perlu dihubungkan]({filename}images/micropython_2_pinout.png)

Contoh sambungan
![Contoh Sambungan]({filename}images/push_button_breadboard.png)

## Mendapatkan State Tekan
Asumsi saya, kamu sudah menginstall `mpremote` sebagaimana yang telah dijelaskan pada artikel sebelumnya. Ketik `mpremote` di terminal dan enter.

Selanjutnya, ketik kode di bawah ini:

```python
from machine import Pin
import time

button = Pin(15, Pin.IN, Pin.PULL_DOWN)

while True:
    print(button.value())
    time.sleep(0.5)
```

Kode diatas sangatlah simple. Yang kita lakukan adalah membaca pin 15 sebagai masukan.

Kemudian kita melakukan infinite loop untuk melihat value dari button.

Terakhir, kita melakukan sleep selama 0.5 detik.

Kamu akan melihat value adalah `0` ketika kondisi button tidak kamu tekan. dan `1` ketika button kamu tekan.


### Kontrol Led dengan Button

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

Semua hampir sama seperti sebelumnya, hanya saja kali ini kita menyalakan atau mematikan led menggunakan push button.
Tekanan pertama berarti menyalakan. Kemudian tekanan selanjutnya berarti mematikan. Dan begitu seterusnya

## Penutup

class `Pin` bisa kita gunakan untuk mengatur dan bisa juga kita gunakan untuk menerima perintah. Argumen pertama adalah ID dari pin, dan yang kedua adalah state dia mau jadi apa, input atau output.

Tugas untuk kamu:

1. Buat ketika button kamu tekan, led menyala. Ketika button kamu lepas, led mati.

Selamat mencoba.

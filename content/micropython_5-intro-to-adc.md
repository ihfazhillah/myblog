Title: [Micropython 5] Membaca Potentiometer Menggunakan Micropython
Slug: micropython-5-membaca-potentio-meter-menggunakan-micropython
Date: 2023-09-15 21:09
Tags: raspberrypi pico, micropython, potentiometer, voltage divider, adc
Category: Micropython
Summary: Selain kita bisa membaca on dan off dari suatu pin, kita juga bisa membaca value selain on dan off. Misal kita ingin mengetahui berapa voltase baterai yang sedang kita gunakan. Atau seberapa putaran potentiometer sehingga kita bisa tahu berapa volumenya. Semuanya menjadi mungkin menggunakan program yang bernama ADC. Analog to Digital Converter.


[![Potentio]({filename}images/potentio.jpeg)](https://tokopedia.link/Oc4i60jo8Cb)

# Bismillah

Potentiometer adalah pegangan yang biasa kita putar ketika mengatur suatu volume. Atau semacam pegangan di motor bagian kanan untuk mengatur gas. 

Di seri ini, kita akan mempelajari bagaimana menggunakan ADC Analog to Digital Converter yang bisa kita gunakan untuk membaca value dari potentiometer.

Seperti biasa, asumsi saya kamu telah membeli paket [Get Started With Micropython In Raspberry Pi Pico](https://tokopedia.link/mY83NSZNHCb) karena semua yang kita butuhkan di seri seri awal ini ada disana semua. Bila tidak, maka berikut beberapa alat yang kamu perlukan:

1. [Breadboard](https://tokopedia.link/QkgWSqRYICb)
2. [Raspberry pi pico](https://tokopedia.link/Rq0eCOYYICb)
3. [Potentiometer 10K](https://tokopedia.link/Oc4i60jo8Cb)
4. Kabel data micro usb
5. Beberapa kabel jumper male to male

### ADC

Di seri-seri sebelumnya, kita hanya bisa membaca on off dari push button. Itu adalah representasi dari high dan low, atau 1 dan 0. Lalu, bagaimana dengan membaca suara, temperature, voltase baterai atau hal hal lain yang hasil keluarannya tidak hanya 1 dan 0?

Dengan fitur ADC yang tertanam di raspberry pi pico, kita bisa melakukan itu semua. Raspberry pi pico menggunakan resolusi 12-bit untuk ADC-nya. Sehingga rentang angka yang akan kamu dapatkan ketika membaca dari Pin khusus ADC adalah 0 - 4095.

Namun di micropython, semua boards diseragamkan untuk menggunakan resolusi 16-bit. Sehingga kamu akan mendapatkan angka pada rentang 0 - 65535.

Pin ADC yang tersedia untuk kita pakai ada 3. **Pin 26, 27 dan 28**.

![Pinout ADC]({filename}images/pinout-adc.png)
Lihat https://pico.pinout.xyz/

### Potentiometer

[![Potentio Meter](https://www.olelectronics.in/wp-content/uploads/Metal-Potentiometer-4.jpg)](https://tokopedia.link/QCvnrqp28Cb)
Gambar dari https://www.olelectronics.in/product/10k-potentiometer-metal/


Potentiometer ini memiliki 3 kaki. Kaki tengah adalah kaki yang perlu kamu hubungkan ke salah satu Pin yang khusus untuk ADC tadi. Bisa 26, 27 atau 28. Adapun kaki kanan dan kirinya, salah satu kamu masukkan ke pin power 3.3v, dan satunya hubungkan ke pin ground. 

Tidak masalah terbalik, dia hanya menentukan arah putarannya. 

### Kode

Ketikkan kode berikut dan simpan dengan nama `potentio.py`

```python
from machine import ADC
import time

potentio = ADC(26)

while True:
    print(f"Value sekarang adalah: {potentio.read_16()}")
    time.sleep(0.5)
```

Pertama kita definisikan variable `potentio` ke `ADC(26)` karena kita hubungkan kaki tengah ke pin 26. Bila kamu menghubungkan ke pin lainnya, ubah angka pin tersebut.

Lalu di `while loop` kita baca value potentio menggunakan method `read_16()`

Jalankan dengan `mpremote run potentio.py` dan lihat hasilnya di console.

Kamu akan dapati bahwa angka akan berubah ubah dari besar ke kecil atau sebaliknya ketika kita memutar potentionya.

Kalau sudah, coba balik antara positif dan ground nya kemudian putar putar potentionya. Kamu akan dapati bahwa perubahan dari besar ke kecil atau sebaliknya akan terbalik.

### Mendapatkan voltase keluaran

Mari berhitung sejenak. 

Bila keluaran dari potentio adalah mendekati 0, maka kita anggap 0v. Bila keluaran dari potentio mendekati 65535, maka kita anggap voltasenya adalah 3.3v.

```
0v = 0
3.3v = 65535
?v = 50000
```

Kita cari pengalinya dengan rumus `3.3 / 65535`

Lalu hasil pengali tersebut kita gunakan untuk mengalikan `50000`. Akhirnya kita dapatkan voltase akhirnya. 

Kemudian kita ubah logika diatas menjadi kode berikut ini:

```python
from machine import ADC
import time

potentio = ADC(26)
pengali = 3.3 / 65535

while True:
    print(f"Voltase sekarang adalah: {potentio.read_16() * pengali}")
    time.sleep(0.5)
```

### Penutup

Nah itu dia berkaitan dengan ADC. Di raspberry pi pico, kamu hanya bisa menggunakan 3 Pin untuk keperluan ini, 26, 27 dan 28.

Kamu bisa menggunakan ADC untuk mengukur suhu, membaca potentiometer, mengukur voltase suatu baterai, dan lain sebagainya.

Sampai bertemu di seri selanjutnya. Kita akan menggabungkan konsep ini dengan mengatur terang gelapnya LED insyaAlloh di seri selanjutnya.

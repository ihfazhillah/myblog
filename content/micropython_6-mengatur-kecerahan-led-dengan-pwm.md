Title: [Micropython 6] Mengatur Kecerahan LED Menggunakan PWM
Slug: micropython-6-mengatur-kecerahan-led-menggunakan-pwm
Date: 2023-09-23 21:49
Tags: raspberrypi pico, micropython, pwm, pulse width modulation, kecerahan led, redup led
Category: Micropython
Summary: Bagaimana mengatur kecerahan LED secara terprogram menggunakan micropython? Kamu bisa menggunakan PWM. Pulse Width Modulation. Simak lebih lengkapnya di seri ini.


![Duty Cycle](https://upload.wikimedia.org/wikipedia/commons/b/b8/Duty_Cycle_Examples.png)

# Bismillah

Pernah menemui lampu kamar yang bisa diatur kecerahannya dengan memutar saklar putar yang tertempel di tembok? Kamu bisa melakukan hal tersebut menggunakan raspberry pi pico kamu menggunakan PWM. Pulse Width Modulation.

Dengan PWM ini, kamu bisa mengontrol presentase kecerahan LED dari 0% sampai 100%.

Seperti biasa, asumsi saya kamu telah membeli paket [Get Started With Micropython In Raspberry Pi Pico](https://tokopedia.link/mY83NSZNHCb) karena semua yang kita butuhkan di seri seri awal ini ada disana semua. Bila tidak, maka berikut beberapa alat yang kamu perlukan:

1. [Breadboard](https://tokopedia.link/QkgWSqRYICb)
2. [Raspberry pi pico](https://tokopedia.link/Rq0eCOYYICb)
3. [LED](https://tokopedia.link/Yjn7jjfZICb)
4. [Resistor 330 Ohm](https://tokopedia.link/jB7zBp2YICb)
4. Kabel data micro usb
5. Beberapa kabel jumper male to male

### Skema

Kamu bisa menggunakan skema untuk LED pada [seri ke 4](https://blog.ihfazh.com/micropython-4-mengontrol-external-led-menggunakan-push-button). Asumsi saya kamu menggunakan skema persis pada [seri ke 4](https://blog.ihfazh.com/micropython-4-mengontrol-external-led-menggunakan-push-button) ini, yaitu menggunakan pin 16 untuk mengontrol LED kamu.

### Kode

Tulis kode dibawah ini dan simpan menggunakan nama `pwm_dasar.py`. 

```python
from machine import Pin, PWM


red = Pin(16, Pin.OUT)
pwm = PWM(red)
pwm.freq(200)
pwm.duty_u16(int(30/100 * 65535))
```

Jalankan dengan `mpremote run pwm_dasar.py`

### Penjelasan

Seperti biasa, diawal kita meng-import library yang kita butuhkan. Kita butuh `Pin` karena dengan itu kita 
mendefinisikan dimana LED kita terkoneksikan.

Kita juga membutuhkan modul PWM untuk mengatur kecerahan LED pada pin tersebut.

Perhatikan `pwm = PWM(led)`. `PWM` ini menerima Pin object sebagai parameter, bukan angka atau string untuk ID suatu Pin. Ini berarti, kita akan menggunakan modul pwm untuk mengatur kecerahan LED.

Kemudian kita mengatur frekuensi pada `pwm.freq(200)`

Pada akhirnya, kita mengatur kecerahan LED menggunakan `pwm.duty_u16` untuk sekitar kecerahan 30% dari total kecerahan LED. Karena fungsi `duty_u16` membutuhkan integer, maka kita perlu mengkonversi nilai pecahan menjadi integer menggunakan fungsi `int`.

### PWM

PWM adalah sebuah metode yang berguna untuk mengontrol daya rata rata yang akan dikirimkan ke beban. Dalam hal ini, beban kita adalah LED. Dan pada contoh kode diatas, daya rata rata yang kita inginkan adalah 30%.

Cara untuk memberikan daya rata rata tersebut adalah dengan menyala matikan beban dengan kecepatan lebih cepat daripada yang dibutuhkan oleh beban. Semakin lama matinya, semakin redup. Sebaliknya, semakin lama menyala, semakin terang.

Di kode sebelumnya, kamu mengatur frekuensi dengan menggunakan method `freq`. Frekuensi ini adalah berapa kali beban nyala dan mati dalam satu detik. Satuannya adalah Hertz. Untuk mengatur LED, 100 - 120 Hz sudah cukup.

Adapun **duty** adalah jarak lama antara hidup dan mati. Jadi dalam rentang 100 kali per detik itu, berapa lama perbandingan antara hidupnya beban dan matinya beban.

![](https://upload.wikimedia.org/wikipedia/commons/b/b8/Duty_Cycle_Examples.png)

Untuk di micropython sendiri kamu bisa mengatur duty menggunakan `duty_u16` atau `duty_ns`. Yang pertama menggunakan rentang 0 - 65535. Sedangkan yang kedua menggunakan satuan nano seconds. 

Untuk membuktikan bahwa PWM itu adalah siklus antara nyala dan mati dari suatu pin, maka kamu bisa mengecilkan frekuensi menjadi 10. Kamu akan lihat bahwa LED berkedip dengan kecerahan 100%. 

### Penutup

Nah itu dia tentang PWM. Kamu bisa mengatur kecerahan LED menggunakan PWM. Kamu juga sudah belajar tentang cara kerja PWM, frekuensi dan duty. Selain untuk mengatur kecerahan LED, PWM ini biasa digunakan untuk mengatur kecepatan dinamo motor, dan juga dipakai dalam Solar Charger Controller.

Kamu juga bisa menggabungkan dengan [seri sebelumnya](https://blog.ihfazh.com/micropython-5-membaca-potentio-meter-menggunakan-micropython). Mendapatkan presentase menggunakan potentiometer, dan mengatur kecerahan menggunakan kembalian potentiometer tersebut ke led. 

Selamat mencoba.
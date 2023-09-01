Title: [Micropython 4] Mengontrol External LED Menggunakan Push Button
Slug: micropython-4-mengontrol-external-led-menggunakan-push-button
Date: 2023-08-31 13:32
Tags: raspberrypi pico, micropython, external led, push button
Category: Micropython
Summary: Setelah mengetahui bagaimana mengontrol internal led sebagaimana di seri pertama dan ke-2 kemarin, kita akan mencoba untuk mengontrol led external. Kita juga akan buat simulasi lampu kerlap kerlip di akhir nanti. Siapkan alat alatnya ya.

# Bismillah

Di seri kali ini, kita akan mempelajari bagaimana mengontrol external led menggunakan push button. Kita akan mulai dengan 1 LED saja, dan mempelajari satu persatu komponennya.
Selanjutnya, saya akan ajak untuk membuat lampu kerlap kerlip dari 3 led yang berbeda warna dan berjalan sesuai state nya.

Seperti biasa, asumsi saya kamu telah membeli paket [Get Started With Micropython In Raspberry Pi Pico](https://tokopedia.link/mY83NSZNHCb) karena semua yang kita butuhkan di seri seri awal ini ada disana semua. Bila tidak, maka berikut beberapa alat yang kamu perlukan:

1. [Breadboard](https://tokopedia.link/QkgWSqRYICb)
2. [Raspberry pi pico](https://tokopedia.link/Rq0eCOYYICb)
3. [3 resistor 330 ohm](https://tokopedia.link/jB7zBp2YICb)
4. [3 Led berbeda warna (merah, hijau, kuning)](https://tokopedia.link/Yjn7jjfZICb)
5. [Push Button](https://tokopedia.link/ySO8WBjZICb)
6. Kabel data micro usb
7. Beberapa kabel jumper male to male

### Kontrol 1 LED

#### Skema

Untuk mengetahui katub positif dan negatif led, kamu bisa lihat panjang kakinya. Yang lebih panjang maka positif (anoda), dan sebaliknya adalah negatif (katoda). Atau, kamu dapat melihat bagian dalam LED nya, yang lebih kecil adalah positif, dan lebih besar adalah negatif.

![elektronika-dasar.web.id](http://elektronika-dasar.web.id/wp-content/uploads/2012/06/Bentuk-Dan-Simbol-LED.jpg)

Gambar dari [elektronika-dasar.web.id](http://elektronika-dasar.web.id)


Hubungkan kaki positif dengan salah satu kaki resistor, dan kaki resistor satunya hubungkan ke pin 16. Kemudian hubungkan kaki led negatif ke ground.

Adapun push buttonnya, kaki depan kanan hubungkan ke power 3v3, dan kaki belakang kiri ke pin 15.

Berikut gambar skemanya:

![skema]()


### Kode

Ketikkan kode berikut untuk mengontrol led menggunakan push button

```python
# toggle_led.py
from machine import Pin


led_red = Pin(16, Pin.OUT)
push_btn = Pin(15, Pin.IN, Pin.PULL_DOWN)


def handle_toggle(pin):
    led_red.toggle()


push_btn.irq(handle_toggle, trigger=Pin.IRQ_RISING)
```

Ada yang berbeda dengan [seri sebelumnya](https://blog.ihfazh.com/micropython-2-control-device-dari-luar-menggunakan-push-button)? Yap, kita menggunakan method `irq`. IRQ adalah Interrupt Request. Yakni, sebuah signal yang dikirimkan kepada prosesor untuk mematikan prosesnya sementara.

Jadi, taruhlah pico sedang menjalankan suatu program, misal nyala matikan led secara terus menerus. IRQ ini akan memerintahkan Pico untuk menghentikan sementara program tersebut, dan menjalankan fungsi yang ditentukan sebagai gantinya.

Di kode diatas, sinyalnya adalah perubahan state pada push button. Ketika state push button berubah, maka fungsi `handle_toggle` akan dipanggil.

`trigger=Pin.IRQ_RISING` sinyalnya akan dikirimkan ketika sedang ada perubahan state dari low ke high, atau dalam kata lain dari 0 menuju 1.

Jalankan program diatas dengan:

```mpremote run toggle_led.py```

coba tekan bolak balik buttonnya. 


### State LED tidak konsisten

Yap, benar. State LED tidak konsisten. Terkadang ketika kita tekan button, LED nyala mati dalam satu kali tekan. Terkadang tidak menyala. Apa yang sebenarnya terjadi?

Fenomena ini dinamakan bouncing atau pantulan. Hal ini dikarenakan problem mekanik dari push button itu sendiri, sehingga terkadang terdeteksi buka/tutup dalam sekali tekan. Sehingga, microcontroller membaca beberapa kali perubahan state.

Kita perlu menyelesaikan problem ini dengan mengecek selisih detik terakhir terdeteksi perubahan state dan waktu sekarang. Bila selisihnya paling tidak 300ms, maka kita anggap bahwa ketika push button berubah state, itu adalah perubahan yang kita inginkan.

Perhatikan kode berikut


```python
from machine import Pin
import time


led_red = Pin(16, Pin.OUT)
push_btn = Pin(15, Pin.IN, Pin.PULL_DOWN)

latest_click = time.ticks_ms()
delay = 300  # in ms


def handle_toggle(pin):
    global latest_click

    if (time.ticks_ms() - latest_click) > delay and pin.value():
        latest_click = time.ticks_ms()
        led_red.toggle()


push_btn.irq(handle_toggle, trigger=Pin.IRQ_RISING)
```

Statement `global latest_click` artinya kita akan mengubah variable diluar fungsi `handle_toggle`. Bila kita tidak definisikan dengan `global` statement, maka assignment yang ada di dalam fungsi ini tidak bisa mengubah variable yang diluar.

Perhatikan if statement setelahnya, kita kurangkan ticks sekarang dengan ticks sebelumnya, kemudian kita bandingkan apakah sudah lebih besar dari delay yang kita tentukana atau belum. Bila sudah, 
maka kita ubah latest_click dengan tick baru dan lakukan toggle led nya. Bila belum, maka kita tidak melakukan apa apa.

### Satu LED 3 State

Setelah kita faham bagaimana mengatur LED dengan push button, mari kita ubah program diatas menjadi lebih menarik dan menantang. Kali ini kita akan simpan state LED dan mengubahnya tiap kali kita tekan push button menjadi 3 state dibawah ini:

1. Mati
2. Nyala terus menerus
3. Berkedip setiap 1/2 detik

Bagaimana alurnya? 

Kita buat push button ini sebagai perubah state. Kemudian kita monitor state tersebut dalam while loop. 

```python
from machine import Pin
import time


led_red = Pin(16, Pin.OUT)
push_btn = Pin(15, Pin.IN, Pin.PULL_DOWN)

latest_click = time.ticks_ms()
delay = 300  # in ms

states = ["mati", "nyala", "kedip"]
current_state = 0


def handle_toggle(pin):
    global latest_click, current_state

    if (time.ticks_ms() - latest_click) > delay and pin.value():
        latest_click = time.ticks_ms()

        current_state += 1



push_btn.irq(handle_toggle, trigger=Pin.IRQ_RISING)

while True:
    state = states[current_state % 3]
    if state == "mati":
        led_red.value(0)
    elif state == "nyala":
        led_red.value(1)
    elif state == "kedip":
        led_red.value(1)
        time.sleep(0.5)
        led_red.value(0)
        time.sleep(0.5)
```

Sebelum menjalankan script diatas, reset dahulu micropythonnya dengan `mpremote reset 0`, atau lepas usb dahulu kemudian pasang kembali. Kemudian jalankan program diatas dengan `mpremote run led_external.py`

Kita definisikan states dengan 3 array, mati, nyala dan kedip. Kemudian kita definisikan counter di current_state. Kita juga jadikan `current_state` sebagai global di handle_toggle sehingga kita dapat mengubah valuenya.

Di while loop, kita dapatkan state sekarang. Kita gunakan trick modulo disini. `0 % 3 = 0`, `1 % 3 = 1`, `2 % 3 = 3`, `3 % 3 = 0`, dst... Sehingga kita dapatkan index state saat ini tanpa kena IndexError exception.

Setelah kita dapatkan statenya, baru kita jalankan program kita sesuai permintaan diatas.

### 3 LED

Kali ini kita akan menggunakan 3 LED. Yap, bukan saya yang mengerjakan ya. Saya searahkan kepada kamu untuk mengontrol ke-3 LED ini dengan beberapa state berikut:

Gunakan 3 LED berbeda warna. Di sini, saya asumsikan kamu menggunakan hijau, merah dan kuning. Berikut beberapa keadaan lednya:

1. Mati semua
2. Nyala Semua
3. Kedip berbarengan (ketiga lampu menyala, kemudian mati, kemudian nyala, dst...)
4. Menyala satu satu bergantian
5. Menyala 2 kemudian 1 bergantian

Nah, saya serahkan kamu untuk mengerjakan 5 state ini. Kunci jawabannya saya akan sertakan link di akhir artikel.

Hasil akhir kurang lebih seperti ini

<iframe width="560" height="315" src="https://www.youtube.com/embed/SenaBzI2K40?si=TiK64HZTBLeKOtgp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Kenapa butuh resistor ?

Kalau kamu perhatikan, untuk pemasangan LED butuh resistor, kenapa? Karena LED sendiri membutuhkan voltase sekitar 2 Volt, dan Pin dari raspberry pi pico keluarannya adalah 3.3v. Bila kamu langsung menyambung kaki LED dengan voltase 3.3v maka lampu LED akan meledak.

Sedangkan diantara kegunaan resistor adalah menghambat tegangan. Ketika tegangan dihambat, maka harapannya voltase keluaran sebelum masuk ke LED bisa berkurang. Anggap saja jalan raya yang motor atau mobilnya pada ngebut ngebut. Nah, disuatu tempat ada kecelakaan, atau perbaikan bahu jalan. Mau tidak mau, kecepatan kendaraan yang lewat akan berkurang. Seperti itu kurang lebih analoginya. 

Berikut ada beberapa video bagus yang menjelaskan tentang resistor dan LED

1. [Resistor, fungsi & prinsip kerja](https://www.youtube.com/watch?v=34_pGkD0Hd0&pp=ygUZZ3VydSBlbGVrdHJvbmlrYSByZXNpc3Rvcg%3D%3D)
2. [Resistor dan lampu led](https://www.youtube.com/watch?v=u9oAlR_xnKU&pp=ygUZZ3VydSBlbGVrdHJvbmlrYSByZXNpc3Rvcg%3D%3D)

### Penutup

Nah, bagaimana? Menarik bukan? Di seri ini kamu sudah bisa mengontrol external LED dengan push button. Tidak hanya itu, kamu sudah bisa mengontrol pantulan dari push button, dan juga beberapa lampu LED dengan beberapa state yang berbeda. 

Bila belum, kamu bisa [check link ini untuk melihat jawaban permasalah 3 LED diatas](https://gist.github.com/ihfazhillah/c86b67288225efb852c103f2e6a7d30b).

Apa lagi ya yang bisa kita lakukan dengan [raspberry pi pico](https://tokopedia.link/Rq0eCOYYICb)? Kita akan lanjutkan pada seri berikutnya insyaAlloh.
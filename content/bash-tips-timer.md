Title: (bashtips) Timer di Bash
Slug: (bashtips)-timer-di-bash
Date:  2019-03-09 17:40
Category: BashTips
Tags: productivity, bashtips
Authors: Ihfazhillah
Summary: membuat timer di bash, pomodoro, atau yang lainnya.

# Bismillah

Suatu hari, saya mulai bekerja. Namun karena suatu hal, 1 jam berikutnya saya harus melakukan sesuatu yang lainnya. Hari hari, memang saya banyak bekerja di terminal. Saya butuh semisal `timer 60h` dan enter, kemudian saya mulai bekerja. Setelah 1 jam, saya mendapat peringatan.

## Installasi

Di linux, pastikan sudah ada ini:
- bc
- sox
- libsox-fmt-mp3

```
$ curl -o ~/bin/timer https://raw.githubusercontent.com/rlue/timer/master/bin/timer
$ chmod +x ~/bin/timer
```


## How to Use

- `timer 5` => 5 menit kemudian, kamu akan mendapatkan notifikasi
- `timer -r 10 500` => 500 menit kemudian, kamu akan mendapatkan notifikasi. 10x
- `timer 10 20 30` => berurut, pertama 10 menit, kemudian 20 menit, kemudian 30 menit.

## Penutup

Meskipun saya berada di depan laptop, dan mostly berada di depan terminal, saya dengan mudah dapat membuat semisal alarm untuk membantu saya mengingat waktu. Paling nggak, molor dikit. Ha ha.

Semoga membantu..

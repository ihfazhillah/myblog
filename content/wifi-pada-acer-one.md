Title: Wifi Pada Acer one 14 ubuntu
Date: 2016-7-3 19:02
Tags: tips, ubuntu, wifi, acer one, acer one 14, acer z1402-38gr
Category: Tips
Slug: wifi-pada-acer-one-14-ubuntu
Authors: Ihfazhillah
Summary: Mengaktifkan wifi pada acer one 14 di ubuntu
Modified: 2017-5-7 21:11

# Bismillah, 

Ada sedikit problem ketika menginstall ubuntu (sekarang saya sedang menggunakan ubuntu 16.04) di acer one 14. Meskipun di windows (dari tokonya), wifi berjelan dengan semestinya.

Inti dari permasalahannya adalah, dikarenakan driver tidak terdeteksi dengan baik. Untuk mengatasinya, maka perlu kita menginstall driver tersebut.

```bash
sudo apt-get install git build-essential
git clone https://github.com/lwfinger/rtl8723bu
cd rtl8723bu
make
sudo make install
sudo modprobe -v 8723bu
```

Nah, silahkan reboot, dan anda bisa mengaktifkan atau menonaktifkan menggunakan tombol fn-f4 berbarengan dengan bluetoth juga.

[Sumber](https://forums.linuxmint.com/viewtopic.php?t=208434)

## Update 7/5/2017

Ubuntu 17.04 dengan kernel 4.10 wifi sudah terdeteksi. Namun kabar buruknya, untuk meng-koneksikan ke router masih susah. Tidak terkoneksi. 

Permasalahannya berada pada module `rtl8xxxu` dalam kernel ini yang belum berfungsi dengan baik.

Jadi, solusi sementara adalah mendisable dan blacklist module kernel tersebut.

### Blacklist

Pergi, dan edit file `/etc/modprobe.d/blacklist.conf` dan tambahkan `blacklist rtl8xxxu` di akhir file. Save.

### Disable

Jalankan perintah: `sudo modprobe -rv rtl8xxxu`

Setelah itu lakukan perintah seperti di awal artikel ini.

Sumber: https://ubuntuforums.org/showthread.php?t=2359516&page=2

### Permasalahan lain Muncul 2 Device

Dengan perintah diatas, maka akan menampilkan 2 device wifi. Kalau tidak mau, maka anda bisa menjalankan langkah berikut sebelum melakukan `make`

1. Buka file `MakeFile`
2. Cari `EXTRA_CFLAGS += -DCONFIG_CONCURRENT_MODE`, comment line tersebut
3. Baru setelah ini, `make`
4. `sudo make install`
5. `sudo modprobe -v 8723bu`

Title: Wordpress - wp.media Javascript Object
Slug: wordpress-wp-media-javascript-object
Date: 2018-04-19 05:30
Category: Wordpress Plugin
Tags: wordpress, wordpress-plugin, wp-media, upload modal, wordpress upload modal
Authors: Ihfazhillah
Summary: wp.media adalah sebuah objek javascript yang digunakan oleh wordpress untuk menampilkan upload modal di wordpress admin. Sebagai contoh, ketika kamu membuka New Post, dan menekan tombol media, atau add featured image.

# Bismillah

`wp.media` adalah sebuah objek javascript yang wordpress gunakan untuk menampilkan upload modal di wordpress admin. Sebagai contoh, ketika kamu membuka `New Post` dan menekan tombol media, atau add featured image. 
Kamu bisa membuat semisal link `add featured image` dan menampilkan upload modal dalam wordpress sendiri dengan `wp.media` ini. Artikel ini, akan membahas bagaimana kamu membuatnya.

Cara paling mudah, kamu buka `New Post` atau `New Page`, kemudian buka browser console kamu. Disini, saya akan mengenalkan `wp.media`, bagaimana meng-eksekusinya, dan meng-handle file / gambar yang kamu pilih di upload modal tersebut.

## Contoh

Yuk mulai menggunakan `wp.media` ! Saya anggap kamu sudah membuka browser console. Ketikkan kode dibawah ini, setelah itu saya akan mencoba menjelaskan apa yang terjadi.

```javascript

var frame = wp.media({
  title: "Unggah Logo Kamu",
  button: {
    text: "Gunakan media ini"
  },
  multiple: false
})


```

Pertama, kita buat variable bernama `frame`. Assign `wp.media` di isi dengan properties yang di inginkan. Berikut properties `wp.media` yang saya masukkan dan keterangannya.

[jtable separator="|"]
No. | Property | Deskripsi
1 | `title` | Sesuai nama, ini sebagai judul yang akan di tampilkan di kiri atas modal / frame yang muncul nanti
2 | `button` | Untuk override button dibawah, ketika kita telah selesai memilih image/file
3 | `multiple` | mau milih multiple image atau hanya satu saja? Karena di contoh, saya menggunakan `wp.media` untuk mengupload logo, maka cocoknya satu gambar saja.
[/jtable]

Setelah selesai menulis kode ini, kamu akan dapati, bahwa belum terjadi apa apa. `wp.media` belum menampilkan modal / frame nya. Tenang, untuk menampilkannya, kamu hanya butuh mengetikkan `frame.open()`. Daaaan...

### Handle Perubahan

Setelah memilih milih file / gambar dari modal / frame yang dibuat oleh `wp.media`, bagaimana caranya mendapatkan file/gambar yang saya pilih?
Gunakan `.on('select' callback)` method dari `iframe` instance.

Perhatikan kode berikut

```javascript
frame.on('select', function(){
  var attachment = frame.state().get('selection').first().toJSON()
  console.log(attachment)
});
```

perhatikan variable `attachment` diatas. Kita mengambil `selection` yang pertama, dan mengkonversi nya menjadi json objek.

Bila kamu ingin mengambil semua objek, atau mendapatkan array, maka gunakan `.all` sebagai ganti dari `.first`.

Kemudian, saya menuliskannya di terminal. Tapi kamu dapat idenya. Insya Alloh.

## Penutup

Fuih, selesai sudah pembahasan tentang `wp.media`. Kamu dapat menggunakan `wp.media` untuk keperluan : 

- upload logo untuk website kamu
- upload custom banner wordpress
- menambahkan custom images di metabox
- dan lain sebagainya

Bagaimana, sudah dapat ide untuk membuat apa?


Title: Menggunakan Twitter Bootstrap di Wordrpess Admin
Slug: using-twitter-bootstrap-in-wordpress-admin
Date: 2018-02-08 06:34
Category: Wordpress
Tags: twitter, bootstrap, twitter-bootstrap, wp-admin, fix conflict, bootstrap wp-admin conflict, konflik wp-admin dan bootstrap, wp admin gak jelas, tampilan wp-admin aneh
Authors: Ihfazhillah
Summary: Kamu adalah plugin developer, dan kamu butuh bootstrap untuk memudahkanmu styling. Tapi ternyata, ketika kamu menambahkan style ini ke wp-admin, tampilan jadi tidak seperti yang kamu harapkan. Artikel ini semoga dapat membantu kamu.

# Bismillah

Kamu sedang develop wordpress plugin, dan menggunakan twitter bootstrap untuk styling. Kamu bisa saja menambahkannya dengan `wp_enqueue_style`. Css bootstrap ke-*load*, tapi tampilan admin kamu berantakan.

Kalau kamu melihat source code-nya css milik bootstrap dan juga wordpress, kamu akan dapati ada selector yang tabrakan. 

Misalkan selector `h1,.h1` dari bootstrap, dia akan menimpa selector `h1`-nya milik wordpress css. Sehingga, berlakulah permasalahan perhitungan [specifity](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity)

## Solusi

Kamu sudah tahu permasalahannya, maka bagaimana solusinya ? Bungkus selector css milik bootstrap dengan wrapper selector. Sehingga, selector bootstrap yang tadinya hanya `h1, .h1`, menjadi `.bootstrap-wrapper h1, .bootstrap-wrapper .h1` bila kamu tentukan wrappernya adalah `.bootstrap-wrapper`.

>> Wrapper ini terserah kamu loh yah mau pakai apa

Sehingga, ketika kamu ingin menggunakan selector dari bootstrap ini di admin panel kamu, yang kamu butuhkan adalah, **Membungkus tag yang ada, dengan div yang memiliki class atau id yang kamu tentukan di selector**

Misalkan nih, kamu ingin menggunakan `.modal` nya bootstrap. Maka, jangan langsung menulis begini : 

```
<div class="modal">blablabla</div>
```

tapi, bungkus tag tadi dengan wrapper yang sudah kamu tentukan tadi, anggap saja `.bootstrap-wrapper`.

```
<div class="bootstrap-wrapper">
  <div class="modal">blablabla</div>
</div>
```

## Apa ada cara cepat ?

Kamu bisa mengubah langsung file `bootstrap.css`, baris demi baris. Tapi, kebayangkan berapa banyak baris yang kamu perlu ubah?

Oleh karena itu, kamu butuh css pre processor semacam [sass](https://sass-lang.com/) atau [less](http://lesscss.org/) atau juga yang lainnya. 

### Sass

Pastikan kamu sudah install sass di local kamu. Karena saya kerjaan banyak menggunakan nodejs, saya install `node-sass` dengan `yarn add node-sass`. atau kamu juga bisa menginstall dengan `npm install node-sass`.

#### Langkah :

Saya ambil asumsi, bahwa kamu sudah unduh `bootstrap.css`. Selanjutnya, ubah filename menjadi `_bootstrap.scss`.

lalu buat file baru bernama `wrap-boostrap.scss` dan isi dengan :

```
.bootstrap-wrapper {
  @import "boostrap";
}
```

Kemudian, compile file `wrap-bootstrap.scss` dan jadikan single file css yang semua selector sudah di bungkus menggunakan `.bootstrap-wrapper`. `node-sass wrap-bootstrap.scss wrap.bootstrap.css`.

Baru, load file `wrap.bootstrap.css` tadi ke wordpress seperti tadi.

### Less

Untuk installasi juga sama, kamu gunakan `npm` atau `yarn` disini. `npm install less` atau `yarn add less`.

#### Langkah:

Sama seperti tadi, asumsi saya kamu sudah unduh `bootstrap.css`. Selanjutnya, kamu buat file `wrap-bootstrap.less` dengan isi sebagai berikut :

```
.bootstrap-wrapper {
	@import (less) url('bootstrap.min.css');
}
```

Setelah itu, compile dengan `lessc wrap-bootstrap.less wrap.bootstrap.css`. 

Done.

## Penutup

Sebagai penutup, saya ringkaskan langkah yang dapat kamu lakukan disini:

1. Buat wrapper untuk semua css selector di dalam bootstrap
2. ketika ingin menggunakan bootstrap di html tags, kamu juga perlu membungkus dengan selector yang sudah kamu tentukan
3. untuk membuat wrapper untuk semua css selector, kamu bisa menggunakan css preprocessor yang ada semacam `less` atau `sass`.

Mungkin cara ini, juga bisa digunakan untuk yang lainnya? Beritahu saya di kotak komentar bila kamu berhasil.

[Sumber Utama](https://rushfrisby.com/using-bootstrap-in-wordpress-admin-panel/)

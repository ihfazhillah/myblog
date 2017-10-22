Title: Urlparse - Parse Url Menjadi Beberapa Bagian
Slug: urlparse-parse-url-menjadi-beberapa-bagian
Date: 2017-05-15 09:32
Category: Python
Tags: urlparse, urllib.parse, python3, python2, parse url, tool parse url python
Authors: Ihfazhillah
Summary: Memudahkan tugas parsing url di python3 maupun python2

# Bismillah

Pembahasan kita kali ini akan khusus ke sebuah tool yang bernama `urlparse` dan
`urlunparse`. 

## urlparse 

ini berguna untuk keperluan membagi url yang kita berikan menjadi 6
bagian. Perhatikan contoh dan table berikut. Taruhlah kita memiliki url seperti
berikut 
`http://user:pass@NetLoc:80/path;parameters/path2;parameters2?query=argument#fragment`

maka, hasilnya kurang lebih sebagai berikut:

|Bagian|Index|Value|
|------|------|--------|
|scheme|0|http|
|netloc|1|user:pass@NetLoc:80|
|path|2|/path;parameters/path2;parameters2|
|params|3|params|
|query|4|query|
|fragment|5|fragment|
|username||user|
|password||pass|
|hostname||netloc|
|port||80|

`urlparse` dan `urlunparse` merupakan library yang sangat berguna bagi kita
yang berurusan dengan permasalahan url. Dan library ini adalah library
`builtin`, sehingga kita tidak perlu lagi menginstall library tambahan.untuk bagian yang tidak ada indexnya, maka kita tidak dapat memanggilnya
menggunakan index. Akan tetapi menggunakan notasi dot. 

Perhatikan contoh berikut (masih menggunakan url di atas)

```python
url =
"http://user:pass@NetLoc:80/path;parameters/path2;parameters2?query=argument#fragment"
parsed = urlparse(url)

`urlparse` dan `urlunparse` merupakan library yang sangat berguna bagi kita
yang berurusan dengan permasalahan url. Dan library ini adalah library
`builtin`, sehingga kita tidak perlu lagi menginstall library tambahan`urlparse` dan `urlunparse` merupakan library yang sangat berguna bagi kita yang berurusan dengan permasalahan url. Dan library ini adalah library `builtin`, sehingga kita tidak perlu lagi menginstall library tambahan`urlparse` dan `urlunparse` merupakan library yang sangat berguna bagi kita yang berurusan dengan permasalahan url. Dan library ini adalah library `builtin`, sehingga kita tidak perlu lagi menginstall library tambahan`urlparse` dan `urlunparse` merupakan library yang sangat berguna bagi kita yang berurusan dengan permasalahan url. Dan library ini adalah library `builtin`, sehingga kita tidak perlu lagi menginstall library tambaha`urlparse` dan `urlunparse` merupakan library yang sangat berguna bagi kita yang berurusan dengan permasalahan url. Dan library ini adalah library `builtin`, sehingga kita tidak perlu lagi menginstall library tambahan.n....# kita memanggil dengan index, hanya bisa sampai 5
print(parsed[8]) # index error, gunakan notasi dot
print(parsed.port)

```

Untuk hasil yang dihasilkan oleh `urlparse` maka dia `readonly`, maknanya tidak
bisa diubah ubah. Jadi, ketika kita ingin mengubah suatu bagian dari yang
disebutkan diatas, netloc misalnya (sebagaimana dalam studi kasus yang akan
datang), maka kita perlu untuk mengubahnya menjadi
list dahulu.

## urlunparse
adapun `urlunparse` adalah sebaliknya. Yaitu membungkus pecahan yang dihasilkan
oleh `urlparse` menjadi url utuh. Atau bisa juga digunakan untuk membungkus
list/tuple dengan isi dengan urutan sebagaimana `urlparse` mengurutkannya.

## Beda python2 dan python3

Hanya di peletakan library saja. Di python2 library `urlparse` dan `urlunparse` berada di
`urlparse.urlparse` dan `urlparse.urlunparse`. Sedangkan di python3 dia terletak
di `urllib.parse.urlparse` dan `urllib.parse.urlunparse`.

## Studi Kasus

url =
http://3.bp.blogspot.com/-ROyYC5sfXeg/VB5aAa2iLWI/AAAAAAAABac/KX3hgNJGcCo/s1600/Gambar%2BPemandangan%2BAlam%2BTerindah%2Bdi%2BDunia%2BPuncak%2BGung%2BBukit%2BHijau%2BCantik.jpg

jadikan url diatas menjadi
http://i0.wp.com/3.bp.blogspot.com/-ROyYC5sfXeg/VB5aAa2iLWI/AAAAAAAABac/KX3hgNJGcCo/s1600/Gambar%2BPemandangan%2BAlam%2BTerindah%2Bdi%2BDunia%2BPuncak%2BGung%2BBukit%2BHijau%2BCantik.jpg

Yuk, perhatikan analisa dan langkah berikut:

Perubahan diatas, berada di bagian `netloc`. Dengan menambahkan `i0.wp.com/` di
depannya. Dan `netloc` ini berada di index 1. Karena `ParseResult` object
adalah **readonly**, maka kita perlu mengubah hasilnya menjadi list. Kemudian
kita ubah isi dari index 1 menjadi yang di inginkan. Setelah itu baru
kembalikan menjadi url utuh.

Jadi secara ringkas, langkah yang akan kita lakukan seperti ini:

1. parse url (gunakan `urlparse`)
2. ubah menjadi list (gunakan `list`)
3. ubah index 1
4. unparse lagi (gunakan `urlunparse`)

```python
from urllib.parse import urlparse, urlunparse
url =
"http://3.bp.blogspot.com/-ROyYC5sfXeg/VB5aAa2iLWI/AAAAAAAABac/KX3hgNJGcCo/s1600/Gambar%2BPemandangan%2BAlam%2BTerindah%2Bdi%2BDunia%2BPuncak%2BGung%2BBukit%2BHijau%2BCantik.jpg"
parsed = urlparse(url)
parsed.netloc # 3.bp.blogspot.com
parsed[1] # 3.bp.blogspot.com

parsed_list = list(parsed)
parsed_list[1] = 'i0.wp.com/' + parsed_list[1]

unparsed = urlunparse(parsed_list)
```

## Kesimpulan

`urlparse` dan `urlunparse` merupakan library yang sangat berguna bagi kita
yang berurusan dengan permasalahan url. Dan library ini adalah library
`builtin`, sehingga kita tidak perlu lagi menginstall library tambahan.

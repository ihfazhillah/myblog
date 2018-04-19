Title: Memahami Fungsi Enumerate
Slug: memahami-fungsi-enumerate
Date: 2018-04-19 21:45
Tags: python, enumerate, memahami enumerate, membuat enumerate
Category: Python
Summary: Setelah mengenal fungsi enumerate, yuk kita pahami alurnya dengan membuat fungsi enumerate kita sendiri. Mudah kok.

# Bismillah

Di post kemarin, kita sudah mengenal apa itu fungsi enumerate dalam python dan juga bagaimana cara menggunakan dan keuntungannya. Di post sekarang, yuk kita mendalami alur kerja fungsi enumerate. Kemudian membuat kloningan fungsi enumerate ini.

## Alur Kerja

Secara garis besar, fungsi enumerate ini me-_loop_ iterable, dan mengubah dari item satuan menjadi tuple. Index pertama adalah nomor urut, dan index kedua adalah item.

Sebagai contoh: Ada list `aList` dengan isian berikut ini `['buku', 'polpen']`. Maka, dengan fungsi enumerate ini, item `buku` akan berubah menjadi `(0, 'buku')`.

### iterable ?
Yang bisa di iterasi, bisa list, tuple, string.

## Mari kita buat

**Disclaimer:** versi asli dari fungsi enumerate adalah menggunakan keyword `yield` dan tidak menggunakan keyword `return`. Kita tidak membahas `yield` disini. Untuk memudahkan pemahaman, kita akan membuat fungsi enumerate yang mengembalikan list.

```python
def my_enumerate(iterable, start=0):

    index = start
    result = []

    for x in iterable:
        result.append((index, x))
        index += 1

    return result
```

## Penutup

Bagaimana, mudah bukan? 

Sebagai bonus, berikut adalah versi javascript dari fungsi enumerate.

```javascript
function enumerate(iterable, start) {
  var index = start ? start : 0;
  var result = [];

  iterable.forEach(function(item) {
    result.push([index, item]);
    index++;
  });

  return result;
}
```

Kamu mau menyumbang fungsi enumerate dalam bahasa lain ? Yuk kita diskusikan di komentar.


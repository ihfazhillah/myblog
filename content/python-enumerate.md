Title: Python Enumerate
Slug: python-enumerate
Date: 2018-04-18 22:36
Tags: python, built-in function, enumerate
Authors: Ihfazhillah
Summary: Mengenal enumerate dalam python. fungsi enumerate sangat powerful. Dikarenakan enumerate memudahkan kamu untuk mendapatkan index ketika melakukan loop.

# Bismillah

Sudah lama tidak menulis post saya. Untuk pemanasan, saya akan membahas tentang fungsi bawaan python yang bernama `enumerate`. Fungsi `enumerate` ini akan memudahkan kamu ketika melakukan _looping_ suatu _iterable_ dan juga membutuhkan indexnya.

## Fungsi Built-in ?

Di awal, saya mengatakan bahwa fungsi `enumerate` adalah fungsi bawaan. Atau dalam kata lain _built-in function_. Maksudnya adalah, sebuah fungsi yang sudah ada tanpa harus kamu import dahulu. Nah, fungsi `enumerate` ini adalah salah satunya.

## Penggunaa dan Contoh

`enumerate` menerima dua argument. Pertama sebuah objek yang bisa di iterasi/ di loop. Dan kedua adalah `start` dengan default `0`.

`start` dalam `enumerate` ini bukan index keberapa objek ini di mulai. Akan tetapi, index `0` dalam objek ini, akan di nomori berapa ?. 

### Contoh

```python3
iterable = ['semarang', 'bandung', 'salatiga']
list(enumerate(iterable))
# [(0, 'semarang'), (1, 'bandung'), (2, 'salatiga')]

list(enumerate(iterable, 1))
# [(1, 'semarang'), (2, 'bandung'), (3, 'salatiga')]
```

## Penutup

Nah, itu tadi tentang `enumerate`. Sebagai bonus, berikut contoh saya menggunakan `enumerate` untuk mempermudah iterasi ketika saya membutuhkan index.

```python
s = 'ihfazh'
even = ""
odd = ""

for i, c in enumerate(s):
    if i % 2 == 0:
        even += c
    else:
        odd += c

print(even + " " odd)
```

berikut versi tanpa enumerate

```python
s = 'ihfazh'
even = ""
odd = ""

for i in range(len(s)):
    if i % 2 == 0:
        even += s[i]
    else:
        odd += s[i]

print(even + " " odd)
```

Bagaimana ? Sudah menemukan keuntungan dari `enumerate` ?

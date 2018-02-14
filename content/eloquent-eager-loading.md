Title: Eager Loading pada Eloquent
Slug: eager-loading-pada-eloquent
Date: 2018-02-14 19:56
Category: Eloquent
Tags: eloquent, php, laravel, eager loading, relational, relasi table, langsung load
Authors: Ihfazhillah
Summary: Mengenal tentang eager loading pada eloquent, dan apa benefit-nya.

# Bismillah

Dalam eloquent query dan model yang memiliki relasi, tentunya kamu pernah mendengar `lazy loading` dan `eager loading`.

`lazy loading` adalah meload data relasi ketika pertama kali digunakan. Dengan kata lain, ketika kamu query parent modelnya, model relasi belum di load.

Sedangkan `eager loading` adalah, meload relasi langsung ketika query parent dilakukan.

## Lazy Loading

Sebagai contoh, kita punya dua table / model. `Post` dengan `Comment`. `Post` memiliki beberapa `Comment`, sedang `Comment` hanya terkait dengan satu `Post`. Jadi, relasinya adalah `one` (Post) to `many` (Comment).

Dalam `lazy loading`, ketika kita melakukan query seperti ini `Post::all()`, maka `comments` tidak akan keload langsung. Baru akan diload ketika kamu akses `comments` property nya.

```
$posts = Post::all();

foreach($posts as $post){
    echo $post->comments->count();
}
```

pada baris `echo $post->comments->count();`, comments baru di load.

Hal ini, menimbulkan masalah `N + 1` query.

Misalkan, jumlah dari `$posts` disitu adalah 25, maka di kode diatas, dia akan melakukan query sebanyak `N` + `1`. `N` = Jumlah posts, `1` = query pertama kali.

Terkadang, memang kita memerlukan `lazy loading` ini. Namun, diwaktu yang lain, kita ingin untuk tampilkan parent dengan semua relasi yang ada.

## Eager Loading pada Eloquent

### 1. Cara Dasar

menggunakan method `with` dan memasukkan string sebagai argument. Contoh:

```
$posts = Post::with('comments')->get();

foreach ($posts as $post){
    echo $post->comments;
}
```

### 2. Beberapa Relasi

Terkadang, relasi ke suatu table banyak. Misal Post memiliki beberapa tags, dan comments, pun authors? Kamu dapat menggunakan `with` juga, namun `array` sebagai argument. Contoh:

```
$posts = Post::with(['comments', 'tags', 'authors'])->get();

foreach($posts as $post){
    echo $post->comments;
    echo $posts->tags;
    echo $posts->authors;
}
```

### 3. Relasi Bersarang

Nah, misal author juga memiliki kontak. Maka kamu bisa men-spesifikasikannya menggunakan `dot` syntax.

```
$posts = Post::with('author.contact')->get();
```

### 4. Hanya Kolom Tertentu

Ketiga cara diatas, akan melakukan query `select * from`. Nah, bagaimana kalau kita ingin memilih beberapa kolom saja? Kamu dapat menggunakan syntax dibawah ini:

```
table:id,col2
```

> sebagai catatan, kamu harus memasukkan kolom id.

Contoh:

```
$posts = Post::with('author:id,username');
```

## Penutup

Sebagai penutup, saya menggunakan teknik `eager loading` ini ketika membutuhkan array dengan seluruh bentuk, dari parent sampai childnya. Sebagai contoh dalam json :

```
[
    {
        "id": "1",
        "title": "hello world",
        "comments": {
            "id": '1',
            "name": "hello"
        }
    }
]
```

anggep saja hanya seperti itu, tapi banyak. Dan saya tidak mungkin untuk melakukan query terpisah untuk mendapatkan data dari comments.

Semoga bermanfaat. Walhamduillah....

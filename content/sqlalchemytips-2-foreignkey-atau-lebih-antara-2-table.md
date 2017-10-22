Title: #sqlalchemytips - 2 Foreignkey (Atau Lebih) Antara 2 Table
Slug: sqlalchemytips-2-foreignkey-atau-lebih-antara-2-table
Date: 2017-05-24 10:55
Category: Tips
Tags: error, AmbiguousForeignKeyError, 2 foreignkey ke satu table, sqlalchemy, sqlalchemytips, flask-sqlalchemy
Authors: Ihfazhillah
Summary: Tips untuk mengatasi error AmbiguousForeignKeyError dalam sqlalchemy ketika mempunyai 2 atau lebih foreignkey dari satu table yang me-link ke table yang lainnya


# Bismillah,

## Masalah

Saat saya mendesain database, ternyata ada 2 kolom di suatu table yang
berhubungan dengan satu table yang lainnya. 

Sebagai contoh (ini contoh dari project yang sedang saya kerjakan). Saya punya dua table **Kajian** dan
**User**. Setiap **Kajian** memiliki 2 kolom yang kedua duanya ini berkaitan /
memiliki `ForeignKey` menuju table **User**. Yaitu **ustadz** dan
**koordinator**. Maka, berikut Model table yang saya buat.

> catatan: saya menggunakan `flask-sqlalchemy` sedangkan dokumentasi yang saya
> gunakan adalah milik `sqlalchemy`. Secara garis besar sama.

```python

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200))


class Kajian(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(200))

    koordinator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    koordinator = db.relationship('User',
                                  backref=db.backref('koordinator_kajian'))

    ustadz_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ustadz = db.relationship('User',
                             backref=db.backref('ustadz_kajian'))
```

Ringkasnya, kode diatas kita mendefiniskan 2 `ForeignKey` di table **Kajian**
menuju table **User**.

Masalahnya, ketika kode diatas di jalankan, maka akan keluar error `AmbiguousForeignKeyError`. Kenapa?
karena defaultnya, fungsi `relationship()` akan mencari -secara otomatis-
`ForeignKey` antara dua table dari kolom yang didefinisikan sebagai
`ForeignKey`. Jadi, baik di `koordinator` dan `ustadz`, maka keduanya akan sama
sama mencari `ForeignKey` yang menghubungkan table ini ke table `User`.
`relationship()` ini ternyata menemukan ada 2 `ForeignKey` menuju `user.id`,
sehingga keluarlah error ini.

## Solusi

Tambahkan `foreign_keys` argument ke `relationship()` yang berisi `list` untuk
menentukan, `ForeignKey` mana yang akan dipakai. Mana yang untuk `ustadz` dan
mana yang untuk `koordinator`.

Lebih jelasnya, perhatikan kode berikut.

```python

class Kajian(db.Model):
    ....
    koordinator = db.relationship('User', foreign_keys=[koordinator_id],
                                  backref=db.backref('koordinator_kajian'))
    ....
    ustadz = db.relationship('User', foreign_keys=[ustadz_id],
                             backref=db.backref('ustadz_kajian'))
```

Perhatikan, di kode tadi, kita menentukan mana `ForeignKey` untuk
`relationship`-nya `ustadz`. Dan mana yang miliknya `koordinator`. Menggunakan
argument bernama `foreign_keys` di fungsi `relationship`.

## Kesimpulan

`relationship` secara default akan mencari kolom mana yang digunakan sebagai
relasi ke table yang di tentukan di fungsi ini. Ini akan menjadi masalah ketika
ada 2 atau lebih relasi yang ada di table ini. Di artikel ini satu di antara
contohnya.

Sebagai tambahan bacaan, pembaca bisa membacanya lebih lengkap di
dokumentasinya Sqlalchemy bagian Configuring How Relationship Joins.

Semoga bermanfaat, dan semoga dapat terfahami.

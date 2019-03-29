Title: How To: Scrape Website Menggunakan JSON Data
Slug: how-to:-scrape-website-menggunakan-json-data
Date:  2019-03-25 22:58
Category: py-instant-crawl
Tags: scraping, json-scraping, py-instant-crawl, turn any website into json, website2api, site2json
Authors: Ihfazhillah
Summary: Library untuk melakukan screen scraping menggunakan json sebagai selector, dan juga bentuk data yang ingin di dapatkan. Kemudian me-result data dengan bentuk json.

# Bismillah

Berawal dari sebuah ide, scraping website bermodalkan sebuah template. Template ini adalah spesifikasi bentuk data yang akan di dapatkan.

Output dari program adalah data yang telah kamu spesifikasikan.

Misalkan ada template seperti berikut:

```json
{
    "name": {
        "expression": "//p[@class='name']/text()",
        "type": "xpath",
        "getter": "getall"
    }
}
```

dan akan mengembalikan data dengan bentuk kurang lebih :
```json
{
    "name": ["Ihfazh", "sakinah", "fukaihah"]
}
```

Beberapa keuntungan menggunakan konsep seperti ini:

1. DRY (Don't repeat yourself). Untuk task sesederhana ini, kita tidak perlu import requests, beautifulsoup / parsel.Selector. Tinggal buat template, panggil template dan url tujuan. Simple
2. Data sudah terstruktur, sesuai yang kita spesifikasikan.
3. Mungkin, kamu ada ide lain untuk buat SaaS :D

Kabar baiknya, saya sudah mulai buat library ini, meskipun simple namun sudah cukup membantu. Ide awal sudah berjalan dengan baik.

## Installasi

### Menggunakan PIP

```
pip install pyinstantcrawl
```

### Clone dari github

```
git clone https://github.com/ihfazhillah/py-instant-crawl.git
cd py-instant-crawl
python setup.py install
```

## Quickstart

Sebagai contoh, kita akan scrape https://www.producthunt.com/protips dan ambil tips yang ada di halaman tersebut.

### 1. Buat template

Data yang akan kita dapatkan ada di class `.protips_[somenumber]`. Dan dengan membungkus xpath selector dengan `string()`, kita akan dapatkan text tanpa tag html.

```json
{
    "protips": {
        "expression": "string(//div[contains(@class, 'protips')])",
        "type": "xpath",
        "getter": "get"
    }
}
```

dan simpan dengan nama `protips.json`.

Jadi, setiap key kita butuh 3 property:

1. `expression` : xpath atau css expression, sesuai yang kamu spesifikasikan di `type`
2. `type`: string, `xpath` atau `css`
3. `getter`: string, `get` atau `getall`. `get` akan ambil hasil pertama. Bila tidak ada, maka akan mengembalikan `None`. `getall` akan mengembalikan list.

### 2. panggil script dan pipe ke file kalau mau

```
pyinstantcrawl https://www.producthunt.com/protips protips.json
# atau simpan ke file
pyinstantcrawl https://www.producthunt.com/protips protips.json > producthunt-protips-result.json
```

## Dengan children

Ketika mengambil data dari suatu website, seringnya kita butuh beberapa
attribut dari item. Dan, `pyinstantcrawl` support itu.
Caranya: tambahkan property `children` di setiap item.

Sebagai contoh:

```
Posts
  |_ title
  |_ url
  |_ date
```

Sehingga, contoh json selector-nya adalah sebagai berikut:

```json
{
    "contents": {
        "expression": "//section[@id='content']/ul/li",
        "type": "xpath",
        "children": {
            "datetime": {
                "expression": "./time/text()",
                "type": "xpath",
                "getter": "get"
            },
            "url": {
                "expression": "./a/@href",
                "type": "xpath",
                "getter": "get"
            },
            "title": {
                "expression": "./a/text()",
                "type": "xpath",
                "getter": "get"
            }
        }
    }
}
```

simpan script diatas dengan `sample_with_child.json`, kemudian panggil dengan
`pyinstantcrawl https://blog.ihfazh.com/archives.html sample_with_child.json`

Di setiap children item, kita juga bisa kasih children lagi, dan di dalamnya
lagi seterusnya.

***

Perhatikan !

`"expression": "./time/text()"`, dot kemudian diteruskan dengan selector.
Maksudnya adalah selector / expression ini adalah relative dari
parentnya. Dengan kata lain ini seperti `parent_selector.child_selector`.
Kalau kita hilangkan dot, maka selector akan memulai lagi dari awal dokumen.

## Sebagai library

Kitapun dapat menggunakan `pyinstantcrawl` sebagai python library. Buka python intrepeter dan tuliskan kode berikut:

```
import pyinstantcrawl

sample_json = """
{
    "articles": {
        "expression": "//section[@id='listing']/article",
        "type": "xpath",
        "children": {
            "url": {
                "expression": ".//header//a/@href",
                "type": "xpath",
                "getter": "get"
            },
            "title": {
                "expression": ".//header//a/text()",
                "type": "xpath",
                "getter": "get"
            },
            "tags": {
                "expression": ".//header//div[has-class('w3-margin-right')][not(contains(@class, 'w3-opacity'))]/span",
                "type": "xpath",
                "children": {
                    "url": {
                        "expression": "./a/@href",
                        "type": "xpath",
                        "getter": "get"
                    },
                    "title": {
                        "expression": "./a/text()",
                        "type": "xpath",
                        "getter": "get"
                    }
                }
            }
        }
    },
    "next": {
        "expression": "//ul[has-class('w3-pagination')]/li/a[not(contains(@class, 'w3-green'))][last()]/@href",
        "type": "xpath",
        "getter": "get"
    }
}

"""

result = pyinstantcrawl.fetch('https://blog.ihfazh.com', sample_json)
```

## Penutup

`pyinstantcrawl` masih sangat baru, belum ada exception handling sama sekali. But its works as expected.

Untuk scrape simple website, `pyinstantcrawl` sudah cukup mengurangi "melanggar" DRY.

`pyinstantcrawl` juga cocok sebagai base dari *turn any website into json*. Atau dengan kata lain, untuk layanan mengubah website menjadi json, yang nantinya dipanggil dari frontend framework semisal reactjs, vue, angular, jquery atau lainnya bisa kamu sebutkan sendiri satu satu.

### Lebih lanjut:

- https://parsel.readthedocs.io/en/latest/usage.html#using-selectors
- https://www.w3schools.com/xml/xpath_syntax.asp
- https://www.w3schools.com/cssref/css_selectors.asp

Title: How To Get Random Item From Database Using Django
Date: 2022-12-29 11:37
Category: Django
Tags: django, query, random, queryset,python
Slug: how-to-get-random-item-from-database-using-django
Authors: Ihfazhillah
Summary: Are you a Django developer looking to get a random item from a database? We've got the answer for you — learn how here!

# Bismillah

Are you a Django developer looking to get a random item from a database? We've got the answer for you — learn how here!

### 1. Order by random, then limit 1

In django, we can sort the queryset by random using `order_by('?')` then get the first item. Here is the example

```python
from hello.models import Article

random_article = Article.objects.order_by("?").first()
```

However, this will scan through all rows in the database first. Then pick one result randomly.

Ofcourse, if the database has millions rows, this will slow down the database server and maybe kill your server. 
We should have another way to retrieve the random data.

### 2. Get the max id, get id randomly.

This only applicable if you have auto increment id. And in Django, this is the default one.

```python
import random

max_id = Article.objects.order_by("id").last()
random_id = random.randint(1, max_id)
random_article = Article.objects.get(pk=random_id)
```

although this method requires 2 hit into database, but this will more efficient for the larger database.

### How if the record not found?

Good catch!

Sometimes we deleted a row or multiple rows. Then when random_id match with the deleted rows, the django application will roar into us
"Hey, the record doesn't exist"

How we can avoid that? 

Well, you can do a `try` `except` until the record found.

```python
import random


article = None
max_id = Article.objects.order_by("id").last()
while article is None:
    random_id = random.randint(1, max_id)
    try:
        article = Article.objects.get(pk=random_id)
    except Article.DoesNotExists:
        print(f"article with id: {random_id} not found. Trying again...")
```

### Conclusion

That is:

- go with `order_by('?')` if you know the records not so big, or you have a big memory for your database.
- go with the second option, if you have many many of rows. Although it requires 2 or more hit into database, but the memory consumption is not so big.
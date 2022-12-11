Title: How To Zip Folder in Python
Slug: zipping-in-python
Date: 2022-12-11 22:35
Tags: python, django, zipfile, response
Category: Django
Summary: Zip folder in django on the fly.

# Bismillah

How if you want to provide your user a list of files in your backend server, and you want to provide them a zip file generated on the fly?

This article will cover that using python, and django framework. Let's dive in.

---

You can use `ZipFile` library to handle such condition. The constructor need a required parameter called `file`. The `file` parameter can be:
- a string. If a string provided, then ZipFile will use it as a path.
- a File object
- a file like object
- a path file like object

And the second parameter was an opening mode flag. Think like `open` library. `r` for read, and `w` as write, etc...

and also, you can use instance of `ZipFile` as context manager. That means if you go outside the `with` block, the zip file will be closed automatically.

---
Let's try to create a zip file from a folder. Supposed you have tree like this

```bash
folder
- audio1
- audio2
- audio3
```

After creating a `ZipFile` instance, you can use method `write` that accept `filename` parameter. 

In the following example, you can see I use the `arcname` parameter. This is optional. If not specified, the filename inside the zip file will match `filename` and stored in the one level.

But, if you want to persist the directory structure, you should specify this.


```python
import os
from zipfile import ZipFile

# we assume that the active directory was 
# same level with the `folder`

with ZipFile('folder.zip', mode='r') as compressor:
    for f in os.listdir("folder"):
        compressor.write(f, arcname=f)

```
---
Okay, that's enough. Let's use it in django. You may thinking to create a temporary file using `tempfile` library.

But, think again!

Django's `Response` was a File like object. You can use it as first parameter of `ZipFile` instead of create a temp file, then deleting it.

```python
    files = ["abc.txt", "def.txt", "ghi.txt"]

    response = HttpResponse(
        content_type="application/zip",
        headers={
            "Content-Disposition": f"attachment; filename=helloworld.zip"
        }
    )

    with zipfile.ZipFile(response, "w") as compressor:
        for file in files:
            compressor.write(default_storage.path(f"{file}"), arcname=file)

    return response
```
That's it. 
---

Refs:
- https://docs.python.org/3/library/zipfile.html
- https://docs.djangoproject.com/en/4.1/howto/outputting-csv

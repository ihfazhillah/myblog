Title: Nginx Error: connect() to /var/run/php7 .... no such file or directory
Date: 2017-12-12 06:53
Category: PHP
Tags: php, nginx, php7-fpm, error, no-such-file-or-directory
Author: Ihfazhillah
Summary: Cara mengatasi nginx-connect-to-unix-var-run-php7-0-fpm-sock-failed-2-no-such-file-or-dir

Bismillah,

Error ini, saya dapati ketika mengikuti tutorial di digitalocean. Kenapa ketika saya arahkan url ke folder dimana file php saya set di nginx malah muncul *502* error? Saya check di nginx log, ternyata errornya adalah sebagaimana yang disebutkan diatas.

Solusinya mudah: gunakan alamat `unix:/var/run/php/php7.0-fpm.sock`.

Perlu di ingat, ini adalah perbedaan letak antara `php5-fpm` dengan `php7.0-fpm`.

```
Nginx communicates with PHP-FPM using a Unix domain socket. Sockets map to a path on the filesystem, and our PHP 7 installation uses a new path by default:

PHP 5  /var/run/php5-fpm.sock

PHP 7  /var/run/php/php7.0-fpm.sock
```

https://stackoverflow.com/questions/40059745/nginx-connect-to-unix-var-run-php7-0-fpm-sock-failed-2-no-such-file-or-dir

Semoga membantu...

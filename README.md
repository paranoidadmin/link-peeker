# link-peeker
grow tiny urls

## Supported Shorteners
- tinyURL
- Bit.ly

##Usage
```
$ ./lp.py -h
usage: lp.py [-h] link

Reveal hidden links behind shortend URLS

positional arguments:
  link        The link you want to grow

optional arguments:
  -h, --help  show this help message and exit
$
```

##Example:
```
$ ./lp.py https://tinyurl.com/8k467rsz
The long link is: https://isitdns.com
$
```

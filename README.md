# Domain Expiry

Finds the given domain name's expiration date using only the Python Standard Library

## Usage

```
python3 domain_expiry.py example.com
```

Alternatively:

```
from domain_expiry import domain_expiry_date

expiry_date = domain_expiry_date('example.com')
```

The input should be any .com domain name, without prefixes like https:// or www.

## Output

The expiration date as a datetime object

As a fallback, if the date string couldn't be parsed, returns the date string as provided by the registrar

## Notes

Developed and tested using Python 3.9

Thanks to [Silver Moon at Binary Tides](https://www.binarytides.com/python-program-to-fetch-domain-whois-data-using-sockets/)

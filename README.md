BDPCrypt
=======

Encode/Decode Sony(TM) blueray images.

From console:
=============

$ pip install bdpcrypt


* Decrypt:

bdpcrypt  -s FW-CRYPTED.BIN -t FW-DECRYPTED.IMG -d true

* Encrypt:

bdpcrypt -s FW-DECRYPTED.IMG -t FW-ENCRYPTED.BIN -e true

From python
===============


```python

from bdpcrypt import BDPCrypter

crypter = BDPCrypter(options.source, options.destination)
crypter.crypt(options.encrypt)
```

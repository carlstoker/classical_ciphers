# Classical Ciphers
A collection of ciphers from the classical era. Inspired by [Practical Cryptography](https://practicalcryptography.com/ciphers/classical-era).

### rotation.py
[Caesar](https://en.wikipedia.org/wiki/Caesar_cipher) and [ROT13](https://en.wikipedia.org/wiki/ROT13) ciphers

#### Example
```python
import rotation
caesar = rotation.Rotate(-3) # Caesar cipher
rot13 = rotation.Rotate(13) # ROT13 cipher
```
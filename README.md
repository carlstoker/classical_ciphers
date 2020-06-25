# Classical Ciphers
A collection of ciphers from the classical era. Inspired by [Practical Cryptography](https://practicalcryptography.com/ciphers/classical-era).

### affine.py
Affine and Atbash ciphers
#### Example
The default alphabet for this cipher is the lowercase English alphabet.

`key_a` and the length of the default alphabet (26) must be [coprime](https://en.wikipedia.org/wiki/Coprime_integers).
````python
import affine
affine = affine.Affine(key_a, key_b)
````

##### Atbash Cipher
The Atbash cipher is a version of the Affine cipher, using 25 as both `key_a` and `key_b`
```` python
atbash = affine.Affine(25, 25)
````

### rotation.py
[Caesar](https://en.wikipedia.org/wiki/Caesar_cipher) and [ROT13](https://en.wikipedia.org/wiki/ROT13) ciphers

#### Example
```python
import rotation
caesar = rotation.Rotate(-3)
rot13 = rotation.Rotate(13)
```

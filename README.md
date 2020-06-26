# Classical Ciphers
A collection of ciphers from the classical era. Inspired by [Practical Cryptography](https://practicalcryptography.com/ciphers/classical-era).

Unless otherwise noted, the default alphabets for these ciphers is the lowercase English alphabet.

### [Affine](https://en.wikipedia.org/wiki/Affine_cipher) Cipher
A [monoalphabetic substitution cipher](https://en.wikipedia.org/wiki/Substitution_cipher#Simple_substitution).

`key_a` and the length of the alphabet (26 by default) must be [coprime](https://en.wikipedia.org/wiki/Coprime_integers).
#### Example
````python
from affine import Affine
key_a = 4
key_b = 9
a = Affine(key_a, key_b)
````

### [Atbash](https://en.wikipedia.org/wiki/Atbash) Cipher
The Atbash cipher is a version of the Affine cipher, using 25 as both `key_a` and `key_b`
````python
from atbash import Atbash
a = Atbash()
````

### [Caesar](https://en.wikipedia.org/wiki/Caesar_cipher) Cipher
A simple substitution cipher using a shift of 3. 

#### Example
```python
from caesar import Caesar
c = Caesar()
```

### [Gronsfeld](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#Variants) Cipher
A variant of the [Vigenère](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) cipher which uses numbers instead of letters for the key.
#### Example
````python
from gronsfeld import Gronsfeld
key = [1, 2, 3, 4, 5]
g = Gronsfeld(key)
````

### [ROT13](https://en.wikipedia.org/wiki/ROT13) Cipher
A simple substitution cipher using a shift of 13.

#### Example
```python
from rot13 import Rot13
r = Rot13()
```

### [Simple Substitution](https://en.wikipedia.org/wiki/Substitution_cipher#Simple_substitution) Cipher
A [monoalphabetic substitution cipher](https://en.wikipedia.org/wiki/Substitution_cipher#Simple_substitution) which shifts the plaintext by the specified `shift` parameter.
#### Example
````python
from substitution import Substitution
shift_value = 5
s = Substitution(shift_value)
````

### [Vigenère](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) Cipher
A [monoalphabetic substitution cipher](https://en.wikipedia.org/wiki/Substitution_cipher#Simple_substitution) which shifts the plaintext by the specified `shift` parameter.
#### Example
````python
from vigenere import Vigenere
key = "foobar"
v = Vigenere(key)
````

from affine import Affine
from atbash import Atbash
from caesar import Caesar
from gronsfeld import Gronsfeld
from rot13 import Rot13
from runningkey import RunningKey
from substitution import Substitution
from vigenere import Vigenere

ciphertexts = {
    'plaintext':    'the quick brown fox jumps over the lazy dog',
    'Affine':       'zrc kewsg npaov hat beqfu ajcp zrc lidy xam',
    'Atbash':       'gsv jfrxp yildm ulc qfnkh levi gsv ozab wlt',
    'Caesar':       'wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj',
    'Gronsfeld':    'ujh uzjen fwpyq jty lxqut qyiw ujh pfaa gsl',
    'Rot13':        'gur dhvpx oebja sbk whzcf bire gur ynml qbt',
    'Running Key':  'tdm puzfc kfpef ycs nrowm akwh npg vlxg qtu',
    'Substitution': 'xli uymgo fvsar jsb nyqtw sziv xli pedc hsk',
    'Viginere':     'vse imqek mtwlu jfz uueha qvpt bwl prbj dgy'
}


def test_affine_encrypt():
    plaintext = ciphertexts['plaintext']
    desired_ciphertext = ciphertexts['Affine']

    cipher = Affine(5, 8)
    encrypted_text = cipher.encrypt(plaintext)

    assert encrypted_text == desired_ciphertext


def test_atbash_encrypt():
    plaintext = ciphertexts['plaintext']
    desired_ciphertext = ciphertexts['Atbash']

    cipher = Atbash()
    encrypted_text = cipher.encrypt(plaintext)

    assert encrypted_text == desired_ciphertext


def test_caesar_encrypt():
    plaintext = ciphertexts['plaintext']
    desired_ciphertext = ciphertexts['Caesar']

    cipher = Caesar()
    encrypted_text = cipher.encrypt(plaintext)

    assert encrypted_text == desired_ciphertext


def test_gronsfeld_encrypt():
    plaintext = ciphertexts['plaintext']
    desired_ciphertext = ciphertexts['Gronsfeld']

    cipher = Gronsfeld([1, 2, 3, 4, 5])
    encrypted_text = cipher.encrypt(plaintext)

    assert encrypted_text == desired_ciphertext


def test_rot13_encrypt():
    plaintext = ciphertexts['plaintext']
    desired_ciphertext = ciphertexts['Rot13']

    cipher = Rot13()
    encrypted_text = cipher.encrypt(plaintext)

    assert encrypted_text == desired_ciphertext


def test_runningkey_encrypt():
    plaintext = ciphertexts['plaintext']
    desired_ciphertext = ciphertexts['Running Key']

    cipher = RunningKey('awizardsjobistovexchumpsquicklyinfogawizardsjobistovexchumpsquicklyinfog')
    encrypted_text = cipher.encrypt(plaintext)

    assert encrypted_text == desired_ciphertext


def test_substitution_encrypt():
    plaintext = ciphertexts['plaintext']
    desired_ciphertext = ciphertexts['Substitution']

    cipher = Substitution(30)
    encrypted_text = cipher.encrypt(plaintext)

    assert encrypted_text == desired_ciphertext


def test_viginere_encrypt():
    plaintext = ciphertexts['plaintext']
    desired_ciphertext = ciphertexts['Viginere']

    cipher = Vigenere('classicalcipher')
    encrypted_text = cipher.encrypt(plaintext)
    print(encrypted_text)

    assert encrypted_text == desired_ciphertext

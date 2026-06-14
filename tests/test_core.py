from shimbas_hax.core import deep_encrypt, deep_decrypt

def test_roundtrip():
    data=b"hello world"
    assert deep_decrypt(deep_encrypt(data))==data

def test_password():
    data=b"secret"
    assert deep_decrypt(deep_encrypt(data,"pw"),"pw")==data

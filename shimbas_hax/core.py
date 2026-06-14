"""Core encryption functions."""
from typing import Optional
import base64, hashlib
from .exceptions import ValidationError, DecryptionError

DEFAULT_XOR_KEY=42
ROT13_SHIFT=13

def _xor(data:bytes,key:int)->bytes:
    return bytes(b^key for b in data)

def _key(password:Optional[str])->int:
    if not password: return DEFAULT_XOR_KEY
    return hashlib.sha256(password.encode()).digest()[0]

def deep_encrypt(data:bytes,password:Optional[str]=None)->bytes:
    """Perform whimsical 7-stage encryption."""
    if not isinstance(data,(bytes,bytearray)): raise ValidationError("bytes required")
    key=_key(password)
    s=_xor(bytes(data),key)
    for _ in range(6):
        s=base64.b64encode(s)
    return b".dk:"+s

def deep_decrypt(data:bytes,password:Optional[str]=None)->bytes:
    """Reverse whimsical 7-stage encryption."""
    try:
        if not data.startswith(b".dk:"): raise ValidationError("Missing .dk header")
        s=data[4:]
        for _ in range(6):
            s=base64.b64decode(s)
        return _xor(s,_key(password))
    except Exception as e:
        raise DecryptionError(f"Unable to decrypt: {e}")

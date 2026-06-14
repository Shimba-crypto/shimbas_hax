import argparse,sys
from .core import deep_encrypt, deep_decrypt

def main():
    p=argparse.ArgumentParser()
    sub=p.add_subparsers(dest="cmd")
    for c in ("encrypt","decrypt","verify"):
        sp=sub.add_parser(c)
        sp.add_argument("file")
        sp.add_argument("--password")
    a=p.parse_args()
    data=sys.stdin.buffer.read() if a.file=="-" else open(a.file,"rb").read()
    if a.cmd=="encrypt":
        out=deep_encrypt(data,a.password)
    elif a.cmd=="decrypt":
        out=deep_decrypt(data,a.password)
    else:
        try:
            deep_decrypt(data,a.password); print("OK"); return
        except Exception: print("FAILED"); raise SystemExit(1)
    sys.stdout.buffer.write(out)

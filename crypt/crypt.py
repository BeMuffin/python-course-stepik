from simplecrypt import encrypt, decrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
    info = decrypt('RVrF2qdMpoq6Lib', encrypted).decode('utf-8') # use pycryptodome instead of pycrypto (it's not working with decrypt)
    print(info)


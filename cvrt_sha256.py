import hashlib
def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature
print("[ Ingrese dato ]")
hash_string = input()
sha_signature = encrypt_string(hash_string)
print("[ SHA256 ] \n",sha_signature.upper())

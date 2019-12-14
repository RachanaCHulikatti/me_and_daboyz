from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

from getpass import getpass






import sys
import os


if not os.path.isdir('keys'):
    print(' Private Key is missing ')
    print(' Decryption Unsuccessful ')
    sys.exit(1)




if len(sys.argv) != 2:
        print('Usage : decrypt.py filename')
        sys.exit(1)






file_in = open(sys.argv[1], "rb")

secret_code = getpass('Enter passphrase to retrieve privatekey >> ')


encoded_key = open(os.path.join('keys',"rsa_key.bin"), "rb").read()
private_key = RSA.import_key( encoded_key, passphrase=secret_code)

enc_session_key, nonce, tag, ciphertext =    [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

# Decrypt the session key with the private RSA key
cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(enc_session_key)

# Decrypt the data with the AES session key
cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)
print('-'*20, "Decrypted Message", '-'*20)
print(data.decode("utf-8"))
print('-'*20, "End of Decrypted Message", '-'*20)

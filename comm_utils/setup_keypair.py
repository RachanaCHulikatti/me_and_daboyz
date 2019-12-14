from Crypto.PublicKey import RSA
from getpass import getpass


import os


if not os.path.isdir('keys'):
    os.mkdir('keys')



if os.path.isfile(os.path.join('keys','rsa_key.bin')):
        print('Do you want to override existing pair ? ', end='')
        while True:
                   answer = input('Enter Yes or No >> ')
                   if answer in {'Yes', 'No' }:
                               print('\n\n') 
                               break

else:
    print('Generating a new keypair')
    answer = 'Yes'



if answer == 'Yes':


    while True:
        secret_code1 = getpass('Enter a passphrase to encrypt(AES128) RSA keypair >> ')
        secret_code = getpass('Confirm passphrase >> ')
        if secret_code == secret_code1:
                print('\n\n')
                break
        print('passphrase mismatch', end='\n\n') 




    key = RSA.generate(2048)
    encrypted_key = key.export_key(passphrase=secret_code, pkcs=8,
                              protection="scryptAndAES128-CBC")

    
    file_out = open(os.path.join("keys","rsa_key.bin"), "wb")
    file_out.write(encrypted_key)

    pubkey = key.publickey().export_key()
    open(os.path.join('keys','pubkey.pem'), 'wb').write(pubkey)

    text = pubkey.decode()
    print(text)



else :
     print("#"*10 + '    OLD PUBLIC KEY    ' + 10*'#', end ='\n\n')
     pubkey_text = open(os.path.join('keys','pubkey.pem')).read()
     print(pubkey_text)

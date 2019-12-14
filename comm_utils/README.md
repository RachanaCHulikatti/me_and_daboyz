

### Me and the boys secret stuff






a) setup a keypair 

Install a module if not exist 
pip3 install pycryptodome

and make a test
python3 -m Crypto.SelfTest


generate keypair and encrypt it with a passphrase

python3 setup_keypair.py




b)   Encrypt message

python3 encrypt.py message_text_file public_key_of_the_guy_you_need_to_communicate

* Produces encrypted_data.bin

c) Decrypt message

python3 decrypt.py  encrpyted_file





# References 


https://pycryptodome.readthedocs.io/en/latest/src/examples.html

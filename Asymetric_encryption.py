import rsa
from rsa.key import PrivateKey, PublicKey

message = "Aditya Parihar"

publicKey, privateKey = rsa.newkeys(512)
print(publicKey, privateKey)

encryption_message = rsa.encrypt(message.encode(), publicKey)
print(encryption_message)

decrypt_message = rsa.decrypt(encryption_message, privateKey).decode()
print(encryption_message)

# Asymmetric is a cryptographic algorithm that requires two separate keys, one private and the other public. 
# The message is encrypted with the public key and decrypted with the private key. 
# As a result, anyone with the public key can encrypt but not decrypt information. 
# The information can only be decrypted by someone who has the corresponding private key.
import rsa
from rsa.key import PrivateKey, PublicKey

message = "Aditya Parihar"

publicKey, privateKey = rsa.newkeys(512)
print(publicKey, privateKey)

encryption_message = rsa.encrypt(message.encode(), publicKey)
print(encryption_message)

decrypt_message = rsa.decrypt(encryption_message, privateKey).decode()
print(encryption_message)


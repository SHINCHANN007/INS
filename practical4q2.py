#aes

from aes_cipher import *

data = input("ENTER DATA : ")

data_encrypter = DataEncrypter()

data_encrypter.Encrypt(data,"palapala")
ct = data_encrypter.GetEncryptedData()

print("ENCRYPTED DATA : ",ct)

data_decrypted = DataDecrypter()
data_decrypted.Decrypt(ct,"palapala")

pt = data_decrypted.GetDecryptedData()

print("DECRYPTED DATA : ",pt)
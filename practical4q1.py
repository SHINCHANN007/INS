#des

from pyDes import *

pt = input("ENTER DATA : ")
key = input("ENTER KEY : ")

pt = pt.encode()
key = key.encode()

k = des(key,padmode=PAD_PKCS5)

ct = k.encrypt(pt)

print("ENCRYPTED DATA : ",ct.hex())
print("DECRYPTED DATA : ",k.decrypt(ct))






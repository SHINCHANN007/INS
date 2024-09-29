#rsa
from math import gcd

def isprime(a):
    for i in range(2,a):
        if a%i == 0:
            return False
    return True

p = int(input("ENTER P : "))
q = int(input("ENTER Q : "))

if not(isprime(p) and isprime(q)):
    raise Exception("NOT PRIME P AND Q")

n = p*q

phi = (p-1)*(q-1)

e= 2

while(e< phi):
    if(gcd(e,phi) == 1):
        break
    else:
        e+=1
        
d=2
while(True):
    if(((d*e)%phi)==1):
        break
    else:
        d+=1
        
m =int(input("message"))

c=(m**e)%n

k = (c**d)%n

print("encrypted",c)
print("decrypted",k)
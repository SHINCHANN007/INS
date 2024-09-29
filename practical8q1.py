#schonar
import hashlib

p = int(input("Enter a prime number: "))
q = int(input(f"Enter a prime factor of {p-1}: "))

alpha = 2
while True:
    if pow(alpha,q,p) == 1:
        break
    alpha += 1
print(alpha)

s = int(input(f"Enter a secret key between 0 and {q}: "))
a_s_mod = pow(alpha,s,p) 
v = pow(a_s_mod,-1,p)
print(v)
r = int(input(f"Enter a random number between 0 and {q}: "))
x = pow(alpha,r,p)

message = input("Enter a message: ")
combined = f"{message}{x}"
e = hashlib.sha1(combined.encode()).hexdigest()
e_int = int(e,16)

y = (r+s*e_int) % q
print(y)
#Verification
x_ = (pow(alpha,y,p)*pow(v,e_int,p)) % p
combined = f"{message}{x_}"
e_ = hashlib.sha1(combined.encode()).hexdigest()

print(f"Is signature valid?: {e==e_}")
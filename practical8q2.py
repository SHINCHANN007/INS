#elgamal

import math
import sympy
import hashlib

# Function to find a random integer k relatively prime to q-1
def relative_prime(q):
    for i in range(2, q):
        if math.gcd(i, q-1) == 1:
            return i
    return None

q = int(input("Enter a prime number (q): "))
alpha = sympy.primitive_root(q)
Xa = int(input("Enter private key (Xa): "))  # Private key
Ya = pow(alpha, Xa, q)  # Public key Ya = alpha^Xa mod q
print(f"Public key (Ya): {Ya}")

message = input("Enter message: ")
# Hash the message using SHA-1 and convert to an integer
m = int(hashlib.sha1(message.encode()).hexdigest(), 16)

# Select a random k that is relatively prime to q-1
k = relative_prime(q)
print(f"Random k: {k}")

# Calculate S1 and S2 for the signature
S1 = pow(alpha, k, q)
k_inv = sympy.mod_inverse(k, q-1)
S2 = (k_inv * (m - Xa * S1)) % (q-1)

# Signature (S1, S2)
print(f"Signature: S1 = {S1}, S2 = {S2}")


# Verification
v1 = pow(alpha, m, q)
v2 = (pow(Ya, S1, q) * pow(S1, S2, q)) % q

print(f"v1 = {v1}")
print(f"v2 = {v2}")

# Check if signature is valid
if v1 == v2:
    print("Signature is valid!")
else:
    print("Signature is invalid.")
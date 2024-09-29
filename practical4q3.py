#rc4
def rc4(key, data):
    S = list(range(256))
    j = 0
    key_length = len(key)

    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]

    i = 0
    j = 0
    output = []

    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        output.append(byte ^ K)

    return bytes(output)

key = input("Enter the key: ").encode() 
data = input("Enter the data: ").encode() 

ciphertext = rc4(key, data)
print(f'Encrypted: {ciphertext}')

plaintext = rc4(key, ciphertext)
print(f'Decrypted: {plaintext.decode()}')

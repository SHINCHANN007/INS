#cc
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encry(pt,k):
    
    ct =""
    
    if k.isalpha():
        k = chars.index(k.upper())
    else:
        k = int(k)
        
    for letter in pt.upper():
        ct += chars[(chars.index(letter)+k)%26]
    print(ct)
    
def decry(ct,k):
    
    pt =""
    
    if k.isalpha():
        k = chars.index(k.upper())
    else:
        k = int(k)
        
    for letter in ct.upper():
        pt += chars[(chars.index(letter)-k)%26]
    print(pt)
    


pt = input("ENTER PLAIN TEXT : ")
k =  input("ENTER KEY : ")

encry(pt,k)

ct = input("ENTER CHIPHER TEXT : ")

decry(ct,k)
    
#vigener

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encry(pt,k):
    
    ct = ""
    
    for i in range(len(pt)):
        ct += chars[ ( chars.index( pt[i].upper() ) + chars.index( k[i%len(k)].upper()) ) % 26 ] 
        
    print(ct)  
    return ct

def decry(ct,k):
    
    pt = ""
    
    key_len = len(k)
    
    for i in range(len(ct)):
        pt += chars[ ( chars.index(ct[i].upper()) - chars.index(k[i%len(k)].upper()) ) % 26 ]

    print(pt)
    return pt

pt = input("ENTER PLAIN TEXT : ")
k =  input("ENTER KEY : ")

ct = encry(pt,k)

decry(ct,k)
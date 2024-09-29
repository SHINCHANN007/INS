#vernam
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encry(pt,k):
    
    ct = ""
        
    for i in range(len(pt)):
        ct += chars[ ( chars.index( pt[i].upper() ) + chars.index( k[i].upper() ) ) %26 ]
        
    print(ct)

def decry(ct,k):
    
    pt = ""
        
    for i in range(len(ct)):
        pt += chars[ ( chars.index( ct[i].upper() ) - chars.index( k[i].upper() ) ) %26 ]
        
    print(pt)
    
pt = input("ENTER PLAIN TEXT : ")
k =  input("ENTER KEY : ")

encry(pt,k)

ct = input("ENTER CHIPHER TEXT : ")

decry(ct,k)
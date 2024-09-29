#railfence
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encry(pt,k):
    
    ct = []
    
    pt = pt.replace(" ","")
    pt = pt.upper()
    
    for i in range(k):
        
        ct.append(pt[i::k])
        
    print("".join(ct))
    return ct

def decry(ct,k):
    pt=""
    
    for i in range(len(ct[0])):
        try:
            for row in ct:
                pt += row[i]
        except IndexError:
            break
    print(pt)
pt = input("ENTER PLAIN TEXT : ")
k =  int(input("ENTER KEY : "))

ct = encry(pt,k)

decry(ct,k)
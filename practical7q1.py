#mb5
import hashlib

def file_check(filename):
    
    hash1=hashlib.md5()
    
    with open(filename,'rb') as fol:
        content = fol.read()
        
        hash1.update(content)
        
    print(hash1.hexdigest())
    
def pass_check(ps):
    hash1 = hashlib.md5(ps.encode('utf-8'))       
    
    print("YOUR MD5 PASSWORD IS : ",hash1.hexdigest())
    
print("ENTER 1 FOR FILE CHECK ")
print("ENTER 2 FOR PASSWORD CHECK ")
choice = int(input("ENTER CHOICE : "))

if choice == 1:
    filename = input("ENTER FILE NAME")
    file_check(filename)
    
elif choice == 2:
    ps= input("ENTER PASSWORD")
    pass_check(ps)
else:
    print(".........................")
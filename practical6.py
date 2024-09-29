#defihellman
import sympy

def hell(q,xa,xb):
    
    alpha = sympy.primitive_root(q)
    
    a=alpha**xa%q
    b=alpha**xb%q
    
    print(f"key pair of a : {xa,a}")
    print(f"key pair of a : {xb,b}")
    
    keya = b**xa%q 
    keyb = a**xa%q
    
    print(f"secret key of A AND B IS : {keya,keyb}")
    

hell(31,67,89)   
    
    
    
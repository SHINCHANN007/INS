#columnar
def encryption(pt,k):
    pt=pt.replace(" ","")
    ct = [""]*len(k) # ["","","","",""] for k =5
    for i in range(len(k)):
        ct[int(k[i])-1] += pt[i::len(k)]
    print(ct)
    ct = "".join(ct)
    print(ct)
    decryption(ct,k)

def decryption(ct,k):
    extra = len(ct) % len(k)
    general_column_length = len(ct) // len(k)
    pt = [""]*len(k)
    start_index = 0
    for i in range(len(k)):
        end_index = start_index + general_column_length
        real_index = k.index(str(i+1)) 
        print(real_index,i)
        if real_index+1 <= extra:
            end_index += 1
        pt[real_index] = ct[start_index:end_index]
        start_index=end_index
    print(pt)
    real_pt = ""
    for i in range(general_column_length):
        for col in pt:
            real_pt += col[i]
    
    for i in range(extra):
        real_pt += pt[i][-1]
    print(real_pt)
        
            
encryption("Hello Good Morning", "51423")
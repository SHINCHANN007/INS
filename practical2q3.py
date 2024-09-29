#playfair
chars = "abcdefghiklmnopqrstuvwxyz"

def matrix(key):
    key = key.lower()
    unique_key = sorted(set(key), key=key.index)
    matrix = []
    letter_pos = {}
    for char in chars:
        if char not in unique_key:
            unique_key.append(char)
    for i in range(5):
        matrix.append(unique_key[i*5:(i+1)*5])
    
    for i in range(5):
        for j in range(5):
            letter_pos[matrix[i][j]] = (i,j)
    
    return matrix,letter_pos

def playfair_encryption(pt,key):
    pt = pt.replace(" ","")
    pt = pt.lower()
    pt = pt.replace("j","i")
    km,lp = matrix(key)
    paired_pt = []
    i1 = 0
    i2 = 1
    while i2 < len(pt):
        if pt[i1] == pt[i2]:
            paired_pt.append([pt[i1],"x"])
            i1 += 1
            i2 += 1
        else:
            paired_pt.append([pt[i1],pt[i2]])
            i1 += 2
            i2 += 2
        if i1 == len(pt) - 1:
            paired_pt.append([pt[i1],"x"])
    ct = ""
    for pair in paired_pt:
        l1 = pair[0]
        l2 = pair[1]
        pos_l1 = lp[l1]    
        pos_l2 = lp[l2]
        if pos_l1[0] == pos_l2[0]:
            ct += km[pos_l1[0]][(pos_l1[1]+1)%5] + km[pos_l2[0]][(pos_l2[1]+1)%5] 
        elif pos_l1[1] == pos_l2[1]:
            ct += km[(pos_l1[0]+1)%5][pos_l1[1]] + km[(pos_l2[0]+1)%5][pos_l2[1]]
        else:
            ct += km[pos_l1[0]][pos_l2[1]] + km[pos_l2[0]][pos_l1[1]]
    print(ct)

def playfair_decrytpion(pt,key):
    km,lp = matrix(key)
    paired_pt = []
    i1 = 0
    i2 = 1
    while i2 < len(pt):
        if pt[i1] == pt[i2]:
            paired_pt.append([pt[i1],"x"])
            i1 += 1
            i2 += 1
        else:
            paired_pt.append([pt[i1],pt[i2]])
            i1 += 2
            i2 += 2
        if i1 == len(pt) - 1:
            paired_pt.append([pt[i1],"x"])
    pt = ""
    for pair in paired_pt:
        l1 = pair[0]
        l2 = pair[1]
        pos_l1 = lp[l1]    
        pos_l2 = lp[l2]
        if pos_l1[0] == pos_l2[0]:
            pt += km[pos_l1[0]][(pos_l1[1]-1)%5] + km[pos_l2[0]][(pos_l2[1]-1)%5] 
        elif pos_l1[1] == pos_l2[1]:
            pt += km[(pos_l1[0]-1)%5][pos_l1[1]] + km[(pos_l2[0]-1)%5][pos_l2[1]]
        else:
            pt += km[pos_l1[0]][pos_l2[1]] + km[pos_l2[0]][pos_l1[1]]
    pt = pt.replace("x","")
    print(pt)

playfair_encryption("helloohi","Hello")
playfair_decrytpion("eldloaaemv","Hello")
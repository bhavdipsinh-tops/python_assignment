with open("abc.txt") as f:
   
    l=f.readlines()
print(l)    

#remove new line char
l=[a.strip() for a in l]
print(l)

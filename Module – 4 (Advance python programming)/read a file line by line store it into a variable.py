f=open("abc.txt","r")
str=""

for i in range(0,100):
    str=str+f.read(i)

print(str)

'''
def read_file(file):
    with open(file,"r") as f:
        F=f.readlines()
        print(F)
read_file("abc.txt")    
'''

file=input("Enter the filename : ") #abc.txt

try:
    f=open(file,"r")
    d=dict()
    for i in f:
        words=i.split()
        print(words)
        for w in words:
            if w in d:
                d[w]=d[w]+1
            else:
                d[w]=1
                
    #print(d)
    for key in d.keys():
        print(key,":",d[key])
except:
    print("file not found")

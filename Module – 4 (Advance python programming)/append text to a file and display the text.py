def file(fname):
        from itertools import islice
        with open(fname, "w") as myfile:
                myfile.write("Python Developer\n")
                myfile.write("File Handling")
        txt = open(fname)
        print(txt.read())
        
file('abc.txt')

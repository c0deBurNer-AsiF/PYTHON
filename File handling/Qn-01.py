#write a function to write given string in a given file.

def writing(filename,text):
    f=open(filename,'w')
    f.write(text)
    f.close()

#writing('fileHandling.txt','hey codeburner')

#copy one file data to other file          

def copyData(oldfile,newfile):
    try:
        f=open(oldfile,'r')
        text=f.read()
        f.close()
        f=open(newfile,'w')
        f.write(''.join(text))
        f.close()
    except FileNotFoundError as e:
        print(e)


#copyData('fileHandling.txt','fileHandlingCopy.txt')

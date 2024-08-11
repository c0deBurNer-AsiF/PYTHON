#write, append, read, search, modify, delete, rename, remove how to do----->
import os

#write--->
def writing(FileName,text):
    f=open(FileName,'w')
    f.write(text)
    f.close()

#writing('File1.txt','Hello')

#append--->


def append(FileName,text):
    f=open(FileName,'a')
    f.write(text)
    f.close()

#append('fileHandling.txt','\n Asif')


#read---->


def read(FileName):
    try:
        f=open(FileName)
        text=f.read()
        print(text)
        f.close()
    except FileNotFoundError:
        print('File Not Found')

#read('File1.txt')

s=' my name is asif ali sahaji \n'
s+='here is my code \n'
s+='I wish its runs good \n'

#append("File1.txt",s)


#search--->


def search(FileName,word):
    try:
        f=open(FileName,'r')
        line_count=0
        for line in f.readlines():
            line_count+=1
            strlist=line.split(' ')
            word_count=0
            for w in strlist:
                word_count+=1
                if w==word:
                    return (line_count,word_count)
        else:
            return None
    except FileNotFoundError as e:
        print(e)
#print(search('File1.txt','here'))


#modify--->


def modify(FileName,Oldname,newName):
    t=search(FileName,Oldname)
    if t!=None:
        mylist=[]
        try:
            f=open(FileName,'r')
            for line in f.readlines():
                line=line.replace(Oldname,newName)
                mylist.append(line)
            f.close()    

            f=open(FileName,'w')
            f.write(''.join(mylist))
            f.close()
        except FileNotFoundError as e:
            print(e)
    else:
        print('Word not found!')

#modify('File1.txt','asif','ASIF')                        


#delete--->>


def delete(FileName,Oldname,newName=''):
    t=search(FileName,Oldname)
    if t!=None:
        mylist=[]
        try:
            f=open(FileName,'r')
            for line in f.readlines():
                line=line.replace(Oldname,newName)
                mylist.append(line)
            f.close()    

            f=open(FileName,'w')
            f.write(''.join(mylist))
            f.close()
        except FileNotFoundError as e:
            print(e)
    else:
        print('Word not found!')

#delete('File1.txt','ali')


#rename--->


os.rename('File1.txt','File2.txt')


#remove--->>


os.remove('File2.txt')






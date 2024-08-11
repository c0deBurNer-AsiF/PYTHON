#write a function to read text from a given file and display it on the screen 

def read(filename):
    try:
        f=open(filename,'r')
        text=f.read()
        print(text)
        f.close()
    except FileNotFoundError as e:
        print(e)
#read('fileHandling.txt') 

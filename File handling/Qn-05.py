#A file contains N lines, each line consist of a name and age separated by comma.
#write a function to read this file and store data in dict object with name as keys and age as value.
#Assuming the names are unique


def name_age(filename):
    try:
        with open(filename,'r') as f:
            dict_list={}
            for line in f:
                name,age=line.strip().split(',')
                dict_list[str(name.strip())]=int(age.strip())
            return dict_list 
           
    except FileNotFoundError:
        print("File not found")
        return {}
                
    
s='asif,21 \n'
s+='nil,20 \n'
s+='tani,24 \n'
filename='dict.txt'
with open(filename,'w') as f:
    f.write(s)

print(name_age(filename))




#2nd type---->>>



def name_age(filename,nameAndage):
    try:
        f=open(filename,'r')
        dict_list={}

        for line in f.readlines():
            key_value=[]
            line=line.strip().split(',')
            for i in line:
                key_value.append(i)
            dict_list[key_value[0]]=key_value[1]
        return dict_list    
        f.close()
    
    except FileNotFoundError as e:
        print(e)
        return {}

    

s='asif,21 \n'
s+='nil,20 \n'
#writing('dict.txt',s)    
#print(name_age('dict.txt',s))


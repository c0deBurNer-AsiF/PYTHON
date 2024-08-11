#write a function to read and store all the numbers found in a given text file into a list


def collectNumbers(filename):
    try:
        with open(filename,'r') as f:
            numbers=[]
            for line in f:
                words=line.split()
                for word in words:
                    try:
                        if '.' in word:
                            number=float(word)
                        else:
                            number=int(word)
                        numbers.append(number)

                    except ValueError:
                        pass 

        return numbers 
    except FileNotFoundError as e:
        print(e)
        return []

s='my age is 21.5 years, my mother is 40 \n'
s+='and my sister is 24 \n'
s+='my wife is 21'        
#writing('fileHandling.txt',s)
#print(collectNumbers('fileHandling.txt')) 



#2nd type--->>



def collectNumbers(filename):
    try:
        f=open(filename,'r')
        numbers=[]
        for text in f:
            text=text.split(' ')
            for number in text:
                if number[0] in '0123456789' and number[-1] in '0123456789':
                    try:
                        if type(eval(number))==int or type(eval(number))==float:
                            numbers.append(eval(number))
                    except NameError:
                        pass  
                    except:
                        pass          
                else:
                    pass          

        f.close()
        writing(filename,str(numbers))
    except FileNotFoundError as e:
        print(e)    
s='my age is 21.5 years, my mother is 40 \n'
s+='and my sister is 24 2abd3 \n'
s+='my wife is 21'        
#writing('fileHandling.txt',s)
#collectNumbers('fileHandling.txt')

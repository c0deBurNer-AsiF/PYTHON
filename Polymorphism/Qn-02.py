#overload greater than (>) operator in Time class which has instance object variable hour,min,sec

class Time:

    def __init__(self,hour,min,sec):
        self.hour=hour
        self.min=min
        self.sec=sec

    def show_time(self):
        print(self.hour,self.min,self.sec,sep=(':'))
  
    def adjustment(self):
        while self.min>60:
            self.min-=60
            self.hour+=1
        while self.sec>60:
            self.sec-=60
            self.min+=1   
 
    def __gt__(self,other):
        if self.hour>other.hour:
            return True
        elif self.hour==other.hour:
            if self.min>other.min:
                return True
            elif self.min==other.min:
                if self.sec>other.sec:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False        
        

'''
obj1=Time(2,130,76)
obj2=Time(2,61,45)
obj1.adjustment()
obj1.show_time()
obj2.adjustment()
obj2.show_time()
if obj1>obj2:
    obj3=obj1
else:
    obj3=obj2    
obj3.show_time()
'''


#2nd type---->>


class Time:

    def __init__(self,hour,min,sec):
        self.hour=hour
        self.min=min
        self.sec=sec

    def show_time(self):
        print(self.hour,self.min,self.sec,sep=(':'))
  
    def adjustment(self):
        while self.min>60:
            self.min-=60
            self.hour+=1
        while self.sec>60:
            self.sec-=60
            self.min+=1 
   
    def __gt__(self,other):
        if  self.hour>other.hour:
            return Time(self.hour,self.min,self.sec)
        elif self.hour==other.hour:
            if self.min>other.min:
                return Time(self.hour,self.min,self.sec)
            elif self.min==other.min:
                if self.sec>other.sec:
                    return Time(self.hour,self.min,self.sec)
                else:
                    return Time(other.hour,other.min,other.sec)
            else:
                return Time(other.hour,other.min,other.sec)
        else:
            return Time(other.hour,other.min,other.sec)

'''
obj1=Time(2,130,76)
obj2=Time(2,160,45)
obj1.adjustment()
obj1.show_time()
obj2.adjustment()
obj2.show_time()
obj3=obj1>obj2    
obj3.show_time()
'''

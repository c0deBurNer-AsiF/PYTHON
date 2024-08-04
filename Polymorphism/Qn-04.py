#define a class matrix with member variables rows and columns and a list to hold matrix elements.
#Overload + operator to add two matrix objects


class Matrix:
    def rowsNo_columnsNo(self,rows,columns):
        self.rows=rows
        self.columns=columns

    def matrix_input(self):
        self.matrix_list=[]
        print("Enter matrix elements row wise:")
        for i in range(0,self.rows*self.columns):
            self.matrix_list.append(eval(input()))


    def print_matrix(self):
        self.i=0
        
        for e in range(0,self.rows):
            self.matrix_rows_columns=[]
            for j in range(0,self.columns):
                self.matrix_rows_columns.append(self.matrix_list[self.i])
                self.i+=1
            print(self.matrix_rows_columns)

        print('\n')        


    def __add__(self,other):
        if len(self.matrix_list)!=len(other.matrix_list):
                raise "Two matrix should be same length"
        else:
            matrix_result=Matrix()
            matrix_result.rowsNo_columnsNo(self.rows,other.columns)
            matrix_result.matrix_list=[self.matrix_list[i]+other.matrix_list[i] for  i in range(len(self.matrix_list))] 
            return matrix_result   
'''
obj1=Matrix()
obj2=Matrix()
obj1.rowsNo_columnsNo(3,3)
obj2.rowsNo_columnsNo(3,3)
obj1.matrix_input()
obj2.matrix_input()
obj1.print_matrix()
obj2.print_matrix()
obj3=obj1+obj2
obj3.print_matrix()
'''

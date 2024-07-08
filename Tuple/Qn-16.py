#python script to create a list of tuple,where each tuple is a pair of elements,
# first elements is uppercase character and second element is its unicode..

l=[(chr(e),e) for e in range(65,91)]   
print(l)    

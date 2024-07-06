#To add two matrices each order of 3 x 3. store matrics elements in a list of lists


print("Enter 1st 3 x 3 matrics value row wise(seprated by comma):")
a=[
    [int(e) for e in input().split(",")],
    [int(e) for e in input().split(",")],
    [int(e) for e in input().split(",")]
]
print("Enter 2nd 3 x 3 matrics value row wise(seprated by comma):")
b=[
    [int(e) for e in input().split(",")],
    [int(e) for e in input().split(",")],
    [int(e) for e in input().split(",")]
]
c=[[0,0,0],[0,0,0],[0,0,0]]

print()

for i in range(0,3):
    for e in range(0,3):
        c[i][e]=a[i][e]+b[i][e]
        print(c[i][e],end=" ")
    print() 

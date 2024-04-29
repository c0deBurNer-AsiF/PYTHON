#Write a recursive function to calculate sum of cubes first N natural numbers.


def Nsumcubes(n):
    if n==1:
        return 1
    return n**3+Nsumcubes(n-1)

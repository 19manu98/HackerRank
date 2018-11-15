import sys


t = int(input("How many Numbers do you want to sum? ").strip())
for a0 in range(t):
    n = int(input("enter the number you want to sum ").strip())
    nFif = 0
    nThree = (n-1)//3
    nFive = (n-1)//5
    nFif = (n-1)//15
    print(3*nThree*(nThree+1)//2 + 5*nFive*(nFive+1)//2 - 15*nFif*(nFif+1)//2)

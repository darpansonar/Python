'''
4 3 2 1
4 3 2
4 3
4
'''
n=int(input("Enter n : "))

for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(j,end=" ")

    print()
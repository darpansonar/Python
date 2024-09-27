'''
A
A B
A B C
A B C D
'''
n=int(input("Enter n : "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print("%c" %(j+64),end=" ")

    print()
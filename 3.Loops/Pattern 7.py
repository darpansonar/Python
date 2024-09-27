'''
a
b b
c c c
d d d d
'''
n=int(input("Enter n : "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print("%c" %(i+96),end=" ")

    print()
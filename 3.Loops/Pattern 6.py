'''
a
a b
a b c
a b c d
'''
n=int(input("Enter n : "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print("%c" %(j+96),end=" ")

    print()
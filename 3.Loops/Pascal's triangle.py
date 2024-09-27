'''
      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
'''

n=int(input("Enter n : "))

for i in range(0,n):
    for j in range(0,n-i):
        print(" ",end="")

    num=1
    for k in range(0,i+1):
        print(num, end=" ")
        # Update num using Pascal's triangle formula
        num = num * (i - k) // (k + 1)

    print()



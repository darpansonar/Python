"""Write a Python program that takes a positive integer n from the user and prints the Collatz sequence
starting from n. The rules for generating the sequence are:
If n is even, the next number is n / 2.
If n is odd, the next number is 3n + 1.
The sequence continues until it reaches 1."""

n=int(input("Enter a positive integer : "))
print(n,end=" ")

while(n!=1):
    if(n%2==0):
        n=n/2
    elif(n%2==1):
        n=3*n+1
    print(int(n),end=" ")
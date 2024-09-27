n=int(input("Enter no. : "))
print("Factors : ")

for i in range(1,8):
    if(n%i==0):
        print(i,end=" , ")

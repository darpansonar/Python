number=str(input("Enter no. : "))
k=int(input("Find freq. of this digit : "))

count=0
for i in number:
    if(i==k):
        count=count+1

print("Freq. of digit",k,":",count)
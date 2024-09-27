sq={}

n=int(input("Enter no. of numbers : "))

for i in range(n):
    num=int(input())
    sq.update({num:num*num})

print("Dict = ",sq)

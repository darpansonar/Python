lst=[]

str=input("Enter elements of list : ")
lst=list(str.split())

n=input("Enter element that is to be searched : ")

if n in lst:
    print(n,"is present in list at the index",lst.index(n))

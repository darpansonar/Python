
list1=[1,2,"a","b","sunday","monday"]
list2=[3,4,"x","y","saturday","friday"]
#printing list
print(list1)

#printing elements of list
print(list1[2])
print(list1[4])
for i in list1:
    print(i,end=" ")

print("\n")

#Changing elements
list2[2]="c"
list2[4]="tuesday"
for i in list2:
    print(i,end=" ")

print("\n")

#Concatenation or addition of 2 lists
print(list1 + list2) ##Here, list1 and list2 are not modified

#Repetition
a=[10]*3
b=[1,2,3]*2
print(a)
print(b)

#Indexing (here, 1st element index=0)
print(list1[3])

#Slicing
print(list1[2:5]) #5 is not included
print(list1[:3])

#Membership
x="sunday"
if x in list1:
    print(x,"is present in list1")
else:
    print(x, "is not present in list1")

#Length of list
print(len(list1))

#list
x=list("Darpan")
print(x)

#index
print(list2.index("friday"))

#Append
list2.append("d")
print(list2)

#Extend
list1.extend(list2) #Here, list1 is modified
print(list1)

#Insert
list2.insert(3,"e")
print(list2)

#Pop
list2.pop(3)
print(list2)

#Remove
list2.remove("friday")
print(list2)

#clear
list1.clear()
print(list1)

#count
list3=['d','a','r','p','p','a','n']
print(list3.count('a'))
print(list3.count('p'))

#reverse
list3.reverse()
print(list3)

#sort
list3.sort()  #accending
print(list3)

list3.sort(reverse=True)  #descending
print(list3)

#sorted
list4=['c','a','b']
list5=sorted(list4)

print(list4)
print(list5)

#min,max,sum
list6=[1,2,3,4,5]
print(min(list6))
print(max(list6))
print(sum(list6))
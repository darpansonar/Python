week={}

print("Enter Day no. and Day names : ")

for i in range(7):
    no=input("Number :")
    day=input("Day name :")
    week.update({no:day})

print("Week = ",week)

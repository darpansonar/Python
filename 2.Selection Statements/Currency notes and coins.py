print("Notes & coins available : 500 , 200 , 100 , 50 , 20 , 10 , 5 , 2 , 1")
am=int (input("Enter amount in Rs : "))

a500=am//500
am=am%500

a200=am//200
am=am%200

a100=am//100
am=am%100

a50=am//50
am=am%50

a20=am//20
am=am%20

a10=am//10
am=am%10

a5=am//5
am=am%5

a2=am//2
am=am%2

a1=am//1

print("No. of rs500 notes : ",a500)
print("No. of rs200 notes : ",a200)
print("No. of rs100 notes : ",a100)
print("No. of rs50  notes : ",a50)
print("No. of rs20  notes : ",a20)
print("No. of rs10  notes : ",a10)
print("No. of rs5   notes : ",a5)
print("No. of rs2   notes : ",a2)
print("No. of rs1   notes : ",a1)





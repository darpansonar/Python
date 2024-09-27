'''
Note - Units = Current - previous units
       rate = Rs 1 if units<100
       rate = Rs 2 if units<=100 and units<200
       rate = Rs 3 if units<=200 and units<300
       rate = Rs 4 if units<>=300
'''

name=input("Customer name  : ")
cu=int(input("Current units  : "))
pu=int(input("Previous units : "))

units = cu - pu
print("Units          :",units)

if(units<100):
    print("Bill           : Rs",units*1)

elif(units>=100 and units<200):
    print("Bill           : Rs",(1*100) + (units-100)*2)

elif(units>=200 and units<300):
    print("Bill           : Rs",(1*100) + (2*100) + (units-200)*3)

elif(units>=300):
    print("Bill           : Rs",(1*100) + (2*100) + (3*100) + (units-300)*5)

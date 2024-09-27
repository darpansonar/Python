'''
Note:Taxable income(TI) = Annual income - Savings
     Maximum savings = Rs 1,50,000
     Tax=Rs 0 if TI <2,50,000
     Tax=Rs 10% of TI if TI >=2,00,000 and <5,00,000
     Tax=Rs 20% of TI if TI >=5,00,000 and <10,00,000
     Tax=Rs 30% of TI if TI >=10,00,000
'''

ai=int(input("Annual Income : "))
s=int(input ("Savings       : "))

if(s>150000):
    print("Savings should be less than Rs 1,50,000")

elif(s>=0 and s<150000):
    TI = ai - s

    if(TI<200000):
        print("Tax : Rs 0")

    elif(TI >= 200000 and TI <500000):
        print("Tax : Rs", (TI-200000)*(10/100 * TI))

    elif(TI>= 500000 and TI <1000000):
        print("Tax : Rs", (300000)*(10/100 * TI) + (TI-500000)*(20/100 * TI))

    elif(TI>=100000):
        print("Tax : Rs", (300000)*(10/100 * TI) + (500000)*(20/100 * TI) + (TI-1000000)*(30/100 * TI))


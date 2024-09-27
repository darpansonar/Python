#Function to find SI and CI - Parameterized

def simple_interest(p,n,r):
    si = (p*n*r)/100
    a = p + si

    print("\nSimple Interest = Rs",si)
    print("Amount = Rs",a)

def compound_interest(p,n,r):
    ci = (p * (1+r/100) ** n) - p
    a = p + ci

    print("\nCompound Interest = Rs %0.2f" %ci)
    print("Amount = Rs %0.2f" %a)

p=int(input("Enter Principal Amount : "))
n=int(input("Enter Period in years : "))
r=int(input("Enter Interest rate : "))

simple_interest(p,n,r)
compound_interest(p,n,r)
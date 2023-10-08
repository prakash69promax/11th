# GP code
a = float(input("Enter The first number :"))
r = float(input("Enter The common ratio :"))
n = float(input("Enter The nth term :"))
print("Enter 1 for finding nth term.")
print("Enter 2 for finding sum till nth term.")
print("Enter 3 for finding sum till infinte terms.")
x = int(input("Enter from (1/2/3) : "))
if x==1:
    nterm= a*(r**(n-1))
    print(nterm,'is the nth term.')
elif x==2:
    if r>1:
        s = (a*((r**n)-1))/(r-1)
        print(s,'is the sum of',n,'terms.')
    elif r<1:
        s1 = (a*(1-(r**n)))/(1-r)
        print(s1,'is the sum of',n,'terms.')
    elif r==1:
        s2 = n*a
        print(s2,'is the sum of',n,'terms.')
    else :
        print('Try again!')
elif x==3:
    if r>1:
        print("Error! As common ratio for infinity terms can not be greater than 1.")
    else:
        su = a/(1-r)
        print(su,'is the sum of infinte terms.')
else:
    print('Error! please try from 1/2/3 only.')




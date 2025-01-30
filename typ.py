a= int(input("enter a no: "))
sum =0 
digits =0
while a>0:
    digits += ((a%10) *10) + digits
    a/=10
print("rev: ",digits)
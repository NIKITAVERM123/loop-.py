i=int(input("enter the number"))
sum=0
org=i
while i>0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if org==sum:
    print("polidarm number")
else:
    print("not")


i=int(input("enter the number"))
fac=1
while i>0:
    fac=fac*i
    i=i-1
print("facterial number",fac)
i=1
while i<=100:
    if i%2!=0 and i%3!=0 and i%5!=0:
        print(i)
    elif i==2 or i==3 or i==5:
        print(i)
    i=i+1
a=int(input("enter the number :"))
i=1
c=0
while i<=a:
    if a%i==0:
        c=c+1
    i=i+1
if c==2:
    print("prime number")
else:
    print("no")


i=int(input("enter the number :"))
rev=0
x=i
while i>0:
    rev=(rev*10)+i%10
    i=i//10
if x==rev:
    print("palendorm")
else:
    print("not")
a=int(input("enter the number :"))
for i in a:
    c=0
    if a%i==0:
        c=c+1
if c==2:
    print("prime number")
else:
    print("na")
i=1
while i<=5:
    b=1
    while b<=5-i:
        print("",end=" ")
        b=b+1
    j=1
    while j<=i:
        print(i,end=" ")
        j=j+1
    print()
    i=i+1
i=1
a=int(input("enter the number :"))
i=1
c=0
while i<=a:
    if a%i==0:
        c=c+1
    i=i+1
if c==2:
    print("o")
else:
    print("nonne")
i=1
while i<=25:
    if i%2!=0 and i%3!=0 and i%5!=0:
        print(i)
    elif i==2 or i==3 or i==5:
        print(i)
    i=i+1
a=int(input("enter the number"))
fac=1
w
b=[]hile a>0:
    fac=fac*a
    a=a-1
print("factreal",fac)
from re import I


from re import I


i=int(input("enter the number :"))
org=i
sum=0
while i>0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if org==sum:
    print("amstrong")
else:
    print("none")
from ast import Num

num=int(input("enter the number :"))
rev=0
s=num
while num>0:
    rev=(rev*10) +num%10
    num=num//10
if s%rev==0:
    print("poliarm")
else:
    print("none")
a=int(input("enter the number:"))
i=0
b=[]
sum=0
while i<a:
    num=int(input("enter the number"))
    sum=sum+num
    b.append(num)
    i=i+1
print(sum)
a=[1,3,4,5,6,7]
i=0
b=[]
sum=0
while i<len(a):
    sum=sum+a[i]
    b.append(sum)
    i=i+1
print(sum)
a=[3,4,5,[4,5,6],9]
i=0
b=[]
sum=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            sum=sum+a[i][j]
            # b.append(sum)
            j=j+1
    else:
        sum=sum+a[i]
    i=i+1
print(sum)
a=[[12,23,11],[19,21,32],[25,16]]
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        s=a[i][j]%10
        d=a[i][j]//10
        f=s+d
        b.append(f)
        j=j+1
    i=i+1
print(b)
i=0
a=[1,2,3,4,5,6]
i=0
b=1
d=4
q=[]
while i<len(a):
    if i==b:
        q.append(10)
        b=b+2
    if i==d:
        q.append(20)
        d=d+1
    q.append(a[i])
    i=i+1
print(q)
def my_function(*kids):
      print("The youngest child is " + kids[8])

# my_function("Emil", "Tobias", "Linus")
def my_function(a):
     print(a+1)
     my_function(1) # def my_function(*kids):
      print("The youngest child is " + kids[8])

# def my_f## def my_function(*kids):
      print# def my_function(*kids):
      print("The youngest child is " + kids[8])

my_function("Emil", "Tb,obias", "Linus")
def my_function(a,b,c):
#      print(c,b,a)
#      print(c,b,a)
#      prinprint("raj")t(c,b,a)
# my_function(2,3,4)
# def fun(a,b,c):
#      print(a+b+1)
# fun(5,6,2)
# print("hellow")
# print("raj")
# a=[103,203,304,405,0]
# i=0
# b=[]
# while i<len(a):
#     s=str(a[i])
#     c=""
#     y=""
#     j=0
#     while j<len(s):
#         if s[j]=="0":
#             c=c+s[j]
#         else:
#             y=y+s[j]
#         j=j+1
#     b.append(int(c+y))
#     i=i+1
# print(b)
# a=[203,402,405,300,000]
# i=0
# b=[]
# while i<len(a):
#     s=str(a[i])
#     g=""
#     h=""
#     j=0
#     while j<len(s):
#         if s[j]!="0":
#             g=g+s[j]
#         else:
#             h=h+s[j]
#         j=j+1
#     b.append(int(g+h))
#     i=i+1
# print(b)
# def fun(num):
#     num=list(str(num))
#     length=len(num)
#     i=length-1
#     final=""
#     while i>=0:
#         if num[i]=="0":
#             num[i]=""
#         else:
#             break
#         i=i-1
#     print("".join (num))
# fun(9850000034434570000000)
# a=[10,20,30,20]
# b=[]
# i=0
# while i<len(a):
#     if a[i]%10==0:
#         b.append(a[i]//10)
#     if a[i]%100==0:
#         b.append(a[i]//100)
#     i=i+1
# print(b)
# a=[60,70,80,20,60]
# i=0
# b=[]
# while i<len(a):
#     while a[i]>0:
#         if  a[i]%
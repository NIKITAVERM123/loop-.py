a="nikita"
a+="verma"
print(a)
a=1
i=1
while i<5:
    j=1
    while j<=i:
        print(a, end="")
        j=j+1
        a=a+1
    print()
    i=i+1
a=1
i=1
while i<5:
    j=1
    while j<=i:
        print(a,end="")
        j=j+1
        a=a+1
    print()
    i=i+1
i=1
while i<=5:
    j=1
    while j<=i:
        print(i*j,end="")
        j=j+1
    print()
    i=i+1
i=1
while i<=9:
    j=1
    while j<=i:
        print(i,end="")
        j=j+2
    print()
    i=i+2
a=65
i=1
while i<=5:
    j=1
    while j<=i:
        print(chr(a),end="")
        j=j+1
        a=a+1
    print()
    i=i+1
a=65
i=1
while i<=5:
    j=1
    while j<=i:
        print(chr(a),end="")
        j=j+1
        a=a+1
    print()
    i=i+1
k=1
i=1
while i<=5:
    b=1
    while b<=5-i:
        print(" ",end=" ")
        b=b+1
    j=1
    while j<=i:
        print("*" ,end=" ")
        j=j+1
    # k=k+2
    print()
    i=i+1
def function():
    a=int(input("enter the number"))
    i=1
    c=0
    while i<=a:
        if a%i==0:
            c=c+1
        i=i+1
    if c==2:
        print("prime ")
    else:
        print("nonne")
function()
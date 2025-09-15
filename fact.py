n=int(input("enter the number"))
if (n<0):
    print("negative numbrers does not have factorial")
elif n==0 or n==1:
    print("factorial of the given number is 1")
else:
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("factorial of the given number is",fact)

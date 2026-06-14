def factorial(n):
    if(n==0 or n==1):
        return 1
    return n * factorial(n-1)

n = int(input("Enter a num: "))
print(f"Factorial of {n} is: {factorial(n)}")


'''Greatest of three num'''

def greatest(a,b,c):
    if(a>b and a>c ):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c
                               
a,b,c = map(int,input("Enter three numbers: ").split())

print(f"The greatest of three numbers is: {greatest(a,b,c)}")

def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

pattern(5)      
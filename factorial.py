#factorial: a Python function to calculate the factorial of a non-negative integer `n`.
'''def factorial(n):
    f=1
    while n>=1:
        f*=n
        n-=1
    return f

fact = int(input('factorial of: '))
print(factorial(fact))'''

#factorial recursive:


def factorial(n):
    #base case for recursion
    if n<1:
        return 1
    #recursive loop
    f = n*factorial(n-1)
    return f

fact = int(input("what number's factorial do you want?"))

print(factorial(fact))


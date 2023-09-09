#factorial program using recursion function#
def fact_rec(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rec(n-1)
number=int(input("Enter the number: "))
res=fact_rec(number)
print("The Value of Factorial of '{}' is '{}'.".format(number,res))
  
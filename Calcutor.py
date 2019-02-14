
from fractions import Fraction
from fractions import gcd
import math


def add(x, y):
   return x + y


def subtract(x, y):
   return x - y


def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y




mode = input("Normal(n) or scientific(s): ")



if mode == 'n':
   num1 = int(input("Enter first number: "))
   choice = input("Sign: ")
   num2 = int(input("Enter second number: "))
   if choice == '+':
      print(num1,"+",num2,"=", add(num1,num2))

   elif choice == '-':
      print(num1,"-",num2,"=", subtract(num1,num2))

   elif choice == '*':
      print(num1,"*",num2,"=", multiply(num1,num2))

   elif choice == '/':
      print(num1,"/",num2,"=", divide(num1,num2))

   elif choice == 'f':
      i = Fraction(num1, num2)
      print(i)

   elif choice == 'gcd':
      print("gcd of",num1,"and",num2,"=",gcd(num1, num2)) 
   else:
      print("Invalid input")

elif mode == 's':
 num1 = int(input("Enter first number: "))
 choice = input("Sign: ")

 if choice == 'surd':
  def sqrt(n):
   list = []
   N = n
   i = 100
   I = 0
   multiplier = []
 
   for p in range(0, 101):
    list.append(p ** 2)
 
   while i > 0:
    if n % list[i] == 0:
     multiplier.append(list[i])
     n //= list[i]
     i -= 1
    else:
     i -= 1
   
   product = multiplier[I]
   x = I + 1

   while x < len(multiplier):
    product *= multiplier[x]
    x += 1

   print("The surd form of the sqrt of", N, "is", int(math.sqrt(product)), "* sqrt of", n, ".")

  n = num1
  sqrt(n)
 elif choice == 'n/a':
   print('done')
 else:
   print('test')

else:
   print('n or s not pressed')





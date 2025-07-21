num = int(input("Enter a number: "))
factorial = 1
if num < 0:
 print("Factorial does not exist for negative numbers")
elif num == 0:
 print("The factorial of 0 is 1")
else:
 for i in range(1, num + 1):
 factorial = factorial * i
 print("The factorial of", num, "is", factorial)
Compiled by Prof. Sujata Oak
# factorial of given number
def factorial(n):
 if n < 0:
 return 0
 elif n == 0 or n == 1:
 return 1
 else:
 fact = 1
 while(n > 1):
 fact *= n
 n -= 1
 return fact
# Driver Code
num = 5
print("Factorial of",num,"is",
factorial(num))

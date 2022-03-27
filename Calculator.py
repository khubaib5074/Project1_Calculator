print('''Author: Khubaib Imran Malik''')
print('''Date: 27/03/2022''')
while True:
 start = int(input('''
 1. Arithmetic operations on two numbers
 2. Average of two numbers
 3. Greatest of four numbers
 4. Table of number
 5. Check if number is prime or not
 6. Find the sum of first 'n' natural numbers
 7. Find the factorial of number
 Select operation: '''))
 # /////////////////////////////////////////////////////
 # 1. Arithmetic operations on two numbers
 if start == 1:
   print('''\t"Program for arithmetic operations on two numbers!"''')
   a = eval(input("  Enter first number: "))
   b = eval(input("  Enter second number: "))
   c = int(input("1)Addition\n2)Subtraction\n3)Multiplication\n4)Division\nSelect operation:"))
   if c == 1:
      print("Value of sum of two numbers is: ", a+b)
   elif c == 2:
      print("Value of difference of two numbers is: ", a-b)
   elif c == 3:
      print("Value of product of two numbers is: ", a*b)
   elif c == 4:
      print("Value of quotient of two numbers is: ", a/b)
   else:
       print("Invalid operation!")
 # /////////////////////////////////////////////////////
 # 2. Average of two numbers
 elif start == 2:
   a = int(input("Enter first number: "))
   b = int(input("Enter second number: "))
   print("Average is:", (a+b)/2)
   A = [18, 23, 64, 92]
   for numbers in A:
    print(numbers)
 # /////////////////////////////////////////////////////
 # 3. Greatest of four numbers
 elif start == 3:
   num1 = int(input("Enter number 1: "))
   num2 = int(input("Enter number 2: "))
   num3 = int(input("Enter number 3: "))
   num4 = int(input("Enter number 4: "))
   l1 = [num1, num2, num3, num4]
   l1.sort() 
   print(f"The greatest of given four numbers is {l1[3]}.")
 # /////////////////////////////////////////////////////
 # 4. Table of number
 elif start == 4:
   number = int(input("Enter the number: "))
   i = 10
   while i > 0:
      print(f"{number} X {i} = {number*i}")
      i = i-1
   for i in range(11, 0, -1):
      # print(str(number) , "X", str(i)  , "=" , str(number*i))
      print(f"{number} X {i} = {number*i}")
 # /////////////////////////////////////////////////////
 # 5. Check if number is prime or not
 elif start == 5:
   num = int(input("Enter the number: "))
   prime = True
   for i in range(2, num):
     if(num%i == 0):
         prime = False
         break
   if prime:
    print("Given number is a prime number!")
   else:
     print("Given number is not a prime number!")
 # /////////////////////////////////////////////////////
 # 6. Find the sum of first 'n' natural numbers.
 elif start == 6:
   print("Program to find the sum of first 'n' natural numbers.")
   nnum = int(input("Enter n: "))
   sum = 0
   for i in range(1, nnum+1):
    sum = sum+i
   print(f"The sum of first {nnum} natural numbers is {sum}")
 # /////////////////////////////////////////////////////
 # 7. Find the factorial of number
 elif start == 7:
   z = int(input("Enter number: "))
   def fact_recursive(n):
    if n==1 or n==0:
        return 1
    return n * fact_recursive(n-1)
   fr = fact_recursive(z)
   print(f"Factorial of given number is {fr}.")
 else:
       print("Invalid operation!")
 # Repeat or not
 if input("Do you want to repeat the program?\n 1) Yes\n 2) No\n Enter: ") == '2':
      print("Thank You!")
      z = input("Press enter to exit program!")
      break
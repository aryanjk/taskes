# 1.  Write a Python function to multiply all the numbers in a list.
# # Sample list = [8,2,3,-1,7]

# def mul():
#     a=[8,2,3,-1,7]
#     b=1
#     for i in range(0,5):
#         b=a[i]*b
#     print(b)
# mul()

# # 2.  Write a Python function to sum all the numbers in a list.
# # Sample list : [8, 2, 3, 0, 7]

# def add():
#     a=[8,2,3,0,7]
#     b=0
#     for i in range(0,5):
#         b=a[i]+b
#     print(b)
# add()

# # 3.  Write a python function to find min of three numbers.(no parameter and no return type)

# def min(x,y,z):
#     if x<y and x<z:
#         print(x, 'is the smallest minimal integer.')
#     elif y<x and y<z:
#         print(y,'is the smallest minimal integer.')
#     else:
#         print(z,'is the smalles minimal integer')
# min(-2,3,1)
    
# ##################incase not with parameters#############################

# def min():
#     x=float(input('enter a number; '))
#     y=float(input('enter next number; '))
#     z=float(input('enter third number; '))
#     if x<y and x<z:
#             print(x, 'is the smallest minimal integer.')
#     elif y<x and y<z:
#         print(y,'is the smallest minimal integer.')
#     else:
#         print(z,'is the smalles minimal integer')
# min()

# # 4. Write a function called fizz_buzz that takes a number.
# # If the number is divisible by 3, it should return “Fizz”.
# # If it is divisible by 5, it should return “Buzz”.
# # If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# # Otherwise, it should return the same number.

# def fizz_buzz(input):
#     if (input % 3 == 0) and (input % 5 == 0):
#         return 'FizzBuzz'
#     if input % 3 == 0:
#         return 'Fizz'
#     if input % 5 == 0:
#         return 'Buzz'
#     return input
# print(fizz_buzz(33))
# print(fizz_buzz(5))

# # 5. Create a function that can accept two arguments name and age and print its value.

# def na(name,age):
#     print(f"your name is {name}, and you are existing from {age} years in time.")
# na("kevin","27")

# # 6. Write a program function to find max of three numbers.(no parameter and no return type)

# def gtx(x,y,z):
#     if x>y and x>z:
#         print(x,"is the greatest")
#     elif y>x and y>z:
#             print(y,"is the greatest")
#     else:
#         print(z,"is the greatest")
# gtx(3,0,1)

# # 7. Write a Python function to print the even numbers from a given list. 
# # sample: [1,2,3,4,5,6]

# def evn():
#     a=[1,2,3,4,5,6]
#     for b in a:
#         if b%2==0:
#             print(b,end=",")
# evn()   

# # 8. Write a Python function to print the odd numbers from a given list. 
# # sample: [1,2,3,4,5,6]

# def odd():
#     a=[1,2,3,4,5,6]
#     for b in a:
#         if b%2!=0:
#             print(b,end=",")
# odd()

# # 9. Write a Python function that takes a number as a parameter and check the number is prime or not

# def p(input):
#     if input>1:
#         for i in range(2,input):
#                 if input%i==0:
#                     print(input,'is not a prime number.')
#                     print(i,'times', input//i,'is', input)
#                 break
#     else:
#         print(input,'is a prime number')
    
# print(p(13))

# # 10. Write a function to reverse a string.

# def rev():
#     x="multiverse"
#     for j in range(9,-1,-1):
#         print(x[j],end="")
# # rev()

# # 12. Write a program to create function func1()
# #  to accept a variable length of arguments and print their value.

# def func1(*args):
#     print(*args)
    
# func1('hello', 'hi', 23, '2383')

# # 13  Write a program to create function calculation() such that it can accept 
# # two variables and calculate addition and subtraction.Also, it must return 
# # both addition and subtraction in a single return call

# def calculation(c,d):
#     print(c+d)
#     print(c-d)
#     return c,d
# calculation(6,3)

# # 14. Write a program to create a function show_employee() using the following conditions.
# # It should accept the employee’s name and salary and display both.
# # If the salary is missing in the function call then assign default value 9000 to salary

# def func(employee, salary=9000):
#     print('employee: ', employee )
#     print('Salary: ', salary)

# func('stevenGrant', 30000)
# func('Marc')

# # 15. Find the largest item from a given list. 
# # sample: [4, 6, 8, 24, 12, 2]

# sample=[4,6,8,24,12,2]
# print(max(sample))

# # 16. Find the smalles item from a given list. 
# # sample: [4, 6, 8, 24, 12, 2]

# smpl=[4,6,8,24,12,2]
# print(min(smpl))

# # 17. Define a function that accepts roll number and returns
# #  whether the student is present or absent.

# def rollno(rno):
#     x=[23,43,22,56]
#     if rno in x:
#         print(f'roll number {rno}, is present.')
#     else:
#         print(f'roll number {rno}, is absent')
# rno=int(input('enter a roll number'))
# rollno(rno)

# # 18. Define a function that accepts a number and returns whether the number is even or odd.

# def func(x):
#     if x%2==0:
#         print(f"{x}, is even")
#     else:
#         print(f"{x}, is odd")
# x=int(input('enter your number: '))
# func(x)

# # 19. Define a function which counts vowels and consonant in a word.

# def count(val):
#     vov=0
#     cons=0
#     for i in range(len(val)):
#         if val[i] in ["a",'e','i','o','u']:
#             vov=vov+1
#         else:
#             cons=cons+1
#     print("count of vowels is", vov)
#     print("count of consonant is", cons)
# x=input("enter sth; ")
# count(x)

# # 20. Define a function that returns Factorial of a number.

# def factorial(num):
#     fact=1
#     while(num!=0):
#         fact*=num
#         num=num-1
#     print("Factorial is", fact)
# num=int(input('enter a number'))
# factorial(num)

# # 21. Define a function that accepts lowercase words
# #  and returns uppercase words.

# def respone(text):
#     z=text.upper()
#     print(z)
# text=input('Enter a string.')
# response(text)

# # 22. Define a function that accepts radius and returns the area of a circle.

# def area(radius):
#     area=3.14*radius**2
#     return area
# radius=int(input('enter radii; '))
# print(area(radius))
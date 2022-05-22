'''
1. Write a python program to reverse a given list using while loop. 
a=[1,2,3,4]
'''
# a=[1,2,3,4]
# a.reverse()
# print(a)      


##----------------

# a=[1,2,3,4]
# temp=[]
# length=len(a)

# i=3
# while i>=0:
#     temp.append(a[i])

#     i=i-1
# print(temp)
   


'''
2.Write a python program to reverse a string using while loop. 
a="python"
'''
#same as list

# a='python'
# i=5
# while i>=0:
#     print(a[i], end="")
#     i=i-1
# print()


'''
3.Write a python program to print a multiplication table of any number using while loop. 
'''

# num1=int(input("Enter a number: "))
# times= int(input("Enter the multiplication maximum: "))
# i=1
# while i<=times:
#     print(f"{num1} * {i} = {num1*i}")
#     i=i+1


'''
4.Write a python program to reverse a given list using while loop.
'''

# list=["apple", 34, "htc", 45,"zte"]
# length= len(list)
# i=length-1                   #index
# reverse_list=[]
# while i>=0:
#     reverse_list.append(list[i])

#     i=i-1
# print(reverse_list)





'''
5.Write a program to print the following using while loop
a. first 10 even numbers
b.first 10 odd numbers
c.first 10 natural numbers
'''

# i=0
# print ("First EVEN numbers: ")
# while i<=19:
    
#     print(i, end=",")
#     i=i+2
# print()

# i=1
# print ("First ODD numbers: ")
# while i<=20:
    
#     print(i, end=",")
#     i=i+2
# print()

# i=1
# print ("First NATURAL numbers: ")
# while i<=10:
    
#     print(i, end=",")
#     i=i+1
# print()


'''
6.Write for loop statement to print the following series:
10 20 30 --------300
'''

# for i in range(10,301,10,):
#     print(i, end=" ")
# print()


'''
7. Write a while loop statement to print the following series:
105 98 -------7
'''


# i=105
# while i>=6:
#     print(i, end=" ")

#     i-=7

# print()


'''
8. Write a program to print the factorial of a number accepted from user.
'''


num=int(input("Enter a number: "))
factorial=1
if num<0:
    print("Factorial can be of positive number only.")
elif num==0:
    print("Factorial of 1: ", factorial)
else:
    for i in range(1,num+1):          #similar to i
        factorial=factorial*i
    print(factorial)
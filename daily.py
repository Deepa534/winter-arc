# number = int(input("Enter a  number:"))
# if number  == 0:
#     print("zero")
# elif number % 2 == 0:
#     print("even")
# else:
#     print("odd")


# number = int(input("Enter a number:"))
# if number > 0:
#     print("positive")
# elif number < 0:
#     print("negative")
# else:
#     print("zero")

#find the largest of two numbers
# a = int(input("Enter a number:"))
# b = int(input("Enter a number:"))
# if a > b:
#     print("a is larger then b")
# elif a < b:
#     print("a is smaller then b")
# else:
#     print(" a is equale to b  ")
#

# #pass or fail
# marks = int(input("Enter a marks:"))
# if marks >= 35:
#     print("pass")
# else:
#     print("fail")



#LOOP CONCEPT
# for i in range(0,4):
#     print(i)
# it prints 0 to 4 .

# WHILE LOOP
# i = 1
# while i <= 5:
#     print(i)
#     i = i+1

# Print a number from 1 to 10
# for i in range(1,11):
#     print(i)

#Print even number(2,20)
# for i in range(2,21,2):
#     print(i)
#

#Multiplication table from 1 to 10
# number = int(input("Multiplication number:"))
# for i in range(1,11):
#     print(f"{number} * {i} = {number * i}")

#SUM OF NUMBER 1 TO 10
# total = 0
# for i in range(1,11):
#     total = total + i
# print(f"sum is{total}")

#LEET CODE: 1
# class Solution:
#      def fizzBuzz(self,n:int):
#          ans = []
#          for i in range(1,n+1):
#              if i  % 3 == 0 and i % 5 == 0:
#                  ans.append("FizzBuzz")
#              elif i % 3 == 0:
#                  ans.append("Fizz")
#              elif i % 5 ==  0:
#                  ans.append("Buzz")
#              else:
#                  ans.append(str(i))
#
#          return ans
#
#
# print(Solution().fizzBuzz(15))
#
#LEET CODE 2413 smallest even multiple
# class Solution:
#     def smallestEvenMultiple(self,n:int ) -> int:
#         if n % 2 == 0:
#             return n
#         else:
#             return 2*n
#
#
# print(Solution().smallestEvenMultiple(5))
# print(Solution().smallestEvenMultiple(6))


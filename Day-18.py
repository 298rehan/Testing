# numbers = int(input("Enter the numbers: "))

# if numbers % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# Positive, Negative, or Zero
# num_first = int(input("Enter the first numbers: "))
# num_second = int(input("Enter the second numbers: "))
# num_third = int(input("Enter the third numbers: "))
#
# if num_first >= num_second and num_first >= num_third:
# print(num_first)
# elif num_second >= num_first and num_second >= num_third:
# print(num_second)
# elif num_third >= num_second and num_third >= num_first:
# print(num_third)
# else:
# print("Error@!@#")
#
# if num >= 1:
# print("Positive Number")
# elif num <= -1:
# print("Negative Number")
# else:
# print("Please Enter Greater or Lower digit from zero")

# # Calculator
# number = int(input("Enter your first number: "))
# operator = input("Enter your operator: ")
# num = int(input("Enter your second number: "))

# if operator == "+":
#     print("The sum is:", number + num)

# elif operator == "-":
#     print("The subtract is:", number - num)

# elif operator == "*":
#     print("The multiplication is:", number * num)

# elif operator == "/":
#     if num == 0:
#         print("Cannot divide by zero")
#     else:
#         print("The division is:", number / num)

# elif operator == "%":
#     if num == 0:
#         print("Cannot use modulo with zero")
#     else:
#         print("The modulo is:", number % num)

# else:
#     print("Invalid operator")

# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i)

# number = 1 + 2 + 3 + 4 + 5 + 6
# print(number)
# num = int(input("Enter your number: "))
# total = 0
#
# for i in range(1, num + 1):
# total = total + i
#
# print("Sum is = ", total)
#
# table_number = int(input("Enter the number: "))
#
# for i in range(1, 11):
# print(f"{table_number} * {i} = ", table_number * i)
#


# check_num = int(input("Enter the number: "))
# even_count = 0
# odd_count = 0
# for i in range(1, check_num + 1):
#     if i % 2 == 0:
#         even_count = even_count + 1
#     else:
#         odd_count = odd_count + 1

# print("Total Even Count = ", even_count)
# print("Total Odd Count = ", odd_count)


# Number Guessing Game

# secret_number = 7

# attempts = 0
# while True:
#     number = int(input("Enter the number b/w 1 to 10: "))
#     if number > 10 or number <= 0:
#         print("Please Enter number b/w 1 to 10")
#     elif number >= 8:
#         print("Go Lower!")
#     elif number <= 6:
#         print("Go Higher!")
#     elif number == 7:
#         print("You Guess Right!!!")
#         break
#     attempts += 1
# print(f"You took {attempts + 1} attempts to guess the number.")
# total attempts = 3 allow only 3 attempts to guess the password
# correct_password = "python123"

# attempts = 0
# while attempts < 3:
#     pass_checker = input(
#         "Guess the password: (Hint: Password starts with py or ends with 23): ")
#     if pass_checker == correct_password:
#         print("Access granted. Welcome!")
#         break
#     attempts += 1
#     if attempts < 3:
#         print("Incorrect password. Try again.")
#     else:
#         print("You have exceeded the maximum number of attempts. Access denied.")

# print("Calculate Your Percentage ")

# number = int(input("Enter your marks: "))

# total_marks = 550


# print(f"Your percentage is: {number / total_marks * 100:,.2f}")


# Day 01:

# print("Age Checker")
#
# age = int(input("Enter your age: "))
#
# if age < 13:
# print("Child")
# elif age <= 17:
# print("Teenager")
# elif age <= 59:
# print("Adult")
# elif age >= 60:
# print("Senior")
# else:
# print("Please type age!")


# print("Even / Odd + Positive / Negative")
#
# number = int(input("Enter your number: "))
#
# if number >= 1:
# print("Positive Number")
# if number % 2 == 0:
# print("Even Number")
# else:
# print("Odd Number")
# elif number <= -1:
# print("Negative Number")
# if number % 2 == 0:
# print("Even Number")
# else:
# print("Odd Number")


# print("Calculator")

# number = int(input("Enter your first number: "))
# operator = input("Enter your operator: ")
# second_number = int(input("Enter your second number: "))

# if operator == "+":
#     print("The sum is:", number + second_number)
# elif operator == "-":
#     print("The subtract is:", number - second_number)
# elif operator == "*":
#     print("The multiplication is:", number * second_number)
# elif operator == "/":
#     if second_number == 0:
#         print("Cannot divide by zero")
# elif operator == "/":
#     print("The division is:", number / second_number)
# elif operator == "  ":
#     if second_number == 0:
#         print("Cannot use modulo with zero")
#     else:
#         print("The modulo is:", number % second_number)
# else:
#     print("Invalid operator")

# print("Marks & Grade Checker")


# marks = int(input("Enter your marks: "))
#
# if marks >= 90:
# print("Your Grade is: A+")
# elif marks >= 80:
# print("Your Grade is: A")
# elif marks >= 70:
# print("Your Grade is: B+")
# elif marks >= 60:
# print("Your Grade is: B")
# elif marks >= 40:
# print("Your Grade is: C")
# elif marks < 40:
# print("Fail")
#
# print("Student Result Checker")


# def grade_checker(marks):
#     if marks >= 90:
#         return "A+"
#     elif marks >= 80:
#         return "A"
#     elif marks >= 70:
#         return "B+"
#     elif marks >= 60:
#         return "B"
#     elif marks >= 40:
#         return "C"
#     else:
#         return "Fail"


# name = input("Enter your name: ")
# math_marks = int(input("Enter your Math marks: "))
# english_marks = int(input("Enter your English marks: "))
# computer_marks = int(input("Enter your Computer marks: "))
# total_marks = math_marks + english_marks + computer_marks
# percentage = (total_marks / 300) * 100


# print(f"Name: {name}\n")

# print(f"Math Marks: {math_marks}")
# print(f"English Marks: {english_marks}")
# print(f"Computer Marks: {computer_marks}\n")

# print(f"Your total marks: {total_marks}")
# print(f"Your percentage is: {percentage:.2f}%")
# Grade = grade_checker(percentage, "\n")
# print(f"Your Grade is: {Grade}")
# status = "Pass" if percentage >= 40 else "Fail"
# print(f"Your Result is: {status}")


# start = int(input("Enter multiplication number = "))
# end = int(input("Enter end number = "))

# i = start
# total = 0
# while i <= end:
# if i % 2 == 0 and i % 7 == 0:
# total = total + i
# i += 1
# print(total)
# i = 1
# while i <= 10:
# print(f"{start} * {i} = ", i * start)
# i += 1
# while i <= start:
# if start % i == 0:
# print(i)
# i += 1
# start = int(input("Enter start number = "))
# end = int(input("Enter end number = "))
#
#
# for i in range(1, start):
# if start % i == 0:
# print(i)
#
#
# total = 0
#
# while True:
# number = int(input("Enter your number: "))
# if number < 0:
# continue
# if number == 0:
# break
# total += number
#
# print("The sum of the numbers is:", total)


# for i in range(1, 8):
#     for j in range(1, 6):
#         print(j, end=" ")
#     print()


for i in range(5, 0, -1):
    for j in range(6, 0, -1):
        print(i, end=" ")
    print()

print()
for i in range(1, 6):
    for j in range(1, i+1):
        print("0", end=" ")
    print()
print()
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print()
''' 
1
2 1
3 2 1
4 3 2 1 
5 4 3 2 1
'''
for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

print()

'''
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''

for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
print()
'''
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
'''
for i in range(1, 6):
    for j in range(5, i-1, -1):
        print(j, end=" ")
    print()

print()

'''
5 4 3 2 1
4 3 2 1
3 2 1
2 1 
1
'''
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

print()

'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
for i in range(4, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
print()
"""
5 
5 4
5 4 3
5 4 3 2
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""

for i in range(5, 0, -1):
    for j in range(5, i-1, -1):
        print(j, end=" ")
    print()
for i in range(1, 5):
    for j in range(5, i, -1):
        print(j, end=" ")
    print()
print()
'''
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
'''

for i in range(1, 6):
    for k in range(1, 6 - i):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print()

'''
        5
      5 4
    5 4 3
  5 4 3 2
5 4 3 2 1
'''

for i in range(1, 6):
    for k in range(1, 6-i):
        print(" ", end=" ")
    for j in range(5, 5-i, -1):
        print(j, end=" ")
    print()

print()

'''
       1
     1 2 3 
   1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
  1 2 3 4 5 6 7
    1 2 3 4 5 
      1 2 3
        1
'''

for i in range(1, 6):
    for j in range(1, 5 - i + 1):
        print(" ", end=" ")
    for k in range(1, (i * 2) - 1 + 1):
        print("*", end=" ")
    print()
for i in range(4, 0, -1):
    for j in range(1, 5 - i + 1):
        print(" ", end=" ")
    for k in range(1, (i * 2) - 1 + 1):
        print("*", end=" ")
    print()

print()

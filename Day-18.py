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


print("Calculate Your Percentage ")

number = int(input("Enter your marks: "))

total_marks = 550


print(f"Your percentage is: {number / total_marks * 100:,.2f}")

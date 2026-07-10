# course = "Programming"
# print(len(course))
# print(course[0])
# print(course[0:4])
# print(course[:5])
# print(course[3:])
# course = "  hello kessy ho  "
# print(course)
# print(course.capitalize())
# print(course.lower())
# print(course.strip())
# print(course.lstrip())
# age = 14
# message = "Eligible" if age >= 18 else "Not eligible"
# print(message)
# high_salary = True
# good_credit = False
# student = False
# if (high_salary or good_credit) and not student:
#     print("Eligible for this loan")
# else:
#     print("Not eligilbe for this loan")
# # Print 2 table:
# Take_num = input("Enter the number=")
# for number in range(1, 11):
#     print(Take_num, "*", number, "=", number * int(Take_num))

# def name(first_name, last_name):
#     print(f"Hello {first_name} {last_name} Welcome to Karachi")


# Take_name = input("Enter your first name:")
# Take_name2 = input("Enter your last name:")
# name(Take_name, Take_name2)
# def number(bill_amount):
#     total_bill = float(bill_amount) * 1.18
#     return total_bill


# bill_input = input("Enter your total bill: ")
# print("Your Total Bill after tax is", number(bill_input))
# ---------------------------------------------------------------------------------------
# Day: 05 learning python
# s = "rehan"
# print("hey", 6, 8, sep="~", end="009\n")
# print("hello")
# ----------------------------------------------------------------------------------
# Day: 06 learning python
# Calculator Program
# n = int(input("Enter first number:"))
# m = int(input("Enter second number:"))
# print("The sum of", n, "and", m, "is", n+m)
# print("The substraction of", n, "and", m, "is", n-m)
# print("The multiplication of", n, "and", m, "is", n*m)
# print("The division of", n, "and", m, "is", n//m)
# print("The square of", n, "is", n**m)
# ---------------------------------------------------------------------------------------
# Day: 07 learning python
# a = 23.4
# print(a)
# print(type(a))
# b = 23
# print(b)
# print(type(b))
# c = a + b
# print(c)
# print(type(c))
# ---------------------------------------------------------------------------------------
# Day: 08 learning python
# a = int(input("Enter Number:"))
# b = int(input("Enter Number:"))
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a ** b)
# print(a % b)

# name = ("Hello my name is Rehan")
# for character in name:
#     print(character)
# name = "Harry"
# print(len(name))
# print(name[-4:-2]) # --> its print ar because if we minus -4 from the len of string which is 5 then it will be 1 and -2 will be 3 so it will print from 1 to 3 & 3 is not included :)

# STRINGS METHODS
# str1 = "welcome to Day 09 of LearNIng PyThon !!! "
# print(len(str1))
# print(str1.endswith("!!! "))
# print(str1.endswith("to", 4, 10))
# print(str1.upper())
# print(str1.lower())
# print(str1.find("heloo"))
# print(str1.capitalize())
# print(str1.strip())
# print(str1.rstrip("!"))
# print(str1.replace("o", "0"))
# print(str1.split(" "))
# print(str1.center(10))
# print(str1.count("n"))
# print(str1.index("D"))
# str2 = "Loginpage123"
# print(str2.isalnum())
# str3 = "enter"
# print(str3.isalpha())
# print(str3.islower())
# print(str3.isprintable())
# str1 = "Welcome"
# print(str1.istitle())
# print(str1.isupper())
# print(str1.startswith("WEL"))
# print(str1.swapcase())
# str4 = "Hello my friend how are you my friend"
# print(str4.title())

# IF-ELSE PRACTICE

# budget = int(input("Enter your budget:"))
# applePrice = 200

# if (budget - applePrice <= 50):
#     print("Mt khareed bhai")
# elif (budget >= 1000):
#     print("Acha khareed le bhai")
# else:
#     print("kahreed na bhai")

# NESTED IF-ELSE PRACTICE

# num = int(input("Enter your number:"))
# if (num < 0):
#     print("Number is negative")
# elif (num > 0):
#     if (num <= 10):
#         print("The number is b/w 0 and 10")
#     elif (num > 10 and num < 20):
#         print("The number is b/w 10 and 20")
#     else:
#         print("the number is greater than 20")

# ---------------------------------------------------------------------------------------

# Day: 09 learning python

# task completed good morning message:

# time = float(input("Enter the time: "))
# check = (input("Enter AM or PM: ")).strip().upper()
# if (check == "AM"):
#     print("Good morning")
# elif (check == "PM"):
#     if (time < 5):
#         print("Good Afternoon")
# else:
#     print("Good Night")


# ---------------------------------------------------------------------------------------
# Day: 09 learning python

# for i in range(1, 11, 3):
#     print(i)

# for i in range(12):
#     if (i == 10):
#         break
#     print("5 X", i + 1, "=", 5 * (i+1))
# print("Loop ended")


# count = 5
# while (count > 0):
#     print(count)
#     count = count - 1
# ---------------------------------------------------------------------------------------
# Day: 10 learning python

# Function
# num = int(input("Enter the number: "))


# def Table(num):
#     for number in range(1, 11):
#         print(num, "*", number, "=", num*number)


# Table(num)


# def oddeven(odd):
#     if (odd % 2 == 0):
#         print(f"{odd} is even number")
#     else:
#         print(f"{odd} is odd number")


# odd = int(input("Enter the number: "))

# oddeven(odd)

# ---------------------------------------------------------------------------------------
# Day: 11 learning python

# learning List

# l = [1, 2, 10, 405, 10, 9000]
# l.append(100)  # --> it will add 100 at the end of the list
# l.sort(reverse=True)  # --> it will sort the list in ascending order
# l.reverse()  # --> it will reverse the list
# --> it will add multiple values at the end of the list
# m = [22, 33, 44]
# l.extend(m)
# l.insert(2, 500)  # --> it will insert 500 at index 1
# print(type(l))
# print(l[0:-2])
# print(m)
# colors = ["voilet", "green", "indigo", "blue"]
# newlist = colors.copy()
# print(colors)
# print(newlist)
# print(l)
# ---------------------------------------------------------------------------------------

# Day: 12 learning python

# learning Tuple
# t = (1, 2, 3, 4, 5)
# print(t)
# print(type(t))
# # t[0] = 10  # --> This will raise an error because tuples are immutable
# t1 = (1,)  # --> This is a tuple with one element
# print(t1)
# t2 = ()  # --> This is an empty tuple
# print(t2)

# KBC project:

# print("Welcome to KBC")

# questions = ["Question 1: What is the capital of Pakistan? a: Islamabad b: Karachi c: Lahore d: Peshawar",
#              "Question 2: SQL stands for? a: Strong Question Language b: Structured Query Language c: Stylish Question Language d: Stylesheet Query Language",
#              "Q4uestion 3: Who is the founder of Microsoft? a: Steve Jobs b: Elon Musk c: Mark Zuckerberg d: Bill Gates",
#              "Question 4: What is the largest planet in our solar system? a: Earth b: Jupiter c: Saturn d: Mars"]
# for q in questions:
#     print(q)
#     answer = input("Enter your answer (a/b/c/d): ")
#     if (q == questions[0] and answer.lower() == 'b') or (q == questions[1] and answer.lower() == 'b') or (q == questions[2] and answer.lower() == 'd') or (q == questions[3] and answer.lower() == 'b'):
#         print("Correct! You win 3000 points.")
#     else:
#         correct_answer = 'b' if q == questions[0] else 'b'
#         print(f"Incorrect! The correct answer is option {correct_answer}.")

# print("Thank you for playing KBC!")
# print("Your total points: 12000")


# ---------------------------------------------------------------------------------------

# Day: 13 learning python

# Fibonacci series:
# def fibonacci(num):
#     if num == 0 or num == 1:
#         return num
#     else:
#         return fibonacci(num-1) + fibonacci(num-2)


# n = int(input("Enter the number of terms: "))
# print("Fibonacci series:", fibonacci(n))


# def fibonacci(num):
#     if num == 0 or num == 1:
#         return num
#     else:
#         return fibonacci(num-1) + fibonacci(num-2)


# n = int(input("Enter the number: "))
# print(f"Fibonacci series of this num {n} is: ", fibonacci(n))


# info = {"Carlos", 38, "Engineer", "Carlos", 123456789}
# print(info)
# for value in info:
#     print(value)

# ---------------------------------------------------------------------------------------

# Age = 19
# Fvrt_food = "Pizza"
# print(f"Your age is {Age}")
# print(f"My favourite food is {Fvrt_food}")
# print("Hello")

# ---------------------------------------------------------------------------------------

# Day: 14 learning python (Shopping Cart Program)
import math

# item = input("Enter the item you want to buy: ")
# quantity = int(input("Enter the quantity: "))
# price = float(input("Enter the price: "))
# total = quantity * price
#
# print(f"The Total of your's is ${total}")

# (Area Of a Circle):

# radius = float(input("Enter the Radius of the Circle: "))

# area = math.pi * pow(radius, 2)

# print(f"The area of a circle is {round(area, 2)}cm²")


# a = float(input("Enter the side A: "))
# b = float(input("Enter the side B: "))

# c = math.sqrt(pow(a, 2) + pow(b, 2))

# print(f"The Side C is {round(c, 2)}")

# operator = input("Enter the operator (+ - / *)")
# number1 = float(input("Enter your first number: "))
# number2 = float(input("Enter your second number: "))
#
# if operator == "+":
# result = number1 + number2
# print(result)
#
# elif operator == "-":
# result = number1 - number2
# print(result)
#
# elif operator == "*":
# result = number1 * number2
# print(result)
#
# elif operator == "/":
# result = number1 / number2
# print(result)
#
# else:
# print("Something is wrong!!")
#
# (Weight Converter Program):

# weight = float(input("Enter yout weight: "))
# unit = input("Kilogram or Pounds? (K or L)")
#
# if unit == "K":
# weight = weight * 2.205
# unit = "Lbs"
# elif unit == "L":
# weight = weight / 2.205
# unit = "Kgs"
# else:
# print(f"{unit} is not valid!")
#
# print(f"Your weight is {round(weight, 1)} {unit}")
#
# (One-Line if-else even or odd check):

# num = float(input("Enter your number: "))
# result = "EVEN" if num % 2 == 0 else "ODD"
# print(result)

# user_role = "primary_user"

# access_level = "Full access" if user_role == "admin" else "Access denied"

# print(access_level)

# (Username checker):

# username = input("Enter Your Username: ")
# #
# if len(username) > 12:
#     print("Your username can't be more than 12 characters")
# elif not username.find(" ") == -1:
#     print("Please enter username without spaces")
# elif not username.isalpha():
#     print("Your username can't be contain numbers")
# else:
#     print(f"Welcome {username}")
#
# ---------------------------------------------------------------------------------------

# Day: 15 learning python

# (Showing last digits credit card number)
# credit_number = "1234-5678-9012-3456"

# last_digits = credit_number[-5:]

# print(f"XXXX-XXXX-XXXX{last_digits}")


# price1 = 3.1241
# price2 = 6453.43
# price3 = 187512.14
#
# print(f"price1 is Rs {price1:,.2f}")
# print(f"price2 is Rs {price2:,.2f}")
# print(f"price3 is Rs {price3:,.2f}")


# (PSX Interest rate calculator)


print("PSX Interest rate calculator")

amount = 0
rate = 0
time = 0
monthly_rate = 0
total_months = 0


while amount <= 0:
    amount = float(input("Enter the amount Rs: "))
    if amount <= 0:
        print("The amount can't be less than zero")

while rate <= 0:
    rate = float(input("Enter the interest rate %: "))
    if rate <= 0:
        print("The interest rate can't be less than zero")

while time <= 0:
    time = float(input("Enter how much year's: "))
    if time <= 0:
        print("The time can't be less than zero")


monthly_rate = (rate / 100) / 12

total_months = time * 12

monthly_amount = total_months * amount

total = amount * (pow(1 + monthly_rate, total_months) - 1) / monthly_rate

your_profit = total - monthly_amount

print(f"Your own deposits Rs: {monthly_amount:,.2f}")

print(f"Balance after {time} year's will be Rs: {total:,.2f}")

print(f"Your profit will be Rs: {your_profit:,.2f}")

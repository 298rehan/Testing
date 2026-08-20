# numbers = int(input("Enter the numbers: "))

# if numbers % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# Positive, Negative, or Zero
num_first = int(input("Enter the first numbers: "))
num_second = int(input("Enter the second numbers: "))
num_third = int(input("Enter the third numbers: "))

if num_first >= num_second and num_first >= num_third:
    print(num_first)
elif num_second >= num_first and num_second >= num_third:
    print(num_second)
elif num_third >= num_second and num_third >= num_first:
    print(num_third)
else:
    print("Error@!@#")

    # if num >= 1:
    # print("Positive Number")
    # elif num <= -1:
    # print("Negative Number")
    # else:
    # print("Please Enter Greater or Lower digit from zero")

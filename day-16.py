# import time
#
# my_time = int(input("Enter a time in seconds: "))
#
# for x in range(my_time, 0, -1):
# seconds = x % 60
# minutes = int(x / 60) % 60
# hours = int(x / 3600)
# print(f"{hours:02}:{minutes:02}:{seconds:02}")
# time.sleep(1)
#
# print("Happy New Year🥳🥳!!!!")


# rows = int(input("Enter the No. of Rows: "))
# columns = int(input("Enter the No. of Columns: "))
# symbol = input("Enter the Symbol: ")

# for x in range(1, 5):
# for y in range(1, 7):
# print("*", end=" ")
# print()

# (Food Cart):

# foods = []
# prices = []
# total = 0
#
# while True:
# food = input("Enter Your Food name (q for Quit): ")
# if food.lower() == "q":
# break
# else:
# price = float(input(f"Enter the price of a {food}: $"))
# foods.append(food)
# prices.append(price)
#
#
# print("----Your Cart----")
#
# for food in foods:
# print(food, end=" ")
# print()
#
# for price in prices:
# total = total + price
#
# print(f"Your Total is: ${total}")


# Concession stand program

menu = {"pizza": 500,
        "burger": 400,
        "popcorn": 600,
        "lays": 100,
        "drinks": 150,
        "fries": 120}

cart = []
total = 0

print("--------MENU--------")
for key, value in menu.items():
    print(f"{key:10}: Rs{value:.2f}")

print("---------------------")


while True:
    food = input("Enter the food name (q for Quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("-----YOUR ORDER-----")

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: Rs{total:.2f}")

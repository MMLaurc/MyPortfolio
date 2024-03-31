# create list called menu with 10 items to sold in cafe
menu_list = ["Cappuccino", 
            "Cafe Latte", 
            "Flat White", 
            "Espresso", 
            "Belgian Chocolate",
            "Iced Tea",
            "Cheesecake", 
            "Brownie", 
            "Choco Fudge", 
            "Strawberry Cake"
            ]
print(menu_list)

# create a dictionary called stock with value of stock for each item
stock_dict = {'Cappucino': 54,
              'Cafe Latte': 78,
              'Flat White': 63,
              'Espresso': 69,
              'Belgian Chocolate': 35,
              'Iced Tea': 55,
              'Cheseecake': 25,
              'Brownie': 29,
              'Choco Fudge': 22,
              'Strawberry Cake': 20}
print(stock_dict)

# create a dictionary called price with the price for each item
price_dict = {'Cappucino': 1.99,
              'Cafe Latte': 2.99,
              'Flat White': 1.49,
              'Espresso': 1.79,
              'Belgian Chocolate': 1.29,
              'Iced Tea': 1.88,
              'Cheseecake': 1.34,
              'Brownie': 4.99,
              'Choco Fudge': 2.39,
              'Strawberry Cake': 3.99}
print(price_dict)

# create a loop called total stock to calculate the total of cafe stock menu and print total
total_stock = 0
for item in stock_dict:
    total_stock = (stock_dict[item] * price_dict[item])
    print(f"Total items stock for {item} is {total_stock}")




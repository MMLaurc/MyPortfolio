"""
Create a holiday calculator

Create a Menu:
- chose one of the 3 city for holiday
- how many days will stay in hotel
- how many days will rent a car

- create user input :   - city_flight
                        - num_nights
                        - rental_days
                        
- create functions to calculate:
                        - hotel_cost
                        - plane_cost
                        - car_rental
                        - holiday_cost
"""

# Show users choise of cities
print("Holiday to: ")
print ("-" * 60)
print("London - £520\nParis - £450\t\t\nBucharest - £346\t")

#Ask the destination city
while True:
    city_flight = input("Please chose one of the city above where you want to flight: ")
    if city_flight.lower() == "london":
        break
    if city_flight.lower() == "paris":
        break
    if city_flight.lower() == "bucharest":
        break
    print("Please chose one of available options")

print ("-" * 60)

# Show user the price per night
print("Price per night to stay in hotel is £70! ")

# Ask user how many nights will stay
while True:
    try:
        num_nights = int(input("Please chose how many nights you will stay in hotel: "))
        break
    except ValueError:
        print("Oops! Please enter a valid number!")

print ("-" * 60)

# Show user the price for rent a car
print("Price per day to rent a car is £25 ")

# Ask the user how many days will rent the car
while True:
    try:
        rental_days = int(input("Please chose how many days you will rent a car: "))
        break
    except ValueError:
        print("Oops! Please enter a valid number!")

print ("-" * 60)

# Calculate the hotel cost for user input
def hotel_cost(nights, price):
    total = int(nights * price)
    return total  

total_hotel_price = hotel_cost(num_nights, 70)
print(f"Total price for {num_nights} nights will be £{total_hotel_price}!")

# Calculate the cost of flight for user
def plane_cost(city_flight):
    if city_flight.lower() == "london":
        return 520
    elif city_flight.lower() == "paris":
        return 450
    elif city_flight.lower() == "bucharest":
        return 346
    return 0

total_plane_cost = plane_cost(city_flight)

# Calculate total price to rent a car for user       
def car_rental(rent, price):
    total = int(rent * price)
    return total

total_rent_car = car_rental(rental_days, 25)
print(f"Total price for {rental_days} days to rent a car will be £{total_rent_car}! ")

# Calculate the total price of holiday for user
def holiday_cost(hotel, plane, car):
    return hotel + plane + car

total = holiday_cost(total_hotel_price, total_plane_cost, total_rent_car)
print(f"The total price of your holiday will be £{total} ")

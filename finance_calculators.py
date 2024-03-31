"""
    start to import math
    print investment and bond as string
    add  input variable to take data from user 
    add condition if user chose investment to take data as money,interest,years
    add another input to chose what tipe of investment user wnat simple or compound
    if user chose simple use formula for simple interest
    if user chose compund use formula for compund interest
    elif in case user chose bond to take data for a house as house value,interest and years
    else in case user chose a wrong option than investment or bond to get a specific message
    
"""
import math
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond \t   - to calculate the amount you'll have to pay on a home loan ")

investment_bond = str(input("Enter either 'investment' or 'bond' from the menu above to proceed:") )
  
if investment_bond.lower() == "investment":
    amount_deposit = int(input("Please add the amount of money you want to deposit:")) 
    interest_rate = int(input("Please enter the interest rate (don't use 8%, example '8'):"))  
    invest_year = int(input("Please enter the number of years you plan to invest:"))
    interest = str(input("Please chose 'simple' or 'compound' interest:"))
    
    if interest.lower() == "simple":
        simple_interest = amount_deposit *(1 + (interest_rate / 100) * invest_year)
        print(f"Total amount once the interest is applied: {simple_interest}")
        
    elif interest.lower() == "compound":
        compound_interest = amount_deposit * math.pow((1 + interest_rate / 100),invest_year)
        print(f"Total amount once the compound interest applied is: {compound_interest}")
        
elif investment_bond.lower() == "bond":
    house_value = int(input("Please enter the value of the house:"))
    interest_rate_house = int(input("Please enter the interest rate (don't use 8%, example '8'):"))
    number_month = int(input("Please enter the number of months you plan to repay the bond:"))
    repayment = (((interest_rate_house/100)/12) * house_value) / (1 - (1 + ((interest_rate_house/100)/12))**(-number_month))  
    print(f"Total amount that you have to repay on a home loan each month is:{repayment}")    
     
else:
    print("Please chose one of available option above.")



# Displaying the menu to the user
print("WELCOME TO FINANCE CALCULATOR!")
print("INVESTMENT - to calculate the amount of interest you'll earn on your investment")
print("BOND - to calculate the amount you'll have to pay on a home loan")
user_input = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# Handling user input for selection
if user_input == 'investment':
    # Getting user input for investment calculation
    principal_amount = float(input("Enter the amount of money that you are depositing: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
    years = int(input("Enter the number of years the money will be invested: "))
    interest_type = input("Enter 'simple' or 'compound' interest: ").lower()
    
    # Calculating the interest amount
    if interest_type == 'simple':
        interest = principal_amount * (1 + interest_rate * years)
    elif interest_type == 'compound':
        interest = principal_amount * (1 + interest_rate) ** years
    
    # Displaying the result
    print(f"The total amount after {years} years will be: {interest}")

elif selection == 'bond':
    # Getting user input for bond calculation
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate: ")) / 100
    months = int(input("Enter the number of months to repay the bond: "))
    
    # Calculating the monthly repayment amount
    monthly_interest_rate = interest_rate / 12
    repayment = (monthly_interest_rate * present_value) / (1 - (1 + monthly_interest_rate) ** -months)
    
    # Displaying the result
    print(f"The monthly repayment will be: {repayment:.2f}")
else:
    # Handling invalid input
    print("Invalid selection. Please enter 'investment' or 'bond'.")

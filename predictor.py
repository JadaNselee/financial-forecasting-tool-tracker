print("Welcome to the Investment Return Predictor!")
  
# Ask user for investment details 
initial_amount = float(input("Enter the amount you're investing (in $): "))
annual_rate = float(input("Enter the expected annual return rate (in %): ")) 
years = int(input("Enter how many years you plan to invest: ")) 

 # Convert rate from percentage to decimal
 rate_decimal = annual_rate / 100 

# Compound interest formula: A = P * (1 + r) ^ t 
final_amount = initial_amount * (1 + rate_decimal) ** years 

print(f"\nAfter {years} years, your investment will be worth approximately ${final_amount:.2f}") 

# Optional: Calculate total profit
profit = final_amount - initial_amount
print(f"Your total profit will be: ${profit:.2f}")

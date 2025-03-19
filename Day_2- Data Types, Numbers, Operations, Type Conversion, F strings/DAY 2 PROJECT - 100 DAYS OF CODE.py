# DAY 2 QUESTION

"""You and your friends went out for dinner and got a total bill. 
You also want to leave a tip (10%, 12%, or 15%). 
Write a Python program that:
Asks the user for the total bill amount.
Asks how much tip they would like to give (10, 12, or 15%).
Asks how many people will split the bill.
Calculates how much each person should pay, including the tip.
Rounds the amount to 2 decimal places and displays the final amount per person.
"""

# solution

print("Welcome to Tip Calculator")
total_bill = float(input("What was the total bill? : $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15 : "))
people_to_share = int(input("How much people to share the bill?"))
bill = (total_bill+ (tip/100 * total_bill) )
amount_per_person = bill/people_to_share
final_amount = round(amount_per_person, 2)
print(f"Each person to pay: $ {final_amount}")






      





      
      

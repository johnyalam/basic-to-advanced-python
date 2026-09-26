# Asks for the user's name.
# Asks how many hours they worked this week (whole number).
# Asks their hourly rate in euros (can be a decimal, e.g. 12.50).
# Calculates the weekly earnings (hours × rate).
# Calculates an estimated monthly earnings (weekly × 4).
# Prints a summary with money shown to 2 decimal places.

name = input("Enter Your Name: ")
hours = int(input("Hours worked this week: "))
rate = float(input("Hourly rate (€): "))

weekly = hours * rate
monthly = weekly * 4

print("--- Earnings Summary ---")
print(f"Name: {name}")
print(f"Weekly earnings: €{weekly:.2f}")
print(f"Estimated monthly: €{monthly:.2f}")
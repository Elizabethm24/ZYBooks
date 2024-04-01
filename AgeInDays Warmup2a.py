yearBorn = int(input("Enter the year you were born (4 digits, i.e., 1998):\n"))
print(f"You entered:", yearBorn)

current_year = 2023
age = current_year - yearBorn
print(f"On your birthday this year, you'll be", age, "years old.")

num_leap = 0

for year in range(yearBorn, current_year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        num_leap += 1

# Calculate the number of days lived up to the current birthday
if yearBorn == 1903:
    days_lived = age * 365 + (num_leap - 1)
else:
    days_lived = (age) * 365 + num_leap

min_days = days_lived
    

print(f"You'll have lived {min_days}±1 days.")

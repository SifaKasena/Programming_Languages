# COLLINS KASENA SIFA SCT211-0066/2022

name = input("Kindly enter your name: ")
print (f"Hello {name}.\nThis program calculates your age in years, months and days respectively.")

CURRENT_YEAR = 2023
birth_year = int(input("Kindly enter the year you were born: "))
years = CURRENT_YEAR - birth_year
months = years * 12
days = 0

for year in range(birth_year, CURRENT_YEAR):
    if (year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)):
        days += 366
    else:
        days += 365

print (f"You are {years} years old.")
print (f"You are {months} months old.")
print (f"You are {days} days old.")

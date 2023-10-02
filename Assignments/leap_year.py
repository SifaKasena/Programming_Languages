# COLLINS KASENA SIFA SCT211-0066/2022

name = input("Kindly enter your name: ")
print (f"Hello {name}.\nThis program checks if a given year is a leap year or not.")

year = int(input("Kindly enter the year you want to check: "))

if (year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)):
    print (f"Hello {name}. The year {year} is a leap year.")
else:
    print (f"Hello {name}. The year {year} is not a leap year.")

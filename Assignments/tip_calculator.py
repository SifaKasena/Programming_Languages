# COLLINS KASENA SIFA SCT211-0066/2022

name = input("Kindly enter your name: ")
print (f"Hello {name}.\nThis program calculates how much each one should pay to cover the bill and tip.")

total_bill = float(input("Kindly enter the total bill to the nearest cent: "))
tip = int(input("Kindly enter the tip percentage form the following options.\n\t1 for 10%\n\t2 for 12%\n\t3 for 15%\nEnter your choice: "))
no_of_people = int(input("Kindly input the total nomber of people splitting the bill: "))

if tip == 1:
    tip_percentage = 10
elif tip == 2:
    tip_percentage = 12
else:
    tip_percentage = 15

tip = tip_percentage/100 * total_bill
total_amount = total_bill + tip
amount_per_person = total_amount/no_of_people

print("Each person should pay total of {:.2f}".format(amount_per_person))

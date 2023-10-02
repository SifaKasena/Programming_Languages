# COLLINS KASENA SIFA SCT211-0066/2022

name = input("Kindly enter your name: ")
print (f"Hello {name}.\nThis program calculates your BMI based on your height and weight and tells you your weight category.")

height = float(input("Kindly enter your height in meters(m) to the closest centimeter: "))
weight = float(input("Kindly enter your weight in kilograms(kg) to the nearest gram: "))

your_bmi = weight / (height**2)

if your_bmi >= 25:
    print ("{}, your BMI is {:.2f}. This shows that you are overweight.".format(name, your_bmi))
elif your_bmi >= 18.5:
    print ("{}, your BMI is {:.2f}. This shows that you are of normal weight.".format(name, your_bmi))
else:
    print ("{}, your BMI is {:.2f}. This shows that you are underweight.".format(name, your_bmi))

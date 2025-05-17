w = int(input("Enter your Weight"))
h = int(input("Enter your Height"))
BMI = w / (h/100)**2
print(BMI)

if BMI > 5 and BMI < 20:
 print("You are Underweight")
elif BMI > 20 and BMI < 35:
 print("You are healthy")
elif BMI > 35 or BMI == 35:
 print("You are Overweight")
else:
 print("You are either Under or Overweight, Please Consult a Doctor")
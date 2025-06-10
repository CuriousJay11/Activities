number=int(input("Input Number: "))
result = 0
temp = number
while temp!=0:
    digit = temp % 10
    result = result+digit**3
    temp =  temp //10
print(result)
if number == result:
    print(number,"Its a armstrong number")
else:
    print(number,"Its not a armstrong number")
 

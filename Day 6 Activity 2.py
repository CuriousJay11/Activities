a = 14
b = 7
c = 4
d = 3
answer = d**c+a*b/a
print(answer)

n1 = int(input("Enter Numerator:"))
n2 = int(input("Enter Denominator:"))

if n1%n2==0:
    print(str(n1)+ " is divisible by "+str(n2))
else:
    print(str(n1)+ " is not divisible by "+str(n2))
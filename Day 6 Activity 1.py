s1 = int(input("Enter Your First Speed : "))
s2 = int(input("Enter Your Second Speed : "))
s3 = int(input("Enter Your Third Speed : "))

average = (s1+s2+s3)/3
print("The average speed is :", average)

if s1<average:
    print("Speed 1 is slower than the average with the difference of",average-s1)
elif s2<average:
    print("Speed 2 is slower than the average with the difference of",average-s2)
elif s3<average:
    print("Speed 3 is slower than the average with the difference of",average-s3)
else:
    print("None of these conditions apply")
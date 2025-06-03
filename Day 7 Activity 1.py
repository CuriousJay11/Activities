Medical_Cause = input("Does the student have a medical cause? (Y or N)?")
Attendance = int(input("Enter student's attendance:"))

if Medical_Cause == "Y"or Medical_Cause == "y":
    print("You are allowed")
else:
    if Attendance>=75:
        print("You are allowed")
    else:
        print("You are not allowed")
    
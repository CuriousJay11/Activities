op = float(input("What is the original price"))
sp = float(input("What is the selling price"))

if sp > op:
    print("The Profit is", sp - op)
else:
 print("The Loss is", op - sp)
 
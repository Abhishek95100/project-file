# दो numbers input लो और print करो कौन सा बड़ा है

num1 = float(input("Enter the number:"))
num2 = float(input("Enter the number:"))

if num1>num2:
    print(num1,"is greater")
elif num2>num1:
    print(num2,"is greater")
else:
    print("both number are equal")


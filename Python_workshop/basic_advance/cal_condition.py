num1 = int(input("enter first no: "))
num2 = int(input("enter second no : "))

choice = input("enter the operation: (option are + , -, *, /, %)")

if choice == "+":
    sum = (num1 + num2)
    print("addition_of_num", sum)

elif choice == "-":
    sub = (num1 -num2)
    print("subtraction_of_num", sub)

elif choice == "*":
    multi = (num1 *num2)
    print("multiplication_of_num",multi)
elif choice == "/":
    division = (num1 / num2)
    print("division_of_num", division)
elif choice == "%" :
    module = (num1 % num2)
    print("reminder_of_num", module)

else:
    
    print("invalid operation")


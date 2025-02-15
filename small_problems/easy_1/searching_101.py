num1 = input("Enter the first number? ")
num2 = input("Enter the second number? ")
num3 = input("Enter the third number? ")
num4 = input("Enter the fourth number? ")
num5 = input("Enter the fifth number? ")
num6 = input("Enter the sixth number? ")

numbers = [num1, num2, num3, num4, num5]

if num6 in numbers:
    print(f"{num6} is in {', '.join(numbers)}")
else:
    print(f"{num6} isn't in {', '.join(numbers)}")
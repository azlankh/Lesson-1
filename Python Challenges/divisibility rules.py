digit = int(input("Enter a Number: "))
digit2 = int(input("Enter another Number: "))
if digit % digit2 == 0:
    print(f"{digit} is divisible by {digit2}")
else:
    print(f"{digit} is not divisible by {digit2}")

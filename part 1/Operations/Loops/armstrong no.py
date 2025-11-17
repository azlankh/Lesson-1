num = int(input("Enter A Number: "))
print("Checking If Armstrong NUmber Or Not.....")
sum = 0
arms = num
while arms > 0:
    digit = arms % 10
    sum += digit ** 3
    arms //= 10
if num == sum:
    print(num, "Is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")
num = int(input("Enter A number that you want to find the sum of: "))

sum = 0

for i in range(1, num+1):
    sum = sum + i
    print("The sum is: ",sum)
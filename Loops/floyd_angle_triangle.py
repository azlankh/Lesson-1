print("The Floyd's Triangle")

rows = int(input("Enter The number Of Rows:"))
num = 1
for i in range(1,rows):
    for j in range(1,i+1):
        print(num, end=" ")
        num += 1
    print()

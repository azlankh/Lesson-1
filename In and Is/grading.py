sub1 = float(input("Enter marks for English: "))
sub2 = float(input("Enter marks for Maths: "))
sum = sub1 + sub2
print("Your total marks are:", sum)
average = sum / 2
print("Your average marks are:", average)
if average >= 90:
    print("Grade A")
elif average >= 80:
    print("Grade B")
else:
    print("Grade C")
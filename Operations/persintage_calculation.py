science = float(input("Enter Your Marks IN Science:"))
maths = float(input("Enter The Marks Of Maths:"))
hindi = float(input("Enter The Marks Of Hindi:"))
sst = float(input("Enter The Mars Of SST:"))

sum_of_marks = science + maths + sst + hindi
print("Your Overall Marks Are:",sum_of_marks)

percentage = (sum_of_marks/400)*100

print("Your percantage is- ", percentage,"%")
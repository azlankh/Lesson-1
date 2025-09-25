medical_health = input("Are you In Good Health? (Y/N): ")
attendence = int(input("Enter your Attendence Percentage: "))
if medical_health == 'Y' or medical_health == 'y':
    print("You are Cabable to Attend the Exam")
else:
    if attendence >= 75:
        print("You are Allowed to Attend the Exam")
    else:
        print("You are Not Allowed to Attend the Exam")

try:
    num=int(input("Enter a Number:"))
    print("You Entered", num)
except ValueError:
    print("Invlid Input! Please enter a integer Value.")
    print("Try Again")
a = input("Is 1 bigger than 2? (YES OR NO)")
b = input("Is 2 bigger than 0? (YES OR NO)")
if (a == "NO" and b == "YES"):
    print("Both are Correct")
elif (a == "NO" or b == "YES"):
    print("One of them is Correct")
else:
    print("None of them are Correct")
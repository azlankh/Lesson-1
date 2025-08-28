a = input("Is 1 bigger than 2? (YES OR NO) ")
b = input("Is 2 bigger than 0? (YES OR NO) ")
if (a == "NO" and b == "YES"):
    print("Both are Correct")
elif(a == "NO" and b == "NO"):
    print("One of them is Correct")
elif(a == "YES" and b == "YES"):
    print("One of them is Correct")
elif(a == "YES" and b == "NO"):
    print("None of them are Correct")
    
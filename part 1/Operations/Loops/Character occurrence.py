String = str(input("Enter a Word: "))
letter = str(input("Enter a Letter You Want To Check: "))

i = 0
count = 0

while i < len(String):
    if String[i] == letter:
        count = count + 1
    i = i + 1
print("The Word", String, "has", count, letter, "in it")
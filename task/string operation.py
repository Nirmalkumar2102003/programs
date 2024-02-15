s = input("Enter string: ")
print("1. Length \n2. Uppercase \n3. Lowercase \n4. Swapcase")

ch = int(input("Enter your choice: "))
if ch == 1:
    print("Length:", len(s))
elif ch == 2:
    print("Uppercase:", s.upper())
elif ch == 3:
    print("Lowercase:", s.lower())
elif ch == 4:
    print("Swapcase:", s.swapcase())
else:
    print("Invalid choice")

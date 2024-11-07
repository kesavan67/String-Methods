
string = input("Enter the a String:")


rep = set()


for i in string:
    if i in rep:
        print(f"The first repeating character is: {i}")
        break
    rep.add(i)
else:
    print("No repeating characters found.")

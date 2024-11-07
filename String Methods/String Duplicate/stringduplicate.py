
string = input("Enter a string:")

result = ""
dupli = set()


for i in string:
    if i not in dupli:
        result += i
        dupli.add(i)

print(result)

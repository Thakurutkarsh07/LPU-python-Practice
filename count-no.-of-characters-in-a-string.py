# count number of characters in a a string
String=input("Input string to count no. of character")
len(String)

# Count number of vowels in a string
Str=input("Enter a string")
lis=["a","e","i","o","u"]
n=0
for i in Str.lower():
    if i in lis:
        n+=1
print(n)

# count max number of occuring letter
string=input("Enter a string")
characters = {}

for i in characters:
    if i in characters:
        characters[i] += 1
    else:
        characters[i] = 1
print(characters)

# count words in a string

strings=input("Enter Some Words")
a=len(strings.split())
print(a)

#
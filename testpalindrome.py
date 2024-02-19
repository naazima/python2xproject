# writing a reverse function to check if a word is a palindrome or not

def palindromefunc(str):
    reverse_str = ""
    for i in str:
        reverse_str = i + reverse_str
    #return reverse_str
    print(reverse_str)


palindromefunc(str="naaz")

Original_str = input("enter a str")
reverse_str = ""
for i in Original_str:
    reverse_str = i + reverse_str
print(reverse_str, end="")

# check for palindrome

if reverse_str == Original_str:
    print("palindrome")
else:
    print("not palindrome")

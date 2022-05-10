#My first solution
""""
word = input("Enter your name: ")

if ((len(word) >= 3) and (len(word) <= 10)):
    print("Your name is normal")
else:
    print("Your name is too short or your name is too long")
Input()
"""
#Solution after optimalization

word = input("Enter your name: ")

if 3 <= len(word) <= 10:
    print("Your name is normal")
else:
    print("Your name is too short or your name is too long")
    Input()
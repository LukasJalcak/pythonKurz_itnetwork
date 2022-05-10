emoji = input("\nEnter the emoji: ")
answer = "Your emoji is"

type = ""

if emoji == ":)" or emoji == ":-)":
    type = "smile"
elif emoji == ":(" or emoji == ":-(":
    type = "frown"
elif emoji == ":*" or emoji == ":-*":
    type = "kiss"
elif emoji == ":p" or emoji == ":-p":
    type = "tongue"
else:
    type = "unknown"

print(answer, type)
input()
left_limit_1 = int(input("Enter the left limit of the 1st interval: "))
right_limit_1 = int(input("Enter the left limit of the 1st interval: "))
left_limit_2 = int(input("Enter the left limit of the 2nd interval: "))
right_limit_2 = int(input("Enter the left limit of the 2nd interval: "))
text = ("Pairs of numbers (1st from the first interval and 2nd from the second interval), " 
        "whose sum lies in at least one of the intervals: ")
print(text)
for i in range(left_limit_1, right_limit_1 + 1):
    for j in range(left_limit_2, right_limit_2 + 1):
        sum = i + j
        if (left_limit_1 <= sum <= right_limit_1 or
            left_limit_2 <= sum <= right_limit_2):
            string = "[" + str(i) + ";" + str(j) + "]"
            print(string)
input("")



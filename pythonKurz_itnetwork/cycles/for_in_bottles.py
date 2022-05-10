import time
for x in range(10, -1, -1):
    if x > 1:
        print(x, "green bottles stand on the table and one falls")
        time.sleep(0.2)
    elif x == 1:
        print(x, "green bottle stand on the table and one falls")
        time.sleep(0.2)
    else:
        print("\nAnd there was no bottle left on the table.")
        time.sleep(1)

input("\nTo exit press: ENTER")
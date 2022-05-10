print("\nProgram for calculating quadratic equations\n")
print("Equation form: ax^2+bx+c=0\n")
a = int(input("Enter the coefficient a: "))
b = int(input("Enter the coefficient b: ")) 
c = int(input("Enter the coefficient c: "))
if a != 0:
    D = b ** 2 -(4*a) * c
    if D == 0:
        x = -b / 2*a
        print("\nThe equation has one root:")
        print(x)
    elif D > 0:
        x1 = (- b + (D ** 0.5)) / 2 * a
        x2 = (- b - (D ** 0.5)) / 2 * a
        print("\nThe equation has two roots:")
        print(x1)
        print(x2)    
    else:
        print("the equation has no solution")
    input()
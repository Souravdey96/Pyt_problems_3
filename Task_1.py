
def recursions(a):
    if a < 2:
        return 1
    else:
        return a * (recursions(a - 1))


num = int(input("Enter a number: "))
result = recursions(num)
print("Factorial: of", num, "is :", result )

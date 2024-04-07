x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

num = x**2 + y**2 + z**2

if num > 1000:
    print("x**2 + y**2 + z**2 = ", num)
elif num <= 1000:
    print("x + y + z = ", x + y + z)

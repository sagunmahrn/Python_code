# print("hello,world")

try:
    x = int(input("What's X?"))    
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
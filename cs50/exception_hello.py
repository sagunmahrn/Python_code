# print("hello,world")

try:
    x = int(input("What's X?"))    
except ValueError:
    print("x is not an integer")
print(f"x is {x}")
# print("hello,world")

while True:
    try:
        x = int(input("What's X?"))    
    except ValueError:
        print("x is not an integer")
    else:
        break  
        # if interger value is inserted then break is executed
    
print(f"x is {x}")

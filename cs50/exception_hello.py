# print("hello,world")
def main():
    x=get_int()
    print(f"x is {x}")




def get_int():
    while True:
        try:
            return int(input("What's X?"))    
        except ValueError:
            # print("x is not an integer")
            pass

main()
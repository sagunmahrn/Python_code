# # for loop with range
# for i in range(3):
#     print("meow")


## While loops
# while True:
#     n = int(input("What's n?"))
#     if n<0:
#         continue
#     else:
#         break

def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("what's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")
main()
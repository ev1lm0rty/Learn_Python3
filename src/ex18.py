def print_two(*args):
    arg1 ,arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1,arg2):
    print(f"{arg1} {arg2}")

def print_one(arg1):
    print(f"{arg1}")

def print_none():
    print("I got nothin'.")

print_two("hey","baby")
print_two_again("hello","there")
print_one("bitch")
print_none()

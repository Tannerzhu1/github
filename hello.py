def main():
    greet()

    
    
def greet():
    p1_age = age()
    p1_name = name()
    print("\033[2J", end="")
    print(f"Hello world!")
    print(f"I'm {p1_name} and I'm {p1_age} years old")

def age():
    age = int(input("Enter your age: "))
    return age

def name():
    name = input("Enter your name: ")
    return name


main()

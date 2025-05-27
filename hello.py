def main():
    greet()

    
    
def greet():
    print(f"Hello world!")
    print(f"I'm {age()} years old")

def age():
    age = int(input("Enter your age: "))
    return age

main()

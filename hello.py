import job

def main():
    greet()

    
def greet():
    p1_age = age()
    p1_name = name()
    p1_employer, p1_title, p1_rank, p1_annual = job.workplace()
    print("\033[2J", end="")
    print(f"Hello world!")
    print(f"I'm {p1_name} and I'm {p1_age} years old")
    print(f"My company is {p1_employer} and I'm the {p1_rank} of the {p1_title}. I make {p1_annual}")

def age():
    age = int(input("Enter your age: "))
    return age

def name():
    name = input("Enter your name: ")
    return name


main()

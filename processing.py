enter_name = input('Enter name: ').strip()
enter_lastName = input('Enter lastname: ').strip()
def welcome(name: str, lastname: str):
    print(f"Welcome {name.capitalize()} {lastname.capitalize()}!")
welcome(enter_name, enter_lastName)
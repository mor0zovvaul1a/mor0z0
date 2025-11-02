from utils import capitalize_name

class Greeter:
    def __init__(self, name: str):
        self.name = capitalize_name(name)

    def greet(self):
        return f"Hello, {self.name}!"

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(Greeter(name).greet())

from datetime import datetime


class User:
    def __init__(self):
        self.name = None
        self.age = None
        self.current_year = datetime.now().year

    def get_user_info(self):
        self.name = input("Enter your name: ")
        while True:
            try:
                self.age = int(input("Enter your age: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid age.")

    def display_user_info(self):
        birth_year = self.current_year - self.age
        print(f"Hi, {self.name}, your year of birth is {birth_year}")
        # print(f"User Age: {self.age}")


if __name__ == "__main__":
    user = User()
    user.get_user_info()
    user.display_user_info()

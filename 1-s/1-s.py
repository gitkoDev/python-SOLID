""" SRP = Single Responsibility principle
This principle states that each class (or structure) should only execute methods directly connected with it. 
In other words: a class or function should do only one thing - and do it well.
Below we have a superclass Person, which is inherited by 2 child classes: User and Customer. We need to save data about our customers and users in txt files. 
However, if we create a new superclass other than Person, we would need to duplicate the saving functionality. This could potentially lead to bugs.
Instead, we should follow the Separation of Concern approach (SOC a.k.a SRP) and create a separate class that would handle the saving of data for us. 
This way, if we create new classes that need saving or decide to change the saving process completely, we would only need to edit the code in one place.
"""


class Person:
    def __init__(self, name, email) -> None:
        self.__name = name
        self.__email = email

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @name.setter
    def set_name(self, name):
        self.__name = name

    @email.setter
    def set_email(self, email):
        self.__email = email

    # Bad practice! What if later we created another superclass (for example, Vehicles) with its own properties and methods, which we would also need to save data about? In this case we would need to create a separate save_data method for it, which would result in code repetition (and, quite possibly, bugs)
    def save_data(self):
        user_data = f"{self.__name}: {self.__email}"
        file = open("users.txt", "w")
        file.write(user_data)
        file.close()


class User(Person):
    def __str__(self) -> str:
        return f"User name: {self.__name}. Email: {self.__email}"


class Customer(Person):
    def __init__(self, name, email, money) -> None:
        super().__init__(name, email)
        self.__money = money

    def __str__(self) -> str:
        return f"Customer name: {self.__name}. Email: {self.__email}"

    @property
    def money(self):
        return self.__money

    def pay(self, sum):
        if self.money - sum < 0:
            print(f"You have ${self.__money}. Not enough to pay ${sum}")
            return
        self.__money -= sum
        print(f"Paying ${sum}. ${self.money} left")


# Creating a separate handler for saving data about all our classes is a much cleaner and less error-prone approach to organizing code. This way, if we want to create a new entity and save data about it, we would just need to edit the Storage class
class Storage:
    def save_data(self, data):
        if type(data) is User:
            file = open("users.txt", "w")
            data = f"{data.name}: {data.email}"
            file.write(data)
        elif type(data) is Customer:
            file = open("customers.txt", "w")
            data = f"{data.name}: {data.email}: ${data.money}"
            file.write(data)
        else:
            print("only users and customers can be saved")
            return
        file.close()


storage = Storage()
john = User(name="John", email="john@gmail.com")
alice = Customer(name="Alice", email="alice@gmail.com", money=50)

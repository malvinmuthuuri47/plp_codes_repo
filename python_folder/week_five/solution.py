# Illustrate Polymorphism, encapsulation, Inheriance, and abstration in OOP

from abc import ABC, abstractmethod

# Abstraction
class Smartphone(ABC):
    @abstractmethod
    def call(self, number):
        pass

    @abstractmethod
    def take_photo(self):
        pass

# Inheritance
class AndroidPhone(Smartphone):
    def __init__(self, brand, model):
        # Encapsulation
        self.__brand = brand
        self.__model = model
        self.__battery_level = 100

    # encapsulated getter for brand
    def get_brand(self):
        return self.__brand

    # encapsulated setter for battery (restricts access)
    def set_battery_level(self, level):
        if 0 <= level <= 100:
            self.__battery_level = level
        else:
            print("Invalid battery level!")
    
    def call(self, number):
        print(f"{self.__brand} {self.__model} calling {number}")

    def take_photo(self):
        print(f"{self.__brand} {self.__model} takes a photo with 12MP camera.")

    def battery_status(self):
        print(f"Battery level: {self.__battery_level}%")

# Polymorphism
class Iphone(Smartphone):
    def __init__(self, model):
        self.__model = model

    def call(self, number):
        print(f"Iphone {self.__model} facetiming {number}...")

    def take_photo(self):
        print(f"Iphone {self.__model} takes a photo with 48MP camera.")


if __name__ == "__main__":
    # Demo
    samsung = AndroidPhone("Samsung", "Galaxy S24")
    iphone = Iphone("15 Pro")

    # Encapsulation demo
    samsung.set_battery_level(85)
    samsung.battery_status()

    # Abstraction + Polymorphism
    for phone in [samsung, iphone]:
        phone.call("123-456-7890")
        phone.take_photo()

# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery = battery  # in mAh

    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def charge(self):
        print(f"{self.brand} {self.model} is charging...")

    def __str__(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage and {self.battery}mAh battery."


# Subclass: Smartwatch (inherits from Smartphone)
class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, battery, heart_rate_monitor=True):
        super().__init__(brand, model, storage, battery)
        self.heart_rate_monitor = heart_rate_monitor

    def check_heart_rate(self):
        if self.heart_rate_monitor:
            print(f"{self.brand} {self.model} is checking your heart rate...")
        else:
            print(f"{self.brand} {self.model} does not support heart rate monitoring.")

    # Polymorphism: overriding the charge method
    def charge(self):
        print(f"{self.brand} {self.model} (Smartwatch) is charging on a magnetic dock...")


# Creating instances
phone = Smartphone("Samsung", "Galaxy S23", 256, 4500)
watch = Smartwatch("Apple", "Watch Series 9", 64, 350)

# Using the objects
print(phone)
phone.make_call("123-456-7890")
phone.charge()

print()

print(watch)
watch.make_call("987-654-3210")
watch.check_heart_rate()
watch.charge()

class Vehicle:
    def move(self):
        # Base method to be overridden
        pass

class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water 🚤")

# Function to demonstrate polymorphism
def vehicle_movement(vehicle):
    vehicle.move()

# Create instances
my_car = Car()
my_plane = Plane()
my_boat = Boat()

# Use polymorphism
vehicle_movement(my_car)
vehicle_movement(my_plane)
vehicle_movement(my_boat)

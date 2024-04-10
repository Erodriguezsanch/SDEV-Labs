"""Edgar Rodriguez

M03Lab.py

This Python program uses a superclass called vehicle and a sub-class called autombile to get the information for the vehicle.
The information included is vehicle type, year, make, model, doors, and roof type. The information is then displayed for the user
"""


class Vehicle:
    """vehicle_type attribute for the Vehicle class"""
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
        


class Automobile(Vehicle):
    """Attributes for the Automobile class"""
    def __init__(self, year, make, model, doors, roof):
        super().__init__("Car") # Vehicle type is "CAR"
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


    """Display will show the user the information that they typed in. 
    self.vehicle_type retrieves the type of vehicle from super().__init__("Car").
    self.year through self.roof is retrieved from the main() function."""
    def display(self):
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Doors: {self.doors}")
        print(f"Roof type: {self.roof}")


"""Here the user will input the vehicle information for each variable.
car variable uses the Automobile class and the vehicle information that the user typed in to display the information."""
def main():
        year = input("Enter the year of the car: ")
        make = input("Enter the make of the car: ")
        model = input("Enter the model of the car: ")
        doors = input("How many doors(2 or 4)?: ")
        roof = input("Enter the roof type (solid or sun roof): ")

        car = Automobile(year, make, model, doors, roof)
        print("\nVehicle Information:")
        car.display()

if __name__ == "__main__":
    main()

class Truck:

    def __init__(self):
        self.capacity = 16
        self.packages = []
        self.current_location = "4001 South 700 East, Salt Lake City, UT 84107"
        self.distance_traveled = 0.0
        self.route = []

    def add_package(self, package):
        if self.capacity > 0:
            self.packages.append(package)
            self.capacity -= 1
            return True
        else:
            print("Truck is fully loaded")
            return False



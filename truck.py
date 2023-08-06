import csv
from hashtable import HashTable
from datetime import datetime, timedelta


class Truck:
    # Method/Constructor to initialize a Truck object
    def __init__(self, truck_id, time):
        self.truck_id = truck_id  # unique identifier for a truck
        self.capacity = 16  # Truck's package capacity
        self.packages = HashTable()  # A hashtable to store packages
        self.location = "4001 South 700 East"  # Tracks the location of a truck. Every truck starts at the Hub
        self.speed = 18 / 60  # Speed of a truck in miles per minute
        self.distance_traveled = 0.0  # Accumulated distance traveled by a truck
        self.time = datetime.strptime(time, '%I:%M %p')
        self.truck_list = None  # A list of package IDs assigned to a truck
        self.route = []  # List to track the route taken by the truck
        self.query_list = []

    # Method to add a package to a truck using a custom hashtable
    def add_package(self, package):
        if self.capacity > 0:
            self.packages.put(package.package_id, package)
            self.capacity -= 1
            return True
        else:
            print("Truck is fully loaded")
            return False

    # Method to read the distance table from a CSV file and return it as a 2D Array/Matrix
    @staticmethod
    def distance_matrix():
        distance_table = []
        with open('CSV_files/distance_table.csv', 'r') as distance_file:
            reader = csv.reader(distance_file)
            for row in reader:
                adjacency_list = []
                for column in row:
                    adjacency_list.append(float(column))
                distance_table.append(adjacency_list)
        return distance_table

    # Method to read the location map from a CSV file and return it as a dictionary
    @staticmethod
    def location_matrix():
        with open('CSV_files/location_map.csv', 'r') as location_file:
            location_map = {}
            reader = csv.reader(location_file, delimiter=',')
            for row in reader:
                location_map[row[2]] = [row[0], row[1]]
            return location_map

    # Method to find the distance between two locations using the location_map dictionary key and distance matrix
    def find_distance(self, current_location, next_location):
        location_map = self.location_matrix()
        distance_between = self.distance_matrix()
        return distance_between[int(location_map[current_location][0])][int(location_map[next_location][0])]

    # Method to load packages onto a truck based on the truck's ID
    def load_truck(self, package_list):
        if self.truck_id == 1:
            self.truck_list = [40, 35, 23, 25, 22, 6, 7, 10, 11, 12, 13, 5, 27, 33, 3, 2]
        elif self.truck_id == 2:
            self.truck_list = [34, 21, 14, 15, 16, 17, 18, 19, 20, 1, 36, 37, 29, 31, 30, 8]
        elif self.truck_id == 3:
            self.truck_list = [9, 24, 26, 28, 38, 32, 4, 39]
        for package in package_list:
            if package.package_id in self.truck_list:
                self.add_package(package)

    # Method to get the current time of a truck starting from hub departure
    def get_time(self):
        return self.time

    # Method to show the route taken by a truck
    def show_route(self):
        for location in self.route:
            if location == self.location:
                print(f"\nTruck_{self.truck_id} starts at: {self.location}")
            else:
                print(f"It's next location is: {location}")
        print(f"Finally it returns to {self.location}\n")

    # Method to show packages on the truck that are going to a specific address
    def show_packages_by_address(self, address):
        for package_id in self.truck_list:
            package = self.packages.get(package_id)
            if package.delivery_address == address:
                self.query_list.append(package)
        if self.query_list:
            print(f"Packages to {address} include:")
            print("----------------------------------------------")
            for package_ in self.query_list:
                print(f"ID:{package_.package_id}{'':<5}Deadline: {package_.delivery_deadline}{'':<5}Delivery Time: {package_.delivery_time}{'':<5}Address: {package_.delivery_address}{'':<5}City: {package_.delivery_city}{'':<5}State: {package_.state}{'':<5}Zip Code: {package_.zip_code}\n")
        self.query_list = []

    # Method to show packages on a truck that are going to a specific city
    def show_packages_by_city(self, city):
        for package_id in self.truck_list:
            package = self.packages.get(package_id)
            if package.delivery_city == city:
                self.query_list.append(package)
        if self.query_list:
            print(f"Packages going to {city} on Truck_{self.truck_id} include:")
            print("---------------------------------------------------")
        for package_ in self.query_list:
            print(f"ID:{package_.package_id}{'':<5}Deadline: {package_.delivery_deadline}{'':<5}Delivery Time: {package_.delivery_time}{'':<5}Address: {package_.delivery_address}{'':<5}City: {package_.delivery_city}{'':<5}State: {package_.state}{'':<5}Zip Code: {package_.zip_code}\n")
        self.query_list = []

    # Method to show packages on a truck sharing the same zip code
    def show_packages_by_zip_code(self, zip_code):
        for package_id in self.truck_list:
            package = self.packages.get(package_id)
            if package.zip_code == zip_code:
                self.query_list.append(package)
        if self.query_list:
            print(f"Packages having Zip Code: {zip_code} on Truck_{self.truck_id} include:")
            print("---------------------------------------------------------")
        for package_ in self.query_list:
            print(f"ID:{package_.package_id}{'':<5}Deadline: {package_.delivery_deadline}{'':<5}Delivery Time: {package_.delivery_time}{'':<5}Address: {package_.delivery_address}{'':<5}City: {package_.delivery_city}{'':<5}State: {package_.state}{'':<5}Zip Code: {package_.zip_code}\n")
        self.query_list = []

    # Method to show packages on the truck with a specific weight
    def show_packages_by_weight(self, weight):
        for package_id in self.truck_list:
            package = self.packages.get(package_id)
            if int(package.weight) == int(weight):
                self.query_list.append(package)
        if self.query_list:
            print(f"Packages weighing {weight}kg(s) on Truck_{self.truck_id} include:")
            print("---------------------------------------------------------")
        for package_ in self.query_list:
            print(f"ID:{package_.package_id}{'':<5}Deadline: {package_.delivery_deadline}{'':<5}Delivery Time: {package_.delivery_time}{'':<5}Address: {package_.delivery_address}{'':<5}City: {package_.delivery_city}{'':<5}State: {package_.state}{'':<5}Zip Code: {package_.zip_code}\n")
        self.query_list = []

    # Method to show packages on a truck with a specific delivery deadline
    def show_packages_by_deadline(self, deadline):
        deadline = datetime.strptime(deadline, '%I:%M %p').time()
        for package_id in self.truck_list:
            package = self.packages.get(package_id)
            if package.delivery_deadline == deadline:
                self.query_list.append(package)
        if self.query_list:
            print(f"Packages with deadline of {deadline} on Truck_{self.truck_id} include:")
            print("-----------------------------------------------------------")
            for package_ in self.query_list:
                print(f"ID:{package_.package_id}{'':<5}Deadline: {package_.delivery_deadline}{'':<5}Delivery Time: {package_.delivery_time}{'':<5}Address: {package_.delivery_address}{'':<5}City: {package_.delivery_city}{'':<5}State: {package_.state}{'':<5}Zip Code: {package_.zip_code}\n")
        self.query_list = []

    # Method to check the delivery status of a package at a given time
    def check_delivery_status(self, package_id, time):
        time = datetime.strptime(time, '%I:%M %p').time()
        package = self.packages.get(package_id)
        # If the time to check is less than the departure time, the package is still at the hub
        if time < datetime.strptime("8:00 AM", '%I:%M %p').time() and self.truck_id == 1:
            print(f"ID:{package.package_id}{'':<5}Deadline: {package.delivery_deadline}{'':<5}Status: At Hub{'':<5}Address: {package.delivery_address}{'':<5}City: {package.delivery_city}{'':<5}State: {package.state}{'':<5}Zip Code: {package.zip_code}")
        elif time < datetime.strptime("9:05 AM", '%I:%M %p').time() and self.truck_id == 2:
            print(f"ID:{package.package_id}{'':<5}Deadline: {package.delivery_deadline}{'':<5}Status: At Hub{'':<5}Address: {package.delivery_address}{'':<5}City: {package.delivery_city}{'':<5}State: {package.state}{'':<5}Zip Code: {package.zip_code}")
        elif time < datetime.strptime("10:25 AM", '%I:%M %p').time() and self.truck_id == 3:
            print(f"ID:{package.package_id}{'':<5}Deadline: {package.delivery_deadline}{'':<5}Status: At Hub{'':<5}Address: {package.delivery_address}{'':<5}City: {package.delivery_city}{'':<5}State: {package.state}{'':<5}Zip Code: {package.zip_code}")
        else:
            # If the delivery time is less than the time to check, the package has been delivered
            if package.delivery_time < time:
                print(f"ID:{package.package_id}{'':<5}Deadline: {package.delivery_deadline}{'':<5}Status: Delivered{'':<5}Delivery Time: {package.delivery_time}{'':<5}Address: {package.delivery_address}{'':<5}City: {package.delivery_city}{'':<5}State: {package.state}{'':<5}Zip Code: {package.zip_code}")
            # If the delivery time is greater than the time to check, the package is on route to be delivered
            else:
                print(f"ID:{package.package_id}{'':<5}Deadline: {package.delivery_deadline}{'':<5}Status: On Route{'':<5}Address: {package.delivery_address}{'':<5}City: {package.delivery_city}{'':<5}State: {package.state}{'':<5}Zip Code: {package.zip_code}")

    # Method to change the delivery address of a package (Package 9 specifically)
    def change_address(self, package_id):
        package = self.packages.get(package_id)
        if package:
            package.delivery_address = '410 S State St'
            package.state = 'UT'
            package.city = 'Salt Lake City'
            package.zip_code = '84111'
            self.packages.put(package_id, package)
        else:
            print(f"Package not located on Truck_{self.truck_id}")

    # Method to calculate the total mileage traveled by all trucks
    @staticmethod
    def total_mileage(trucks):
        mileage = 0
        for truck in trucks:
            mileage += truck.distance_traveled
            print(f"\nMileage for truck_{truck.truck_id} is: {truck.distance_traveled:.2f}")
        print(f"\nThe total mileage for all trucks is {mileage:.2f}\n")
        return mileage

    # Method to update the truck's time based on the distance traveled
    def update_time(self, distance):
        minutes = int(distance / self.speed)
        self.time = self.time + timedelta(minutes=minutes)

    # Method to update the delivery time of packages that arrive at their delivery location
    def update_delivery_time(self, location):
        for package_id in self.truck_list:
            package = self.packages.get(package_id)
            if package.delivery_address == location:
                package.delivery_time = self.get_time().time()

    # Method to deliver packages
    # Implemented using nearest neighbor algorithm
    def deliver_packages(self):
        current_location = self.location  # Start the delivery from the truck's initial location
        visited = set()  # Set to keep track of each distinct location visited during delivery
        visited.add(current_location)
        self.route.append(current_location)
        while self.packages:
            shortest_distance = float('inf')
            nearest_location = None
            # Loop through all the packages on the truck to find the nearest location
            for package_id in self.truck_list:
                package = self.packages.get(package_id)
                if package.delivery_address in visited:
                    package.delivery_status = "Delivered"
                    continue
                distance = self.find_distance(current_location, package.delivery_address)
                if distance < shortest_distance:
                    shortest_distance = distance
                    nearest_location = package.delivery_address
            # If there are no more unvisited package locations, the delivery is complete
            if nearest_location is None:
                break
            # Update the total distance traveled by the truck
            self.distance_traveled += shortest_distance
            # Update the truck's time based on the distance traveled
            self.update_time(shortest_distance)
            # Mark the nearest location as visited and add it to the truck's route
            visited.add(nearest_location)
            self.route.append(nearest_location)
            self.update_delivery_time(nearest_location)
            current_location = nearest_location

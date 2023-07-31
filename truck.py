import csv
from hashtable import HashTable
from datetime import datetime, timedelta


class Truck:

    def __init__(self, truck_id, time):
        self.truck_id = truck_id
        self.capacity = 16
        # self.packages = []
        self.packages = HashTable()
        self.location = "4001 South 700 East"
        self.speed = 18 / 60
        self.distance_traveled = 0.0
        self.time = datetime.strptime(time, '%I:%M %p')
        self.route = []

    def add_package(self, package):
        if self.capacity > 0:
            self.packages.put(package.package_id, package)
            self.capacity -= 1
            return True
        else:
            print("Truck is fully loaded")
            return False

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

    @staticmethod
    def location_matrix():
        with open('CSV_files/location_map.csv', 'r') as location_file:
            location_map = {}
            reader = csv.reader(location_file, delimiter=',')
            for row in reader:
                location_map[row[2]] = [row[0], row[1]]
            return location_map

    def find_distance(self, current_location, next_location):
        location_map = self.location_matrix()
        distance_between = self.distance_matrix()
        return distance_between[int(location_map[current_location][0])][int(location_map[next_location][0])]

    def load_truck(self, package_list, truck_list):
        if self.truck_id == 1:
            truck_list = [40, 35, 23, 25, 22, 6, 7, 10, 11, 12, 13, 5, 27, 33, 3, 2]
        elif self.truck_id == 2:
            truck_list = [34, 21, 14, 15, 16, 17, 18, 19, 20, 1, 36, 37, 29, 31, 30, 8]
        elif self.truck_id == 3:
            truck_list = [9, 24, 26, 28, 38, 32, 4, 39]
        for package in package_list:
            if package.package_id in truck_list:
                self.add_package(package)

    def get_time(self):
        return self.time

    def check_delivery_status(self, time):
        time = datetime.strptime(time, '%I:%M %p').time()
        for index in self.packages.table:
            for package_id, package in index:
                if package.delivery_time is None:
                    print("Package is at the Hub")
                elif package.delivery_time < time:
                    print(f"Package to {package.delivery_address} was delivered at {package.delivery_time}, Deadline: {package.delivery_deadline}")
                else:
                    print(f"Package to {package.delivery_address} is on the truck to be delivered")

    @staticmethod
    def total_mileage(trucks):
        mileage = 0
        for truck in trucks:
            mileage += truck.distance_traveled
        return mileage

    def update_time(self, distance):
        minutes = int(distance / self.speed)
        self.time = self.time + timedelta(minutes=minutes)

    def update_delivery_time(self, location):
        for bucket in self.packages.table:
            for package_id, package in bucket:
                if package.delivery_address == location:
                    package.delivery_time = self.get_time().time()

    def deliver_packages(self):
        current_location = self.location
        visited = set()
        visited.add(current_location)
        while self.packages:
            shortest_distance = float('inf')
            nearest_location = None
            for index in self.packages.table:
                for package_id, package in index:
                    if package.delivery_address in visited:
                        package.delivery_status = "Delivered"
                        continue
                    distance = self.find_distance(current_location, package.delivery_address)
                    if distance < shortest_distance:
                        shortest_distance = distance
                        nearest_location = package.delivery_address
            if nearest_location is None:
                break
            self.distance_traveled += shortest_distance
            self.update_time(shortest_distance)
            visited.add(nearest_location)
            self.update_delivery_time(nearest_location)
            self.route.append(nearest_location)
            current_location = nearest_location

import csv


class Truck:

    def __init__(self):
        self.capacity = 16
        self.packages = []
        self.location = "4001 South 700 East"
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

    def deliver_packages(self):
        current_location = self.location
        visited = set()
        visited.add(current_location)
        self.route.append(current_location)
        while self.packages:
            shortest_distance = float('inf')
            nearest_location = None
            if len(visited) - 1 == len(self.packages):
                break
            for package in self.packages:
                if package.delivery_address in visited:
                    package.delivery_status = "Delivered"
                    continue
                distance = self.find_distance(current_location, package.delivery_address)
                if distance < shortest_distance:
                    shortest_distance = distance
                    nearest_location = package.delivery_address
            if nearest_location is None:
                self.route.append(self.location)
                break
            visited.add(nearest_location)
            self.route.append(nearest_location)
            current_location = nearest_location
        return self.route

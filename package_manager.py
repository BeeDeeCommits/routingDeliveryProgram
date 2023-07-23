import csv
from package import Package


class PackageManager:

    def __init__(self):
        self.packages = []

    def read_packages(self):
        with open('/Users/sirbanks/PycharmProjects/pythonProject/PackageCSV/package_file_CSV.csv', 'r') as package_file:
            reader = csv.reader(package_file)
            for line in package_file:
                pid, address, state, city, zip_code, deadline, weight = line.split(',')
                package = Package(pid, address, state, city, zip_code, deadline, weight)
                self.packages.append(package)
        return self.packages

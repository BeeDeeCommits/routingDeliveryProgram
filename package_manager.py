import csv
from package import Package


class PackageManager:

    def __init__(self):
        self.packages = []

    def read_packages(self, path):
        with open(path) as package_file:
            for line in package_file:
                pid, address, state, city, zip_code, deadline, weight = line.split(',')
                package = Package(pid, address, state, city, zip_code, deadline, weight)
                self.packages.append(package)
        return self.packages

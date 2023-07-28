import csv
from package import Package
from datetime import datetime


class PackageManager:

    def __init__(self):
        self.packages = []

    @staticmethod
    def format_package_time(time):
        if time == "EOD":
            return "04:00 PM"
        else:
            return time

    def read_packages(self, path):
        with open(path) as package_file:
            for line in package_file:
                pid, address, state, city, zip_code, deadline, weight = line.split(',')
                time = self.format_package_time(deadline)
                deadline = datetime.strptime(time, '%I:%M %p').time()
                package = Package(pid, address, state, city, zip_code, deadline, weight)
                self.packages.append(package)
        return self.packages

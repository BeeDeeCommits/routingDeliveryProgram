from package import Package
from datetime import datetime


class PackageManager:
    # Method/Constructor to initialize the PackageManager object
    def __init__(self):
        self.packages = []

    @staticmethod
    def format_package_time(time):
        # If the deadline is EOD, set the time to "04:00 PM"
        if time == "EOD":
            return "04:00 PM"
        # Otherwise return the parsed time
        else:
            return time

    def read_packages(self, path):
        with open(path, encoding='utf-8-sig') as package_file:
            for line in package_file:
                # Split the file line into individual data fields
                pid, address, city, state, zip_code, deadline, weight = line.split(',')
                # Format the package deadline time
                time = self.format_package_time(deadline)
                deadline = datetime.strptime(time, '%I:%M %p').time()
                # Create a new Package object using the extracted data fields
                package = Package(int(pid), address, state, city, zip_code, deadline, weight)
                # Append the Package object to the class' packages list
                self.packages.append(package)
        # Return the list of packages
        return self.packages

from datetime import datetime
from package_manager import PackageManager
from truck import Truck
from hashtable import HashTable
from package import Package


def main():
    name = "Bankole Abawonse"
    student_id = "010533366"
    print(f"Name: {name}\nStudent ID: {student_id}")
    path = 'CSV_files/package_file_CSV.csv'
    package_handler = PackageManager()
    truck = Truck(1, "8:00 AM")
    truck_list = [truck]
    packages = package_handler.read_packages(path)
    truck.load_truck(packages, [])
    print(truck.time)
    print(f"{Truck.total_mileage(truck_list):2f}")
    truck.deliver_packages()
    print(truck.time)
    print(f"{Truck.total_mileage(truck_list):2f}")

    truck.check_delivery_status("12:00 PM")


if __name__ == "__main__":
    main()

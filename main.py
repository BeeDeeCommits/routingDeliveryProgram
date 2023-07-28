from package_manager import PackageManager
from truck import Truck
from package import Package


def main():
    name = "Bankole Abawonse"
    student_id = "010533366"
    print(f"Name: {name}\nStudent ID: {student_id}")
    path = 'CSV_files/package_file_CSV.csv'
    package_handler = PackageManager()
    truck = Truck()
    packages = package_handler.read_packages(path)
    for _ in range(16):
        print(packages[_].delivery_deadline)
        truck.add_package(packages[_])
    for package in truck.packages:
        print(package.delivery_status)
    truck.deliver_packages()
    for package in truck.packages:
        print(package.delivery_status)

    # print("works at this point 2")
    # print(route)
    # for path in route:
    #     count += 1
    # print(count)
    """print(matrix)"""
    """for package in packages:
        print(f"{package.package_id}, {package.delivery_status}")"""


if __name__ == "__main__":
    main()

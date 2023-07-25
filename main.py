from package_manager import PackageManager
import csv


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


def main():
    name = "Bankole Abawonse"
    student_id = "010533366"
    print(f"Name: {name}\nStudent ID: {student_id}")
    path = 'CSV_files/package_file_CSV.csv'
    matrix = distance_matrix()
    package_handler = PackageManager()
    packages = package_handler.read_packages(path)
    print(matrix)
    """for package in packages:
        print(f"{package.package_id}, {package.delivery_status}")"""


if __name__ == "__main__":
    main()

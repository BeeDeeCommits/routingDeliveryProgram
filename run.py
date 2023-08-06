import time
from truck import Truck
from package_manager import PackageManager
from datetime import datetime
import sys


class Run:

    @staticmethod
    def run():
        # Create truck objects
        truck_1 = Truck(1, "8:00 AM")
        truck_2 = Truck(2, "9:05 AM")
        truck_3 = Truck(3, "10:25 AM")
        # Boolean to determine if program can run
        can_run = True
        starting_time = datetime.strptime("7:30 AM", '%I:%M %p')
        print(f"WGUPS DELIVERY LOG")
        print("------------------------------------------------------------------")
        print(f"{starting_time.time()} AM: Packages are being loaded onto trucks...\n")
        path = 'CSV_files/package_file_CSV.csv'
        package_handler = PackageManager()
        packages = package_handler.read_packages(path)

        user_setup = input('View setup log? Y/N: ')
        user_setup = user_setup.lower()
        if user_setup == 'y':
            # View truck setup and delivery log
            Run.setup_with_log(truck_1, truck_2, truck_3, packages)
        else:
            # Setup truck and deliveries without log
            Run.setup_without_log(truck_1, truck_2, truck_3, packages)

        while can_run:
            wgu_trucks = [truck_1, truck_2, truck_3]
            print("Welcome to WGU Routing Program.\nPlease select from the menu option below:")
            print("------------------------------------------------------------------")
            print("1. Check Status of Package by ID and time")
            print("2. Check Status of all Packages by time")
            print("3. Check packages by delivery address")
            print("4. Check packages by city")
            print("5. Check packages by weight")
            print("6. Check packages by delivery deadline")
            print("7. Check packages by zip code")
            print("8. View total mileage Traveled by all Trucks")
            print("9. Show route travelled by each truck")
            print("0. Exit")

            user_option = input('\nEnter option here: ')
            # Looks up a single package and its delivery status at the specified time
            if user_option == '1':
                print("*** Please use a 12 hour format ending in AM/PM as in 9:00 AM/PM ***")
                print("Leave a space between time and AM/PM")
                print("------------------------------------------------------------------")
                package_id = input("Input the package ID:  ")
                time_to_check = input("Input the time: ")
                print()
                for truck in wgu_trucks:
                    if int(package_id) in truck.truck_list:
                        truck.check_delivery_status(int(package_id), time_to_check)
            # Looks up all packagea and their delivery status's at the specified time
            if user_option == '2':
                print("*** Please use a 12 hour format ending in AM/PM as in 9:00 AM/PM ***")
                print("Leave a space between time and AM/PM")
                print("------------------------------------------------------------------")
                time_to_check = input("Input the time: ")
                print()
                for truck in wgu_trucks:
                    print(f"Package status in Truck_{truck.truck_id} as of {time_to_check} : ")
                    for package_id in truck.truck_list:
                        truck.check_delivery_status(package_id, time_to_check)
            # Looks up all packages to be delivered to the specified address
            if user_option == '3':
                print("*** Type in Address as in: 4300 S 1300 E")
                print("------------------------------------------------------------------")
                address = input("Enter address here:  ")
                print()
                for truck in wgu_trucks:
                    truck.show_packages_by_address(address)
            # Looks up all packages to be delivered to the specified city
            if user_option == '4':
                print("*** Type in city as in: Salt Lake City")
                print("------------------------------------------------------------------")
                city = input("Enter city here: ")
                print()
                for truck in wgu_trucks:
                    truck.show_packages_by_city(city)
            # Looks up packages by weight
            if user_option == '5':
                print("*** Type weight as in: 4")
                print("------------------------------------------------------------------")
                weight = input("Enter weight here: ")
                for truck in wgu_trucks:
                    truck.show_packages_by_weight(weight)
            # Looks up all packages sharing a deadline
            if user_option == '6':
                print("*** Please use a 12 hour format ending in AM/PM as in 9:00 AM ***")
                print("------------------------------------------------------------------")
                deadline = input("Enter deadline here: ")
                for truck in wgu_trucks:
                    truck.show_packages_by_deadline(deadline)
            # Looks up all packages sharing a zip code
            if user_option == '7':
                print("*** Type zip code as in: 84115")
                print("------------------------------------------------------------------")
                zip_code = input("Enter zip here: ")
                for truck in wgu_trucks:
                    truck.show_packages_by_zip_code(zip_code)
            # Looks up the total mileage for each truck as well as their combined mileage
            if user_option == '8':
                Truck.total_mileage(wgu_trucks)
            # Looks up the route travelled by each truck
            if user_option == '9':
                truck_number = input("Enter truck number here (1, 2 or 3) : ")
                for truck in wgu_trucks:
                    if truck.truck_id == int(truck_number):
                        truck.show_route()
            # Ends the program
            if user_option == '0':
                sys.stdout.write("Logging Off")
                time.sleep(0.5)
                sys.stdout.write(".")
                time.sleep(0.5)
                sys.stdout.write(".")
                time.sleep(0.5)
                sys.stdout.write(".")
                can_run = False

    @staticmethod
    def setup_with_log(truck_1, truck_2, truck_3, packages):
        # Load method adds packages to each truck based on the package requirements
        truck_1.load_truck(packages)
        truck_2.load_truck(packages)
        truck_3.load_truck(packages)
        print(f"{truck_1.get_time().time()} AM: Truck_{truck_1.truck_id} leaves the hub with {truck_1.packages.size} packages.\n")
        time.sleep(0.3)
        print(f"{truck_2.get_time().time()} AM: Truck_{truck_2.truck_id} leaves the hub with {truck_2.packages.size} packages.\n")
        time.sleep(0.3)
        # Delivery method uses nearest neighbor algorithm to deliver the packages
        truck_1.deliver_packages()
        truck_2.deliver_packages()
        print(f"{truck_1.get_time().time()} AM: Truck_{truck_1.truck_id} completes it's delivery and returns to the hub\n")
        # Retrieves package #9
        package_9 = truck_3.packages.get(9)
        time.sleep(0.3)
        # Prior to 10:20 AM the address for package #9 is incorrect
        print(f"{truck_1.get_time().time()} AM: The current address for package #9 is {package_9.delivery_address}, {package_9.delivery_city}, {package_9.state}\n")
        time.sleep(0.3)
        print(f"{truck_1.get_time().time()} AM: Updating address for package #9...\n")
        # The change address method updates the address of package #9
        truck_3.change_address(9)
        time.sleep(0.3)
        print(f"{truck_1.get_time().time()} AM: The address for package #9 is now {package_9.delivery_address}, {package_9.delivery_city}, {package_9.state}\n")
        time.sleep(0.3)
        print(f"{truck_3.get_time().time()} AM: Truck_{truck_3.truck_id} leaves the hub with {truck_3.packages.size} packages.\n")
        truck_3.deliver_packages()
        time.sleep(0.3)
        print(f"{truck_2.get_time().time()} AM: Truck_{truck_2.truck_id} completes it's delivery and returns to the hub\n")
        time.sleep(0.3)
        print(f"{truck_3.get_time().time()} AM: Truck_{truck_3.truck_id} completes it's delivery and returns to the hub\n")

    #  Sets up trucks by loading, updating addresses and delivering packages without log
    @staticmethod
    def setup_without_log(truck_1, truck_2, truck_3, packages):
        truck_1.load_truck(packages)
        truck_2.load_truck(packages)
        truck_3.load_truck(packages)
        truck_1.deliver_packages()
        truck_2.deliver_packages()
        truck_3.change_address(9)
        truck_3.deliver_packages()

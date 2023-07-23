from package_manager import PackageManager


def main():
    name = "Bankole Abawonse"
    student_id = "010533366"
    print(f"Name: {name}\nStudent ID: {student_id}")
    package_handler = PackageManager()
    packages = package_handler.read_packages()
    for package in packages:
        print(f"{package.package_id}, {package.delivery_status}")


if __name__ == "__main__":
    main()

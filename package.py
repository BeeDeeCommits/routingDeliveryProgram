
class Package:
    # Method/Constructor to initialize a Package object
    def __init__(self, package_id, delivery_address, state, delivery_city, zip_code, delivery_deadline, weight):
        self.package_id = package_id  # unique identifier for each package
        self.state = state  # state attribute for each package
        self.delivery_address = delivery_address  # address attribute for each package
        self.delivery_city = delivery_city  # city attribute for each package
        self.delivery_status = "At the hub"
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.delivery_time = None  # time a package is delivered
        self.weight = weight  # weight attribute for each package





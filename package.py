
class Package:

    def __init__(self, package_id, delivery_address, state, delivery_city, zip_code, delivery_deadline, weight):
        self.package_id = package_id
        self.state = state
        self.delivery_address = delivery_address
        self.delivery_city = delivery_city
        self.delivery_status = "At the hub"
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.weight = weight


class Employee():
    """a class for all EMPLOYEE objects"""
    # Class initializer. It has 2 custom parameters, plus the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, address, location_id):
        self.id = id
        self.name = name
        self.address = address
        self.location_id = location_id
        
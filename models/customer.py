class Customer():
    """a class for all CUSTOMER objects"""
    # Class initializer. It has 6 custom parameters, plus the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, address, email = "", password = ""):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.password = password
        
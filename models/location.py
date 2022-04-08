class Location():
    """a class for all LOCATION objects"""
    # Class initializer. It has 3 custom parameters, plus the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address
       
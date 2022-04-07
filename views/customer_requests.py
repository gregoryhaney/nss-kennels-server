CUSTOMERS = [
    {
        "id": 1,
        "name": "Bruce Wayne"
    },
    {
        "id": 2,
        "name": "Clark Kent"
    },
    {
        "id": 3,
        "name": "Wynona Ryder"
    }
]



def get_all_customers():
    """dummy docstring"""
    return CUSTOMERS



# Function with a single parameter
def get_single_customer(id):
    """dummy docstring"""
    # Variable to hold the found animal, if it exists
    requested_customer = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer



def create_customer(customer):
    """dummy docstring"""
    #get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]    
    #add 1 to whatever that number is
    new_id = max_id + 1    
    #add an `id` property to the customer dictionary
    customer["id"] = new_id    
    #add the customer dictionary to the list
    CUSTOMERS.append(customer)    
    #return the dict with `id` property added
    return customer
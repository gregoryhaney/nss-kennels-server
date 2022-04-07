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
        "name": "Wynn Ryder"
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

def delete_customer(id):
    """dummy docstring"""
    # Initial -1 value for customer index, in case one isn't found
    customer_index = -1

    # Iterate the CUSTOMERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Store the current index.
            customer_index = index

    # If the customer was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    """dummy docstring"""
    # iterate the CUSTOMERS list using enumerate() so we
    # can access the index value of each customer
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # found the customer, so update the value
            CUSTOMERS[index] = new_customer
            break
        
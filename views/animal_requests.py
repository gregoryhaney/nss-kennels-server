ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "Gypsy",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1
    }
]


def get_all_animals():
    """dummy docstring"""
    return ANIMALS


# Function with a single parameter
def get_single_animal(id):
    """dummy docstring"""
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above.
    for animal in ANIMALS:
        if animal["id"] == id:
            requested_animal = animal
    return requested_animal


def create_animal(animal):
    #get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]
    
    #add 1 to whatever that number is
    new_id = max_id + 1
    
    #add an `id` property to the animal dictionary
    animal["id"] = new_id
    
    #add the animal dictionary to the list
    ANIMALS.append(animal)
    
    #return the dict with `id` property added
    return animal

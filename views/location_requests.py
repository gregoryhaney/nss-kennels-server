LOCATIONS = [
        {
            "id": 1,
            "name": "Nashville North",
            "address": "8422 Johnson Pike"
        },
        {
            "id": 2,
            "name": "Nashville South",
            "address": "209 Emory Drive"
        }
    ]


def get_all_locations():
    """dummy docstring"""
    return LOCATIONS

def get_single_location(id):
    """dummy docstring"""
    # Variable to hold the found location, if it exists
    requested_location = None

    # Iterate the LOCATIONS list above.
    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location

    return requested_location


def create_location(location):
    #get the id value of the last location in the list
    max_id = LOCATIONS[-1]["id"]
    #add 1 to whatever that number is
    new_id = max_id + 1
    #add an `id` property to the location dictionary
    location["id"] = new_id
    #add the location dictionary to the list
    LOCATIONS.append(location)
    #return the dict with `id` property added
    return location

import sqlite3
import json
from models import Location, location

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
    """new FN to get all the locations from DB"""
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM Location l
        """)

        # Initialize an empty list to hold all location representations
        locations = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create a location instance from the current row.
            # Note that database fields are specified in
            # exact order of the parameters defined in the
            # Location class above.
            location = Location(row['id'], row['name'], row['address'])

            locations.append(location.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(locations)

# Function with a single parameter
def get_single_location(id):
    """FN to fetch a single location based on provided id"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM Location l
        WHERE l.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()
        # Create location instance from the current row
        location = Location(data['id'], data['name'], data['address'])
        return json.dumps(location.__dict__)

def create_location(location):
    """FN to create a new location"""
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

def delete_location(id):
    """FN to perform DELETE operation for a single location"""
    # Initial -1 value for location index, in case one isn't found
    location_index = -1

    # Iterate the LOCATIONS list, but use enumerate() so that you
    # can access the index value of each item
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the location. Store the current index.
            location_index = index

    # If the location was found, use pop(int) to remove it from list
    if location_index >= 0:
        LOCATIONS.pop(location_index)

def update_location(id, new_location):
    """FN to make an update for a single location"""
    # iterate the LOCATIONS list using enumerate() so we
    # can access the index value of each location
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # found the location, so update the value
            LOCATIONS[index] = new_location
            break
     
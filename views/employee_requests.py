EMPLOYEES = [
    {
        "id": 1,
        "name": "Leonard Hoffsteader"
    },
    {
        "id": 2,
        "name": "Sheldon Cooper"
    },
    {
        "id": 3,
        "name": "Raj Kuthropoli"
    }
]


def get_all_employees():
    """dummy docstring"""
    return EMPLOYEES



# Function with a single parameter
def get_single_employee(id):
    """dummy docstring"""
    # Variable to hold the found animal, if it exists
    requested_employee = None

    # Iterate the EMPLOYEES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee


def create_employee(employee):
    #get the id value of the last employee in the list
    max_id = EMPLOYEES[-1]["id"]  
    #add 1 to whatever that number is
    new_id = max_id + 1
    #add an `id` property to the employee dictionary
    employee["id"] = new_id   
    #add the employee dictionary to the list
    EMPLOYEES.append(employee)  
    #return the dict with `id` property added
    return employee

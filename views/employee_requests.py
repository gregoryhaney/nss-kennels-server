EMPLOYEES = [
    {
        "id": 1,
        "name": "Leonard Hofstadter"
    },
    {
        "id": 2,
        "name": "Sheldon Cooper"
    },
    {
        "id": 3,
        "name": "Raj Smith"
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
    """dummy docstring"""
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

def delete_employee(id):
    """dummy docstring"""
    # Initial -1 value for employee index, in case one isn't found
    employee_index = -1

    # Iterate the EMPLOYEES list, but use enumerate() so that you
    # can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Store the current index.
            employee_index = index

    # If the employee was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    """dummy docstring"""
    # iterate the EMPLOYEES list using enumerate() so we
    # can access the index value of each employee
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # found the employee, so update the value
            EMPLOYEES[index] = new_employee
            break
        
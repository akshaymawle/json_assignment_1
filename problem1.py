import json

# Data of 5 employees
data = {
    "employees": [
        {
            "Name": "Akshay",
            "DOB": "1999-05-15",
            "Height": 175,
            "City": "Pune",
            "State": "Maharashtra"
        },
        {
            "Name": "Avinash",
            "DOB": "2000-11-25",
            "Height": 162,
            "City": "Mumbai",
            "State": "Maharashtra"
        },
        {
            "Name": "Kajal",
            "DOB": "1998-07-10",
            "Height": 160,
            "City": "Bangalore",
            "State": "Karnataka"
        },
        {
            "Name": "Avani",
            "DOB": "1999-03-30",
            "Height": 170,
            "City": "Chennai",
            "State": "Tamilnadu"
        },
        {
            "Name": "Rutuja",
            "DOB": "2001-09-05",
            "Height": 168,
            "City": "Guwahati",
            "State": "Assam"
        }
    ]
}

# Writing data into a JSON file
with open('employee.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("JSON file 'employee.json' created successfully.")


class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

# Read the JSON file and convert it into a list of Employee objects
employee_list = []

with open('employee.json', 'r') as json_file:
    data = json.load(json_file)
    employees_data = data.get("employees", [])

    for employee_data in employees_data:
        name = employee_data.get("Name", "")
        dob = employee_data.get("DOB", "")
        height = employee_data.get("Height", 0)
        city = employee_data.get("City", "")
        state = employee_data.get("State", "")

        employee = Employee(name, dob, height, city, state)
        employee_list.append(employee)

# Print the list of Employee objects
for employee in employee_list:
    print(f"Name: {employee.name}, DOB: {employee.dob}, Height: {employee.height}, City: {employee.city}, State: {employee.state}")

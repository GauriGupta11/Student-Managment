import json
import os

data_path = "data"

students_file = os.path.join(data_path, "students.json")
percentages_file = os.path.join(data_path, "percentages.json")
houses_file = os.path.join(data_path, "houses.json")
routes_file = os.path.join(data_path, "routes.json")
fees_file = os.path.join(data_path, "fees.json")

def load_json(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return {}

def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

# Global mutable data structures
students = load_json(students_file).get("students", [])
percentages = load_json(percentages_file)
houses = load_json(houses_file)
routes = load_json(routes_file)
fees = load_json(fees_file)

def save_all_data():
    save_json(students_file, {"students": students})
    save_json(percentages_file, percentages)
    save_json(houses_file, houses)
    save_json(routes_file, routes)
    save_json(fees_file, fees)

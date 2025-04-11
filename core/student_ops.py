from core.utils import students, percentages, houses, routes, fees, save_all_data

def handle_user_input():
    try:
        choice = int(input("Select an option: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return True

    if choice == 1:
        print("\nStudent List:")
        for s in students:
            print(f"- {s}")
    elif choice == 2:
        count = int(input("How many students to add? "))
        for _ in range(count):
            name = input("Enter student name: ")
            if name in students:
                print(f"{name} is already in the list.")
            else:
                students.append(name)
                print(f"Added {name}")
    elif choice == 3:
        name = input("Enter name to search: ")
        if name in students:
            print(f"Record found. Roll No: {students.index(name)+1}")
        else:
            print(f"No record found for {name}")
    elif choice == 4:
        name = input("Enter name to remove: ")
        if name in students:
            students.remove(name)
            print(f"Removed {name}")
        else:
            print("Student not found.")
    elif choice == 5:
        students.clear()
        count = int(input("How many new students? "))
        for _ in range(count):
            students.append(input("Enter name: "))
        print("New list created.")
    elif choice == 6:
        for name, per in sorted(percentages.items(), key=lambda x: x[1], reverse=True):
            print(f"{name}: {per}%")
    elif choice == 7:
        for name in students:
            per = int(input(f"Enter % for {name}: "))
            percentages[name] = per
    elif choice == 8:
        for name in students:
            house = input(f"Enter house for {name}: ")
            houses[name] = house
    elif choice == 9:
        for name, house in houses.items():
            print(f"{name} - {house}")
    elif choice == 10:
        for name in students:
            route = input(f"Enter bus route for {name}: ")
            routes[name] = route
    elif choice == 11:
        for name, route in routes.items():
            print(f"{name} - {route}")
    elif choice == 12:
        for name in students:
            fee = input(f"Has {name} deposited fees? (yes/no): ")
            fees[name] = fee
    elif choice == 13:
        for name, fee in fees.items():
            print(f"{name} - {fee}")
    elif choice == 0:
        save_all_data()
        print("Thank you for using the system.")
        return False
    else:
        print("Invalid option. Try again.")
    return True

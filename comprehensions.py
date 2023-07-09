def to_mod_list(employee_list):
    mod_list = [emp['name'].replace(" ", "_") + emp['department'] for emp in employee_list]
    return mod_list


def generate_usernames(mod_list):
    usernames = [item.replace(" ", "_") for item in mod_list]
    return usernames


def map_id_to_initial(employee_list):
    id_to_initial = {emp['name'].split()[0]: emp['id'] for emp in employee_list}
    return id_to_initial


def main():
    employee_list = [
        {"id": 12345, "name": "John", "department": "Kitchen"},
        {"id": 12456, "name": "Paul", "department": "House Floor"},
        {"id": 12478, "name": "Sarah A", "department": "Management"},
        {"id": 12434, "name": "Lisa B", "department": "Cold Storage"},
        {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
        {"id": 12419, "name": "Gill", "department": "Cashier"}
    ]

    mod_emp_list = to_mod_list(employee_list)
    print("Modified employee list: " + str(mod_emp_list) + "\n")

    usernames = generate_usernames(mod_emp_list)
    print(f"List of usernames: {usernames}\n")

    id_to_initial = map_id_to_initial(employee_list)
    print(f"Initials and ids: {id_to_initial}")


if __name__ == "__main__":
    main()

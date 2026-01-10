import json
import os

FILE_NAME = "data.json"

# Step 1: Check if file exists, if not create it
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump([], f)

# Helper function to load data
def load_data():
    with open(FILE_NAME, "r") as f:
        return json.load(f)

# Helper function to save data
def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

# Step 2: Main menu loop
while True:
    print("\n--- MENU ---")
    print("1. Add details")
    print("2. View details")
    print("3. Update details")
    print("4. Delete details")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    # ADD
    if choice == "1":
        name = input("Enter name: ")
        age = input("Enter age: ")
        email = input("Enter email: ")

        data = load_data()
        data.append({
            "name": name,
            "age": age,
            "email": email
        })

        save_data(data)
        print("✅ Details added successfully")

    # VIEW
    elif choice == "2":
        data = load_data()
        if not data:
            print("⚠️ No data found")
        else:
            for i, user in enumerate(data):
                print(f"{i}. Name: {user['name']}, Age: {user['age']}, Email: {user['email']}")

    # UPDATE
    elif choice == "3":
        data = load_data()
        if not data:
            print("⚠️ No data to update")
            continue

        for i, user in enumerate(data):
            print(f"{i}. {user['name']}")

        index = int(input("Enter index to update: "))

        if 0 <= index < len(data):
            data[index]["name"] = input("Enter new name: ")
            data[index]["age"] = input("Enter new age: ")
            data[index]["email"] = input("Enter new email: ")
            save_data(data)
            print("✏️ Details updated successfully")
        else:
            print("❌ Invalid index")

    # DELETE
    elif choice == "4":
        data = load_data()
        if not data:
            print("⚠️ No data to delete")
            continue

        for i, user in enumerate(data):
            print(f"{i}. {user['name']}")

        index = int(input("Enter index to delete: "))

        if 0 <= index < len(data):
            deleted = data.pop(index)
            save_data(data)
            print(f"🗑️ Deleted {deleted['name']}")
        else:
            print("❌ Invalid index")

    # EXIT
    elif choice == "5":
        print("👋 Exiting program")
        break

    else:
        print("❌ Invalid choice, try again")

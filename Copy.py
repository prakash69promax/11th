data = []
while True:
    print("\nTelephone CSV Menu:")
    print("1. Add Record")
    print("2. Display Records")
    print("3. Search Records by ID")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        id = input("Enter ID: ")
        name = input("Enter Name: ")
        brand = input("Enter Brand: ")
        price = input("Enter Price: ")
        type = input("Enter Type: ")
        data.append([id, name, brand, price, type])
        print("Record added successfully!")

    elif choice == '2':
        for record in data:
            print("ID:", record[0])
            print("Name:", record[1])
            print("Brand:", record[2])
            print("Price:", record[3])
            print("Type:", record[4])
            print()

    elif choice == '3':
        search_id = input("Enter ID to search: ")
        found = False
        for record in data:
            if record[0] == search_id:
                print("Record found:")
                print("ID:", record[0])
                print("Name:", record[1])
                print("Brand:", record[2])
                print("Price:", record[3])
                print("Type:", record[4])
                found = True
                break
        if not found:
            print("Record not found!")

    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")

# CHAPTER 6 EXERCISE 1


# Example data
grades = {
    "Anna": 5,
    "Mikko": 4,
    "Sara": 3
}

while True:
    print("\n---Students Grade System ---")
    print("1 - Add/Update a grade")
    print("2 - Search student's grade")
    print("3 - Print all students grade")
    print("0 - Exit")

    choice = input("Choose an action: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = int(input("Enter a grade: "))
        grades[name] = grade
        print(f"Grade for {name} has been added or updated.")

    elif choice == "2":
        name = input("Enter student name to search: ")
        if name in grades:
            print(f"{name}'s grade is {grade[name]}")
        else:
            print("Student not found.")
    elif choice == "3":
        print("\nAll students and grades:")
        for name, grade in grades.items():
            print(f"{name}: {grade}")

    elif choice == "0":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")

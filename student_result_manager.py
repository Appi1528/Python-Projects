import json

try:
    with open("students.json", "r") as file:
        student = json.load(file)
except:
    student = {}

def save_data():
    with open("students.json", "w") as file:
        json.dump(student, file, indent=4)
while True:
    print("\n----------STUDENT MANAGER APPLICATION-----------")
    print("1. Add Student")
    print("2. View Students")
    print("3. Check Result")
    print("4. Exit")
    print("5. Delete Student")
    print("6. Update Marks")
    print("7. Show Topper")
    print("8. Show Fail Students")

    choice = input("Enter Your Choice: ")

    # 1. Add Student
    if choice == "1":
        name = input("Enter Student Name: ")
        subjects = int(input("Enter Number of Subjects: "))
        marks_list = []

        for i in range(subjects):
            m = int(input(f"Enter marks for subject {i+1}: "))
            marks_list.append(m)

        percentage = sum(marks_list) / subjects

        student[name] = {
            "marks": marks_list,
            "percentage": percentage
        }
        save_data()

        print(f"{name} Added Successfully!!")

    # 2. View Students
    elif choice == "2":
        if not student:
            print("No Student Found")
        else:
            for name, data in student.items():
                print(f"\nName: {name}")
                print("Marks:", data["marks"])
                print(f"Percentage: {data['percentage']:.2f}%")

    # 3. Check Result + Grade
    elif choice == "3":
        name = input("Enter Student Name: ")

        if name in student:
            data = student[name]
            percentage = data["percentage"]

            if percentage >= 75:
                grade = "A"
                result = "Pass"
            elif percentage >= 60:
                grade = "B"
                result = "Pass"
            elif percentage >= 40:
                grade = "C"
                result = "Pass"
            else:
                grade = "F"
                result = "Fail"

            print("Marks:", data["marks"])
            print(f"Percentage: {percentage:.2f}%")
            print("Result:", result)
            print("Grade:", grade)
        else:
            print("Student Not Found")

    # 4. Exit
    elif choice == "4":
        print("Exit")
        break

    # 5. Delete Student
    elif choice == "5":
        name = input("Enter Student Name to Delete: ")

        if name in student:
            del student[name]
            save_data()
            print(f"{name} Deleted Successfully!!")
        else:
            print("Student Not Found")

    # 6. Update Marks
    elif choice == "6":
        name = input("Enter Student Name to Update: ")

        if name in student:
            subjects = int(input("Enter Number of Subjects: "))
            marks_list = []

            for i in range(subjects):
                m = int(input(f"Enter marks for subject {i+1}: "))
                marks_list.append(m)

            percentage = sum(marks_list) / subjects

            student[name] = {
                "marks": marks_list,
                "percentage": percentage
            }
            save_data()

            print(f"{name} Marks Updated Successfully!!")
        else:
            print("Student Not Found")

    # 7. Show Topper
    elif choice == "7":
        if not student:
            print("No Student Data Available")
        else:
            topper = max(student, key=lambda name: student[name]["percentage"])

            print("\n Topper Student:")
            print("Name:", topper)
            print("Marks:", student[topper]["marks"])
            print(f"Percentage: {student[topper]['percentage']:.2f}%")

    # 8. Show Fail Students
    elif choice == "8":
        if not student:
            print("No Student Data Available")
        else:
            found = False
            print("\n Fail Students List:")

            for name, data in student.items():
                if data["percentage"] < 40:
                    print(f"\nName: {name}")
                    print("Marks:", data["marks"])
                    print(f"Percentage: {data['percentage']:.2f}%")
                    found = True

            if not found:
                print("No Fail Students ")

    else:
        print("Invalid Input...")
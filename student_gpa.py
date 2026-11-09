# Francisco Huesca
# student_gpa.py
# This app accepts student names and GPAs as inputs
# and then determines whether students qualify for the Dean's List or the Honor Roll.

while True:
    last_name = input("Enter student's last name (ZZZ to quit): ")

    if last_name.upper() == "ZZZ":
        break

    first_name = input("Enter student's first name: ")

    gpa = float(input("Enter student's GPA: "))

    if gpa >= 3.5:
        print(first_name, last_name, "has made the Dean's List!")

    elif gpa >= 3.25:
        print(first_name, last_name, "has made the Honor Roll!")

    else:
        print(first_name, last_name, "does not qualify for either list.")

    print()

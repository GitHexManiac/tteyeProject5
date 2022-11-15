import time
student_list = []


def load_data(file_name, deliminator):
    """who knows what this could do????"""
    student_file = open(file_name,"r")
    for line in student_file:
        student_split = line.split(deliminator)
        student_name = student_split[0]
        student_id = int(student_split[1])
        student_cred = int(student_split[2])
        student_gpa = float(student_split[3]) #Splitting the students.txt file into a list of dictionaries
        student = {
            "name": student_name,
            "id": student_id,
            "credits": student_cred,
            "gpa": student_gpa
        }
        student_list.append(student)
    student_file.close()
    return student_list


def print_menu():
    print("=====================================================")
    print("Select one of the following:")
    print("[1] Add a student ")
    print("[2] Find masters students")
    print("[3] Find students on probation")
    print("[4] Find honors students")
    print("[5] Exit the program")
    print("====================================================")


def add():
    time.sleep(0.5)
    print("Ok, time to add a new student.")
    time.sleep(0.7)
    new_student_name = input("Please enter the student's first name: ")
    time.sleep(0.5)
    new_student_id = int(input(f"Please enter the id# of {new_student_name}: "))
    time.sleep(0.5)
    new_student_credits = int(input(f"Please enter the number of credits for {new_student_name}: "))
    time.sleep(0.5)
    new_student_gpa = float(input(f"Please enter the current GPA of {new_student_name}: "))
    time.sleep(1)
    new_student = {
        "name": new_student_name,
        "id": new_student_id,
        "credits": new_student_credits,
        "gpa": new_student_gpa
    }
    student_list.append(new_student)
    time.sleep(2)
    print("The student has been successfully added. Returning to menu...")
    time.sleep(2)


def masters():
    print("The students who qualify as masters are...")
    time.sleep(1)
    for students in student_list:
        if students["credits"] < 25:
            print(students["name"])
            time.sleep(0.7)


def probation():
    print("The students who qualify for probation are...")
    time.sleep(1)
    for students in student_list:
        if students["gpa"] < 2.0:
            print(students["name"])
            time.sleep(0.7)


def honors():
    print("The students who qualify for honors are...")
    time.sleep(1)
    for students in student_list:
        if students["gpa"] > 3.0:
            print(students["name"])
            time.sleep(0.7)


def exit_process():
    time.sleep(0.5)
    print("Thank you for using the program...")
    time.sleep(2)
    print("Exiting.")
    time.sleep(0.7)
    print("Exiting..")
    time.sleep(0.7)
    print("Exiting...")
    time.sleep(1)
    exit()


def main():
    student_data = load_data("students.txt", "|")
    while True:
        print_menu()
        option = input("Please choose [1-5]: ")
        if option == "1":
            add()
        elif option == "2":
            masters()
        elif option == "3":
            probation()
        elif option == "4":
            honors()
        elif option == "5":
            exit_process()
        else:
            print("Bruh what was that... that wasn't a correct input, silly")


main()
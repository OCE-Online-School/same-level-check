import csv
import recent_attendance_check as rac
import write_csv as write
import teacher_attendance_stats as details

# limit of months at same level
MONTH_LIMIT = 9

# read this file
FILE_PATH = "no_quitter.csv"
#FILE_PATH = "data.csv"

# list of students at or above number of months specified
list_of_same_level_students = []

# information to track
current_student_name = False
current_student_id = False
current_level = False
current_month = False
current_counter = 0

# column header
STUDENT_MONTH_ENTRY = 2
STUDENT_NAME = 7
STUDENT_ID = 6
STUDENT_LEVEL = 33

# constants for cleaner data review
BREAK_STUDENT = "休会"
QUIT_STUDENT = "退会"
SIGNUP_WISH = "入会のみ"
LESSON_LINK_ACCOUNT = "Lesson-Link"
PERA_PERA_STUDENT = "PeraPera"

def main(filepath_contract, filepath_attendance, month_limit):

    print("Checking contract file - START")
    read_file(filepath_contract, month_limit)
    print("Checking contract file - COMPLETED")

    """
    for item in list_of_same_level_students:
        print(item)
    print(len(list_of_same_level_students))
    """

    print("Checking the attendance file for found students - START")
    rac.attendance_check_main(list_of_same_level_students, filepath_attendance)
    print("Checking the attendance file for found students - COMPLETED")

    print("Adding extra details of main teacher and attendance ratio - START")
    details.review_main_teacher_attendance(list_of_same_level_students)
    print("Adding extra details of main teacher and attendance ratio - COMPLETED")

    print("Writing to csv file - START")
    write.write_to_csv(list_of_same_level_students)
    print("Writing to csv file - COMPLETED")


def read_file(filepath, month_limit):

    global current_student_name, current_student_id, current_level, current_counter

    with open(filepath, encoding="shift_jis", errors='ignore') as f:
        csv_reader = csv.reader(f)

        # skip the first row
        next(csv_reader)

        # show the data
        for line in csv_reader:

            row_student_name = line[STUDENT_NAME]
            row_student_id = line[STUDENT_ID]
            row_student_month_entry = line[STUDENT_MONTH_ENTRY]

            # check if active student
            if (row_student_id != current_student_id):
                active_student = active_student_check(row_student_name)
                if (not active_student):
                    continue
                active_student = active_student_check(line[STUDENT_LEVEL])
                if (not active_student):
                    continue
                pera_pera_student = pera_pera_check(line[STUDENT_LEVEL])
                if (pera_pera_student):
                    continue

            # check if student is OCE staff (not active student)
            if (row_student_id != current_student_id):
                OCE_staff = staff_member_check(row_student_id)
                if (OCE_staff):
                    continue

            row_level = get_student_level(line[STUDENT_LEVEL])

            # check if student has multiple entries for same month
            if (row_student_id == current_student_id):
                if (row_student_month_entry == current_month):
                    current_counter -= 1
            current_month = row_student_month_entry

            # for first run of code, get student details
            if (current_student_name == False):
                current_student_name = row_student_name
                current_student_id = row_student_id
                current_level = row_level

            # if row is a different student
            if (current_student_id != row_student_id):
                if(current_counter >= month_limit):
                    list_of_same_level_students.append([current_student_id, current_student_name, current_level, current_counter])
                current_student_name = row_student_name
                current_student_id = row_student_id
                current_level = row_level
                current_counter = 0

            # if same student, increment counter if at same level or reset if level up
            if (current_student_id == row_student_id):
                if (current_level == row_level):
                    current_counter += 1
                else:
                    current_level = row_level
                    current_counter = 1

def get_student_level(student_level_string):
    if "入門" in student_level_string:
        return 0
    if "L1" in student_level_string:
        return 1
    if "L2" in student_level_string:
        return 2
    if "L3" in student_level_string:
        return 3
    if "L4" in student_level_string:
        return 4
    if "スペシャルレッスン" in student_level_string:
        return current_level
    return "no level found"

def active_student_check(student_info):
    if BREAK_STUDENT in student_info:
        return False
    if QUIT_STUDENT in student_info:
        return False
    if SIGNUP_WISH in student_info:
        return False
    if LESSON_LINK_ACCOUNT in student_info:
        return False
    return True

def staff_member_check(student_id):
    # check if OCE staff member
    if "9" == student_id[0]:
        return True
    return False

def pera_pera_check(student_level):
    if PERA_PERA_STUDENT in student_level:
        return True
    return False

#if __name__ == "__main__":
#    main()
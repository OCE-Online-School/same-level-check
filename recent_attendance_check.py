import csv
import datetime

# read this file
FILE_PATH = "attendance_large.csv"

# column header
TEACHER_NAME_COL = 1
DATE_COL = 2
LESSON_TIME = 3
CONTRACT_TYPE = 5
STUDENT_ID_COL = 6
STUDENT_ENG_NAME_COL = 8
ATTENDANCE_COL = 9

# global variables
attendance_data_list = []
DAY_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def attendance_check_main(same_level_data, filepath):

    first_date = False
    last_date = False

    # check same level list has data
    if (len(same_level_data) == 0):
        print("Same level student list has no data.")
        return

    # build the list of attendance data
    read_file(filepath)

    # check list of attendance data has data
    if (len(attendance_data_list) == 0):
        print("Attendance list has no data.")
        return
    
    # get the first and last date of attendance data
    if (first_date == False):
        first_date = attendance_data_list[0][DATE_COL]
    if (last_date == False):
        last_index = len(attendance_data_list) - 1
        last_date = attendance_data_list[last_index][DATE_COL]

    # check recent attendance for same level students (teacher + attendance status)
    check_recent_attendance(same_level_data)

    """
    print(f'Attendance data checked for {first_date} to {last_date}.')
    print("~~~~~~~~~~~")
    for item in same_level_data:
        for sub_item in item:
            print(sub_item)
        print("~~~~~~~~~~~")
    """

def read_file(filepath):

    with open(filepath, encoding="shift_jis", errors='ignore') as f:
        csv_reader = csv.reader(f)

        # skip the first row
        next(csv_reader)

        # write csv data to a list
        for line in csv_reader:
            attendance_data_list.append(line)

def check_recent_attendance(same_level_data):

    # constants to check same level student data
    STUDENT_ID_INDEX = 0
    INSERT_NAME_INDEX = 1
    INSERT_STUDENT_TYPE = 2

    length_students = len(same_level_data)
    for i in range(length_students):
        
        student_name_eng = "not found"
        length_attendance = len(attendance_data_list)
        id_to_check = same_level_data[i][STUDENT_ID_INDEX]
        info_to_add = {"Present": 0, "Absent": 0, "Unrecorded": 0}
        contract_type = "Unsure"
        group_class_day = "-"
        group_class_time = "-"
        GROUP_IDENTIFIER = "group"
        PAIR_IDENTIFIER = "pair"
        PRIVATE_IDENTIFIER = "private"

        for k in range(length_attendance):
            if (id_to_check == attendance_data_list[k][STUDENT_ID_COL]):

                # assign data
                teacher_name = attendance_data_list[k][TEACHER_NAME_COL]
                print(teacher_name)
                student_name_eng = attendance_data_list[k][STUDENT_ENG_NAME_COL]
                print(student_name_eng)
                attendance_status = attendance_data_list[k][ATTENDANCE_COL]
                print(attendance_status)
                
                # check type of student contract
                contract_column = attendance_data_list[k][CONTRACT_TYPE].lower()
                print(contract_column)

                if GROUP_IDENTIFIER in contract_column:
                    contract_type = "Group"
                    date_to_check = attendance_data_list[k][DATE_COL]
                    date = datetime.datetime.strptime(date_to_check, "%Y/%m/%d")
                    group_class_day = DAY_OF_WEEK[date.weekday()]
                    group_class_time = attendance_data_list[k][LESSON_TIME]
                if PAIR_IDENTIFIER in contract_column: 
                    contract_type = "Pair"
                if PRIVATE_IDENTIFIER in contract_column:
                    contract_type = "Private"

                if (teacher_name in info_to_add):
                    info_to_add[teacher_name] += 1
                else:
                    info_to_add[teacher_name] = 1

                if (attendance_status in info_to_add):
                    info_to_add[attendance_status] += 1
                else:
                    if (attendance_status == ""):
                        info_to_add["Unrecorded"] += 1
                    else:
                        info_to_add[attendance_status] = 1

        print(student_name_eng)
        
        same_level_data[i].append(info_to_add)
        same_level_data[i].insert(INSERT_NAME_INDEX, student_name_eng)
        same_level_data[i].insert(INSERT_STUDENT_TYPE, contract_type)
        same_level_data[i].insert(INSERT_NAME_INDEX, group_class_day)
        same_level_data[i].insert(INSERT_NAME_INDEX, group_class_time)
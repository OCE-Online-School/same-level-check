DETAILS_INDEX = 8
INSERT_CLASS_DETAILS_INDEX = 5
POP_FROM_CLASS_DETAILS_INDEX = 1
INSERT_JP_NAME_INDEX = 1
POP_FROM_JP_NAME_INDEX = 6

def review_main_teacher_attendance(data_list):

    for item in data_list:

        print("previously structured item")
        print(item)

        restructure_date_list(item)

        print("restructured item")
        print(item)

        # set default values for teacher
        main_teacher = "unknown"
        highest_taught = 0

        # check attendance rate
        present_total = item[DETAILS_INDEX]["Present"]
        absent_total = item[DETAILS_INDEX]["Absent"]
        attendance_rate = 0
        if (present_total > 0):
            attendance_rate = present_total / (present_total + absent_total)

        # find the teacher that had the highest number of lessons
        
        for key in item[DETAILS_INDEX].keys():
            #print(f"Found key: {key} with value {item[DETAILS_INDEX][key]} with type of {type(item[DETAILS_INDEX][key])}.")

            teacher_name = True

            if (key == "Present"):
                teacher_name = False
            if (key == "Absent"):
                teacher_name = False
            if (key == "Unrecorded"):
                teacher_name = False

            value = int(item[DETAILS_INDEX][key])

            #print("Teacher name: ", teacher_name)
            if (teacher_name == True): 
                #print("Teacher Name: ", key)
                #print("Highest Value: ", highest_taught)
                #print("Teacher Value: ", value)

                if (value == highest_taught):
                    main_teacher = "Multiple teachers"
                if (value > highest_taught):
                    #print("New highest found")
                    main_teacher = key
                    highest_taught = value

        item.insert(DETAILS_INDEX, attendance_rate)
        item.insert(0, main_teacher)

# move the elements to their intended position
def restructure_date_list(item):
    # move day
    item.insert(INSERT_CLASS_DETAILS_INDEX, item.pop(POP_FROM_CLASS_DETAILS_INDEX))
    # move time
    item.insert(INSERT_CLASS_DETAILS_INDEX, item.pop(POP_FROM_CLASS_DETAILS_INDEX))
    # move JP name
    item.insert(INSERT_JP_NAME_INDEX, item.pop(POP_FROM_JP_NAME_INDEX))
    # manual changing the order of the list - very messy 
    item.insert(1, item.pop(4))
    item.insert(2, item.pop(3))
    item.insert(4, item.pop(5))
    item.insert(4, item.pop(5))
    item.insert(5, item.pop(6))
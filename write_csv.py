import csv

def write_to_csv(data_list):
    fields = ['Main Teacher', 'Student ID', 'Student Name (JP)', 'Student Name (ENG)', 'Student Level', 'Type of Student', '[Group Student] Class Day', '[Group Student] Class Time', 'Number of Months at the Same Level', 'Recent Attendance Rate', 'Attendance Record (Full Detail)']
    
    with open('same_level_students.csv', 'w', newline='') as f:
      
        # using csv.writer method from CSV package
        write = csv.writer(f)
        
        write.writerow(fields)
        write.writerows(data_list) 
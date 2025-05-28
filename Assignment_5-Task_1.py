# Create a Dictionary of Student Marks

data = {'Ram':43,'Shyam':65,'Alice':57,'Emma':72,'Utkarsh':92}

stu_name = input("Enter the student's name: ")

if stu_name in data:
    print("{}'s marks: {}".format(stu_name,data[stu_name]))
else:
    print("Student not found.")

# manaage student info about L1 NCEA credits
# Ms Lee
# 11/2/2020

# display all students in a list
def display_all_students():
    for index in range(0, len(students)):
        print("{}. Name: {}".format(index+1, students[index]))    


# stores student details
students = ["Justine Lee", "Bryn Lewis", "Meredith Lewis", "Rhys Lewis","Phil Adams"]

display_all_students()

    
# add a student
new_student = input("Enter the name of a student: ")
students.append(new_student)

display_all_students()
    
# delete a student
student_num = int(input("Enter number of student to delete: "))
del(students[student_num-1])

display_all_students()
    
# change student details
# get details of which student to change and what the updated name is
student_num = int(input("Enter number of student to change: "))    
new_name = input("Enter updated name: ")

# change student details
students[student_num-1] = new_name

display_all_students()

# manaage student info about L1 NCEA credits
# Ms Lee
# 11/2/2020

# display all students in a list
def display_all_students():
    for index in range(0, len(students)):
        print("{}. Name: {}".format(index+1, students[index]))    


# stores student details
students = [["Justine Lee",50], ["Bryn Lewis",20], ["Meredith Lewis",10], ["Rhys Lewis",5],["Phil Adams",100]]


display_all_students()

    
# add a student
student_name = input("Enter the name of a student: ")
student_credit_total = int(input("Enter total NCEA level 1 credits"))

new_student = [student_name, student_credit_total]

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
new_total = int(input("Enter new total: "))

# change student details
students[student_num-1][0] = new_name
students[student_num-1][1] = new_total

display_all_students()

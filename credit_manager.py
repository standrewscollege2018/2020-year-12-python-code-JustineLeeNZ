''' manage student info about L1 NCEA credits '''
# Ms Lee
# 11/2/2020

# display all students in a list
def display_all_students():
    print("\nLIST OF STUDENTS")
    for index in range(0, len(students)):
        print("{}. {} Credits: {}".format(index+1, students[index][0], students[index][1] ))    


# stores initial student details
students = [["Justine Lee",50], ["Bryn Lewis",20], ["Meredith Lewis",10], ["Rhys Lewis",5],["Phil Adams",100]]


# use loop to display menu until user decides to quit

display_menu = True

while display_menu == True :
    print("\n=====MENU=====")
    print("1. Display all students")
    print("2. Add a student")
    print("3. Delete a student")
    print("4. Update a student")
    print("5. Quit program\n")
    
    # get selected menu option
    choice = int(input("Please choose a menu option: "))
    
    # display all student
    if choice == 1:
        display_all_students()
    
    # add a student
    elif choice == 2:
        # add a student
        student_name = input("Enter the name of a student: ")
        student_credit_total = int(input("Enter total NCEA level 1 credits: "))
        
        new_student = [student_name, student_credit_total]
        
        students.append(new_student)
    
    # delete a student
    elif choice == 3:
        display_all_students()  
        student_num = int(input("Enter number of student to delete: "))
        del(students[student_num-1])
    
    # change student details
    elif choice == 4:
        display_all_students()
        # get details of which student to change and what the updated name is
        student_num = int(input("Enter number of student to change: "))    
        new_name = input("Enter updated name: ")
        new_total = int(input("Enter new total: "))
        
        # change student details
        students[student_num-1][0] = new_name
        students[student_num-1][1] = new_total
        
    # exit program
    else:
        display_menu = False
        
        
print("Bye")
        


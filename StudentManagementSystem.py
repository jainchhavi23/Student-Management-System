operations = """
1. Add Student data 
2. Update Student data 
3. View Student data
4. Delete Student data
5. Search Student by Id/Name
6. Exit
"""

def add_data():
   student_id = input("Enter Student ID: ")
   name = input("Enter Student Name: ")
   age = input("Enter Student Age: ")
   course = input("Enter Student Course: ")
   grade = input("Enter Student Grade: ")

   with open("studentdata.txt","a") as f:
        f.write(f"{student_id},{name},{age},{course},{grade}\n")
        print("Data Saved Sucessfully.")   

def update_data():
    student_id = input("Enter Student ID to update: ")
    found = False
    try:
       with open("studentdata.txt","r") as f:
            lines = f.readlines()
        
       with open("studentdata.txt","w") as f:
           for line in lines:
             data = line.strip().split(",")
             if data[0] == student_id:
                found = True
                name = input("Enter New Name: ")
                age = input("Enter New Age: ")
                course = input("Enter New Course: ")
                grade = input("Enter New Grade: ")
                f.write(f"{student_id},{name},{age},{course},{grade}\n")
             else:
                f.write(line)

       if found:
            print("Record updated successfully")
       else:
            print("Record not found")

    except FileNotFoundError:
        print("File not found")

def view_data():
    try:
        with open("studentdata.txt","r") as f:
            print("Student Records")
            print(f.read())
    except FileNotFoundError:
        print("File not found ")

def delete_data():
    student_id = input("Enter Student ID to delete: ")
    found = False
    try:
       with open("studentdata.txt","r") as f:
         lines = f.readlines()
    
       with open("studentdata.txt","w") as f:
          for line in lines:
            data = line.strip().split(",")
            if data[0] == student_id:
               found = True
               continue   
            f.write(line) 

       if found:
           print("Record deleted successfully ")
       else:
           print("Record not found ")    
    except FileNotFoundError:
        print("File not found ")

def search_data():
    key = input("Enter Student ID or Name to search: ")
    found = False
    try:
        with open("studentdata.txt","r") as f:
         for line in f:
            data = line.strip().split(",")
            if data[0] == key or data[1].lower() == key.lower():
                 print("Record Found")
                 print("ID:", data[0])
                 print("Name:", data[1])
                 print("Age:", data[2])
                 print("Course:", data[3])
                 print("Grade:", data[4])
                 found = True
        if not found:
            print("Record not found")
    except FileNotFoundError:
        print("File not found")

print(operations)
while True:
    try:
         oper = int(input("Enter Operation in the form of (1,2,3 ...):"))
    except ValueError:
        print("Enter Operation in the form of (1,2,3 ...)")
    if oper == 1:
        print("Enter Student Details:") 
        add_data()
    elif oper == 2:
         update_data() 
    elif oper == 3:
         view_data()
    elif oper == 4:   
         delete_data()
    elif oper == 5:
         search_data() 
    elif oper == 6:
        print("Exit the Program...")
        break
    else:
        print("Enter Valid Operation Number.")
     

                                                               
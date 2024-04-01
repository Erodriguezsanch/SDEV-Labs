"""Edgar Rodriguez

M02Lab.py

Description: This program will ask verify if the name entered will make the Dean's List, Honor Roll, or none.
It will ask for the last name or the sentinel value to end the loop / program.
After last name, it will ask for first name, and lastly the GPA.
GPA for Dean's List is greater than or equal to 3.5.
GPA for Honor Roll is greater than or equal to 3.25 and less than 3.5.
GPA below 3.25 does not qualify for any. 
"""

dean_gpa = 3.5
honor_roll_gpa = 3.25
while True:
    try:
        student_last_name = input("Student last name or type 'ZZZ' to quit: ").upper()
        if student_last_name == "ZZZ": # Sentinel Value
            break # This will end the loop if "ZZZ" is entered.
        student_first_name = input("Student first name: ")
        student_gpa = float(input("Enter the student's GPA: "))
        
        
        if student_gpa >= dean_gpa:
            print(f"Congratulations, {student_first_name.upper()} made the Dean's List!\n")
        elif honor_roll_gpa <= student_gpa < dean_gpa:
            print(f"Congratulations, {student_first_name.upper()} made the Honor Roll!\n")
        else:
            print(f"{student_first_name.upper()} did not qualify for the Honor Roll or the Dean's List.\n")
    
    except ValueError:
        print("Invalid input. GPA must be a numeric value.\n") # If the GPA entered is not a numeric value 
        
    
    
def main():
    # Create a dictionary where keys are student names and values are lists of their grades
    test_results = {}
    
    # Keep the program running until user decides to exit
    while True:
        student_input(test_results)


# Ask student name and grade function
def student_input(test_results):    
    # Constants
    ADD_GRADE = 1
    ADD_STUDENT = 2
    AVG_GRADE = 3
    GRADES = 4

    # Give user options to choose:
    try:
        user_choice = int(input('What would you like to do? \n' +
                            '1. Add a new grade \n' +
                            '2. Add a new student \n' +
                            '3. Display average grade \n' +
                            '4. Display student grades \n' ))
    except ValueError:
        print('Invalid input. Must be 1 number from 1 to 5. ')
        return # Allows you to go back to the caller (Hence 'return')

    if user_choice == ADD_GRADE:
        # Prompt user
        name = input('Enter student name: ').strip()
        grade = validate_grade()
        # Input validation if student already exists
        student_exist(name, grade, test_results)

        # Display test_results
        print(test_results)
    # elif user_choice == 

def validate_grade():
    while True:
        try:
            grade = int(input('Enter student grade: '))
            if grade < 0 or grade > 100:
                print('Invalid input. Grade must be between 1 - 100 ')
            else:
                return grade
        except ValueError:
            print('Invalid input type. Grade must be a number between 1 - 100')

def student_exist(name, grade, results):
    # Check if student exists in test_results
    if name in results:
        while True:
            append_grade = input(f'{name} already exists. Do you want to append grade? (y/n) ').strip().lower()
            if append_grade == 'y':
                results[name].append(grade) # Appending grade to list
                break
            elif append_grade == 'n':
                print('No changes made. ')
                break
            else:
                print('Invalid input. Must be "y" or "n". ' )
    else:
        results[name] = [grade] # Add student grade in list using SQUARE BRACKETS
        print(f'Student {name} added with grade {grade}. ')


main()
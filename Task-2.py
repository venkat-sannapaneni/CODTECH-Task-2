def calculate_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def calculate_gpa(average):
    if average >= 90:
        return 4.0
    elif average >= 80:
        return 3.0
    elif average >= 70:
        return 2.0
    elif average >= 60:
        return 1.0
    else:
        return 0.0

def main():
    print("Welcome to the Student Grades Tracker!")
    grades = []

    while True:
        try:
            grade = float(input("Enter the grade for the subject/assignment (or type 'done' to finish): "))
            grades.append(grade)
        except ValueError:
            done = input("Are you done entering grades? (yes/no): ")
            if done.lower() == 'yes':
                break
            else:
                continue

    if grades:
        average = sum(grades) / len(grades)
        letter_grade = calculate_letter_grade(average)
        gpa = calculate_gpa(average)

        print(f"\nTotal grades entered: {len(grades)}")
        print(f"Average Grade: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"GPA: {gpa:.2f}")
    else:
        print("No grades were entered.")

if __name__ == "__main__":
    main()

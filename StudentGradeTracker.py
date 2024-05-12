class StudentGradeTracker:
    def __init__(self):
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]

    def remove_grade(self, subject, index):
        if subject in self.grades and 0 <= index < len(self.grades[subject]):
            del self.grades[subject][index]
            if len(self.grades[subject]) == 0:
                del self.grades[subject]
            return True
        else:
            return False

    def calculate_average_grade(self):
        total_grades = 0
        total_subjects = 0
        for subject, grades in self.grades.items():
            total_grades += sum(grades)
            total_subjects += len(grades)
        if total_subjects == 0:
            return 0
        else:
            return total_grades / total_subjects

    def display_grades(self):
        if not self.grades:
            print("No grades recorded yet.")
            return
        print("Grades:")
        for subject, grades in self.grades.items():
            print(subject + ":")
            for i, grade in enumerate(grades):
                print(f"  {i+1}. {grade}")
        print("Average Grade:", self.calculate_average_grade())


def main():
    grade_tracker = StudentGradeTracker()

    while True:
        print("\nSTUDENT GRADE TRACKER")
        print("1. Add Grade")
        print("2. Remove Grade")
        print("3. Display Grades")
        print("4. Quit")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == "1":
            subject = input("Enter subject: ")
            grade = float(input("Enter grade: "))
            grade_tracker.add_grade(subject, grade)
        elif choice == "2":
            subject = input("Enter subject: ")
            index = int(input("Enter index of grade to remove: "))
            if grade_tracker.remove_grade(subject, index - 1):
                print("Grade removed successfully.")
            else:
                print("Invalid subject or index.")
        elif choice == "3":
            grade_tracker.display_grades()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()

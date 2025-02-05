

# def enroll_students():

#     print()
#     name = input("what is your name ? ")
#     # print(name)

#     while not name.strip():
#         print("Invalid input. Please provide a name")

#         while True:
#             try:
#                 name = str(input("What is your name ? "))
#                 break
#             except ValueError:
#                 print("Invalid input, please provide a valid name")

#     print(f"Hello {name}!, Welcome to UDIS Console ")
#     while True:
#         try:
#             age  = int(input("How old are you ? "))
#             break
#         except ValueError:
#             print("Invalid input. please enter a valid age.")

#     print(f"Okay {name}, you are {age} years old. Is that correct?. Reply wiith Y for Yes and N for NO")
#     reply = input().strip().lower()

#     if reply == "y":
#         print("Congrats, you have successfully been enrolled!")
#     elif reply == "n":
#         print("Okay, Please update your records.")
#     else:
#         print("Invalid reply. Enrollment process terminated.")

# enroll_students()    



# Global list to store enrolled students
# enrolled_students = []

# def enroll_students():
#     """Enroll a new student by asking for their name and age."""
#     global enrolled_students
    
#     # Ask for the user's name
#     name = input("What is your name? ").strip()
#     while not name:
#         print("Invalid input. Please provide a valid name.")
#         name = input("What is your name? ").strip()

#     # Ask for the user's age
#     while True:
#         try:
#             age = int(input("How old are you? "))  # Convert input to integer
#             break
#         except ValueError:
#             print("Invalid input. Please enter a valid number for age.")

#     # Confirm the details with the user
#     print(f"Okay {name}, you are {age} years old. Is that correct? Reply Y/N")
#     reply = input().strip().lower()

#     if reply == "y":
        
#         # Add the student to the global list
#         details = {"name": name, "age": age}
        
#         enrolled_students.append(details)
#         print("Congrats, you have been successfully enrolled!")
#     elif reply == "n":
#         print("Okay, please restart the enrollment process.")
#     else:
#         print("Invalid reply. Enrollment process terminated.")

# def save_students_to_file(filename="students.txt"):
#     """Save the list of enrolled students to a file."""
#     try:
#         with open(filename, "w") as file:
#             file.write("Name Age\n")  # Header
#             for student in enrolled_students:
#                 file.write(f"{student['name']},{student['age']}\n")
#         print(f"Enrolled students have been saved to {filename}.")
#     except Exception as e:
#         print(f"An error occurred while saving to file: {e}")

# def display_enrolled_students():
#     """Display the list of currently enrolled students."""
#     if not enrolled_students:
#         print("No students have been enrolled yet.")
#     else:
#         print("\nList of Enrolled Students:")
#         print("Name\tAge")
#         for student in enrolled_students:
#             print(f"{student['name']}\t{student['age']}")
#     print()

# def main():
#     while True:
#         print("\nUDIS Console - Enrollment System")
#         print("1. Enroll a Student")
#         print("2. View Enrolled Students")
#         print("3. Save Enrolled Students to File")
#         print("4. Exit")

#         choice = input("Choose an option (1-4): ").strip()

#         if choice == "1":
#             enroll_students()
#         elif choice == "2":
#             display_enrolled_students()
#         elif choice == "3":
#             save_students_to_file()
#         elif choice == "4":
#             print("Exiting the program. Goodbye!")
#             break
#         else:
#             print("Invalid option. Please choose again.")

# # Run the program
# if __name__ == "__main__":
#     main()



import os

class EnrollmentSystem:
    def __init__(self):
        """Initialize the Enrollment System."""
        self.enrolled_students = []
        self.filename = "students.txt"

    def load_students_from_file(self):
        """Load students from the file if it exists."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    for line in file.readlines()[1:]:  # Skip header
                        name, age = line.strip().split(",")
                        self.enrolled_students.append({"name": name, "age": int(age)})
                print(f"Loaded {len(self.enrolled_students)} students from {self.filename}.")
            except Exception as e:
                print(f"Error loading students from file: {e}")

    def save_students_to_file(self):
        """Save the list of enrolled students to a file."""
        try:
            with open(self.filename, "w") as file:
                file.write("Name,Age\n")  # Header
                for student in self.enrolled_students:
                    file.write(f"{student['name']},{student['age']}\n")
            print(f"Enrolled students have been saved to {self.filename}.")
        except Exception as e:
            print(f"An error occurred while saving to file: {e}")

    def enroll_student(self):
        """Enroll a new student."""
        name = self._get_valid_name()
        age = self._get_valid_age()

        print(f"Okay {name}, you are {age} years old. Is that correct? Reply Y/N")
        reply = input().strip().lower()

        if reply == "y":
            self.enrolled_students.append({"name": name, "age": age})
            print("Congrats, you have been successfully enrolled!")
        elif reply == "n":
            print("Okay, please restart the enrollment process.")
        else:
            print("Invalid reply. Enrollment process terminated.")

    def display_students(self):
        """Display the list of currently enrolled students."""
        if not self.enrolled_students:
            print("No students have been enrolled yet.")
        else:
            print("\nList of Enrolled Students:")
            print(f"{'Name':<20}{'Age':<5}")  # Table headers
            print("-" * 25)
            for student in self.enrolled_students:
                print(f"{student['name']:<20}{student['age']:<5}")
            print()

    def search_student(self):
        """Search for a student by name."""
        search_name = input("Enter the name of the student to search for: ").strip()
        results = [s for s in self.enrolled_students if search_name.lower() in s['name'].lower()]
        if results:
            print("\nSearch Results:")
            print(f"{'Name':<20}{'Age':<5}")
            print("-" * 25)
            for student in results:
                print(f"{student['name']:<20}{student['age']:<5}")
        else:
            print(f"No students found with the name '{search_name}'.")

    def delete_student(self):
        """Delete a student by name."""
        name_to_delete = input("Enter the name of the student to delete: ").strip()
        for student in self.enrolled_students:
            if student['name'].lower() == name_to_delete.lower():
                self.enrolled_students.remove(student)
                print(f"Student {name_to_delete} has been removed.")
                return
        print(f"No student found with the name '{name_to_delete}'.")

    def _get_valid_name(self):
        """Prompt the user for a valid name."""
        name = input("What is your name? ").strip()
        while not name:
            print("Invalid input. Please provide a valid name.")
            name = input("What is your name? ").strip()
        return name

    def _get_valid_age(self):
        """Prompt the user for a valid age."""
        while True:
            try:
                age = int(input("How old are you? "))
                if age <= 0:
                    raise ValueError
                return age
            except ValueError:
                print("Invalid input. Please enter a valid positive number for age.")

    def run(self):
        """Run the main menu of the enrollment system."""
        self.load_students_from_file()

        while True:
            print("\nUDIS Console - Enrollment System")
            print("1. Enroll a Student")
            print("2. View Enrolled Students")
            print("3. Search for a Student")
            print("4. Delete a Student")
            print("5. Save Enrolled Students to File")
            print("6. Exit")

            choice = input("Choose an option (1-6): ").strip()

            if choice == "1":
                self.enroll_student()
            elif choice == "2":
                self.display_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.delete_student()
            elif choice == "5":
                self.save_students_to_file()
            elif choice == "6":
                print("Exiting the program. Goodbye!")
                self.save_students_to_file()  # Save on exit
                break
            else:
                print("Invalid option. Please choose again.")


# Run the program
if __name__ == "__main__":
    system = EnrollmentSystem()
    system.run()

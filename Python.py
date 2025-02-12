
def get_integer(prompt):
    """Safely get an integer from the user."""
    while True:
        try:
            age =  int(input(prompt))
            if age > 100:
                print("Wow! You have already turned 100 years old!")
                continue
            if age < 0:
                print("❌ Age cannot be negative. Please enter a valid number.")
                continue
            return age
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")
            
def get_float(prompt):
    """Safely get a float from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
def validate_student(prompt):
    """Validate if the student is a student."""
    while True:
     is_student = input(prompt).strip().lower()
     if is_student in ["yes", "no"]:
        return is_student == "yes"
     print("❌ Invalid input! Please type 'yes' or 'no'.")
     
def get_color(prompt):
    """Ensure the user enters a non-empty favorite color."""
    while True:
        color = input(prompt).strip()  # Remove spaces
        if color:  # If not empty, return it
            return color
        print("❌ Please enter a valid color!")  # Ask again if empty

    

name = input("Enter your name: ")
age = get_integer("Enter your age: ")
height = get_float("Enter your height in meters: ")
is_student = validate_student("Are you a student? (yes/no): ")
favorite_color = get_color("What's your favorite color? ")

print("\n--- User Information ---")  
print(f"Name       : {name}")
print(f"Age        : {age} years")
print(f"Height     : {height:.2f} meters") 
print(f"Student?   : {'Yes' if is_student else 'No'}")
print(f"Hey {name}, you will turn 100 years old in {100 - age} years!")
print(f"Your favorite color is {favorite_color}.")
import re

class Validation:

    @staticmethod
    def validate_name(name):
        # First letter capital, only alphabets
        return bool(re.fullmatch(r"[A-Z][a-zA-Z]*", name))

    @staticmethod
    def validate_email(email):
        # Username starts with alphabet, no consecutive _ or .
        # Domain must be kust.edu.pk
        pattern = r"^[A-Za-z] [A-Za-z0-9._]*@kust\.edu\.pk$"
        return bool(re.fullmatch(pattern, email))

    @staticmethod
    def validate_phone(phone):
        # Format: 0-3XX-XXXXXXX
        return bool(re.fullmatch(r"0-3\d{2}-\d{7}", phone))

    @staticmethod
    def validate_registration(reg_no):
        # CSF student of IoC KUST
        # Example: CSF-21-KUST-001 
        return bool(re.fullmatch(r"CSF-\d{2}-KUST-\d{3}", reg_no))
class FileHandler:

    @staticmethod  
    def write_file(filename, text):
        try:
            with open(filename, "w") as file:
                file.write(text)
            print("Text written successfully.")
        except Exception as e:
            print("Error writing file:", e)
            
    @staticmethod
    def read_file(filename):
        try:
            with open(filename, "r") as file:
                print("File Content:")
                print(file.read())
        except Exception as e:
            print("Error reading file:", e)

    @staticmethod
    def append_file(filename, text):
        try:
            with open(filename, "a") as file:
                file.write(text)
            print("Text appended successfully.")
        except Exception as e:
            print("Error appending file:", e)
from validation import Validation

def main():
    # Validation testing
    print("Name Valid:", Validation.validate_name("Murtaza"))
    print("Email Valid:", Validation.validate_email("student01@kust.edu.pk"))
    print("Phone Valid:", Validation.validate_phone("0-300-1234567"))
    print("Registration Valid:", Validation.validate_registration("CSF-21-KUST-001"))

    filename = "lab15.txt"

    # File handling
    FileHandler.write_file(filename, "Hello, this is Lab Week 15.\n")
    FileHandler.append_file(filename, "Python file handling practice.\n")
    FileHandler.read_file(filename)

if __name__ == "__main__":
    main()

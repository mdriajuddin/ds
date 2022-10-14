# Produces a student report form data extracted from an external source.
from studentfile import StudentFileReader

# Name of the file to open.
FILE_NAME = "students.txt"

def main():
    # Extract the student records form the given text file.
    reader = StudentFileReader(FILE_NAME)

    reader.open()
    studentList = reader.fetchAll()
    reader.close()


    # Sort the list by id number. Each object is passed to the lambda
    # expression which returns the idNum field of the objcet.
    studentList.sort(key = lambda rec: rec.idNum)

    # Print the student report.
    printReport( studentList)

# Prints the student report.
def printReport(theList):
    # The class names associated with the class codes.
    classNames = (None, "Freshman","Sophomore","Junior","Senior")

    # Print the header.
    print("LIST OF STUDENTS".center(50))
    print("")

    print("ID","NAME","CLASS","GPA")
    # print(f"{}{}{}{}")
    
    # Print the body.
    for record in theList:
        print(f"{record.id} {record.firstName} {record.gpa}")

    # Add a footer.
    print("-" * 50)
    print("Number of students:", len(theList))

# Executes the main Routine.
main()
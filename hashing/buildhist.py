# Prints a  histogram for a distribution of letter grades computed
# form  a collectionof numeric grades extracted form a text file.

from maphist import Histogram

def main():
    # Creates a Histogram instance for computing th frequencies.
    gradeHist = Histogram("ABCDF")

    # Open the text file  containg the grades.
    gradeFile = open('cs102grades.txt', "r")

    # Extract the grades and increment the appropriate counter.
    for line in gradeFile:
        grade = int(line)
        gradeHist.incCount(letterGrade(grade))
    # Print the histogram char.
    printChart(gradeHist)

# Determines th eletter grade for the given numeric value.
def letterGrade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"

# Prints th histogram as horizontal bar chart.
def PrintChart(gradeHist):
    print("Grade Distribution")
    # Print the body of the chart.
    letterGrades = ("A","B","C","D","F")
    for letter in letterGrades:
        print("       |")
        print(letter + "+ ", end="")
        freq = gradeHist.getCount(letter)
        print("*" * freq)
    # Print the x-asis.
    print("        |" )
    print("+--------------------+-------------------+")
    print("0     5     10   15 20 25       30")

# Calls the mian routine.
main()

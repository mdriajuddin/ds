# Count the number of occurences of each letter in a text file.

from array import Array, Array2D


# Create an array for the counters and initialize each element to 0.
theCounters = Array(27)
theCounters.clear(0)

# Open the text file for reading and extract each line form the file
# and iterate over each character in the line.

theFile = open('atextfile.txt','r')

for line in theFile:
    for letter in line:
        code = ord(letter)
        theCounters[code] += 1
    # Close the file
    theFile.close()

    # Print the results. The uppercase letters hace ASCII values in the
    # range 65.. 90 and the lowercase letters are in the range 97..122.
    for i in range(26):
        print("%c - %4d   %c - %4d "% (chr(65+i), theCounters[65+i],chr(97+i), theCounters[97+i]))


# 2-D array

# Open the text file for reading 
gradeFile = open("grade.txt", 'r')

# Extract the fiest tow values which indicate the size of the array.
numExams = int(gradeFile.readline())
numStudents = int(gradeFile.readline())


# Create the 2-D arrray to store the grades.
examGrades = Array2D(numStudents, numExams)

# Extract the frades form the remaining lines.
i = 0
for student in gradeFile:
    grades = student.split()
    for j in range(numExams):
        examGrades[i, j] = int(grades[j])
    i += 1
# Close the text file.
gradeFile.close()


# Compute each student's acerage eam grade.

for i in range(numStudents):
    # Tally the exam grades for the ith student.
    total = 0
    for j in range(numExams):
        total += examGrades[i, j]

    # Compute average for the ith student.
    examAvg = total / numExams
    print("%2d: %6.2f"% (i+1, examAvg))











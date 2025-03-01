# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))#needs int along with open parenthesis-edited by Svetlana 

exam_three = int(input("Input exam grade three: "))#change to int as data type as its numerical,instead of str as the data type
                                               #change 3 to three to keep a same format-edited by svetlana

grades = [exam_one, exam_two, exam_three]#commas between each element in the list-edited by svetlana
sum = 0
for grade in grades:#the grade on the right hand side should be grades it can cause the code to repeat by itself-edited by svetlana
  sum = sum + grade

avg = sum / len(grades)#spelling error should be grades instead of grade-edited by svetlana

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:#colon has been added at the end of the elif statement-edited by Svetlana
    letter_grade = "B"
elif avg > 70 and avg < 80:#shouldnt be 69, should be 70-edited by svetlana
    letter_grade = "C"#double quotation instead of single-edited by svetlana
elif avg >= 60 and avg >= 70:#sign should be changed from <= to >= and number should be 60 to 70-edited by svetlana
    letter_grade = "D"
else:#this elif statement should be else-edited by svetlana
    letter_grade = "F"

print(f"Exams: {grades[0]}, {grades[1]}, {grades[2]}")#change format to get all grades in the list in one line according to required output-edited by svetlana
print(f"Average: {int(avg)}")  # Change average to int to match the format
#curly braceket added, to put the input directly-edited by svetlana

print("Grade: " + str(letter_grade))#str data type is missing-edited by svetlana

if letter_grade == "F":#should be == instead of is, used comparative statement and there should be an underscore instead of hyphen-edited by svetlana
    print ("Student is failing.")#print statement in bracket-edited by svetlana
else:
    print ("Student is passing.")#print statement in bracket-edited by svetlana

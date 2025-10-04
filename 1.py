# Program to accept marks for 5 subjects, calculate average, and print grade

marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

avg = sum(marks) / 5

if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'
else:
    grade = 'Fail'

print("Average marks:", avg)
print("Grade:", grade)
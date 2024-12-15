students = ['Alice', 'Bob', 'Charlie', 'David']
students_0_score = { student: 0 for student in students }
print(students_0_score)

scores = { 'Alice': 100, 'Bob': 90, 'Charlie':80, 'David': 70 }
over_90 = { name: score for name, score in scores.items() if score > 90 }
print(over_90)

grades = { name: 'PASS' if score > 80 else 'Non-PASS' for name, score in scores.items() }
print(grades)
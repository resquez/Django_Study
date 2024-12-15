# 실습 2. 중복 제거 후 정렬
# 학생 명단이 주어졌을 때, 중복된 이름을 제거하고 알파벳 순으로 정렬해서 반환하는 unique_sorted_students 함수를 작성해 보세요. 

def unique_sorted_students(students):
    print(students)
    students = set(students)
    print(students)
    students = list(students)
    students.sort()
    return students

def unique_sorted_students2(students):
    return list(set(students)).sort                   # sort는 None을 반환

def unique_sorted_students3(students):
    return sorted(list(set(students)))

students_list = ["John", "Jane", "Charles", "John", "Alice", "Bob", "Alice"]
uss = unique_sorted_students(students_list)
print(uss)      # ['Alice', 'Bob', 'Charles', 'Jane', 'John']

students_list = ["John", "Jane", "Charles", "John", "Alice", "Bob", "Alice"]
uss2 = unique_sorted_students2(students_list)
print(uss2)

students_list = ["John", "Jane", "Charles", "John", "Alice", "Bob", "Alice"]
uss3 = unique_sorted_students3(students_list)
print(uss3)
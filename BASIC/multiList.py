matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [ num for row in matrix for num in row ]              # 평탄화

print(matrix)
print(flattened)

# 중첩된 for 문
flattened = []
for row in matrix:
    for num in row:
        flattened.append(num)
print(flattened)
for i in range(5):
    print(i, end=' ')      # 0 1 2 3 4


for i in range(5):
    if i == 3:
        break
    print(i, end=' ')      # 0 1 2


print()


for i in range(3):
    for j in range(3):
        print(f'i: {i}, j: {j}')


print("*" * 10)


for i in range(3):
    if i == 1:
        break
    for j in range(3):
        print(f'i: {i}, j: {j}')


print("*" * 10)


for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(f'i: {i}, j: {j}')

# 1부터 3까지의 숫자와 10부터 12까지의 숫자를 조합한 결과 중 두 숫자가 다른 경우만 모아서 리스트로 반환

combine = [ (x, y) for x in range(1, 4) for y in range(1, 3) if x != y ]
print(combine)

combine = []
for x in range(1, 4):
    for y in range(1, 3):
        if x != y:
            combine.append((x, y))
print(combine)
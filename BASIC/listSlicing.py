fruits = ['apple', 'banana', 'cherry', 'durian', 'elderberry']


# 첫 두 요소를 가져와서 출력
print(fruits[:2])       # ['apple', 'banana'] <= 인덱스 0, 1


# 세번째 요소부터 마지막 요소까지 가져와서 출력
print(fruits[2:])       # ['cherry', 'durian', 'elderberry'] <= 인덱스 2, 3, 4


# 두번째 요소부터 네번째 요소까지 가져와서 출력
print(fruits[1:4])      # ['banana', 'cherry', 'durian'] <= 인덱스 1, 2, 3


# 모든 요소를 가져와서 출력
print(fruits[:])        # ['apple', 'banana', 'cherry', 'durian', 'elderberry'] <= 인덱스 0, 1, 2, 3, 4


# 간격을 지정해서 슬라이싱
print(fruits[::2])      # ['apple', 'cherry', 'elderberry'] <= 인덱스 0, 2, 4
print(fruits[1::2])     # ['banana', 'durian'] <= 인덱스 1, 3  


# 음수 인덱스와 함께 슬라이싱
# 뒤에서부터 세번째 요소부터 마지막 요소까지 가져와서 출력
print(fruits[-3:])      # ['cherry', 'durian', 'elderberry'] <= 인덱스 2, 3, 4


# 리스트의 처음부터 마지막에서 두번째 항목까지 가져와서 출력
print(fruits[:-2])      # ['apple', 'banana', 'cherry', 'durian'] <= 인덱스 0, 1, 2, 3


# 리스트 역순으로 출력
print(fruits[::-1])     # ['elderberry', 'durian', 'cherry', 'banana', 'apple'] <= 인덱스 4, 3, 2, 1, 0

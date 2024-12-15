# 단어로 구성된 리스트를 이용해서 새로운 리스트를 생성
# 새로운 리스트는 원래 리스트의 단어들을 대문자로 변환한 것으로 구성

words = ['hello', 'world', 'python', 'is', 'fun']
upper_words = [ word.upper() for word in words ]
print(upper_words)
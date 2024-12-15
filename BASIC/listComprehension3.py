# words 리스트에서 길이가 5글자 이하인 문자열만 추출하여 새로운 리스트를 생성
fruits = ['apple', 'banana', 'orange', 'melon', 'grape', 'watermelon', 'avocado']
result = [ word for word in fruits if len(word) <= 5 ]
print(result)

# word 리스트에서 길이가 5글자 이하이고 첫 글자가 a로 시작하는 문자열만 추출해서 대문자로 변환한 값을 가지고 새로운 리스트를 생성
words = ['apple', 'banana', 'orange', 'melon', 'grape', 'add']
result = [ word.upper() for word in words if len(word) <= 5 and word[0] == 'a']
print(result)
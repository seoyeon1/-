#기본 문법(변수, 자료형, 조건문, 반복문, 기타 내장 라이브러리)

#조건문

# age = 24
#
# if age >20:
#     print('성인입니다.')
# else:
#     print('학생입니다.')

#반복문
fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

count = 0
for fruit in fruits:#리스트 길이만큼 반복, 요소 출력
    if fruit == '사과':#값이 사과일때만 count 1 증가
        count += 1

print(count)#2


people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for person in people:#딕셔너리 길이만큼 반복. 반복할 때마다 요소 하나를 person에 대입
    if person['age'] > 20:#나이가 20살보다 많을 때
        print(person['name'])#사람의 이름 출력


#문자열 쪼개기 : split
#이메일의 domain찾기
myemail = 'lauraura@kakao.com'

result1 = myemail.split('@')[1].split('.')[0]
print(result1)#kakao

#문자열 변경하기(치환)
result = myemail.replace('kakao', 'gmail')
print(result)#lauraura@gmail.com

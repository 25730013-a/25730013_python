## 2026-11-12

```
#문자열 슬라이싱
#[start:end:step]
#[인덱스 번호]
#[::]->전체 출력
#[-4:]->뒤에서 4자리
string="Monty Python"
print(string[-4:]) #string[-4::]


#학생 정보가 담긴 문자열
#기호 | 김한결(3글자) 김한|(2글자) 김|(1글자)
student="20261234홍길동|컴퓨터공학과"
student1="20261234홍길|컴퓨터공학과"
student2="20261234홍|컴퓨터공학과"

pos=student1.find("|")
print(pos)

#문자열 슬라이싱으로 정보 추출
student_id= student1[0:8] #학번
name= student1[8:pos]     #이름
major= student1[11:]      #학과
#student
student_id= student[0:8] 
name= student[8:pos]     
major= student[pos+1:] 

#결과 출력
print("학번:",student_id)
print("이름:",name)
print("학과:",major)


string="Monty Python"
print(string[-1])
print(string[:-1])


#문자(열) 자료형+문자(열) 자료형->연결
print("H"+"E")

#in, not in -> A in B -> A라는게 B에 존재하는지
#           -> A not in B -> A라는게 B에 존재하지 않는지 
print("H" in "hello") #False
print("H" not in "hello") #True


#Palindrome
a="python"
b=a[::-1] #nohtyp
if a == b:
    print("Palindrome")
else:
    print("Not Palindrome")


#input()표준입력함수(키보드->변수저장)

respone=input('게임을 계속 하시겠어요?')
if response.lower() == 'yes'or 'y':
    print('게임을 계속합니다.')
else:
    print('다음에 또 뵈요.')



print(' '.isspace())
print('\n'.isspace())
print('  '.isspace())

while True:
    password=input('새로운 패스워드를 입력하시오(문자의 숫자만 가능)')
    if password.isalnum():
        print("(정상)")
        break
    print('문자와 숫자만을 입력하여 패스워드를 선택하시오.')

#startswith(s) s로 시작하는지 검사
#endswith(s) s로 끝나는지 검사(주로 확장명 검사)
    
#split(공백)->리스트
string="welcome to python"
string=string.split()
string.split(' ')
print(string)

string1="welcome/to/python"
string1.split('/')
print(string1)

#문자열을 하나의 문자 요소들로 변환 list()
string="welcome to python"
string=list(string)
print(string)

#문자열을 하나의 문자 요소들로 변환 list() 공백은 빼고
#replace(), join()
string1="welcome to python"
string1=list(string1.replace(" ","")
```


## 2026-10-08

- 문자를 숫자로 바꾸기
```
>>> ord("A")
>>> 65
```
- 숫자를 문자로 바꾸기
```
>>> chr(65)
>>>'A'
```
- A부터 Z까지 출력
```
for i in range(65,91):
    print(chr(i), end=" ")
```
---
- 반복제어문3 - 자가진단 5-1 예제#1
```
a,b=input().split()
#숫자->문자 chr()
#문자->숫자 ord()

for i in range(ord(a), ord(b)+1):
    print(chr(i), end=" ")
```
- 반복제어문3 - 자가진단 5-1 예제#2
```
a,b=input().split()
#숫자->문자 chr()
#문자->숫자 ord()

if ord(a)<ord(b):
    for i in range(ord(a), ord(b)+1):
        print(chr(i), end=" ")

else:
    for i in range(ord(a), ord(b)-1,-1):
        print(chr(i), end=" ")
```
---
- 리스트 비교
```
>>>10 == 10
True
>>>'10' == 10
False
>>>[1,2,3] == [1,2,3]
True
>>>[3,2,1] == [1,2,3]
False

>>>[3,2,1] != [1,2,3]
True

>>>[3,2,1] > [1,2,3]
True    #첫 번째 값만 비교(3, 1 비교)
>>>[1,3,2] > [1,2,3]
True    #첫 번째 값이 같으면 두 번째 값 비교(3. 2 비교)

>>>['a','b'] > ['c','d']
False
```
---
- 리스트 복사_얕은 복사
```
temps = [28, 31, 33, 35, 27, 26, 25]
values = temps

print("temps:",temps)
print("values:",values)
values.append("A")
print("values:",values)
print("temps:",temps)
```
- 리스트 복사_깊은 복사
```
temps = [28, 31, 33, 35, 27, 26, 25]
values = list(temps)

print("temps:",temps)
print("values:",values)
values.append("A")
print("values:",values)
print("temps:",temps)
```
- 복사하기 실습
```
a="Hello"
b=list(a)

#첫번째 값
#print(a[0])
print(b)

#or

a="Hello"
b=list(a)

c=[]

for i in a:
    c.append(i)

print(c)
```
---
- 슬라이싱
```
a="Hello"
print(a[::])
#for i in range(시작값, 끝값, 단계)

#a[시작값:끝값:단계]

# ell
print(a[1:4:1]) #단계 생략 가능(기본값 1)

#거꾸로 출력
print(a[::-1])

license_plate="24가 2210"
print(license_plate[-4::]) #뒤 4자리만 출력(공백도 포함)

string="홀짝홀짝홀짝"
print(string[::2])  #홀만 출력
print(string[1::2]) #짝만 출력

#문자열 부분 수정 안됨
```

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
### 반복제어문3 - 자가진단 5-1
- 예제#1
```
a,b=input().split()
#숫자->문자 chr()
#문자->숫자 ord()

for i in range(ord(a), ord(b)+1):
    print(chr(i), end=" ")
```
- 예제#2
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
### 리스트 비교
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
### 리스트 복사
- 얕은 복사
```
temps = [28, 31, 33, 35, 27, 26, 25]
values = temps

print("temps:",temps)
print("values:",values)
values.append("A")
print("values:",values)
print("temps:",temps)
```
- 깊은 복사
```
temps = [28, 31, 33, 35, 27, 26, 25]
values = list(temps)

print("temps:",temps)
print("values:",values)
values.append("A")
print("values:",values)
print("temps:",temps)
```
- 실습
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
### 슬라이싱
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
---
### 리스트 변경
```
#리스트가 비워짐
>>> lst = [1, 2, 3, 4, 5, 6, 7, 8]
>>> lst[:] = [ ]
>>> lst
[]

#새로운 리스트를 만듬
>>> lst = [1, 2, 3, 4, 5, 6, 7, 8]
>>> lst = [ ]
>>> lst
[]

#1
a=[10,30,20,60,50,40]
a.sort()
del a[-1]    #del
a.remove(50) #remove("값") /요소 값을 알고 있을 때 유리
a.pop()      #pop(index)
print(a)

#2
a=[10,30,20,60,50,40]
a.sort(reverse=True)
del a[-1]    #del
a.remove(50) #remove("값")
a.pop()      #pop(index)
print(a)

#3
a=[10,30,20,60,50,40]
a.sort(reverse=True) #정렬
del a[:3]    #del
a.remove(50) #remove("값")
a.pop()      #pop(index)
print(a)

#del
a=10
del a
print(a)
```
---
### 리스트 함축
```
#99까지 출력
a=[i for i in range(100)]
print(a)


#1부터 100사이 짝수 출력
a=[i for i in range(1,101)if i% 2==0] 
print(a)

a=[i+2 for i in range(1,101)if i% 2==0] 
print(a)
```
```
#리스트 함축 
numbers=[]

for x in range(100):
    if x%2 == 0 and x %3 == 0:
        numbers.append(x)

print(numbers)

#함축식
numbers=[x for x in range(1, 100) if x%2 == 0 and x%3 == 0]
```
```
#5주차_52장

a=[1,2,3,4]
for i in range(len(a))

a=[1,2,3,4]
print(sum(a[0:2]))
```
---
### 튜플
```
a=[1,2,3,4] #리스트
b=(1,2,3,4) #튜플 read-only
            #리스트와 다르게 튜플은 변경 불가능

a=1,2,3,4
print(type(a)) #class 'tuple'
```

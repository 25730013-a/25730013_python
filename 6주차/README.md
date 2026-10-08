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
- 

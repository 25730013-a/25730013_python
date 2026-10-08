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

```

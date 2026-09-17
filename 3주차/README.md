## 2026-09-17

-get_area
```
def get_area(radius):
    area=3.14*radius**2
    return area

result=get_area(3)
print("반지름이 3인 원의 면적=",result)
```

-중첩 별찍기
```
for y in range(5):
    for x in range(10):
        print("*", end="")
    print("")

#거꾸로 출력
for i in range(5,0,-1):
    for j in range(i):
        print("*", end="")
    print()
```

-행, 열, 문자
```
def printPattern(rows=5, clse=5, char="*"):
                 for _ in range(rows):
                     for _ in range(cols):
                         print(char, end="")
                     print()

printPattern(3,10,"%")
```

-가변인수 합계
```
def add(*numbers):
    sum=0
    for i in numbers:
        print(type(numbers))

print(add(10,20))





def add(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum

print(add(10,20,30,40,50))
```

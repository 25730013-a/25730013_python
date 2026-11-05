## 2026-11-05

```
#list
a=1,2,3   #<--turple
a=list(a)
print(type(a))

#set(고유한 값을 갖는다, 순서가 없다)
b=[1,2,3,1,2,3,1,2,3]
a=set(b)
print(*a)

#len() 개수 반환 
fruits={"apple", "banana", "grape"}
size=len(fruits)
print(size)

#in 포함되는지
fruits={"apple", "banana", "grape"}
if "apple" in fruits:
    print("apple 있습니다.")
else:
    print("없습니다.")
##
string=input()
fruits={"apple", "banana", "grape"}  #리스트, 튜플 다 똑같음
if string in fruits:
    print(string, "있습니다.")
else:
    print(string, "없습니다.")

#출력(저장된 순서가 없다)
fruits={"apple", "banana", "grape"}
print(fruits)

#출력(출력시 정렬해서 출력할수는 있다)
fruits={"apple", "banana", "grape"}
for x in sorted(fruits):         #오름차순(fruits, reverse=False)
    print(x, end=" ")

fruits={"apple", "banana", "grape"}
for x in sorted(fruits, reverse=True):    #내림차순
    print(x, end=" ")

#add() 요소 추가
fruits={"apple", "banana", "grape"}
fruits,add("kiwi")
print(fruits)
fruits.remove("kiwi")
print(fruits)
fruits.discard("o") #remove()
print(fruits)
fruits.clear()
print(fruits)
```

```
capital={"one":1,"two":2,"three":3}
print(num["one"]) #key를 사용해서 value 출력
print(num["four"]) #key error

#get() 메서드는 특정 키에 해당하는 값을 가져올때 사용
#존재하지 않는 키를 조회해도 오류가 발생하지 않는다.
print(num.get("four","해당키가 없습니다."))

#get() 개수를 카운트 할때 사용 가능  (중요)
fruits=["apple","banana","apple","melon","banana","apple"]
count={} #set을 만들려면 b=set() 

for fruit in fruits:
    count[fruit]=count.get(fruit,0)+1

print(count)

#항목 key, value출력 (items())
for key, value in count.items():
    print(key,":",value)

#딕셔너리에서 key만 출력(keys())
print(count.keys())

#딕셔너리에서 value만 출력(values())
print(count.values())
print(*count.values())
```

```
s = 'Monty Python'
#슬라이싱 [start:end:step]
#Python
print(s[6:12])
print(s[6:])

#Monty
print(s[0:5])
print(s[:5])
print(s[5])  #XXXX
#거꾸로 출력
print(s[::-1])

#문자자료형+문자자료형(연결)
print(s[:5]+s[6:])

#문자열안에 문자 혹은 문자열을 포함하고 있는지 체크
#영어는 대소문자를 구분한다.
print("a" in "Abc") #False
print("a" in "abc") #True
print("a" not in "Abc") #True

#숫자->문자로 형변환 str()
name="홍길동"
age=21
print("제 이름은"+name+"입니다.")
print("제 나이는"+str(age)+"입니다.")

#print % 서식문자(%d 정수, %f 실수, %c 문자, %s 문자열)   
print("제 이름은 %s입니다."%name)
print("제 이름은 %s입니다. 저는 %s살입니다." % (name, age)) #차이 기억해두기

#f-string 활용해서 문자열 출력
print(f"제 이름은 {name}입니다. 저는 {age}살 입니다.")

#format()활용해서 문자열 출력
print("제 이름은 {}입니다. 저는 {}살 입니다.".format(name, age))

#format()번호로 출력정의(생략하면 순서대로)
print("제 이름은 {1}입니다. 저는 {0}살 입니다.".format(name, age))
```

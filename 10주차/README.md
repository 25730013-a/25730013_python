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

## 2026-10-01

- append()
```
fruits=[]
fruits.append("apple")
fruits.append("banana")
print(fruits)
```

- insert()
```
fruits=["apple", "banana", "grape"]
fruits.insert(1, "cherry")
print(fruits)
```

- 리스트 탐색하기
```
fruits=["apple", "banana", "grape"]
n=fruits.index("banana")

if "banana" in fruits:
    print(fruits.index("banana"))
```

- 리스트 오름차순, 내림차순
```
a=[5, 2, 1, 4, 6]

a.sort(reverse=False)  #오름차순
print(a)

a.sort(reverse=True)   #내림차순
print(a)
```

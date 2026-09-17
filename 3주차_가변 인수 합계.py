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

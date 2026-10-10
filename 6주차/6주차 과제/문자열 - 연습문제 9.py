word=input()
word=word.split()
A=word[0]
B=word[1]

a=A*3

if B in a:
    print(f"{A+B}")
else:
    print(f"{B*2}")

a,b=input().split()
#숫자->문자 chr()
#문자->숫자 ord()

for i in range(ord(a), ord(b)+1):
    print(chr(i), end=" ")


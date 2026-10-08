a,b=input().split()
#숫자->문자 chr()
#문자->숫자 ord()

if ord(a)<ord(b):
    for i in range(ord(a), ord(b)+1):
        print(chr(i), end=" ")

else:
    for i in range(ord(a), ord(b)-1,-1):
        print(chr(i), end=" ")

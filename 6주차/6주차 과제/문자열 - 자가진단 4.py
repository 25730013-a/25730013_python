a=input()
a=a.split()
oldname=a[0]
oldage=int(a[1])

b=input()
b=b.split()
youngname=b[0]
youngage=int(b[1])

sum=oldage-youngage

print(f"{oldname}'s age - {youngname}'s age =", sum)

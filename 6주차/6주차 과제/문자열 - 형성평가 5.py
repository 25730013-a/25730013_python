a=input()
a=a.split()

name=a[0]
height=a[1]
weight=float(a[2])

print(f"NAME: {name}")
print(f"HEIGHT: {height}cm")
print(f"WEIGHT: {weight:.2f}kg")

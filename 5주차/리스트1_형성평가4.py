N = int(input())
lst = []

for i in range(N):
    temp=int(input())
    lst.append(temp)

print(int(sum(lst)/N))

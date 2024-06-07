n = int(input())

all = [0] * (n+1)
pr = []

for i in range(2, n+1):
    if all[i] == 0:
        all[i] = i
        pr.append(i)
    j = 0
    while j < len(pr) and pr[j] <= all[i] and i*pr[j] <= n:
        all[i * pr[j]] = pr[j]
        j += 1

print(pr)
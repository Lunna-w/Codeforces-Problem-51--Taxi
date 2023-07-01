n = int(input())
s = list(map(int, input().split()))

count = [0, 0, 0, 0, 0]
groups = 0

for i in range(n):
    count[s[i]] += 1


groups += count[4]


min_groups = min(count[3], count[1])
groups += min_groups
count[3] -= min_groups
count[1] -= min_groups


groups += count[3]


groups += count[2] // 2
count[2] %= 2


if count[2] > 0 and count[1] > 0:
    groups += 1
    count[2] -= 1
    count[1] -= 2


if count[2] > 0:
    groups += 1

groups += (count[1] + 3) // 4

print(groups)
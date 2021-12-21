y = 0

for i in range(0, 300):
    for j in range(i, -i - 10, -1):
        y += j
        if -86 <= y <= -59:
            print(i, y, j)
            y = 0
            break

y = 0
h = []
for i in range(85, -90, -1):
    y += i
    h.append(y)
print(max(h))

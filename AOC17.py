xvalues = []
yvalues = []

for i in range(-86, 86):
    y = 0
    for j in range(i, -i - 200, -1):
        y += j
        if -86 <= y <= -59:
            yvalues.append(i)
            break

for i in range(1, 239):
    x = 0
    for j in range(i, 0, -1):
        x += max(j, 0)
        if 209 <= x <= 238:
            xvalues.append(i)
            break

print(xvalues)
y = 0
h = []
for i in range(85, -90, -1):
    y += i
    h.append(y)
print(max(h))

hits = []

for i in xvalues:
    for j in yvalues:
        x = 0
        y = 0
        for k in range(239):
            x = x + max(i - k, 0)
            y += (j - k)
            if 209 <= x <= 238 and -86 <= y <= -59:
                hits.append((i, j))
                print(hits[-1])
                break

print(len(hits))

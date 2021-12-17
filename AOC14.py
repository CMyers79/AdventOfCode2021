import string
import llist
from llist import sllist, sllistnode


with open('input14.txt') as file:
    lines = file.readlines()
    rules = []
    template = lines[0].strip()
    tempset = set()
    chardist = []
    sll = sllist()
    for char in template:
        tempset.add(char)
        sll.append(char)

    for row in range(2, len(lines)):
        rules.append(lines[row].strip().split())

    for _ in range(40):
        insert = []
        k = 0
        for i in range(sll.size - 1):
            for j in range(len(rules)):
                if sll[i] + sll[i + 1] == rules[j][0]:
                    insert.append([i + k, rules[j][2]])
                    k += 1

        for i in range(len(insert)):
            sll.insertafter(rules[j][2], sll.nodeat(insert[i][0]))

    for char in tempset:
        chardist.append(template.count(char))

    print(max(chardist) - min(chardist))

import string


with open('input14.txt') as file:
    lines = file.readlines()
    rules = []
    template = lines[0].strip()
    tempset = set()
    chardist = []
    for char in template:
        tempset.add(char)


    for row in range(2, len(lines)):
        rules.append(lines[row].strip().split())

    for _ in range(10):

        insert = []
        for i in range(len(template) - 1):
            for j in range(len(rules)):
                if template[i] + template[i + 1] == rules[j][0]:
                    insert.append([i + 1, rules[j][2]])

        for i in range(len(insert)):
            template = template[:insert[i][0]] + insert[i][1] + template[insert[i][0]:]
            for j in range(i + 1, len(insert)):
                insert[j][0] += 1

    for char in tempset:
        chardist.append(template.count(char))

    print(max(chardist) - min(chardist))

with open('input14.txt') as file:
    lines = file.readlines()
    rules = {}
    template = lines[0].strip()
    chardict = {}
    tempdict = {}
    stepdict = {}
    for char in template:
        chardict[char] = 0

    for row in range(2, len(lines)):
        rules[lines[row].strip().split()[0]] = lines[row].strip().split()[2]

    for pair in rules:
        pairlist = [pair]

        for step in range(20):
            start = len(pairlist)
            for char in chardict:
                tempdict[char] = 0
            for i in range(start - 1, -1, -1):
                pairlist.append(pairlist[i][0] + rules[pairlist[i]])
                pairlist.append(rules[pairlist[i]] + pairlist[i][1])
                tempdict[pairlist[i][0]] += 1
                tempdict[pairlist[i][1]] += 1
                tempdict[rules[pairlist[i]]] += 2
            del pairlist[:start]

        if (pair, step + 1) not in stepdict:
            stepdict[(pair, step + 1)] = {char: tempdict[char] for char in tempdict}

    print(stepdict)

    pairs = [template[i] + template[i + 1] for i in range(len(template) - 1)]

    for pair in pairs:
        pairlist = [pair]

        for step in range(20):
            start = len(pairlist)
            for char in chardict:
                tempdict[char] = 0
            for i in range(start - 1, -1, -1):
                pairlist.append(pairlist[i][0] + rules[pairlist[i]])
                pairlist.append(rules[pairlist[i]] + pairlist[i][1])
                tempdict[pairlist[i][0]] += 1
                tempdict[pairlist[i][1]] += 1
                tempdict[rules[pairlist[i]]] += 2
            del pairlist[:start]

        for p in pairlist:
            for char in chardict:
                chardict[char] += stepdict[(p, 20)][char]

    chardict[template[0]] += 1
    chardict[template[-1]] += 1
    for char in chardict:
        chardict[char] /= 2

    print(max(chardict.values()) - min(chardict.values()))

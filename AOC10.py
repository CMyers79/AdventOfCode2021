import statistics

with open('input10.txt') as file:
    lines = file.readlines()
    total = 0
    remlist = []
    for line in lines:
        stack = []
        chars = line.strip()
        error = False
        index = 0
        while index < len(chars) and not error:
            char = chars[index]
            index += 1
            if char in "[{(<":
                stack.append(char)
            elif char == "]" and stack[-1] == "[" or char == ")" and stack[-1] == "(" or char == "}" and stack[-1] == "{" or char == ">" and stack[-1] == "<":
                stack.pop()
            else:
                error = char

        if error == ")":
            total += 3
        elif error == "]":
            total += 57
        elif error == "}":
            total += 1197
        elif error == ">":
            total += 25137

        if not error and len(stack) > 0:
            rem = []
            score = 0
            while len(stack) > 0:
                rem.append(stack.pop())
            for i in range(len(rem)):
                if rem[i] == "(":
                    score *= 5
                    score += 1
                if rem[i] == "[":
                    score *= 5
                    score += 2
                if rem[i] == "{":
                    score *= 5
                    score += 3
                if rem[i] == "<":
                    score *= 5
                    score += 4
            remlist.append(score)

    print(total)

    print(statistics.median(remlist))

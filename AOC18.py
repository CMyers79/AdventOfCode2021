with open('input18.txt') as file:
    lines = file.readlines()

    while len(lines) > 1:
        cur = lines[0]
        lines = lines[1:]
        lines[0] = "[" + cur.strip() + ',' + lines[0].strip() + "]"
        done = False
        while not done:
            print(lines[0])
            depth = 0
            maxdepth = 0
            num = None
            nums = []
            done = True
            i = 0
            while i < len(lines[0]):
                if lines[0][i] == "[":
                    depth += 1
                    if depth > maxdepth:
                        maxdepth += 1
                    if depth == 5:  # explode
                        done = False
                        if lines[0][i + 2] == ",":
                            l = lines[0][i + 1]
                            r = lines[0][i + 3]
                        else:
                            l = lines[0][i + 1:i + 3]
                            r = lines[0][i + 4]

                        lines[0] = lines[0][:i] + "0" + lines[0][i + 5:]
                        j = i - 1
                        while lines[0][j] not in "1234567890" and j > 0:
                            j -= 1
                        if lines[0][j] in "1234567890":
                            lines[0] = lines[0][:j] + str(int(lines[0][j]) + int(l)) + lines[0][j + 1:]
                        j = i + 2
                        while lines[0][j] not in "1234567890" and j < len(lines[0]):
                            j += 1
                        if lines[0][j] in "1234567890":
                            lines[0] = lines[0][:j] + str(int(lines[0][j]) + int(r)) + lines[0][j + 1:]
                        depth -= 1
                        i += 2
                    i += 1

                elif lines[0][i] == "]":
                    depth -= 1
                    i += 1
                else:
                    i += 1

            for i in range(len(lines[0])):

                if lines[0][i] in "1234567890":
                    if num:  # split
                        done = False
                        num = int(num + lines[0][i])
                        lnum = num // 2
                        rnum = num - lnum
                        lines[0] = lines[0][:i - 1] + "[" + str(lnum) + "," + str(rnum) + "]" + lines[0][i + 1:]
                        break

                    else:
                        num = lines[0][i]

                elif lines[0][i] == ",":
                    if num:
                        nums = [num]
                        num = None
                    else:
                        pass

                elif lines[0][i] == "]":
                    if num and len(nums) == 1:
                        nums.append(num)
                    elif num:
                        num = None

    depth = 0
    i = 0
    while maxdepth >= 0:
        while i < len(lines[0]):

            if lines[0][i] == "[":
                depth += 1
                i += 1
                if depth == maxdepth:
                    mag = 3 * int(lines[0][i]) + 2 * int(lines[0][i + 2])
                    lines[0] = lines[0][:i - 1] + str(mag) + lines[0][i + 4:]
                    depth -= 1
            elif lines[0][i] == "]":
                depth -= 1
                i += 1
            else:
                i += 1

            maxdepth -= 1

    print(lines[0])




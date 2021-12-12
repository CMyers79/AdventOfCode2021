with open('input8.txt') as file:
    lines = file.readlines()
    signals = [line.split("|")[0] for line in lines]
    outputs = [line.split("|")[1] for line in lines]
    signal = [signal.split() for signal in signals]
    output = [output.split() for output in outputs]

    easy_digits = 0

    for num in output:
        for digit in num:
            if len(digit) in (2, 3, 4, 7):
                easy_digits += 1

    print(easy_digits)
    numbers = []

    for i in range(len(signal)):
        twothreefive = []
        zerosixnine = []

        for digit in signal[i]:
            if len(digit) == 2:
                one = digit
            elif len(digit) == 3:
                seven = digit
            elif len(digit) == 4:
                four = digit
            elif len(digit) == 7:
                eight = digit
            elif len(digit) == 5:
                twothreefive.append(digit)
            else:
                zerosixnine.append(digit)

        notthree = []
        notsix = []

        for j in range(len(twothreefive)):
            for segment in twothreefive[j]:
                if segment not in twothreefive[(j + 1) % 3] and segment not in twothreefive[(j + 2) % 3]:
                    notthree.append(twothreefive[j])

        three = [num for num in twothreefive if num not in notthree][0]

        for num in notthree:
            for segment in num:
                if segment not in three and segment in four:
                    five = num
                    two = [num for num in notthree if num != five][0]

        for num in zerosixnine:
            if one[0] not in num or one[1] not in num:
                six = num
            else:
                notsix.append(num)

        for num in notsix:
            for segment in four:
                if segment not in num:
                    zero = num
                    nine = [num for num in notsix if num != zero][0]

        numlist = [zero, one, two, three, four, five, six, seven, eight, nine]

        for k in range(len(output[i])):
            index = 0
            while {char for char in output[i][k]} != {char for char in numlist[index]}:
                index += 1

            output[i][k] = index
            print(output[i])

        number = 0
        for l in range(4):
            number += output[i][l] * 10 ** (3 - l)

        numbers.append(number)

    print(sum(numbers))

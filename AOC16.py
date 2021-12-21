import math


def op(stack, ops):
    cur = ops.pop()
    if cur == "sum":
        return sum(stack)
    elif cur == "product":
        return math.prod(stack)
    elif cur == "min":
        return min(stack)
    elif cur == "max":
        return max(stack)
    elif cur == "greater":
        if stack[0] > stack[1]:
            return 1
        else:
            return 0
    elif cur == "less":
        if stack[0] < stack[1]:
            return 1
        else:
            return 0
    elif cur == "equals":
        if stack[0] == stack[1]:
            return 1
        else:
            return 0


def packet(binary, i, stack, index, stopbits, packets, curtrigger, ops):
    tid = binary[i + 3:i + 6]
    i += 6
    if tid == "100":  # if literal, push value on stack
        groups = []
        done = False
        while not done:
            if binary[i] == "0":
                done = True
            groups.append(binary[i + 1:i + 5])
            i += 5
        num = int("".join(groups), 2)
        stack.append(num)
        index[-1] += 1

        while curtrigger[-1] == "bits" and i > stopbits[-1]:
            stopbits.pop()
            curtrigger.pop()
            stack.append(op(stack[-index[-1]:], ops))
            stack = stack[:-index.pop() - 1] + [stack[-1]]
            index[-1] += 1

        if curtrigger[-1] == "packets":
            packets[-1] -= 1
            if packets[-1] == 0:
                packets.pop()
                curtrigger.pop()
                stack.append(op(stack[-index[-1]:], ops))
                stack = stack[:-index.pop() - 1] + [stack[-1]]
                index[-1] += 1

        if i > len(binary) - 5:
            return stack

    else:  # if subpacket, read length type
        index.append(0)
        lid = binary[i]
        i += 1
        if curtrigger[-1] == "packets":
            packets[-1] -= 1

        if lid == "0":  # if bit-delimited, push limit and limit type on stacks
            length = int(binary[i:i + 15], 2)
            i += 15
            stopbits.append(i + length - 1)
            curtrigger.append("bits")

        else:  # if packet-delimited, push limit and limit type on stacks
            number = int(binary[i:i + 11], 2)
            i += 11
            packets.append(number)
            curtrigger.append("packets")

        if tid == "000":  #
            ops.append("sum")
        elif tid == "001":
            ops.append("product")
        elif tid == "010":
            ops.append("min")
        elif tid == "011":
            ops.append("max")
        elif tid == "101":
            ops.append("greater")
        elif tid == "110":
            ops.append("less")
        else:
            ops.append("equals")

    return packet(binary, i, stack, index, stopbits, packets, curtrigger, ops)


with open('input16.txt') as file:
    lines = file.readlines()
    chars = lines[0].strip()
    binary = "".join([bin(int(char, 16))[2:].rjust(4, "0") for char in chars])

    i = 0
    stack = []
    index = []
    nums = []
    packets = []
    stopbits = []
    ops = []
    curtrigger = [None]

    result = packet(binary, i, stack, index, stopbits, packets, curtrigger, ops)
    print(result)

with open('input16.txt') as file:
    lines = file.readlines()
    chars = lines[0].strip()
    binary = "".join([bin(int(char, 16))[2:] for char in chars])
    print(binary)

    i = 0
    groups = []
    while i < len(binary):
        vnum = binary[i:i + 3]
        tid = binary[i + 3:i + 6]
        i += 6
        if tid == "100":
            while binary[i] != 0:
                groups.append(binary[i:i + 4])
                i += 4
        else:
            lid = binary[i]
            if lid == "0":
                i += 1
                length = int(binary[i:i + 15, 2])
                i += 15

            else:

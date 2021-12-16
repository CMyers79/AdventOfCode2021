import string


with open('input12.txt') as file:
    lines = file.readlines()
    paths = [line.strip().split("-") for line in lines]
    caves = {}
    for path in paths:  # construct adjacency list from input
        for cave in path:
            if cave not in caves:
                caves[cave] = [othercave for othercave in path if othercave != cave]
            else:
                caves[cave] += [othercave for othercave in path if othercave != cave if othercave not in caves[cave]]

    routes = [["start"]]
    done = False
    while not done:
        done = True
        for route in routes:
            doubles = []
            for i in range(len(route) - 2):
                if route[i + 2] in route[1:i + 2] and route[i + 2][0] in string.ascii_lowercase:
                    doubles.append(route[i + 2])

            if route[-1] != "end":
                for cave in [adjcave for adjcave in caves[route[-1]] if adjcave != "start"]:
                    if route + [cave] not in routes and (cave == "end" or cave[0] in string.ascii_uppercase or doubles == [] or cave not in route):
                        routes.append(route + [cave])
                        done = False

                routes.remove(route)

    print(len(routes))

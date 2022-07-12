iters = 0

transitions = 0

transitionmap = open("reaction_list.txt", "w")

with open("test_v2.txt", "r") as f:
    count = 0
    while True:
        line = f.readline()
        if not line:
            break
        if line[0] == ">":
            if line[11:16] != "idling":
                iters += 1
        if line[0] == "<":
            transitions += 1
            transitionmap.write(line[24:25])
            transitionmap.write("\t")
        if line[0] == "t":
            count = count + 1
            transitionmap.write("\n\nRun ")
            transitionmap.write(str(count))
            transitionmap.write(" information\n\nIterations before idling was reached: ")
            transitionmap.write(str(iters))
            transitionmap.write("\nNumber of transitions: ")
            transitionmap.write(str(transitions))
            iters = 0
            transitions = 0

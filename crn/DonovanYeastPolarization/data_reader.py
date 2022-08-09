Totaltran = 0
Totaliter = 0
Totalr1 = 0
Totalr2 = 0
Totalr3 = 0
Totalr4 = 0
Totalr5 = 0
Totalr6 = 0
Totalr7 = 0
Totalr8 = 0
Totaliterlist = []
Totaltranlist = []
r1iters = []
r2iters = []
r3iters = []
r4iters = []
r5iters = []
r6iters = []
r7iters = []
r8iters = []

with open("test2_reaction_list.txt", "r") as f:
    count = 0
    while True:
        line = f.readline()
        if not line:
            break
        if line[0] == "N":
            Totaltran = Totaltran + int(line[23:26])
            Totaltranlist.append(int(line[23:26]))
        elif line[0] == "I":
            Totaliter = Totaliter + int(line[38:41])
            Totaliterlist.append(int(line[38:41]))
        elif line[0:2] == "r1":
            if len(line) == 17:
                Totalr1 = Totalr1 + int(line[14:16])
                r1iters.append(int(line[14:16]))
            elif len(line) == 16:
                Totalr1 = Totalr1 + int(line[14])
                r1iters.append(int(line[14]))
        elif line[0:2] == "r2":
            if len(line) == 17:
                Totalr2 = Totalr2 + int(line[14:16])
                r2iters.append(int(line[14:16]))
            elif len(line) == 16:
                Totalr2 = Totalr2 + int(line[14])
                r2iters.append(int(line[14]))
        elif line[0:2] == "r3":
            if len(line) == 17:
                Totalr3 = Totalr3 + int(line[14:16])
                r3iters.append(int(line[14:16]))
            elif len(line) == 16:
                Totalr3 = Totalr3 + int(line[14])
                r3iters.append(int(line[14]))
        elif line[0:2] == "r4":
            if len(line) == 17:
                Totalr4 = Totalr4 + int(line[14:16])
                r4iters.append(int(line[14:16]))
            elif len(line) == 16:
                Totalr4 = Totalr4 + int(line[14])
                r4iters.append(int(line[14]))
        elif line[0:2] == "r5":
            if len(line) == 17:
                Totalr5 = Totalr5 + int(line[14:16])
                r5iters.append(int(line[14:16]))
            elif len(line) == 16:
                Totalr5 = Totalr5 + int(line[14])
                r5iters.append(int(line[14]))
        elif line[0:2] == "r6":
            if len(line) == 17:
                Totalr6 = Totalr6 + int(line[14:16])
                r6iters.append(int(line[14:16]))
            elif len(line) == 16:
                Totalr6 = Totalr6 + int(line[14])
                r6iters.append(int(line[14]))
        elif line[0:2] == "r7":
            if len(line) == 17:
                Totalr7 = Totalr7 + int(line[14:16])
                r7iters.append(int(line[14:16]))
            elif len(line) == 16:
                Totalr7 = Totalr7 + int(line[14])
                r7iters.append(int(line[14]))
        elif line[0:2] == "r8":
            if len(line) == 17:
                Totalr8 = Totalr8 + int(line[14:16])
                r8iters.append(int(line[14:16]))
            elif len(line) == 16:
                Totalr8 = Totalr8 + int(line[14])
                r8iters.append(int(line[14]))

print("\n\nAverage num of transitions is:", str(Totaltran/250))
print("\nThe biggest num of transitions recorded is:", max(Totaltranlist))
print("\nThe smallest num of transitions recorded is:", min(Totaltranlist))
print("\n\nAverage num of iters is:", str(Totaliter/250))
print("\nThe biggest num of iters recorded is:", max(Totaliterlist))
print("\nThe smallest num of iters recorded is:", min(Totaliterlist))
print("\n\nAverage num of r1 executions is:", str(Totalr1/250))
print("\nThe biggest num of r1 executions recorded is:", max(r1iters))
print("\nThe smallest num of r1 executions recorded is:", min(r1iters))
print("\n\nAverage num of r2 executions is:", str(Totalr2/250))
print("\nThe biggest num of r2 executions recorded is:", max(r2iters))
print("\nThe smallest num of r2 executions recorded is:", min(r2iters))
print("\n\nAverage num of r3 executions is:", str(Totalr3/250))
print("\nThe biggest num of r3 executions recorded is:", max(r3iters))
print("\nThe smallest num of r3 executions recorded is:", min(r3iters))
print("\n\nAverage num of r4 executions is:", str(Totalr4/250))
print("\nThe biggest num of r4 executions recorded is:", max(r4iters))
print("\nThe smallest num of r4 executions recorded is:", min(r4iters))
print("\n\nAverage num of r5 executions is:", str(Totalr5/250))
print("\nThe biggest num of r5 executions recorded is:", max(r5iters))
print("\nThe smallest num of r5 executions recorded is:", min(r5iters))
print("\n\nAverage num of r6 executions is:", str(Totalr6/250))
print("\nThe biggest num of r6 executions recorded is:", max(r6iters))
print("\nThe smallest num of r6 executions recorded is:", min(r6iters))
print("\n\nAverage num of r7 executions is:", str(Totalr7/250))
print("\nThe biggest num of r7 executions recorded is:", max(r7iters))
print("\nThe smallest num of r7 executions recorded is:", min(r7iters))
print("\n\nAverage num of r8 executions is:", str(Totalr8/250))
print("\nThe biggest num of r8 executions recorded is:", max(r8iters))
print("\nThe smallest num of r8 executions recorded is:", min(r8iters))

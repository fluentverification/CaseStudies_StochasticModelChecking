numofreactions = 8
Totaltran = 0
Totaliter = 0
Total = []

for x in range(numofreactions):
    Total.append(0)

Totaliterlist = []
Totaltranlist = []

iterations = []
for x in range(numofreactions):
    iterations.append([])

with open("250Runs_reaction_list.txt", "r") as f:
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
        for x in range(numofreactions):
            stringnum = str(x+1)
            stringreact = "r" + stringnum
            if line[0:2] == stringreact:
                if len(line) == 17:
                    Total[x] = Total[x] + int(line[14:16])
                    iterations[x].append(int(line[14:16]))
                elif len(line) == 16:
                    Total[x] = Total[x] + int(line[14])
                    iterations[x].append(int(line[14]))

runswanted = 250

print("\n\nAverage num of transitions is:", str(Totaltran/runswanted))
print("\nThe biggest num of transitions recorded is:", max(Totaltranlist))
print("\nThe smallest num of transitions recorded is:", min(Totaltranlist))
print("\n\nAverage num of iters is:", str(Totaliter/runswanted))
print("\nThe biggest num of iters recorded is:", max(Totaliterlist))
print("\nThe smallest num of iters recorded is:", min(Totaliterlist))

for x in range(numofreactions):
    print("\n\nAverage number of reaction", x+1, "executions is:", str(Total[x]/runswanted))
    print("\nThe biggest number of reaction", x+1, "executions recorded is:", max(iterations[x]))
    print("\nThe smallest number of reaction", x+1, "executions recorded is:", min(iterations[x]))

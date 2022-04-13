import os
import sys

if len(sys.argv) == 2:
  folder = str(sys.argv[1])
else:
  folder = str(input("folder: "))

index = 0

with open("traces_" + folder + ".txt", 'w') as traces:
  while os.path.exists(folder + "/" + str(index) + ".txt"):
    trace = ["init"]
    with open(folder + "/" + str(index) + ".txt") as rin:
      for line in rin:
        if "call ext:spec." in line:
          action = line.split("call ext:spec.")[1].rstrip("\n")
          trace.append(action)
    for state in trace:
      traces.write(state + "\t")
    traces.write("\n")
    print("Trace complete: " + str(index))
    index = index + 1
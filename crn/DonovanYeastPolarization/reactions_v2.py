numofreactions = int(input("Number of reactions: "))

class reaction:
    def __init__(self, reactant1, reactant1num, reactant2, reactant2num, product1, product1num, product2, product2num, priority):
        self.reactant1 = reactant1
        self.reactant1num = reactant1num
        self.reactant2 = reactant2
        self.reactant2num = reactant2num
        self.product1 = product1
        self.product1num = product1num
        self.product2 = product2
        self.product2num = product2num
        self.priority = priority

class species:
    def __init__(self, value, name):
        self.value = value
        self.name = name

class secondtarget:
    def __init__(self, name, min_amount):
        self.name = name
        self.min_amount = min_amount

Reactions = []
for x in range(numofreactions):
    print("\n\n","reaction",x+1, ": \n")
    firstreactant = input("What is the first reactant (if no reactants type 'NA' or leave blank): ")
    if(firstreactant.lower() == "na" or firstreactant == ""):
        firstreactant = ""
        firstreactantnum = 0
        secondreactant = ""
        secondreactantnum = 0
    else:
        firstreactantnum = int(input("What amount of this reactant is needed (type an integer): "))
        if (firstreactantnum == 0):
            print("Error, must be greater than 0, please start over")
            exit()
        secondreactant = input("What is the second reactant (if no second reactant type 'NA' or leave blank): ")
        if(secondreactant.lower() == "na" or secondreactant == ""):
            secondreactant = ""
            secondreactantnum = 0
        else:
            secondreactantnum = int(input("What amount of this reactant is needed (type an integer): "))
            if (secondreactantnum == 0):
                print("Error, must be greater than 0, please start over")
                exit()
    firstproduct = input("What is the first product (if no products type 'NA' or leave blank): ")
    if(firstproduct.lower() == "na" or firstproduct == ""):
        if(firstreactant == ""):
            print("Error, this reaction has no reactants or products please start over")
            exit()
        firstproduct = ""
        firstproductnum = 0
        secondproduct = ""
        secondproductnum = 0
    else:
        firstproductnum = int(input("What amount of this product is produced (type an integer): "))
        if(firstproductnum == 0):
            print("Error, must be greater than 0, please start over")
            exit()
        secondproduct = input("What is the second product (if no second product type 'NA' or leave blank): ")
        if(secondproduct.lower() == "na" or secondproduct == ""):
            secondproduct = ""
            secondproductnum = 0
        else:
            secondproductnum = int(input("What amount of this product is produced (type an integer): "))
            if (secondproductnum == 0):
                print("Error, must be greater than 0, please start over")
                exit()
    Reactions.append(reaction(firstreactant,firstreactantnum,secondreactant,secondreactantnum,firstproduct,firstproductnum,secondproduct,secondproductnum,15))

print("\n\nThe follwing reactions will be considered in the model:\n")

count = 0
for obj in Reactions:
    count = count + 1
    if (obj.reactant1num >= 1 and obj.reactant2num >= 1 and obj.product1num >= 1 and obj.product2num >= 1):
        print(str(count),": ",obj.reactant1num,obj.reactant1," + ",obj.reactant2num, obj.reactant2," -> ", obj.product1num,obj.product1," + ", obj.product2num,obj.product2)
    elif (obj.reactant1num >= 1 and obj.reactant2num == 0 and obj.product1num >= 1 and obj.product2num >= 1):
        print(str(count),": ",obj.reactant1num,obj.reactant1," -> ",obj.product1num, obj.product1," + ", obj.product2num, obj.product2)
    elif (obj.reactant1num >= 1 and obj.reactant2num == 0 and obj.product1num >= 1 and obj.product2num == 0):
        print(str(count),": ",obj.reactant1num,obj.reactant1," -> ", obj.product1num, obj.product1)
    elif (obj.reactant1num >= 1 and obj.reactant2num >= 1 and obj.product1num >= 1 and obj.product2num == 0):
        print(str(count),": ",obj.reactant1num,obj.reactant1," + ",obj.reactant2num, obj.reactant2," -> ", obj.product1num,obj.product1)
    elif (obj.reactant1num == 0 and obj.product1num >= 1 and obj.product2num == 0):
        print(str(count),": ","NULL"," -> ",obj.product1num, obj.product1)
    elif (obj.reactant1num >= 1 and obj.reactant2num == 0 and obj.product1num == 0):
        print(str(count),": ",obj.reactant1num, obj.reactant1," -> ", "NULL")
    elif (obj.reactant1num >= 1 and obj.reactant2num >= 1 and obj.product1num == 0):
        print(str(count),": ",obj.reactant1num,obj.reactant1," + ",obj.reactant2num,obj.reactant2," ->  NULL")
    elif (obj.reactant1num == 0 and obj.product1num >= 1 and obj.product2num >= 1):
        print(str(count),": ","NULL  -> ",obj.product1num,obj.product1," + ",obj.product2num,obj.product2)

print("\n")
spec = []

for obj in Reactions:
    if (obj.reactant1 not in spec and obj.reactant1 != ""):
        spec.append(obj.reactant1)
    if (obj.reactant2 not in spec and obj.reactant2 != ""):
        spec.append(obj.reactant2)
    if (obj.product1 not in spec and obj.product1 != ""):
        spec.append(obj.product1)
    if (obj.product2 not in spec and obj.product2 != ""):
        spec.append(obj.product2)

specieslist = []

for obj in spec:
    print("What is the initial value of", obj, "?")
    val = int(input())
    specieslist.append(species(val, obj))

print("The initial values reported are:")

for obj in specieslist:
    print(obj.name,"=",obj.value)

print("\n")

targetspecies = input("Which species is going to be monitored? ")
if(targetspecies not in spec):
    print("Error, species specified not found in the reactions reported please start over")
    exit()
targetnum = input("What is the target number for this species? ")

print("\n\nWhich option is your desired guard?\n\n","1:", targetspecies, ">=", targetnum, "\n 2:", targetspecies, ">", targetnum, "\n 3:", targetspecies, "<=", targetnum,"\n 4:", targetspecies, "<", targetnum,"\n 5:", targetspecies, "=", targetnum) 

upOrDown = input("\n\n(Please type an integer corresponding to your desired guard):  ")

if upOrDown == "5":
    for obj in specieslist:
        if obj.name == targetspecies:
            if obj.value > int(targetnum):
                upOrDown = "3"
            elif obj.value < int(targetnum):
                upOrDown = "1"
            elif obj.value == int(targetnum):
                print("\nSpecified target is already achieved in target state, please start over")
                exit()

for obj in specieslist:
    if obj.name == targetspecies:
        if upOrDown == "1":
            if obj.value >= int(targetnum):
                print("\nSpecified target is already achieved in target state, please start over")
                exit()
        elif upOrDown == "2":
            if obj.value > int(targetnum):
                print("\nSpecified target is already achieved in target state, please start over")
                exit()
        elif upOrDown == "3":
            if obj.value <= int(targetnum):
                print("\nSpecified target is already achieved in target state, please start over")
                exit()
        elif upOrDown == "4":
            if obj.value < int(targetnum):
                print("\nSpecified target is already achieved in target state, please start over")
                exit()
            if targetnum == "0":
                print("Error, no species can reach a value lower than zero")
                exit()
        else:
            print("Problem with information entered (check make sure your answer you only entered a integer between 1 and 4 and there are no spaces)")
            exit()

secondtargetlist = []
if upOrDown == "1" or upOrDown == "2":
    for obj in Reactions:
        if obj.product1 == targetspecies or obj.product2 == targetspecies:
            obj.priority = obj.priority + 10
        elif obj.reactant1 == targetspecies or obj.reactant2 == targetspecies:
            obj.priority = obj.priority - 10
elif upOrDown == "3" or upOrDown == "4":
    for obj in Reactions:
        if obj.product1 == targetspecies or obj.product2 == targetspecies:
            obj.priority = obj.priority - 10
        elif obj.reactant1 == targetspecies or obj.reactant2 == targetspecies:
            obj.priority = obj.priority + 10


for obj in Reactions:
    if upOrDown == "1" or upOrDown == "2":
        if obj.priority >= 25:
            if obj.reactant1 != "" and obj.reactant2 != "":
                if obj.reactant1 != targetspecies:
                    if obj.product1 == targetspecies:
                        for tar in specieslist:
                            if tar.name == targetspecies:
                                tarnumone = tar.value
                                secondtargetlist.append(secondtarget(obj.reactant1, obj.reactant1num * abs(int(targetnum) - tar.value)/obj.product1num))
                    elif obj.product2 == targetspecies:
                        for tar in specieslist:
                            if tar.name == targetspecies:
                                tarnumone = tar.value
                                secondtargetlist.append(secondtarget(obj.reactant1, obj.reactant1num * abs(int(targetnum) - tar.value)/obj.product2num))
                if obj.reactant2 != targetspecies:    
                    if obj.product1 == targetspecies:
                        for tar in specieslist:
                            if tar.name == targetspecies:
                                tarnumone = tar.value
                                secondtargetlist.append(secondtarget(obj.reactant2, obj.reactant2num * abs(int(targetnum) - tar.value)/obj.product1num))
                    elif obj.product2 == targetspecies:
                        for tar in specieslist:
                            if tar.name == targetspecies:
                                tarnumone = tar.value
                                secondtargetlist.append(secondtarget(obj.reactant2, obj.reactant2num * abs(int(targetnum) - tar.value)/obj.product2num))
            elif obj.reactant1 != "" and obj.reactant2 == "":
                if obj.reactant1 != targetspecies:
                    if obj.product1 == targetspecies:
                        for tar in specieslist:
                            if tar.name == targetspecies:
                                tarnumone = tar.value
                                secondtargetlist.append(secondtarget(obj.reactant1, obj.reactant1num * abs(int(targetnum) - tar.value)/obj.product1num))
                    elif obj.product2 == targetspecies:
                        for tar in specieslist:
                            if tar.name == targetspecies:
                                tarnumone = tar.value
                                secondtargetlist.append(secondtarget(obj.reactant1, obj.reactant1num * abs(int(targetnum) - tar.value)/obj.product2num))
    elif upOrDown == "3" or upOrDown== "4":
        if obj.priority >= 25:
            if obj.reactant1 != "" and obj.reactant2 != "":
                if obj.reactant1 != targetspecies:
                    if obj.reactant2 == targetspecies:
                        for tar in specieslist:
                            if tar.name == targetspecies:
                                tarnumone = tar.value
                                secondtargetlist.append(secondtarget(obj.reactant1, obj.reactant1num * abs(int(targetnum) - tar.value)/obj.reactant2num))
                if obj.reactant2 != targetspecies:    
                    if obj.reactant1 == targetspecies:
                        for tar in specieslist:
                            if tar.name == targetspecies:
                                tarnumone = tar.value
                                secondtargetlist.append(secondtarget(obj.reactant2, obj.reactant2num * abs(int(targetnum) - tar.value)/obj.reactant1num))
            
 
for obj in Reactions:
    if obj.priority < 25:
        for tar in secondtargetlist:
            for species in specieslist:
                if species.name == tar.name:
                    if species.value >= (2*tar.min_amount):
                        if obj.reactant1 == tar.name:
                            obj.priority = obj.priority - 1
                        if obj.reactant2 == tar.name:
                            obj.priority = obj.priority - 1
                    elif species.value >= tar.min_amount:
                        if obj.reactant1 == tar.name:
                            obj.priority = obj.priority - 2
                        if obj.reactant2 == tar.name:
                            obj.priority = obj.priority - 2
                    elif species.value >= (tar.min_amount/2):
                        if obj.reactant1 == tar.name:
                            obj.priority = obj.priority - 3
                        if obj.reactant2 == tar.name:
                            obj.priority = obj.priority - 3
                    elif species.value >= (tar.min_amount/4):
                        if obj.reactant1 == tar.name:
                            obj.priority = obj.priority - 4
                        if obj.reactant2 == tar.name:
                            obj.priority = obj.priority - 4
                    elif species.value < (tar.min_amount/4):
                        if obj.reactant1 == tar.name:
                            obj.priority = obj.priority - 5
                        if obj.reactant2 == tar.name:
                            obj.priority = obj.priority - 5

        
for obj in Reactions:
    if obj.priority < 25:
        for tar in secondtargetlist:
            for species in specieslist:
                if species.name == tar.name:
                    if obj.product1 == tar.name:
                        if species.value >= (2*tar.min_amount):
                            obj.priority = obj.priority + 1
                        elif species.value >= tar.min_amount:
                            obj.priority = obj.priority + 2
                        elif species.value >= (tar.min_amount/2):
                            obj.priority = obj.priority + 3
                        elif species.value >= (tar.min_amount/4):
                            obj.priority = obj.priority + 4
                        elif species.value < (tar.min_amount/4):
                            obj.priority = obj.priority + 5
                    elif obj.product2 == tar.name:
                        if species.value >= (2*tar.min_amount):
                            obj.priority = obj.priority + 1
                        elif species.value >= tar.min_amount:
                            obj.priority = obj.priority + 2
                        elif species.value >= (tar.min_amount/2):
                            obj.priority = obj.priority + 3
                        elif species.value >= (tar.min_amount/4):
                            obj.priority = obj.priority + 4
                        elif species.value < (tar.min_amount/4):
                            obj.priority = obj.priority + 5

print("\n\nThe following priorities have been noted for the reactions: \n")

count = 0
for obj in Reactions:
    count = count + 1
    print("reaction", str(count), ":", str(obj.priority))

ivy_file = open("test_v2.ivy", "w")

ivy_file.write("#lang ivy 1.7\n\nobject updater = {\n")
ivy_file.write("\ttype num\n\tinterpret num -> bv[10]\n\ttype exec_var\n\tinterpret exec_var -> bv[8]\n\ttype exec_stage\n\tinterpret exec_stage -> bv[3]\n\n\taction incr(x:num) returns(y:num) = {\n\t\ty := x + 1\n\t}\n\n\taction decr(x:num) returns(y:num) = {\n\t\ty := x - 1\n\t}\n}")
ivy_file.write("\n\nobject goal = {\n\taction achieved(v:updater.num)\n\tobject spec = {\n\t\tbefore achieved {\n\t\t\tassert v ")
if upOrDown == "1":
    ivy_file.write(">= ")
elif upOrDown == "2":
    ivy_file.write("> ")
elif upOrDown == "3":
    ivy_file.write("<= ")
elif upOrDown == "4":
    ivy_file.write("< ")
ivy_file.write(targetnum)
ivy_file.write(";\n\t\t\tprotocol.idle := 1\n\t\t}\n\t}\n}\n\n")

ivy_file.write("object enabled_checker = {\n\n\t")

count = 0
for obj in Reactions:
    count = count + 1
    ivy_file.write("action is_enabled_r") 
    ivy_file.write(str(count))
    if (Reactions[count-1].reactant1 == ""):
        ivy_file.write(" returns(y:bool) = {\n\t\ty := true\n\t}\n\n\t")
    elif(Reactions[count-1].reactant1 != "" and Reactions[count-1].reactant2 == ""):
        ivy_file.write("(reactant1:updater.num) returns(y:bool) = {\n\t\tif reactant1 >= ")
        ivy_file.write(str(obj.reactant1num))
        ivy_file.write(" {\n\t\t\ty := true\n\t\t}\n\t\telse {\n\t\t\ty := false\n\t\t}\n\t}\n\n\t")
    elif(Reactions[count-1].reactant1 != "" and Reactions[count-1].reactant2 != ""):
        ivy_file.write("(reactant1:updater.num,reactant2:updater.num) returns(y:bool) = {\n\t\tif reactant1 >= ")
        ivy_file.write(str(obj.reactant1num))
        ivy_file.write(" & reactant2 >= ")
        ivy_file.write(str(obj.reactant2num))
        ivy_file.write(" {\n\t\t\ty := true\n\t\t}\n\t\telse {\n\t\t\ty := false\n\t\t}\n\t}\n\n\t")
ivy_file.write("\n}\n\n")

ivy_file.write("object inspector = {\n\t")
count = 0
for obj in Reactions:
    count = count + 1
    ivy_file.write("action check_guard_r")
    ivy_file.write(str(count))
    if (Reactions[count-1].reactant1 == ""):
        ivy_file.write("\n\tbefore check_guard_r")
        ivy_file.write(str(count))
        ivy_file.write(" {\n\t\tassert true\n\t}\n\n\t")
    elif(Reactions[count-1].reactant1 != "" and Reactions[count-1].reactant2 == ""):
        ivy_file.write("(reactant1:updater.num)\n\tbefore check_guard_r")
        ivy_file.write(str(count))
        ivy_file.write(" {\n\t\tassert reactant1 >= ")
        ivy_file.write(str(obj.reactant1num))
        ivy_file.write("\n\t}\n\n\t")
    elif(Reactions[count-1].reactant1 != "" and Reactions[count-1].reactant2 != ""):
        ivy_file.write("(reactant1:updater.num,reactant2:updater.num)\n\tbefore check_guard_r")
        ivy_file.write(str(count))
        ivy_file.write(" {\n\t\tassert reactant1 >= ")
        ivy_file.write(str(obj.reactant1num))
        ivy_file.write(" & reactant2 >= ")
        ivy_file.write(str(obj.reactant2num))
        ivy_file.write("\n\t}\n\n\t")

        
ivy_file.write("\n}")

ivy_file.write("\n\nobject selector = {\n\t")

count = 0

for obj in Reactions:
    count = count + 1
    ivy_file.write("individual r")
    ivy_file.write(str(count))
    ivy_file.write("_exec : updater.exec_var\n\t")

ivy_file.write("\n\t")
count = 0

for obj in Reactions:
    count = count + 1
    ivy_file.write("individual r")
    ivy_file.write(str(count))
    ivy_file.write("_rate : updater.exec_var\n\t")

ivy_file.write("\n\t")

count = 0
for obj in Reactions:
    count = count + 1
    ivy_file.write("individual r")
    ivy_file.write(str(count))
    ivy_file.write("_count : updater.exec_var\n\t")

ivy_file.write("\n\t")

count = 0
for obj in Reactions:
    count = count + 1
    ivy_file.write("individual r")
    ivy_file.write(str(count))
    ivy_file.write("_count_rate : updater.exec_var\n\t")

ivy_file.write("\n\t")

count = 0
for obj in Reactions:
    count = count + 1
    ivy_file.write("individual r")
    ivy_file.write(str(count))
    ivy_file.write("_stage : updater.exec_stage\n\t")

ivy_file.write("\n\n\tafter init {\n\t\t")

count = 0
for obj in Reactions:
    count = count + 1
    ivy_file.write("r")
    ivy_file.write(str(count))
    ivy_file.write("_count := 0")
    ivy_file.write(";\n\t\t")

ivy_file.write("\n\n\t\t")
count = 0
for obj in Reactions:
    count = count + 1
    ivy_file.write("r")
    ivy_file.write(str(count))
    ivy_file.write("_count_rate := 4")
    ivy_file.write(";\n\t\t")

ivy_file.write("\n\t}\n\n\t")

count = 0
for obj in Reactions:
    count = count + 1
    ivy_file.write("action execute_r")
    ivy_file.write(str(count))
    ivy_file.write(" returns(y:bool) = {\n\t\tr")
    ivy_file.write(str(count))
    ivy_file.write("_exec := r")
    ivy_file.write(str(count))
    ivy_file.write("_exec + 1;\n\t\t")
    ivy_file.write("if r")
    ivy_file.write(str(count))
    ivy_file.write("_exec >= r")
    ivy_file.write(str(count))
    ivy_file.write("_rate {\n\t\t\ty := true;\n\t\t\tr")
    ivy_file.write(str(count))
    ivy_file.write("_exec := 0;\n\t\t\tr")
    ivy_file.write(str(count))
    ivy_file.write("_count := r")
    ivy_file.write(str(count))
    ivy_file.write("_count + 1\n\t\t}\n\t\telse {\n\t\t\ty := false\n\t\t};\n\t\tif r")
    ivy_file.write(str(count))
    ivy_file.write("_count >= r")
    ivy_file.write(str(count))
    ivy_file.write("_count_rate {\n\t\t\tr")
    ivy_file.write(str(count))
    ivy_file.write("_stage := r")
    ivy_file.write(str(count))
    ivy_file.write("_stage + 1;\n\t\t\tr")
    ivy_file.write(str(count))
    ivy_file.write("_count := 0\n\t\t};\n\t\t")
    if obj.priority >= 19:
        ivy_file.write("if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 0 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 4;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 1\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 1 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 4;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 1\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 2 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 4;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 1\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 3 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 4;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 1\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 4 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 4;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 1\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 5 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 4;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 1\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 6 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 4;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 1\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 7 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 4;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 1\n\t\t}\n\t\telse {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_stage := 0\n\t\t}\n\t}\n\n\t")
    elif obj.priority == 18:
        ivy_file.write("if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 0 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 4;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 1\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 1 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 2;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 2\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 2 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 2;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 1\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 3 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 3;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 2\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 4 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 5;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 1\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 5 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 2;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 2\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 6 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 4;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 1\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 7 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 4;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 2\n\t\t}\n\t\telse {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_stage := 0\n\t\t}\n\t}\n\n\t")
    elif obj.priority == 17:
        ivy_file.write("if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 0 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 3;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 1\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 1 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 4;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 2\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 2 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 2;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 3\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 3 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 4;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 2\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 4 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 3;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 3\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 5 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 2;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 2\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 6 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 1;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 1\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 7 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 4;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 2\n\t\t}\n\t\telse {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_stage := 0\n\t\t}\n\t}\n\n\t")
    elif obj.priority <= 16 and obj.priority >= 14:
        ivy_file.write("if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 0 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 4;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 3\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 1 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 3;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 4\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 2 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 2;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 2\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 3 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 9;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 5\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 4 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 4;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 2\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 5 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 3;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 1\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 6 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 5;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 3\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 7 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 1;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 5\n\t\t}\n\t\telse {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_stage := 0\n\t\t}\n\t}\n\n\t")
    elif obj.priority == 13:
        ivy_file.write("if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 0 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 4;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 13\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 1 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 3;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 11\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 2 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 2;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 15\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 3 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 9;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 12\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 4 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 4;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 14\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 5 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 4;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 12\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 6 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 5;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 15\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 7 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 3;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 10\n\t\t}\n\t\telse {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_stage := 0\n\t\t}\n\t}\n\n\t")
    elif obj.priority <= 12 and obj.priority >= 10:
        ivy_file.write("if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 0 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 5;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 30\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 1 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 3;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 28\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 2 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 2;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 34\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 3 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 9;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 25\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 4 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 4;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 36\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 5 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 2;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 29\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 6 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 5;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 30\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 7 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 1;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 34\n\t\t}\n\t\telse {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_stage := 0\n\t\t}\n\t}\n\n\t")
    elif obj.priority <= 9 and obj.priority >= 7:
        ivy_file.write("if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 0 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 5;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 50\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 1 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 3;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 56\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 2 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 2;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 62\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 3 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 9;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 48\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 4 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 4;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 63\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 5 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 2;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 52\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 6 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 5;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 58\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 7 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 1;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 82\n\t\t}\n\t\telse {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_stage := 0\n\t\t}\n\t}\n\n\t")
    elif obj.priority <= 6:
        ivy_file.write("if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 0 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 5;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 250\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 1 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 3;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 250\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 2 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 2;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 250\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 3 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 9;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 250\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 4 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 4;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 250\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 5 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 2;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 250\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 6 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 5;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 250\n\t\t}\n\t\t")
        ivy_file.write("else if r")
        ivy_file.write(str(count))
        ivy_file.write("_stage = 7 {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 1;\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_rate := 250\n\t\t}\n\t\telse {\n\t\t\tr")
        ivy_file.write(str(count))
        ivy_file.write("_stage := 0\n\t\t}\n\t}\n\n\t")



ivy_file.write("\n}\n")

ivy_file.write("\nobject protocol = {\n\n\ttype 2bit\n\tinterpret 2bit -> bv[1]\n\tindividual idle : 2bit\n\n")

for obj in spec:
    ivy_file.write("\tindividual ")
    ivy_file.write("r_")
    ivy_file.write(obj)
    ivy_file.write(" : updater.num\n")

ivy_file.write("\n\tafter init {\n\t\t")

for obj in specieslist:
    ivy_file.write("r_")
    ivy_file.write(obj.name)
    ivy_file.write(" := ")
    ivy_file.write(str(obj.value))
    ivy_file.write(";\n\t\t")

ivy_file.write("idle := 0\n\t}\n\n\t")

count = 0
for obj in Reactions:
    count = count + 1
    if(obj.reactant1 == "" and obj.product1 != "" and obj.product2 == ""):
        ivy_file.write("action update_r")
        ivy_file.write(str(count))
        ivy_file.write(" = {\n\t\t")
        ivy_file.write("if selector.execute_r")
        ivy_file.write(str(count))
        ivy_file.write(" {\n\t\t\tcall inspector.check_guard_r")
        ivy_file.write(str(count))
        for x in range(obj.product1num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.product1)
            ivy_file.write(" := updater.incr(")
            ivy_file.write("r_")
            ivy_file.write(obj.product1)
            ivy_file.write(")")
        if obj.priority >= 25:
            ivy_file.write(";\n\t\t")
            ivy_file.write("\tif ")
            ivy_file.write("r_")
            ivy_file.write(targetspecies)
            if upOrDown == "1":
                ivy_file.write(" >= ")
            elif upOrDown == "2":
                ivy_file.write(" > ")
            elif upOrDown == "3":
                ivy_file.write(" <= ")
            elif upOrDown == "4":
                ivy_file.write(" < ")
            ivy_file.write(str(targetnum))
            ivy_file.write(" {\n\t\t\t\tcall goal.achieved(")
            ivy_file.write("r_")
            ivy_file.write(targetspecies)
            ivy_file.write(")\n\t\t\t}\n\t\t")
        else:
            ivy_file.write("\n\t\t")
        ivy_file.write("}\n\t}\n\n\t")
    elif(obj.reactant1 == "" and obj.product1 != "" and obj.product2 != ""):
        ivy_file.write("action update_r")
        ivy_file.write(str(count))
        ivy_file.write(" = {\n\t\t")
        ivy_file.write("if selector.execute_r")
        ivy_file.write(str(count))
        ivy_file.write(" {\n\t\t\tcall inspector.check_guard_r")
        ivy_file.write(str(count))
        for x in range(obj.product1num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.product1)
            ivy_file.write(" := updater.incr(")
            ivy_file.write("r_")
            ivy_file.write(obj.product1)
            ivy_file.write(")")
        for x in range(obj.product2num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.product2)
            ivy_file.write(" := updater.incr(")
            ivy_file.write("r_")
            ivy_file.write(obj.product2)
            ivy_file.write(")")
        if obj.priority >= 25:
            ivy_file.write(";\n\t\t")
            ivy_file.write("\tif ")
            ivy_file.write("r_")
            ivy_file.write(targetspecies)
            if upOrDown == "1":
                ivy_file.write(" >= ")
            elif upOrDown == "2":
                ivy_file.write(" > ")
            elif upOrDown == "3":
                ivy_file.write(" <= ")
            elif upOrDown == "4":
                ivy_file.write(" < ")
            ivy_file.write(str(targetnum))
            ivy_file.write(" {\n\t\t\t\tcall goal.achieved(")
            ivy_file.write("r_")
            ivy_file.write(targetspecies)
            ivy_file.write(")\n\t\t\t}\n\t\t")
        else:
            ivy_file.write("\n\t\t")
        ivy_file.write("}\n\t}\n\n\t")
    elif(obj.reactant1 != "" and obj.reactant2 == "" and obj.product1 == ""):
        ivy_file.write("action update_r")
        ivy_file.write(str(count))
        ivy_file.write(" = {\n\t\t")
        ivy_file.write("if selector.execute_r")
        ivy_file.write(str(count))
        ivy_file.write(" {\n\t\t\tcall inspector.check_guard_r")
        ivy_file.write(str(count))
        ivy_file.write("(")
        ivy_file.write("r_")
        ivy_file.write(obj.reactant1)
        ivy_file.write(")")
        for x in range(obj.reactant1num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant1)
            ivy_file.write(" := updater.decr(")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant1)
            ivy_file.write(")")
        if obj.priority >= 25:
            ivy_file.write(";\n\t\t")
            ivy_file.write("\tif ")
            ivy_file.write("r_")
            ivy_file.write(targetspecies)
            if upOrDown == "1":
                ivy_file.write(" >= ")
            elif upOrDown == "2":
                ivy_file.write(" > ")
            elif upOrDown == "3":
                ivy_file.write(" <= ")
            elif upOrDown == "4":
                ivy_file.write(" < ")
            ivy_file.write(str(targetnum))
            ivy_file.write(" {\n\t\t\t\tcall goal.achieved(")
            ivy_file.write("r_")
            ivy_file.write(targetspecies)
            ivy_file.write(")\n\t\t\t}\n\t\t")
        else:
            ivy_file.write("\n\t\t")
        ivy_file.write("}\n\t}\n\n\t")
    elif(obj.reactant1 != "" and obj.reactant2 == "" and obj.product1 != "" and obj.product2 == ""):
        ivy_file.write("action update_r")
        ivy_file.write(str(count))
        ivy_file.write(" = {\n\t\t")
        ivy_file.write("if selector.execute_r")
        ivy_file.write(str(count))
        ivy_file.write(" {\n\t\t\tcall inspector.check_guard_r")
        ivy_file.write(str(count))
        ivy_file.write("(")
        ivy_file.write("r_")
        ivy_file.write(obj.reactant1)
        ivy_file.write(")")
        for x in range(obj.reactant1num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant1)
            ivy_file.write(" := updater.decr(")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant1)
            ivy_file.write(")")
        for x in range(obj.product1num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.product1)
            ivy_file.write(" := updater.incr(")
            ivy_file.write("r_")
            ivy_file.write(obj.product1)
            ivy_file.write(")")
        if obj.priority >= 25:
            ivy_file.write(";\n\t\t")
            ivy_file.write("\tif ")
            ivy_file.write("r_")
            ivy_file.write(targetspecies)
            if upOrDown == "1":
                ivy_file.write(" >= ")
            elif upOrDown == "2":
                ivy_file.write(" > ")
            elif upOrDown == "3":
                ivy_file.write(" <= ")
            elif upOrDown == "4":
                ivy_file.write(" < ")
            ivy_file.write(str(targetnum))
            ivy_file.write(" {\n\t\t\t\tcall goal.achieved(")
            ivy_file.write("r_")
            ivy_file.write(targetspecies)
            ivy_file.write(")\n\t\t\t}\n\t\t")
        else:
            ivy_file.write("\n\t\t")
        ivy_file.write("}\n\t}\n\n\t")
    elif(obj.reactant1 != "" and obj.reactant2 == "" and obj.product1 != "" and obj.product2 != ""):
        ivy_file.write("action update_r")
        ivy_file.write(str(count))
        ivy_file.write(" = {\n\t\t")
        ivy_file.write("if selector.execute_r")
        ivy_file.write(str(count))
        ivy_file.write(" {\n\t\t\tcall inspector.check_guard_r")
        ivy_file.write(str(count))
        ivy_file.write("(")
        ivy_file.write("r_")
        ivy_file.write(obj.reactant1)
        ivy_file.write(")")
        for x in range(obj.reactant1num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant1)
            ivy_file.write(" := updater.decr(")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant1)
            ivy_file.write(")")
        for x in range(obj.product1num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.product1)
            ivy_file.write(" := updater.incr(")
            ivy_file.write("r_")
            ivy_file.write(obj.product1)
            ivy_file.write(")")
        for x in range(obj.product2num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.product2)
            ivy_file.write(" := updater.incr(")
            ivy_file.write("r_")
            ivy_file.write(obj.product2)
            ivy_file.write(")")
        if obj.priority >= 25:
            ivy_file.write(";\n\t\t")
            ivy_file.write("\tif ")
            ivy_file.write("r_")
            ivy_file.write(targetspecies)
            if upOrDown == "1":
                ivy_file.write(" >= ")
            elif upOrDown == "2":
                ivy_file.write(" > ")
            elif upOrDown == "3":
                ivy_file.write(" <= ")
            elif upOrDown == "4":
                ivy_file.write(" < ")
            ivy_file.write(str(targetnum))
            ivy_file.write(" {\n\t\t\t\tcall goal.achieved(")
            ivy_file.write("r_")
            ivy_file.write(targetspecies)
            ivy_file.write(")\n\t\t\t}\n\t\t")
        else:
            ivy_file.write("\n\t\t")
        ivy_file.write("}\n\t}\n\n\t")
    elif(obj.reactant1 != "" and obj.reactant2 != "" and obj.product1 == ""):
        ivy_file.write("action update_r")
        ivy_file.write(str(count))
        ivy_file.write(" = {\n\t\t")
        ivy_file.write("if selector.execute_r")
        ivy_file.write(str(count))
        ivy_file.write(" {\n\t\t\tcall inspector.check_guard_r")
        ivy_file.write(str(count))
        ivy_file.write("(")
        ivy_file.write("r_")
        ivy_file.write(obj.reactant1)
        ivy_file.write(",")
        ivy_file.write("r_")
        ivy_file.write(obj.reactant2)
        ivy_file.write(")")
        for x in range(obj.reactant1num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant1)
            ivy_file.write(" := updater.decr(")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant1)
            ivy_file.write(")")
        for x in range(obj.reactant2num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant2)
            ivy_file.write(" := updater.decr(")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant2)
            ivy_file.write(")")
        if obj.priority >= 25:
            ivy_file.write(";\n\t\t")
            ivy_file.write("\tif ")
            ivy_file.write("r_")
            ivy_file.write(targetspecies)
            if upOrDown == "1":
                ivy_file.write(" >= ")
            elif upOrDown == "2":
                ivy_file.write(" > ")
            elif upOrDown == "3":
                ivy_file.write(" <= ")
            elif upOrDown == "4":
                ivy_file.write(" < ")
            ivy_file.write(str(targetnum))
            ivy_file.write(" {\n\t\t\t\tcall goal.achieved(")
            ivy_file.write("r_")
            ivy_file.write(targetspecies)
            ivy_file.write(")\n\t\t\t}\n\t\t")
        else:
            ivy_file.write("\n\t\t")
        ivy_file.write("}\n\t}\n\n\t")
    elif(obj.reactant1 != "" and obj.reactant2 != "" and obj.product1 != "" and obj.product2 == ""):
        ivy_file.write("action update_r")
        ivy_file.write(str(count))
        ivy_file.write(" = {\n\t\t")
        ivy_file.write("if selector.execute_r")
        ivy_file.write(str(count))
        ivy_file.write(" {\n\t\t\tcall inspector.check_guard_r")
        ivy_file.write(str(count))
        ivy_file.write("(")
        ivy_file.write("r_")
        ivy_file.write(obj.reactant1)
        ivy_file.write(",")
        ivy_file.write("r_")
        ivy_file.write(obj.reactant2)
        ivy_file.write(")")
        for x in range(obj.reactant1num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant1)
            ivy_file.write(" := updater.decr(")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant1)
            ivy_file.write(")")
        for x in range(obj.reactant2num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant2)
            ivy_file.write(" := updater.decr(")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant2)
            ivy_file.write(")")
        for x in range(obj.product1num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.product1)
            ivy_file.write(" := updater.incr(")
            ivy_file.write("r_")
            ivy_file.write(obj.product1)
            ivy_file.write(")")
        if obj.priority >= 25:
            ivy_file.write(";\n\t\t")
            ivy_file.write("\tif ")
            ivy_file.write("r_")
            ivy_file.write(targetspecies)
            if upOrDown == "1":
                ivy_file.write(" >= ")
            elif upOrDown == "2":
                ivy_file.write(" > ")
            elif upOrDown == "3":
                ivy_file.write(" <= ")
            elif upOrDown == "4":
                ivy_file.write(" < ")
            ivy_file.write(str(targetnum))
            ivy_file.write(" {\n\t\t\t\tcall goal.achieved(")
            ivy_file.write("r_")
            ivy_file.write(targetspecies)
            ivy_file.write(")\n\t\t\t}\n\t\t")
        else:
            ivy_file.write("\n\t\t")
        ivy_file.write("}\n\t}\n\n\t")
    elif(obj.reactant1 != "" and obj.reactant2 != "" and obj.product1 != "" and obj.product2 != ""):
        ivy_file.write("action update_r")
        ivy_file.write(str(count))
        ivy_file.write(" = {\n\t\t")
        ivy_file.write("if selector.execute_r")
        ivy_file.write(str(count))
        ivy_file.write(" {\n\t\t\tcall inspector.check_guard_r")
        ivy_file.write(str(count))
        ivy_file.write("(")
        ivy_file.write("r_")
        ivy_file.write(obj.reactant1)
        ivy_file.write(",")
        ivy_file.write("r_")
        ivy_file.write(obj.reactant2)
        ivy_file.write(")")
        for x in range(obj.reactant1num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant1)
            ivy_file.write(" := updater.decr(")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant1)
            ivy_file.write(")")
        for x in range(obj.reactant2num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant2)
            ivy_file.write(" := updater.decr(")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant2)
            ivy_file.write(")")
        for x in range(obj.product1num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.product1)
            ivy_file.write(" := updater.incr(")
            ivy_file.write("r_")
            ivy_file.write(obj.product1)
            ivy_file.write(")")
        for x in range(obj.product2num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.product2)
            ivy_file.write(" := updater.incr(")
            ivy_file.write("r_")
            ivy_file.write(obj.product2)
            ivy_file.write(")")
        if obj.priority >= 25:
            ivy_file.write(";\n\t\t")
            ivy_file.write("\tif ")
            ivy_file.write("r_")
            ivy_file.write(targetspecies)
            if upOrDown == "1":
                ivy_file.write(" >= ")
            elif upOrDown == "2":
                ivy_file.write(" > ")
            elif upOrDown == "3":
                ivy_file.write(" <= ")
            elif upOrDown == "4":
                ivy_file.write(" < ")
            ivy_file.write(str(targetnum))
            ivy_file.write(" {\n\t\t\t\tcall goal.achieved(")
            ivy_file.write("r_")
            ivy_file.write(targetspecies)
            ivy_file.write(")\n\t\t\t}\n\t\t")
        else:
            ivy_file.write("\n\t\t")
        ivy_file.write("}\n\t}\n\n\t")

ivy_file.write("\n\n\taction idling = {}\n\n\t")
count = 0
for obj in Reactions:
    count = count + 1
    ivy_file.write("before update_r")
    ivy_file.write(str(count))
    if (Reactions[count-1].reactant1 == ""):
        ivy_file.write(" {\n\t\tassert idle = 0;\n\t\tassert enabled_checker.is_enabled_r")
        ivy_file.write(str(count))
        if obj.priority <= 6:
            ivy_file.write(";\n\t\tassert false")
        ivy_file.write("\n\t}\n\t")
    elif(Reactions[count-1].reactant1 != "" and Reactions[count-1].reactant2 == ""):
        ivy_file.write(" {\n\t\tassert idle = 0;\n\t\tassert enabled_checker.is_enabled_r")
        ivy_file.write(str(count))
        ivy_file.write("(")
        ivy_file.write("r_")
        ivy_file.write(Reactions[count-1].reactant1)
        ivy_file.write(")")
        if obj.priority <= 6:
            ivy_file.write(";\n\t\tassert false")
        ivy_file.write("\n\t}\n\t")
    elif(Reactions[count-1].reactant1 != "" and Reactions[count-1].reactant2 != ""):
        ivy_file.write(" {\n\t\tassert idle = 0;\n\t\tassert enabled_checker.is_enabled_r")
        ivy_file.write(str(count))
        ivy_file.write("(")
        ivy_file.write("r_")
        ivy_file.write(Reactions[count-1].reactant1)
        ivy_file.write(",")
        ivy_file.write("r_")
        ivy_file.write(Reactions[count-1].reactant2)
        ivy_file.write(")")
        if obj.priority <= 6:
            ivy_file.write(";\n\t\tassert false")
        ivy_file.write("\n\t}\n\n\t")


ivy_file.write("\n\n\tbefore idling {\n\t\tassert idle = 1\n\t}\n}\n")

count = 0
for obj in Reactions:
    count = count + 1
    ivy_file.write("export protocol.update_r")
    ivy_file.write(str(count))
    ivy_file.write("\n")


ivy_file.write("export protocol.idling\nimport goal.achieved\n")

count = 0
for obj in Reactions:
    count= count + 1
    ivy_file.write("import inspector.check_guard_r")
    ivy_file.write(str(count))
    ivy_file.write("\n")

ivy_file.write("\nisolate iso_proto = protocol with enabled_checker, updater, goal, selector, inspector")

ivy_file.close()

import subprocess

ivy_to_cpp_command = subprocess.Popen(["ivy_to_cpp", "isolate=iso_proto", "target=test", "build=true", "test_v2.ivy"])
ivy_to_cpp_command.wait()
import os
print("starting to run randomized testing and store the results")
os.system("./test_v2 >test_v2.txt")
print("finished randomized testing")

reaction_exec_count = []

for x in range(numofreactions):
    reaction_exec_count.append(0)


iters = 0

transitions = 0

tracelist = open("trace_list.txt", "w")

transitionmap = open("reaction_list.txt", "w")

count3 = 0

with open("test_v2.txt", "r") as f:
    count = 0
    while True:
        count3 += 1
        line = f.readline()
        if not line:
            break
        if iters == 0:
            transitionmap.write("Run ")
            transitionmap.write(str(count+1))
            transitionmap.write(":\n\n")
        if line[0] == ">":
            if line[11:17] != "idling":
                iters += 1
        if line[0] == "<":
            if line[2] == "i":
                transitions += 1
                transitionmap.write(line[24:26])
                transitionmap.write("\t")
                tracelist.write(line[24:26])
                tracelist.write("\t")
                reaction_exec_count[int(line[25])-1] += 1
        if line[0] == "t":
            count = count + 1
            transitionmap.write("\n\nRun ")
            transitionmap.write(str(count))
            transitionmap.write(" information\n\nIterations before idling was reached: ")
            transitionmap.write(str(iters))
            transitionmap.write("\nNumber of transitions: ")
            transitionmap.write(str(transitions))
            count2 = 0
            for x in range(numofreactions):
                transitionmap.write("\nr")
                transitionmap.write(str(x+1))
                transitionmap.write("executions: ")
                transitionmap.write(str(reaction_exec_count[x]))
                reaction_exec_count[x] = 0
            transitionmap.write("\n\n\n\n")
            tracelist.write("\n")
            iters = 0
            transitions = 0

print("\nThe traces recorded and the information on those traces are stored in 'reaction_list.txt'")
print("\nThe traces by themselves are found in 'trace_list.txt'")
transitionmap.close()

tracelist.close()
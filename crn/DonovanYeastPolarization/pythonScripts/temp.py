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
for x in range(numofreactions):     #Reads in all the reactions (accepts up to two reactants and two products)
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
        secondProductNum = 0
    else:
        firstproductnum = int(input("What amount of this product is produced (type an integer): "))
        if(firstproductnum == 0):
            print("Error, must be greater than 0, please start over")
            exit()
        secondproduct = input("What is the second product (if no second product type 'NA' or leave blank): ")
        if(secondproduct.lower() == "na" or secondproduct == ""):
            secondproduct = ""
            secondProductNum = 0
        else:
            secondProductNum = int(input("What amount of this product is produced (type an integer): "))
            if (secondProductNum == 0):
                print("Error, must be greater than 0, please start over")
                exit()
    Reactions.append(reaction(firstreactant,firstreactantnum,secondreactant,secondreactantnum,firstproduct,firstproductnum,secondproduct,secondProductNum,15))

print("\n\nThe follwing reactions will be considered in the model:\n")

count = 0
for obj in Reactions: #Prints each of the reactions that have been recorded
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

for obj in Reactions: #adds all the species recorded in the reactions to a list
    if (obj.reactant1 not in spec and obj.reactant1 != ""):
        spec.append(obj.reactant1)
    if (obj.reactant2 not in spec and obj.reactant2 != ""):
        spec.append(obj.reactant2)
    if (obj.product1 not in spec and obj.product1 != ""):
        spec.append(obj.product1)
    if (obj.product2 not in spec and obj.product2 != ""):
        spec.append(obj.product2)

specieslist = []

for obj in spec: #intial value of each species is asked for and recorded
    print("What is the initial value of", obj, "?")
    val = int(input())
    specieslist.append(species(val, obj))

print("The initial values reported are:")

for obj in specieslist: #initial values reported are displayed
    print(obj.name,"=",obj.value)

print("\n")

targetspecies = input("Which species is going to be monitored? ") #target species identified
if(targetspecies not in spec):
    print("Error, species specified not found in the reactions reported please start over")
    exit()
targetnum = input("What is the target number for this species? ") #target number also identified

print("\n\nWhich option is your desired guard?\n\n","1:", targetspecies, ">=", targetnum, "\n 2:", targetspecies, ">", targetnum, "\n 3:", targetspecies, "<=", targetnum,"\n 4:", targetspecies, "<", targetnum,"\n 5:", targetspecies, "=", targetnum) 

upordown = input("\n\n(Please type an integer corresponding to your desired guard):  ")

#guard is chosen

if upordown == "5":
    for obj in specieslist:
        if obj.name == targetspecies:
            if obj.value > int(targetnum):
                upordown = "3"
            elif obj.value < int(targetnum):
                upordown = "1"
            elif obj.value == int(targetnum):
                print("\nSpecified target is already achieved in target state, please start over")
                exit()

for obj in specieslist:
    if obj.name == targetspecies:
        if upordown == "1":
            if obj.value >= int(targetnum):
                print("\nSpecified target is already achieved in target state, please start over")
                exit()
        elif upordown == "2":
            if obj.value > int(targetnum):
                print("\nSpecified target is already achieved in target state, please start over")
                exit()
        elif upordown == "3":
            if obj.value <= int(targetnum):
                print("\nSpecified target is already achieved in target state, please start over")
                exit()
        elif upordown == "4":
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
if upordown == "1" or upordown == "2": #reactions that directly affect the target species have 10 added or subtracted from their priority
    for obj in Reactions:
        if obj.product1 == targetspecies or obj.product2 == targetspecies:
            obj.priority = obj.priority + 10
        elif obj.reactant1 == targetspecies or obj.reactant2 == targetspecies:
            obj.priority = obj.priority - 10
elif upordown == "3" or upordown == "4":
    for obj in Reactions:
        if obj.product1 == targetspecies or obj.product2 == targetspecies:
            obj.priority = obj.priority - 10
        elif obj.reactant1 == targetspecies or obj.reactant2 == targetspecies:
            obj.priority = obj.priority + 10


for obj in Reactions:       #secondary target species identified and added to a list of secondary target species, also given min_amount value (amount needed for reaction to fire enough times to get to target state)
    if upordown == "1" or upordown == "2":
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
    elif upordown == "3" or upordown== "4":
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
            
 
for obj in Reactions:          #every reaction that consumes a secondary target has its priority modified
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

        
for obj in Reactions:       #every reaction that produces a secondary target has its priority modified
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
for obj in Reactions: #each reactions priority is displayed
    count = count + 1
    print("reaction", str(count), ":", str(obj.priority))

ivy_file = open("test_v2.ivy", "w") #an ivy model for the CRN is made to have assertion failure at first idling action

ivy_file.write("#lang ivy 1.7\n\nobject updater = {\n")
ivy_file.write("\ttype num\n\tinterpret num -> bv[10]\n\ttype exec_var\n\tinterpret exec_var -> bv[8]\n\ttype exec_stage\n\tinterpret exec_stage -> bv[3]\n\n\taction incr(x:num) returns(y:num) = {\n\t\ty := x + 1\n\t}\n\n\taction decr(x:num) returns(y:num) = {\n\t\ty := x - 1\n\t}\n}")
ivy_file.write("\n\nobject goal = {\n\taction achieved(v:updater.num)\n\tobject spec = {\n\t\tbefore achieved {\n\t\t\tassert v ")
if upordown == "1":
    ivy_file.write(">= ")
elif upordown == "2":
    ivy_file.write("> ")
elif upordown == "3":
    ivy_file.write("<= ")
elif upordown == "4":
    ivy_file.write("< ")
ivy_file.write(targetnum)
ivy_file.write(";\n\t\t\tprotocol.idle := 1\n\t\t}\n\t}\n}\n\n")

ivy_file.write("object enabled_checker = {\n\n\t")

count = 0
for obj in Reactions:
    count += 1
    if obj.priority > 15:
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
    if obj.priority > 15:
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
    if obj.priority > 15:
        ivy_file.write("individual r")
        ivy_file.write(str(count))
        ivy_file.write("_exec : updater.exec_var\n\t")

ivy_file.write("\n\t")
count = 0

for obj in Reactions:
    count = count + 1
    if obj.priority > 15:
        ivy_file.write("individual r")
        ivy_file.write(str(count))
        ivy_file.write("_rate : updater.exec_var\n\t")

ivy_file.write("\n\t")

count = 0
for obj in Reactions:
    count = count + 1
    if obj.priority > 15:
        ivy_file.write("individual r")
        ivy_file.write(str(count))
        ivy_file.write("_count : updater.exec_var\n\t")

ivy_file.write("\n\t")

count = 0
for obj in Reactions:
    count = count + 1
    if obj.priority > 15:
        ivy_file.write("individual r")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate : updater.exec_var\n\t")

ivy_file.write("\n\t")

count = 0
for obj in Reactions:
    count = count + 1
    if obj.priority > 15:
        ivy_file.write("individual r")
        ivy_file.write(str(count))
        ivy_file.write("_stage : updater.exec_stage\n\t")

ivy_file.write("\n\n\tafter init {\n\t\t")

count = 0
for obj in Reactions:
    count = count + 1
    if obj.priority > 15:
        ivy_file.write("r")
        ivy_file.write(str(count))
        ivy_file.write("_count := 0")
        ivy_file.write(";\n\t\t")

ivy_file.write("\n\n\t\t")
count = 0
for obj in Reactions:
    count = count + 1
    if obj.priority > 15:
        ivy_file.write("r")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 4")
        ivy_file.write(";\n\t\t")

ivy_file.write("\n\t}\n\n\t")

count = 0
for obj in Reactions:
    count = count + 1
    if obj.priority > 15:
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
        if obj.priority >= 23:
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
        elif obj.priority >= 21:
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
        elif obj.priority >= 19:
            ivy_file.write("if r")
            ivy_file.write(str(count))
            ivy_file.write("_stage = 0 {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_count_rate := 3;\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_rate := 4\n\t\t}\n\t\t")
            ivy_file.write("else if r")
            ivy_file.write(str(count))
            ivy_file.write("_stage = 1 {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_count_rate := 4;\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_rate := 5\n\t\t}\n\t\t")
            ivy_file.write("else if r")
            ivy_file.write(str(count))
            ivy_file.write("_stage = 2 {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_count_rate := 2;\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_rate := 6\n\t\t}\n\t\t")
            ivy_file.write("else if r")
            ivy_file.write(str(count))
            ivy_file.write("_stage = 3 {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_count_rate := 4;\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_rate := 4\n\t\t}\n\t\t")
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
            ivy_file.write("_rate := 4\n\t\t}\n\t\t")
            ivy_file.write("else if r")
            ivy_file.write(str(count))
            ivy_file.write("_stage = 6 {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_count_rate := 1;\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_rate := 3\n\t\t}\n\t\t")
            ivy_file.write("else if r")
            ivy_file.write(str(count))
            ivy_file.write("_stage = 7 {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_count_rate := 4;\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_rate := 5\n\t\t}\n\t\telse {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_stage := 0\n\t\t}\n\t}\n\n\t")
        elif obj.priority == 18:
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
        elif obj.priority == 17:
            ivy_file.write("if r")
            ivy_file.write(str(count))
            ivy_file.write("_stage = 0 {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_count_rate := 1;\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_rate := 200\n\t\t}\n\t\t")
            ivy_file.write("else if r")
            ivy_file.write(str(count))
            ivy_file.write("_stage = 1 {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_count_rate := 3;\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_rate := 189\n\t\t}\n\t\t")
            ivy_file.write("else if r")
            ivy_file.write(str(count))
            ivy_file.write("_stage = 2 {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_count_rate := 2;\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_rate := 192\n\t\t}\n\t\t")
            ivy_file.write("else if r")
            ivy_file.write(str(count))
            ivy_file.write("_stage = 3 {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_count_rate := 9;\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_rate := 212\n\t\t}\n\t\t")
            ivy_file.write("else if r")
            ivy_file.write(str(count))
            ivy_file.write("_stage = 4 {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_count_rate := 4;\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_rate := 192\n\t\t}\n\t\t")
            ivy_file.write("else if r")
            ivy_file.write(str(count))
            ivy_file.write("_stage = 5 {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_count_rate := 4;\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_rate := 232\n\t\t}\n\t\t")
            ivy_file.write("else if r")
            ivy_file.write(str(count))
            ivy_file.write("_stage = 6 {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_count_rate := 5;\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_rate := 190\n\t\t}\n\t\t")
            ivy_file.write("else if r")
            ivy_file.write(str(count))
            ivy_file.write("_stage = 7 {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_count_rate := 3;\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_rate := 200\n\t\t}\n\t\telse {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_stage := 0\n\t\t}\n\t}\n\n\t")
        elif obj.priority == 16:
            ivy_file.write("if r")
            ivy_file.write(str(count))
            ivy_file.write("_stage = 0 {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_count_rate := 5;\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_rate := 1000\n\t\t}\n\t\t")
            ivy_file.write("else if r")
            ivy_file.write(str(count))
            ivy_file.write("_stage = 1 {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_count_rate := 3;\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_rate := 989\n\t\t}\n\t\t")
            ivy_file.write("else if r")
            ivy_file.write(str(count))
            ivy_file.write("_stage = 2 {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_count_rate := 2;\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_rate := 1190\n\t\t}\n\t\t")
            ivy_file.write("else if r")
            ivy_file.write(str(count))
            ivy_file.write("_stage = 3 {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_count_rate := 9;\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_rate := 1053\n\t\t}\n\t\t")
            ivy_file.write("else if r")
            ivy_file.write(str(count))
            ivy_file.write("_stage = 4 {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_count_rate := 4;\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_rate := 942\n\t\t}\n\t\t")
            ivy_file.write("else if r")
            ivy_file.write(str(count))
            ivy_file.write("_stage = 5 {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_count_rate := 2;\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_rate := 1022\n\t\t}\n\t\t")
            ivy_file.write("else if r")
            ivy_file.write(str(count))
            ivy_file.write("_stage = 6 {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_count_rate := 5;\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_rate := 930\n\t\t}\n\t\t")
            ivy_file.write("else if r")
            ivy_file.write(str(count))
            ivy_file.write("_stage = 7 {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_count_rate := 1;\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_rate := 1000\n\t\t}\n\t\telse {\n\t\t\tr")
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
    if obj.priority > 15:
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
                if upordown == "1":
                    ivy_file.write(" >= ")
                elif upordown == "2":
                    ivy_file.write(" > ")
                elif upordown == "3":
                    ivy_file.write(" <= ")
                elif upordown == "4":
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
                if upordown == "1":
                    ivy_file.write(" >= ")
                elif upordown == "2":
                    ivy_file.write(" > ")
                elif upordown == "3":
                    ivy_file.write(" <= ")
                elif upordown == "4":
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
                if upordown == "1":
                    ivy_file.write(" >= ")
                elif upordown == "2":
                    ivy_file.write(" > ")
                elif upordown == "3":
                    ivy_file.write(" <= ")
                elif upordown == "4":
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
                if upordown == "1":
                    ivy_file.write(" >= ")
                elif upordown == "2":
                    ivy_file.write(" > ")
                elif upordown == "3":
                    ivy_file.write(" <= ")
                elif upordown == "4":
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
                if upordown == "1":
                    ivy_file.write(" >= ")
                elif upordown == "2":
                    ivy_file.write(" > ")
                elif upordown == "3":
                    ivy_file.write(" <= ")
                elif upordown == "4":
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
                if upordown == "1":
                    ivy_file.write(" >= ")
                elif upordown == "2":
                    ivy_file.write(" > ")
                elif upordown == "3":
                    ivy_file.write(" <= ")
                elif upordown == "4":
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
                if upordown == "1":
                    ivy_file.write(" >= ")
                elif upordown == "2":
                    ivy_file.write(" > ")
                elif upordown == "3":
                    ivy_file.write(" <= ")
                elif upordown == "4":
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
                if upordown == "1":
                    ivy_file.write(" >= ")
                elif upordown == "2":
                    ivy_file.write(" > ")
                elif upordown == "3":
                    ivy_file.write(" <= ")
                elif upordown == "4":
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
    if obj.priority > 15:
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


ivy_file.write("\n\n\tbefore idling {\n\t\tassert idle = 1\n\t}")#\n}\n")

ivy_file.write("\n\n\tafter idling {\n\t\tassert idle = 0\n\t}\n}\n") #this causes assertion failure for the first run

count = 0
for obj in Reactions:
    count = count + 1
    if obj.priority > 15:
        ivy_file.write("export protocol.update_r")
        ivy_file.write(str(count))
        ivy_file.write("\n")


ivy_file.write("export protocol.idling\nimport goal.achieved\n")

count = 0
for obj in Reactions:
    count= count + 1
    if obj.priority > 15:
        ivy_file.write("import inspector.check_guard_r")
        ivy_file.write(str(count))
        ivy_file.write("\n")

ivy_file.write("\nisolate iso_proto = protocol with enabled_checker, updater, goal, selector, inspector")

ivy_file.close()        #ivy model complete

#quit = input("Should we be done now?")

#if quit == "y":
#    exit()

"""

import subprocess

ivy_to_cpp_command = subprocess.Popen(["ivy_to_cpp", "isolate=iso_proto", "target=test", "build=true", "test_v2.ivy"])
ivy_to_cpp_command.wait()
import os
print("starting to run initial test")
os.system("./test_v2 seed=367 iters=10000000 runs=1 >test_v2.txt")
print("finished initial test") #test is run and results are stored in test_v2.txt

first_iters = 0

with open("test_v2.txt", "r") as f: #The amount of iters needed to reach the goal in the first example is recorded
    count = 0
    while True:
        line = f.readline()
        if not line:
            break
        if line[0] == ">":
            if line[11:17] != "idling":
                first_iters += 1

if first_iters >= 10000:
    print("Trace not found to specified target from randomized testing")
    exit()

print("The iters recorded for this initial example is", first_iters)

######
"""
ivy_file = open("test_v2.ivy", "w") #another ivy model is created that will not have assertion failure

ivy_file.write("#lang ivy 1.7\n\nobject updater = {\n")
ivy_file.write("\ttype num\n\tinterpret num -> bv[10]\n\ttype exec_var\n\tinterpret exec_var -> bv[8]\n\ttype exec_stage\n\tinterpret exec_stage -> bv[3]\n\n\taction incr(x:num) returns(y:num) = {\n\t\ty := x + 1\n\t}\n\n\taction decr(x:num) returns(y:num) = {\n\t\ty := x - 1\n\t}\n}")
ivy_file.write("\n\nobject goal = {\n\taction achieved(v:updater.num)\n\tobject spec = {\n\t\tbefore achieved {\n\t\t\tassert v ")
if upordown == "1":
    ivy_file.write(">= ")
elif upordown == "2":
    ivy_file.write("> ")
elif upordown == "3":
    ivy_file.write("<= ")
elif upordown == "4":
    ivy_file.write("< ")
ivy_file.write(targetnum)
ivy_file.write(";\n\t\t\tprotocol.idle := 1\n\t\t}\n\t}\n}\n\n")

ivy_file.write("object enabled_checker = {\n\n\t")

count = 0
for obj in Reactions:
    count += 1
    if obj.priority > 15:
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
    if obj.priority > 15:
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
    if obj.priority > 15:
        ivy_file.write("individual r")
        ivy_file.write(str(count))
        ivy_file.write("_exec : updater.exec_var\n\t")

ivy_file.write("\n\t")
count = 0

for obj in Reactions:
    count = count + 1
    if obj.priority > 15:
        ivy_file.write("individual r")
        ivy_file.write(str(count))
        ivy_file.write("_rate : updater.exec_var\n\t")

ivy_file.write("\n\t")

count = 0
for obj in Reactions:
    count = count + 1
    if obj.priority > 15:
        ivy_file.write("individual r")
        ivy_file.write(str(count))
        ivy_file.write("_count : updater.exec_var\n\t")

ivy_file.write("\n\t")

count = 0
for obj in Reactions:
    count = count + 1
    if obj.priority > 15:
        ivy_file.write("individual r")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate : updater.exec_var\n\t")

ivy_file.write("\n\t")

count = 0
for obj in Reactions:
    count = count + 1
    if obj.priority > 15:
        ivy_file.write("individual r")
        ivy_file.write(str(count))
        ivy_file.write("_stage : updater.exec_stage\n\t")

ivy_file.write("\n\n\tafter init {\n\t\t")

count = 0
for obj in Reactions:
    count = count + 1
    if obj.priority > 15:
        ivy_file.write("r")
        ivy_file.write(str(count))
        ivy_file.write("_count := 0")
        ivy_file.write(";\n\t\t")

ivy_file.write("\n\n\t\t")
count = 0
for obj in Reactions:
    count = count + 1
    if obj.priority > 15:
        ivy_file.write("r")
        ivy_file.write(str(count))
        ivy_file.write("_count_rate := 4")
        ivy_file.write(";\n\t\t")

ivy_file.write("\n\t}\n\n\t")

count = 0
for obj in Reactions:
    count = count + 1
    if obj.priority > 15:
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
        if obj.priority >= 23:
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
        elif obj.priority >= 21:
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
        elif obj.priority >= 19:
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
        elif obj.priority == 18:
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
            ivy_file.write("_rate := 5\n\t\t}\n\t\t")
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
            ivy_file.write("_rate := 4\n\t\t}\n\t\t")
            ivy_file.write("else if r")
            ivy_file.write(str(count))
            ivy_file.write("_stage = 5 {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_count_rate := 3;\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_rate := 5\n\t\t}\n\t\t")
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
            ivy_file.write("_rate := 4\n\t\t}\n\t\telse {\n\t\t\tr")
            ivy_file.write(str(count))
            ivy_file.write("_stage := 0\n\t\t}\n\t}\n\n\t")
        elif obj.priority == 17:
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
        elif obj.priority == 16:
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

count = 0
for obj in Reactions:
    count = count + 1
    if obj.priority > 15:
        ivy_file.write("\tindividual r")
        ivy_file.write(str(count))
        ivy_file.write("_executions : updater.num\n")

ivy_file.write("\n\tafter init {\n\t\t")

for obj in specieslist:
    ivy_file.write("r_")
    ivy_file.write(obj.name)
    ivy_file.write(" := ")
    ivy_file.write(str(obj.value))
    ivy_file.write(";\n\t\t")

count = 0
for obj in Reactions:
    count = count + 1
    if obj.priority > 15:
        ivy_file.write("r")
        ivy_file.write(str(count))
        ivy_file.write("_executions := 0;\n\t\t")

ivy_file.write("idle := 0\n\t}\n\n\t")

count = 0
for obj in Reactions:
    count = count + 1
    if obj.priority > 15:
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
                if upordown == "1":
                    ivy_file.write(" >= ")
                elif upordown == "2":
                    ivy_file.write(" > ")
                elif upordown == "3":
                    ivy_file.write(" <= ")
                elif upordown == "4":
                    ivy_file.write(" < ")
                ivy_file.write(str(targetnum))
                ivy_file.write(" {\n\t\t\t\tcall goal.achieved(")
                ivy_file.write("r_")
                ivy_file.write(targetspecies)
                ivy_file.write(")\n\t\t\t}\n\t\t")
            else:
                ivy_file.write(";\n\t\t\tr")
                ivy_file.write(str(count))
                ivy_file.write("_executions := updater.incr(r")
                ivy_file.write(str(count))
                ivy_file.write("_executions)")
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
                if upordown == "1":
                    ivy_file.write(" >= ")
                elif upordown == "2":
                    ivy_file.write(" > ")
                elif upordown == "3":
                    ivy_file.write(" <= ")
                elif upordown == "4":
                    ivy_file.write(" < ")
                ivy_file.write(str(targetnum))
                ivy_file.write(" {\n\t\t\t\tcall goal.achieved(")
                ivy_file.write("r_")
                ivy_file.write(targetspecies)
                ivy_file.write(")\n\t\t\t}\n\t\t")
            else:
                ivy_file.write(";\n\t\t\tr")
                ivy_file.write(str(count))
                ivy_file.write("_executions := updater.incr(r")
                ivy_file.write(str(count))
                ivy_file.write("_executions)")
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
                if upordown == "1":
                    ivy_file.write(" >= ")
                elif upordown == "2":
                    ivy_file.write(" > ")
                elif upordown == "3":
                    ivy_file.write(" <= ")
                elif upordown == "4":
                    ivy_file.write(" < ")
                ivy_file.write(str(targetnum))
                ivy_file.write(" {\n\t\t\t\tcall goal.achieved(")
                ivy_file.write("r_")
                ivy_file.write(targetspecies)
                ivy_file.write(")\n\t\t\t}\n\t\t")
            else:
                ivy_file.write(";\n\t\t\tr")
                ivy_file.write(str(count))
                ivy_file.write("_executions := updater.incr(r")
                ivy_file.write(str(count))
                ivy_file.write("_executions)")
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
                if upordown == "1":
                    ivy_file.write(" >= ")
                elif upordown == "2":
                    ivy_file.write(" > ")
                elif upordown == "3":
                    ivy_file.write(" <= ")
                elif upordown == "4":
                    ivy_file.write(" < ")
                ivy_file.write(str(targetnum))
                ivy_file.write(" {\n\t\t\t\tcall goal.achieved(")
                ivy_file.write("r_")
                ivy_file.write(targetspecies)
                ivy_file.write(")\n\t\t\t}\n\t\t")
            else:
                ivy_file.write(";\n\t\t\tr")
                ivy_file.write(str(count))
                ivy_file.write("_executions := updater.incr(r")
                ivy_file.write(str(count))
                ivy_file.write("_executions)")
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
                if upordown == "1":
                    ivy_file.write(" >= ")
                elif upordown == "2":
                    ivy_file.write(" > ")
                elif upordown == "3":
                    ivy_file.write(" <= ")
                elif upordown == "4":
                    ivy_file.write(" < ")
                ivy_file.write(str(targetnum))
                ivy_file.write(" {\n\t\t\t\tcall goal.achieved(")
                ivy_file.write("r_")
                ivy_file.write(targetspecies)
                ivy_file.write(")\n\t\t\t}\n\t\t")
            else:
                ivy_file.write(";\n\t\t\tr")
                ivy_file.write(str(count))
                ivy_file.write("_executions := updater.incr(r")
                ivy_file.write(str(count))
                ivy_file.write("_executions)")
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
                if upordown == "1":
                    ivy_file.write(" >= ")
                elif upordown == "2":
                    ivy_file.write(" > ")
                elif upordown == "3":
                    ivy_file.write(" <= ")
                elif upordown == "4":
                    ivy_file.write(" < ")
                ivy_file.write(str(targetnum))
                ivy_file.write(" {\n\t\t\t\tcall goal.achieved(")
                ivy_file.write("r_")
                ivy_file.write(targetspecies)
                ivy_file.write(")\n\t\t\t}\n\t\t")
            else:
                ivy_file.write(";\n\t\t\tr")
                ivy_file.write(str(count))
                ivy_file.write("_executions := updater.incr(r")
                ivy_file.write(str(count))
                ivy_file.write("_executions)")
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
                if upordown == "1":
                    ivy_file.write(" >= ")
                elif upordown == "2":
                    ivy_file.write(" > ")
                elif upordown == "3":
                    ivy_file.write(" <= ")
                elif upordown == "4":
                    ivy_file.write(" < ")
                ivy_file.write(str(targetnum))
                ivy_file.write(" {\n\t\t\t\tcall goal.achieved(")
                ivy_file.write("r_")
                ivy_file.write(targetspecies)
                ivy_file.write(")\n\t\t\t}\n\t\t")
            else:
                ivy_file.write(";\n\t\t\tr")
                ivy_file.write(str(count))
                ivy_file.write("_executions := updater.incr(r")
                ivy_file.write(str(count))
                ivy_file.write("_executions)")
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
                if upordown == "1":
                    ivy_file.write(" >= ")
                elif upordown == "2":
                    ivy_file.write(" > ")
                elif upordown == "3":
                    ivy_file.write(" <= ")
                elif upordown == "4":
                    ivy_file.write(" < ")
                ivy_file.write(str(targetnum))
                ivy_file.write(" {\n\t\t\t\tcall goal.achieved(")
                ivy_file.write("r_")
                ivy_file.write(targetspecies)
                ivy_file.write(")\n\t\t\t}\n\t\t")
            else:
                ivy_file.write(";\n\t\t\tr")
                ivy_file.write(str(count))
                ivy_file.write("_executions := updater.incr(r")
                ivy_file.write(str(count))
                ivy_file.write("_executions)")
                ivy_file.write("\n\t\t")
            ivy_file.write("}\n\t}\n\n\t")

ivy_file.write("\n\n\taction idling = {}\n\n\t")
count = 0
for obj in Reactions:
    count = count + 1
    if obj.priority > 15:
        ivy_file.write("before update_r")
        ivy_file.write(str(count))
        if (Reactions[count-1].reactant1 == ""):
            ivy_file.write(" {\n\t\tassert idle = 0;\n\t\tassert enabled_checker.is_enabled_r")
            ivy_file.write(str(count))
            count1 = 0
            count2 = 0
            if obj.priority <= 17:
                ivy_file.write(";\n\t\tassert false")
            if obj.priority < 25:
                for y in Reactions:
                    count1 += 1
                    if y.priority > 15 and y.priority < 25:
                        count2 += 1
                        if count2 == 1:
                            ivy_file.write(";\n\t\tassert (r")
                            ivy_file.write(str(count1))
                            ivy_file.write("_executions")
                            ivy_file.write(" * ")
                            for x in secondtargetlist:
                                if y.product1 == x.name:
                                    ivy_file.write(str(y.product1num))
                                elif y.product2 == x.name:
                                    ivy_file.write(str(y.product2num))
                        if count2 >= 2:
                            ivy_file.write(" + r")
                            ivy_file.write(str(count1))
                            ivy_file.write("_executions")
                            ivy_file.write(" * ")
                            for x in secondtargetlist:
                                if y.product1 == x.name:
                                    ivy_file.write(str(y.product1num))
                                elif y.product2 == x.name:
                                    ivy_file.write(str(y.product2num))
                    if count1 == numofreactions:
                        ivy_file.write(") < ")
                        for x in secondtargetlist:
                            if x.name == obj.product1 or x.name == obj.product2:
                                ivy_file.write(str(x.min_amount)) #this needs to modified to be universal
                if obj.priority <= 17:
                    ivy_file.write(";\n\t\tassert false")
            ivy_file.write("\n\t}\n\t")
        elif(Reactions[count-1].reactant1 != "" and Reactions[count-1].reactant2 == ""):
            ivy_file.write(" {\n\t\tassert idle = 0;\n\t\tassert enabled_checker.is_enabled_r")
            ivy_file.write(str(count))
            ivy_file.write("(")
            ivy_file.write("r_")
            ivy_file.write(Reactions[count-1].reactant1)
            ivy_file.write(")")
            count1 = 0
            count2 = 0
            if obj.priority <= 17:
                ivy_file.write(";\n\t\tassert false")
            if obj.priority < 25:
                for y in Reactions:
                    count1 += 1
                    if y.priority > 15 and y.priority < 25:
                        count2 += 1
                        if count2 == 1:
                            ivy_file.write(";\n\t\tassert (r")
                            ivy_file.write(str(count1))
                            ivy_file.write("_executions")
                            ivy_file.write(" * ")
                            for x in secondtargetlist:
                                if y.product1 == x.name:
                                    ivy_file.write(str(y.product1num))
                                elif y.product2 == x.name:
                                    ivy_file.write(str(y.product2num))
                        if count2 >= 2:
                            ivy_file.write(" + r")
                            ivy_file.write(str(count1))
                            ivy_file.write("_executions")
                            ivy_file.write(" * ")
                            for x in secondtargetlist:
                                if y.product1 == x.name:
                                    ivy_file.write(str(y.product1num))
                                elif y.product2 == x.name:
                                    ivy_file.write(str(y.product2num))
                    if count1 == numofreactions:
                        ivy_file.write(") < ")
                        for x in secondtargetlist:
                            if x.name == obj.product1 or x.name == obj.product2:
                                ivy_file.write(str(x.min_amount)) #this needs to modified to be universal
                if obj.priority <= 17:
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
            count1 = 0
            count2 = 0
            if obj.priority <= 17:
                ivy_file.write(";\n\t\tassert false")
            if obj.priority < 25:
                for y in Reactions:
                    count1 += 1
                    if y.priority > 15 and y.priority < 25:
                        count2 += 1
                        if count2 == 1:
                            ivy_file.write(";\n\t\tassert (r")
                            ivy_file.write(str(count1))
                            ivy_file.write("_executions")
                            ivy_file.write(" * ")
                            for x in secondtargetlist:
                                if y.product1 == x.name:
                                    ivy_file.write(str(y.product1num))
                                elif y.product2 == x.name:
                                    ivy_file.write(str(y.product2num))
                        if count2 >= 2:
                            ivy_file.write(" + r")
                            ivy_file.write(str(count1))
                            ivy_file.write("_executions")
                            ivy_file.write(" * ")
                            for x in secondtargetlist:
                                if y.product1 == x.name:
                                    ivy_file.write(str(y.product1num))
                                elif y.product2 == x.name:
                                    ivy_file.write(str(y.product2num))
                    if count1 == numofreactions:
                        ivy_file.write(") < ")
                        for x in secondtargetlist:
                            if x.name == obj.product1 or x.name == obj.product2:
                                ivy_file.write(str(x.min_amount)) #this needs to modified to be universal
                if obj.priority <= 17:
                    ivy_file.write(";\n\t\tassert false")
            ivy_file.write("\n\t}\n\n\t")


ivy_file.write("\n\n\tbefore idling {\n\t\tassert idle = 1\n\t}\n}\n")

#ivy_file.write("\n\n\tafter idling {\n\t\tassert idle = 0\n\t}\n}\n") #this causes assertion failure for the first run

count = 0
for obj in Reactions:
    count = count + 1
    if obj.priority > 15:
        ivy_file.write("export protocol.update_r")
        ivy_file.write(str(count))
        ivy_file.write("\n")


ivy_file.write("export protocol.idling\nimport goal.achieved\n")

count = 0
for obj in Reactions:
    count= count + 1
    if obj.priority > 15:
        ivy_file.write("import inspector.check_guard_r")
        ivy_file.write(str(count))
        ivy_file.write("\n")

ivy_file.write("\nisolate iso_proto = protocol with enabled_checker, updater, goal, selector, inspector")

ivy_file.close()        #ivy model complete

"""
import subprocess

ivy_to_cpp_command = subprocess.Popen(["ivy_to_cpp", "isolate=iso_proto", "target=test", "build=true", "test_v2.ivy"])
ivy_to_cpp_command.wait()
import os

runswanted = input("How many traces do you want to the target specified? (Type an integer greater than 0): ") #Amount of traces desired is recorded

print("starting to run rest of tests")
firsthalf = "./test_v2 iters="
middle = str(first_iters*1.25)
middle2 = " runs="
secondhalf = " >test_v2.txt"
firstpart = firsthalf + middle + middle2 + runswanted
fullstring = firstpart + secondhalf
print(fullstring)
os.system(fullstring)
print("finished randomized testing")#More tests run with twice the amount of iters needed for the first test, for the specified number of traces wanted by the user

reaction_exec_count = []

for x in range(numofreactions):
    reaction_exec_count.append(0)


iters = 0

transitions = 0

tracelist = open("trace_list.txt", "w") #The traces by themselves are recorded in 'trace_list.txt'

transitionmap = open("reaction_list.txt", "w")  #The traces and additional information is stored in 'reactoin_list.txt'

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
                if iters == first_iters * 2:
                    print("Error!\tRun", count+1, "did not reach the target state\n")
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

with open("reaction_list.txt", "r") as f:
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

print("\n\nAverage number of transitions in a trace is:", Totaltran/int(runswanted))
print("\nThe biggest number of transitions recorded in a trace is:", max(Totaltranlist))
print("\nThe smallest number of transitions recorded in a trace is:", min(Totaltranlist))
print("\n\nAverage number of iterations needed in a trace is:", Totaliter/int(runswanted))
print("\nThe biggest number of iterations needed for a trace was:", max(Totaliterlist))
print("\nThe smallest number of iterations needed for a trace was:", min(Totaliterlist))

for x in range(numofreactions):
    print("\n\nAverage number of reaction", x+1, "executions in a trace is:", Total[x]/int(runswanted))
    print("\nThe biggest number of reaction", x+1, "executions recorded in a trace is:", max(iterations[x]))
    print("\nThe smallest number of reaction", x+1, "executions recorded in a trace is:", min(iterations[x]))

"""
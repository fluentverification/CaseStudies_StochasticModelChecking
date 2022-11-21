numOfReactions = int(input("Number of reactions: "))

class reaction:
    def __init__(self, reactant1, reactant1Num, reactant2, reactant2Num, product1, product1Num, product2, product2Num, priority):
        self.reactant1 = reactant1
        self.reactant1Num = reactant1Num
        self.reactant2 = reactant2
        self.reactant2Num = reactant2Num
        self.product1 = product1
        self.product1Num = product1Num
        self.product2 = product2
        self.product2Num = product2Num
        self.priority = priority

class species:
    def __init__(self, value, name):
        self.value = value
        self.name = name

class SecondTarget:
    def __init__(self, name, minAmount):
        self.name = name
        self.minAmount = minAmount

Reactions = []
for x in range(numOfReactions):     #Reads in all the reactions (accepts up to two reactants and two products)
    print("\n\n","reaction",x+1, ": \n")
    firstReactant = input("What is the first reactant (if no reactants type 'NA' or leave blank): ")
    if(firstReactant.lower() == "na" or firstReactant == ""):
        firstReactant = ""
        firstReactantNum = 0
        secondReactant = ""
        secondReactantNum = 0
    else:
        firstReactantNum = int(input("What amount of this reactant is needed (type an integer): "))
        if (firstReactantNum == 0):
            print("Error, must be greater than 0, please start over")
            exit()
        secondReactant = input("What is the second reactant (if no second reactant type 'NA' or leave blank): ")
        if(secondReactant.lower() == "na" or secondReactant == ""):
            secondReactant = ""
            secondReactantNum = 0
        else:
            secondReactantNum = int(input("What amount of this reactant is needed (type an integer): "))
            if (secondReactantNum == 0):
                print("Error, must be greater than 0, please start over")
                exit()
    firstProduct = input("What is the first product (if no products type 'NA' or leave blank): ")
    if(firstProduct.lower() == "na" or firstProduct == ""):
        if(firstReactant == ""):
            print("Error, this reaction has no reactants or products please start over")
            exit()
        firstProduct = ""
        firstProductNum = 0
        secondProduct = ""
        secondProductNum = 0
    else:
        firstProductNum = int(input("What amount of this product is produced (type an integer): "))
        if(firstProductNum == 0):
            print("Error, must be greater than 0, please start over")
            exit()
        secondProduct = input("What is the second product (if no second product type 'NA' or leave blank): ")
        if(secondProduct.lower() == "na" or secondProduct == ""):
            secondProduct = ""
            secondProductNum = 0
        else:
            secondProductNum = int(input("What amount of this product is produced (type an integer): "))
            if (secondProductNum == 0):
                print("Error, must be greater than 0, please start over")
                exit()
    Reactions.append(reaction(firstReactant,firstReactantNum,secondReactant,secondReactantNum,firstProduct,firstProductNum,secondProduct,secondProductNum,15))

print("\n\nThe follwing reactions will be considered in the model:\n")

count = 0
for obj in  reactions: #Prints each of the reactions that have been recorded
    count = count + 1
    if (obj.reactant1Num >= 1 and obj.reactant2Num >= 1 and obj.product1Num >= 1 and obj.product2Num >= 1):
        print(str(count),": ",obj.reactant1Num,obj.reactant1," + ",obj.reactant2Num, obj.reactant2," -> ", obj.product1Num,obj.product1," + ", obj.product2Num,obj.product2)
    elif (obj.reactant1Num >= 1 and obj.reactant2Num == 0 and obj.product1Num >= 1 and obj.product2Num >= 1):
        print(str(count),": ",obj.reactant1Num,obj.reactant1," -> ",obj.product1Num, obj.product1," + ", obj.product2Num, obj.product2)
    elif (obj.reactant1Num >= 1 and obj.reactant2Num == 0 and obj.product1Num >= 1 and obj.product2Num == 0):
        print(str(count),": ",obj.reactant1Num,obj.reactant1," -> ", obj.product1Num, obj.product1)
    elif (obj.reactant1Num >= 1 and obj.reactant2Num >= 1 and obj.product1Num >= 1 and obj.product2Num == 0):
        print(str(count),": ",obj.reactant1Num,obj.reactant1," + ",obj.reactant2Num, obj.reactant2," -> ", obj.product1Num,obj.product1)
    elif (obj.reactant1Num == 0 and obj.product1Num >= 1 and obj.product2Num == 0):
        print(str(count),": ","NULL"," -> ",obj.product1Num, obj.product1)
    elif (obj.reactant1Num >= 1 and obj.reactant2Num == 0 and obj.product1Num == 0):
        print(str(count),": ",obj.reactant1Num, obj.reactant1," -> ", "NULL")
    elif (obj.reactant1Num >= 1 and obj.reactant2Num >= 1 and obj.product1Num == 0):
        print(str(count),": ",obj.reactant1Num,obj.reactant1," + ",obj.reactant2Num,obj.reactant2," ->  NULL")
    elif (obj.reactant1Num == 0 and obj.product1Num >= 1 and obj.product2Num >= 1):
        print(str(count),": ","NULL  -> ",obj.product1Num,obj.product1," + ",obj.product2Num,obj.product2)

print("\n")
spec = []

for obj in  reactions: #adds all the species recorded in the reactions to a list
    if (obj.reactant1 not in spec and obj.reactant1 != ""):
        spec.append(obj.reactant1)
    if (obj.reactant2 not in spec and obj.reactant2 != ""):
        spec.append(obj.reactant2)
    if (obj.product1 not in spec and obj.product1 != ""):
        spec.append(obj.product1)
    if (obj.product2 not in spec and obj.product2 != ""):
        spec.append(obj.product2)

speciesList = []

for obj in spec: #intial value of each species is asked for and recorded
    print("What is the initial value of", obj, "?")
    val = int(input())
    speciesList.append(species(val, obj))

print("The initial values reported are:")

for obj in speciesList: #initial values reported are displayed
    print(obj.name,"=",obj.value)

print("\n")

targetSpecies = input("Which species is going to be monitored? ") #target species identified
if(targetSpecies not in spec):
    print("Error, species specified not found in the reactions reported please start over")
    exit()
targetNum = input("What is the target number for this species? ") #target number also identified

print("\n\nWhich option is your desired guard?\n\n","1:", targetSpecies, ">=", targetNum, "\n 2:", targetSpecies, ">", targetNum, "\n 3:", targetSpecies, "<=", targetNum,"\n 4:", targetSpecies, "<", targetNum,"\n 5:", targetSpecies, "=", targetNum) 

upOrDown = input("\n\n(Please type an integer corresponding to your desired guard):  ")

#guard is chosen

if upOrDown == "5":
    for obj in speciesList:
        if obj.name == targetSpecies:
            if obj.value > int(targetNum):
                upOrDown = "3"
            elif obj.value < int(targetNum):
                upOrDown = "1"
            elif obj.value == int(targetNum):
                print("\nSpecified target is already achieved in target state, please start over")
                exit()

for obj in speciesList:
    if obj.name == targetSpecies:
        if upOrDown == "1":
            if obj.value >= int(targetNum):
                print("\nSpecified target is already achieved in target state, please start over")
                exit()
        elif upOrDown == "2":
            if obj.value > int(targetNum):
                print("\nSpecified target is already achieved in target state, please start over")
                exit()
        elif upOrDown == "3":
            if obj.value <= int(targetNum):
                print("\nSpecified target is already achieved in target state, please start over")
                exit()
        elif upOrDown == "4":
            if obj.value < int(targetNum):
                print("\nSpecified target is already achieved in target state, please start over")
                exit()
            if targetNum == "0":
                print("Error, no species can reach a value lower than zero")
                exit()
        else:
            print("Problem with information entered (check make sure your answer you only entered a integer between 1 and 4 and there are no spaces)")
            exit()

secondTargetList = []
if upOrDown == "1" or upOrDown == "2": #reactions that directly affect the target species have 10 added or subtracted from their priority
    for obj in  reactions:
        if obj.product1 == targetSpecies or obj.product2 == targetSpecies:
            obj.priority = obj.priority + 10
        elif obj.reactant1 == targetSpecies or obj.reactant2 == targetSpecies:
            obj.priority = obj.priority - 10
elif upOrDown == "3" or upOrDown == "4":
    for obj in  reactions:
        if obj.product1 == targetSpecies or obj.product2 == targetSpecies:
            obj.priority = obj.priority - 10
        elif obj.reactant1 == targetSpecies or obj.reactant2 == targetSpecies:
            obj.priority = obj.priority + 10


for obj in  reactions:       #secondary target species identified and added to a list of secondary target species, also given minAmount value (amount needed for reaction to fire enough times to get to target state)
    if upOrDown == "1" or upOrDown == "2":
        if obj.priority >= 25:
            if obj.reactant1 != "" and obj.reactant2 != "":
                if obj.reactant1 != targetSpecies:
                    if obj.product1 == targetSpecies:
                        for tar in speciesList:
                            if tar.name == targetSpecies:
                                tarNumOne = tar.value
                                secondTargetList.append(SecondTarget(obj.reactant1, obj.reactant1Num * abs(int(targetNum) - tar.value)/obj.product1Num))
                    elif obj.product2 == targetSpecies:
                        for tar in speciesList:
                            if tar.name == targetSpecies:
                                tarNumOne = tar.value
                                secondTargetList.append(SecondTarget(obj.reactant1, obj.reactant1Num * abs(int(targetNum) - tar.value)/obj.product2Num))
                if obj.reactant2 != targetSpecies:    
                    if obj.product1 == targetSpecies:
                        for tar in speciesList:
                            if tar.name == targetSpecies:
                                tarNumOne = tar.value
                                secondTargetList.append(SecondTarget(obj.reactant2, obj.reactant2Num * abs(int(targetNum) - tar.value)/obj.product1Num))
                    elif obj.product2 == targetSpecies:
                        for tar in speciesList:
                            if tar.name == targetSpecies:
                                tarNumOne = tar.value
                                secondTargetList.append(SecondTarget(obj.reactant2, obj.reactant2Num * abs(int(targetNum) - tar.value)/obj.product2Num))
            elif obj.reactant1 != "" and obj.reactant2 == "":
                if obj.reactant1 != targetSpecies:
                    if obj.product1 == targetSpecies:
                        for tar in speciesList:
                            if tar.name == targetSpecies:
                                tarNumOne = tar.value
                                secondTargetList.append(SecondTarget(obj.reactant1, obj.reactant1Num * abs(int(targetNum) - tar.value)/obj.product1Num))
                    elif obj.product2 == targetSpecies:
                        for tar in speciesList:
                            if tar.name == targetSpecies:
                                tarNumOne = tar.value
                                secondTargetList.append(SecondTarget(obj.reactant1, obj.reactant1Num * abs(int(targetNum) - tar.value)/obj.product2Num))
    elif upOrDown == "3" or upOrDown== "4":
        if obj.priority >= 25:
            if obj.reactant1 != "" and obj.reactant2 != "":
                if obj.reactant1 != targetSpecies:
                    if obj.reactant2 == targetSpecies:
                        for tar in speciesList:
                            if tar.name == targetSpecies:
                                tarNumOne = tar.value
                                secondTargetList.append(SecondTarget(obj.reactant1, obj.reactant1Num * abs(int(targetNum) - tar.value)/obj.reactant2Num))
                if obj.reactant2 != targetSpecies:    
                    if obj.reactant1 == targetSpecies:
                        for tar in speciesList:
                            if tar.name == targetSpecies:
                                tarNumOne = tar.value
                                secondTargetList.append(SecondTarget(obj.reactant2, obj.reactant2Num * abs(int(targetNum) - tar.value)/obj.reactant1Num))
            
 
for obj in  reactions:          #every reaction that consumes a secondary target has its priority modified
    if obj.priority < 25:
        for tar in secondTargetList:
            for species in speciesList:
                if species.name == tar.name:
                    if species.value >= (2*tar.minAmount):
                        if obj.reactant1 == tar.name:
                            obj.priority = obj.priority - 1
                        if obj.reactant2 == tar.name:
                            obj.priority = obj.priority - 1
                    elif species.value >= tar.minAmount:
                        if obj.reactant1 == tar.name:
                            obj.priority = obj.priority - 2
                        if obj.reactant2 == tar.name:
                            obj.priority = obj.priority - 2
                    elif species.value >= (tar.minAmount/2):
                        if obj.reactant1 == tar.name:
                            obj.priority = obj.priority - 3
                        if obj.reactant2 == tar.name:
                            obj.priority = obj.priority - 3
                    elif species.value >= (tar.minAmount/4):
                        if obj.reactant1 == tar.name:
                            obj.priority = obj.priority - 4
                        if obj.reactant2 == tar.name:
                            obj.priority = obj.priority - 4
                    elif species.value < (tar.minAmount/4):
                        if obj.reactant1 == tar.name:
                            obj.priority = obj.priority - 5
                        if obj.reactant2 == tar.name:
                            obj.priority = obj.priority - 5

        
for obj in  reactions:       #every reaction that produces a secondary target has its priority modified
    if obj.priority < 25:
        for tar in secondTargetList:
            for species in speciesList:
                if species.name == tar.name:
                    if obj.product1 == tar.name:
                        if species.value >= (2*tar.minAmount):
                            obj.priority = obj.priority + 1
                        elif species.value >= tar.minAmount:
                            obj.priority = obj.priority + 2
                        elif species.value >= (tar.minAmount/2):
                            obj.priority = obj.priority + 3
                        elif species.value >= (tar.minAmount/4):
                            obj.priority = obj.priority + 4
                        elif species.value < (tar.minAmount/4):
                            obj.priority = obj.priority + 5
                    elif obj.product2 == tar.name:
                        if species.value >= (2*tar.minAmount):
                            obj.priority = obj.priority + 1
                        elif species.value >= tar.minAmount:
                            obj.priority = obj.priority + 2
                        elif species.value >= (tar.minAmount/2):
                            obj.priority = obj.priority + 3
                        elif species.value >= (tar.minAmount/4):
                            obj.priority = obj.priority + 4
                        elif species.value < (tar.minAmount/4):
                            obj.priority = obj.priority + 5

print("\n\nThe following priorities have been noted for the reactions: \n")

count = 0
for obj in  reactions: #each reactions priority is displayed
    count = count + 1
    print("reaction", str(count), ":", str(obj.priority))

ivyFile = open("test_v2.ivy", "w") #an ivy model for the CRN is made to have assertion failure at first idling action

ivyFile.write("#lang ivy 1.7\n\nobject updater = {\n")
ivyFile.write("\ttype num\n\tinterpret num -> bv[10]\n\ttype exec_var\n\tinterpret exec_var -> bv[8]\n\ttype exec_stage\n\tinterpret exec_stage -> bv[3]\n\n\taction incr(x:num) returns(y:num) = {\n\t\ty := x + 1\n\t}\n\n\taction decr(x:num) returns(y:num) = {\n\t\ty := x - 1\n\t}\n}")
ivyFile.write("\n\nobject goal = {\n\taction achieved(v:updater.num)\n\tobject spec = {\n\t\tbefore achieved {\n\t\t\tassert v ")
if upOrDown == "1":
    ivyFile.write(">= ")
elif upOrDown == "2":
    ivyFile.write("> ")
elif upOrDown == "3":
    ivyFile.write("<= ")
elif upOrDown == "4":
    ivyFile.write("< ")
ivyFile.write(targetNum)
ivyFile.write(";\n\t\t\tprotocol.idle := 1\n\t\t}\n\t}\n}\n\n")

ivyFile.write("object enabled_checker = {\n\n\t")

count = 0
for obj in  reactions:
    count += 1
    if obj.priority > 15:
        ivyFile.write("action is_enabled_r") 
        ivyFile.write(str(count))
        if (Reactions[count-1].reactant1 == ""):
            ivyFile.write(" returns(y:bool) = {\n\t\ty := true\n\t}\n\n\t")
        elif(Reactions[count-1].reactant1 != "" and Reactions[count-1].reactant2 == ""):
            ivyFile.write("(reactant1:updater.num) returns(y:bool) = {\n\t\tif reactant1 >= ")
            ivyFile.write(str(obj.reactant1Num))
            ivyFile.write(" {\n\t\t\ty := true\n\t\t}\n\t\telse {\n\t\t\ty := false\n\t\t}\n\t}\n\n\t")
        elif(Reactions[count-1].reactant1 != "" and Reactions[count-1].reactant2 != ""):
            ivyFile.write("(reactant1:updater.num,reactant2:updater.num) returns(y:bool) = {\n\t\tif reactant1 >= ")
            ivyFile.write(str(obj.reactant1Num))
            ivyFile.write(" & reactant2 >= ")
            ivyFile.write(str(obj.reactant2Num))
            ivyFile.write(" {\n\t\t\ty := true\n\t\t}\n\t\telse {\n\t\t\ty := false\n\t\t}\n\t}\n\n\t")
ivyFile.write("\n}\n\n")

ivyFile.write("object inspector = {\n\t")
count = 0
for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write("action check_guard_r")
        ivyFile.write(str(count))
        if (Reactions[count-1].reactant1 == ""):
            ivyFile.write("\n\tbefore check_guard_r")
            ivyFile.write(str(count))
            ivyFile.write(" {\n\t\tassert true\n\t}\n\n\t")
        elif(Reactions[count-1].reactant1 != "" and Reactions[count-1].reactant2 == ""):
            ivyFile.write("(reactant1:updater.num)\n\tbefore check_guard_r")
            ivyFile.write(str(count))
            ivyFile.write(" {\n\t\tassert reactant1 >= ")
            ivyFile.write(str(obj.reactant1Num))
            ivyFile.write("\n\t}\n\n\t")
        elif(Reactions[count-1].reactant1 != "" and Reactions[count-1].reactant2 != ""):
            ivyFile.write("(reactant1:updater.num,reactant2:updater.num)\n\tbefore check_guard_r")
            ivyFile.write(str(count))
            ivyFile.write(" {\n\t\tassert reactant1 >= ")
            ivyFile.write(str(obj.reactant1Num))
            ivyFile.write(" & reactant2 >= ")
            ivyFile.write(str(obj.reactant2Num))
            ivyFile.write("\n\t}\n\n\t")

        
ivyFile.write("\n}")

ivyFile.write("\n\nobject selector = {\n\t")

count = 0

for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write("individual r")
        ivyFile.write(str(count))
        ivyFile.write("_exec : updater.exec_var\n\t")

ivyFile.write("\n\t")
count = 0

for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write("individual r")
        ivyFile.write(str(count))
        ivyFile.write("_rate : updater.exec_var\n\t")

ivyFile.write("\n\t")

count = 0
for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write("individual r")
        ivyFile.write(str(count))
        ivyFile.write("_count : updater.exec_var\n\t")

ivyFile.write("\n\t")

count = 0
for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write("individual r")
        ivyFile.write(str(count))
        ivyFile.write("_count_rate : updater.exec_var\n\t")

ivyFile.write("\n\t")

count = 0
for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write("individual r")
        ivyFile.write(str(count))
        ivyFile.write("_stage : updater.exec_stage\n\t")

ivyFile.write("\n\n\tafter init {\n\t\t")

count = 0
for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write("r")
        ivyFile.write(str(count))
        ivyFile.write("_count := 0")
        ivyFile.write(";\n\t\t")

ivyFile.write("\n\n\t\t")
count = 0
for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write("r")
        ivyFile.write(str(count))
        ivyFile.write("_count_rate := 4")
        ivyFile.write(";\n\t\t")

ivyFile.write("\n\t}\n\n\t")

count = 0
for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write("action execute_r")
        ivyFile.write(str(count))
        ivyFile.write(" returns(y:bool) = {\n\t\tr")
        ivyFile.write(str(count))
        ivyFile.write("_exec := r")
        ivyFile.write(str(count))
        ivyFile.write("_exec + 1;\n\t\t")
        ivyFile.write("if r")
        ivyFile.write(str(count))
        ivyFile.write("_exec >= r")
        ivyFile.write(str(count))
        ivyFile.write("_rate {\n\t\t\ty := true;\n\t\t\tr")
        ivyFile.write(str(count))
        ivyFile.write("_exec := 0;\n\t\t\tr")
        ivyFile.write(str(count))
        ivyFile.write("_count := r")
        ivyFile.write(str(count))
        ivyFile.write("_count + 1\n\t\t}\n\t\telse {\n\t\t\ty := false\n\t\t};\n\t\tif r")
        ivyFile.write(str(count))
        ivyFile.write("_count >= r")
        ivyFile.write(str(count))
        ivyFile.write("_count_rate {\n\t\t\tr")
        ivyFile.write(str(count))
        ivyFile.write("_stage := r")
        ivyFile.write(str(count))
        ivyFile.write("_stage + 1;\n\t\t\tr")
        ivyFile.write(str(count))
        ivyFile.write("_count := 0\n\t\t};\n\t\t")
        if obj.priority >= 23:
            ivyFile.write("if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 0 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 1 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 2 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 3 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 4 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 5 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 6 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 7 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\telse {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_stage := 0\n\t\t}\n\t}\n\n\t")
        elif obj.priority >= 21:
            ivyFile.write("if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 0 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 1 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 2\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 2 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 3 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 3;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 2\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 4 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 5;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 5 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 2\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 6 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 7 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 2\n\t\t}\n\t\telse {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_stage := 0\n\t\t}\n\t}\n\n\t")
        elif obj.priority >= 19:
            ivyFile.write("if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 0 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 3;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 4\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 1 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 5\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 2 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 6\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 3 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 4\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 4 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 3;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 3\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 5 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 4\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 6 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 1;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 3\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 7 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 5\n\t\t}\n\t\telse {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_stage := 0\n\t\t}\n\t}\n\n\t")
        elif obj.priority == 18:
            ivyFile.write("if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 0 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 5;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 30\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 1 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 3;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 28\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 2 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 34\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 3 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 9;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 25\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 4 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 36\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 5 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 29\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 6 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 5;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 30\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 7 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 1;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 34\n\t\t}\n\t\telse {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_stage := 0\n\t\t}\n\t}\n\n\t")
        elif obj.priority == 17:
            ivyFile.write("if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 0 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 1;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 200\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 1 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 3;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 189\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 2 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 192\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 3 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 9;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 212\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 4 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 192\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 5 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 232\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 6 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 5;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 190\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 7 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 3;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 200\n\t\t}\n\t\telse {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_stage := 0\n\t\t}\n\t}\n\n\t")
        elif obj.priority == 16:
            ivyFile.write("if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 0 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 5;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1000\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 1 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 3;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 989\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 2 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1190\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 3 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 9;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1053\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 4 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 942\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 5 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1022\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 6 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 5;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 930\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 7 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 1;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1000\n\t\t}\n\t\telse {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_stage := 0\n\t\t}\n\t}\n\n\t")
        elif obj.priority <= 9 and obj.priority >= 7:
            ivyFile.write("if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 0 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 5;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 50\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 1 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 3;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 56\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 2 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 62\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 3 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 9;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 48\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 4 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 63\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 5 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 52\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 6 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 5;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 58\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 7 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 1;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 82\n\t\t}\n\t\telse {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_stage := 0\n\t\t}\n\t}\n\n\t")
        elif obj.priority <= 6:
            ivyFile.write("if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 0 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 5;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 250\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 1 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 3;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 250\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 2 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 250\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 3 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 9;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 250\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 4 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 250\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 5 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 250\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 6 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 5;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 250\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 7 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 1;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 250\n\t\t}\n\t\telse {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_stage := 0\n\t\t}\n\t}\n\n\t")



ivyFile.write("\n}\n")

ivyFile.write("\nobject protocol = {\n\n\ttype 2bit\n\tinterpret 2bit -> bv[1]\n\tindividual idle : 2bit\n\n")

for obj in spec:
    ivyFile.write("\tindividual ")
    ivyFile.write("r_")
    ivyFile.write(obj)
    ivyFile.write(" : updater.num\n")

ivyFile.write("\n\tafter init {\n\t\t")

for obj in speciesList:
    ivyFile.write("r_")
    ivyFile.write(obj.name)
    ivyFile.write(" := ")
    ivyFile.write(str(obj.value))
    ivyFile.write(";\n\t\t")

ivyFile.write("idle := 0\n\t}\n\n\t")

count = 0
for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        if(obj.reactant1 == "" and obj.product1 != "" and obj.product2 == ""):
            ivyFile.write("action update_r")
            ivyFile.write(str(count))
            ivyFile.write(" = {\n\t\t")
            ivyFile.write("if selector.execute_r")
            ivyFile.write(str(count))
            ivyFile.write(" {\n\t\t\tcall inspector.check_guard_r")
            ivyFile.write(str(count))
            for x in range(obj.product1Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.product1)
                ivyFile.write(" := updater.incr(")
                ivyFile.write("r_")
                ivyFile.write(obj.product1)
                ivyFile.write(")")
            if obj.priority >= 25:
                ivyFile.write(";\n\t\t")
                ivyFile.write("\tif ")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                if upOrDown == "1":
                    ivyFile.write(" >= ")
                elif upOrDown == "2":
                    ivyFile.write(" > ")
                elif upOrDown == "3":
                    ivyFile.write(" <= ")
                elif upOrDown == "4":
                    ivyFile.write(" < ")
                ivyFile.write(str(targetNum))
                ivyFile.write(" {\n\t\t\t\tcall goal.achieved(")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                ivyFile.write(")\n\t\t\t}\n\t\t")
            else:
                ivyFile.write("\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 == "" and obj.product1 != "" and obj.product2 != ""):
            ivyFile.write("action update_r")
            ivyFile.write(str(count))
            ivyFile.write(" = {\n\t\t")
            ivyFile.write("if selector.execute_r")
            ivyFile.write(str(count))
            ivyFile.write(" {\n\t\t\tcall inspector.check_guard_r")
            ivyFile.write(str(count))
            for x in range(obj.product1Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.product1)
                ivyFile.write(" := updater.incr(")
                ivyFile.write("r_")
                ivyFile.write(obj.product1)
                ivyFile.write(")")
            for x in range(obj.product2Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.product2)
                ivyFile.write(" := updater.incr(")
                ivyFile.write("r_")
                ivyFile.write(obj.product2)
                ivyFile.write(")")
            if obj.priority >= 25:
                ivyFile.write(";\n\t\t")
                ivyFile.write("\tif ")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                if upOrDown == "1":
                    ivyFile.write(" >= ")
                elif upOrDown == "2":
                    ivyFile.write(" > ")
                elif upOrDown == "3":
                    ivyFile.write(" <= ")
                elif upOrDown == "4":
                    ivyFile.write(" < ")
                ivyFile.write(str(targetNum))
                ivyFile.write(" {\n\t\t\t\tcall goal.achieved(")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                ivyFile.write(")\n\t\t\t}\n\t\t")
            else:
                ivyFile.write("\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 != "" and obj.reactant2 == "" and obj.product1 == ""):
            ivyFile.write("action update_r")
            ivyFile.write(str(count))
            ivyFile.write(" = {\n\t\t")
            ivyFile.write("if selector.execute_r")
            ivyFile.write(str(count))
            ivyFile.write(" {\n\t\t\tcall inspector.check_guard_r")
            ivyFile.write(str(count))
            ivyFile.write("(")
            ivyFile.write("r_")
            ivyFile.write(obj.reactant1)
            ivyFile.write(")")
            for x in range(obj.reactant1Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant1)
                ivyFile.write(" := updater.decr(")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant1)
                ivyFile.write(")")
            if obj.priority >= 25:
                ivyFile.write(";\n\t\t")
                ivyFile.write("\tif ")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                if upOrDown == "1":
                    ivyFile.write(" >= ")
                elif upOrDown == "2":
                    ivyFile.write(" > ")
                elif upOrDown == "3":
                    ivyFile.write(" <= ")
                elif upOrDown == "4":
                    ivyFile.write(" < ")
                ivyFile.write(str(targetNum))
                ivyFile.write(" {\n\t\t\t\tcall goal.achieved(")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                ivyFile.write(")\n\t\t\t}\n\t\t")
            else:
                ivyFile.write("\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 != "" and obj.reactant2 == "" and obj.product1 != "" and obj.product2 == ""):
            ivyFile.write("action update_r")
            ivyFile.write(str(count))
            ivyFile.write(" = {\n\t\t")
            ivyFile.write("if selector.execute_r")
            ivyFile.write(str(count))
            ivyFile.write(" {\n\t\t\tcall inspector.check_guard_r")
            ivyFile.write(str(count))
            ivyFile.write("(")
            ivyFile.write("r_")
            ivyFile.write(obj.reactant1)
            ivyFile.write(")")
            for x in range(obj.reactant1Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant1)
                ivyFile.write(" := updater.decr(")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant1)
                ivyFile.write(")")
            for x in range(obj.product1Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.product1)
                ivyFile.write(" := updater.incr(")
                ivyFile.write("r_")
                ivyFile.write(obj.product1)
                ivyFile.write(")")
            if obj.priority >= 25:
                ivyFile.write(";\n\t\t")
                ivyFile.write("\tif ")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                if upOrDown == "1":
                    ivyFile.write(" >= ")
                elif upOrDown == "2":
                    ivyFile.write(" > ")
                elif upOrDown == "3":
                    ivyFile.write(" <= ")
                elif upOrDown == "4":
                    ivyFile.write(" < ")
                ivyFile.write(str(targetNum))
                ivyFile.write(" {\n\t\t\t\tcall goal.achieved(")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                ivyFile.write(")\n\t\t\t}\n\t\t")
            else:
                ivyFile.write("\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 != "" and obj.reactant2 == "" and obj.product1 != "" and obj.product2 != ""):
            ivyFile.write("action update_r")
            ivyFile.write(str(count))
            ivyFile.write(" = {\n\t\t")
            ivyFile.write("if selector.execute_r")
            ivyFile.write(str(count))
            ivyFile.write(" {\n\t\t\tcall inspector.check_guard_r")
            ivyFile.write(str(count))
            ivyFile.write("(")
            ivyFile.write("r_")
            ivyFile.write(obj.reactant1)
            ivyFile.write(")")
            for x in range(obj.reactant1Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant1)
                ivyFile.write(" := updater.decr(")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant1)
                ivyFile.write(")")
            for x in range(obj.product1Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.product1)
                ivyFile.write(" := updater.incr(")
                ivyFile.write("r_")
                ivyFile.write(obj.product1)
                ivyFile.write(")")
            for x in range(obj.product2Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.product2)
                ivyFile.write(" := updater.incr(")
                ivyFile.write("r_")
                ivyFile.write(obj.product2)
                ivyFile.write(")")
            if obj.priority >= 25:
                ivyFile.write(";\n\t\t")
                ivyFile.write("\tif ")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                if upOrDown == "1":
                    ivyFile.write(" >= ")
                elif upOrDown == "2":
                    ivyFile.write(" > ")
                elif upOrDown == "3":
                    ivyFile.write(" <= ")
                elif upOrDown == "4":
                    ivyFile.write(" < ")
                ivyFile.write(str(targetNum))
                ivyFile.write(" {\n\t\t\t\tcall goal.achieved(")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                ivyFile.write(")\n\t\t\t}\n\t\t")
            else:
                ivyFile.write("\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 != "" and obj.reactant2 != "" and obj.product1 == ""):
            ivyFile.write("action update_r")
            ivyFile.write(str(count))
            ivyFile.write(" = {\n\t\t")
            ivyFile.write("if selector.execute_r")
            ivyFile.write(str(count))
            ivyFile.write(" {\n\t\t\tcall inspector.check_guard_r")
            ivyFile.write(str(count))
            ivyFile.write("(")
            ivyFile.write("r_")
            ivyFile.write(obj.reactant1)
            ivyFile.write(",")
            ivyFile.write("r_")
            ivyFile.write(obj.reactant2)
            ivyFile.write(")")
            for x in range(obj.reactant1Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant1)
                ivyFile.write(" := updater.decr(")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant1)
                ivyFile.write(")")
            for x in range(obj.reactant2Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant2)
                ivyFile.write(" := updater.decr(")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant2)
                ivyFile.write(")")
            if obj.priority >= 25:
                ivyFile.write(";\n\t\t")
                ivyFile.write("\tif ")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                if upOrDown == "1":
                    ivyFile.write(" >= ")
                elif upOrDown == "2":
                    ivyFile.write(" > ")
                elif upOrDown == "3":
                    ivyFile.write(" <= ")
                elif upOrDown == "4":
                    ivyFile.write(" < ")
                ivyFile.write(str(targetNum))
                ivyFile.write(" {\n\t\t\t\tcall goal.achieved(")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                ivyFile.write(")\n\t\t\t}\n\t\t")
            else:
                ivyFile.write("\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 != "" and obj.reactant2 != "" and obj.product1 != "" and obj.product2 == ""):
            ivyFile.write("action update_r")
            ivyFile.write(str(count))
            ivyFile.write(" = {\n\t\t")
            ivyFile.write("if selector.execute_r")
            ivyFile.write(str(count))
            ivyFile.write(" {\n\t\t\tcall inspector.check_guard_r")
            ivyFile.write(str(count))
            ivyFile.write("(")
            ivyFile.write("r_")
            ivyFile.write(obj.reactant1)
            ivyFile.write(",")
            ivyFile.write("r_")
            ivyFile.write(obj.reactant2)
            ivyFile.write(")")
            for x in range(obj.reactant1Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant1)
                ivyFile.write(" := updater.decr(")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant1)
                ivyFile.write(")")
            for x in range(obj.reactant2Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant2)
                ivyFile.write(" := updater.decr(")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant2)
                ivyFile.write(")")
            for x in range(obj.product1Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.product1)
                ivyFile.write(" := updater.incr(")
                ivyFile.write("r_")
                ivyFile.write(obj.product1)
                ivyFile.write(")")
            if obj.priority >= 25:
                ivyFile.write(";\n\t\t")
                ivyFile.write("\tif ")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                if upOrDown == "1":
                    ivyFile.write(" >= ")
                elif upOrDown == "2":
                    ivyFile.write(" > ")
                elif upOrDown == "3":
                    ivyFile.write(" <= ")
                elif upOrDown == "4":
                    ivyFile.write(" < ")
                ivyFile.write(str(targetNum))
                ivyFile.write(" {\n\t\t\t\tcall goal.achieved(")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                ivyFile.write(")\n\t\t\t}\n\t\t")
            else:
                ivyFile.write("\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 != "" and obj.reactant2 != "" and obj.product1 != "" and obj.product2 != ""):
            ivyFile.write("action update_r")
            ivyFile.write(str(count))
            ivyFile.write(" = {\n\t\t")
            ivyFile.write("if selector.execute_r")
            ivyFile.write(str(count))
            ivyFile.write(" {\n\t\t\tcall inspector.check_guard_r")
            ivyFile.write(str(count))
            ivyFile.write("(")
            ivyFile.write("r_")
            ivyFile.write(obj.reactant1)
            ivyFile.write(",")
            ivyFile.write("r_")
            ivyFile.write(obj.reactant2)
            ivyFile.write(")")
            for x in range(obj.reactant1Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant1)
                ivyFile.write(" := updater.decr(")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant1)
                ivyFile.write(")")
            for x in range(obj.reactant2Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant2)
                ivyFile.write(" := updater.decr(")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant2)
                ivyFile.write(")")
            for x in range(obj.product1Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.product1)
                ivyFile.write(" := updater.incr(")
                ivyFile.write("r_")
                ivyFile.write(obj.product1)
                ivyFile.write(")")
            for x in range(obj.product2Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.product2)
                ivyFile.write(" := updater.incr(")
                ivyFile.write("r_")
                ivyFile.write(obj.product2)
                ivyFile.write(")")
            if obj.priority >= 25:
                ivyFile.write(";\n\t\t")
                ivyFile.write("\tif ")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                if upOrDown == "1":
                    ivyFile.write(" >= ")
                elif upOrDown == "2":
                    ivyFile.write(" > ")
                elif upOrDown == "3":
                    ivyFile.write(" <= ")
                elif upOrDown == "4":
                    ivyFile.write(" < ")
                ivyFile.write(str(targetNum))
                ivyFile.write(" {\n\t\t\t\tcall goal.achieved(")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                ivyFile.write(")\n\t\t\t}\n\t\t")
            else:
                ivyFile.write("\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")

ivyFile.write("\n\n\taction idling = {}\n\n\t")
count = 0
for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write("before update_r")
        ivyFile.write(str(count))
        if (Reactions[count-1].reactant1 == ""):
            ivyFile.write(" {\n\t\tassert idle = 0;\n\t\tassert enabled_checker.is_enabled_r")
            ivyFile.write(str(count))
            if obj.priority <= 6:
                ivyFile.write(";\n\t\tassert false")
            ivyFile.write("\n\t}\n\t")
        elif(Reactions[count-1].reactant1 != "" and Reactions[count-1].reactant2 == ""):
            ivyFile.write(" {\n\t\tassert idle = 0;\n\t\tassert enabled_checker.is_enabled_r")
            ivyFile.write(str(count))
            ivyFile.write("(")
            ivyFile.write("r_")
            ivyFile.write(Reactions[count-1].reactant1)
            ivyFile.write(")")
            if obj.priority <= 6:
                ivyFile.write(";\n\t\tassert false")
            ivyFile.write("\n\t}\n\t")
        elif(Reactions[count-1].reactant1 != "" and Reactions[count-1].reactant2 != ""):
            ivyFile.write(" {\n\t\tassert idle = 0;\n\t\tassert enabled_checker.is_enabled_r")
            ivyFile.write(str(count))
            ivyFile.write("(")
            ivyFile.write("r_")
            ivyFile.write(Reactions[count-1].reactant1)
            ivyFile.write(",")
            ivyFile.write("r_")
            ivyFile.write(Reactions[count-1].reactant2)
            ivyFile.write(")")
            if obj.priority <= 6:
                ivyFile.write(";\n\t\tassert false")
            ivyFile.write("\n\t}\n\n\t")


ivyFile.write("\n\n\tbefore idling {\n\t\tassert idle = 1\n\t}")#\n}\n")

ivyFile.write("\n\n\tafter idling {\n\t\tassert idle = 0\n\t}\n}\n") #this causes assertion failure for the first run

count = 0
for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write("export protocol.update_r")
        ivyFile.write(str(count))
        ivyFile.write("\n")


ivyFile.write("export protocol.idling\nimport goal.achieved\n")

count = 0
for obj in  reactions:
    count= count + 1
    if obj.priority > 15:
        ivyFile.write("import inspector.check_guard_r")
        ivyFile.write(str(count))
        ivyFile.write("\n")

ivyFile.write("\nisolate iso_proto = protocol with enabled_checker, updater, goal, selector, inspector")

ivyFile.close()        #ivy model complete

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
ivyFile = open("test_v2.ivy", "w") #another ivy model is created that will not have assertion failure

ivyFile.write("#lang ivy 1.7\n\nobject updater = {\n")
ivyFile.write("\ttype num\n\tinterpret num -> bv[10]\n\ttype exec_var\n\tinterpret exec_var -> bv[8]\n\ttype exec_stage\n\tinterpret exec_stage -> bv[3]\n\n\taction incr(x:num) returns(y:num) = {\n\t\ty := x + 1\n\t}\n\n\taction decr(x:num) returns(y:num) = {\n\t\ty := x - 1\n\t}\n}")
ivyFile.write("\n\nobject goal = {\n\taction achieved(v:updater.num)\n\tobject spec = {\n\t\tbefore achieved {\n\t\t\tassert v ")
if upOrDown == "1":
    ivyFile.write(">= ")
elif upOrDown == "2":
    ivyFile.write("> ")
elif upOrDown == "3":
    ivyFile.write("<= ")
elif upOrDown == "4":
    ivyFile.write("< ")
ivyFile.write(targetNum)
ivyFile.write(";\n\t\t\tprotocol.idle := 1\n\t\t}\n\t}\n}\n\n")

ivyFile.write("object enabled_checker = {\n\n\t")

count = 0
for obj in  reactions:
    count += 1
    if obj.priority > 15:
        ivyFile.write("action is_enabled_r") 
        ivyFile.write(str(count))
        if (Reactions[count-1].reactant1 == ""):
            ivyFile.write(" returns(y:bool) = {\n\t\ty := true\n\t}\n\n\t")
        elif(Reactions[count-1].reactant1 != "" and Reactions[count-1].reactant2 == ""):
            ivyFile.write("(reactant1:updater.num) returns(y:bool) = {\n\t\tif reactant1 >= ")
            ivyFile.write(str(obj.reactant1Num))
            ivyFile.write(" {\n\t\t\ty := true\n\t\t}\n\t\telse {\n\t\t\ty := false\n\t\t}\n\t}\n\n\t")
        elif(Reactions[count-1].reactant1 != "" and Reactions[count-1].reactant2 != ""):
            ivyFile.write("(reactant1:updater.num,reactant2:updater.num) returns(y:bool) = {\n\t\tif reactant1 >= ")
            ivyFile.write(str(obj.reactant1Num))
            ivyFile.write(" & reactant2 >= ")
            ivyFile.write(str(obj.reactant2Num))
            ivyFile.write(" {\n\t\t\ty := true\n\t\t}\n\t\telse {\n\t\t\ty := false\n\t\t}\n\t}\n\n\t")
ivyFile.write("\n}\n\n")

ivyFile.write("object inspector = {\n\t")
count = 0
for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write("action check_guard_r")
        ivyFile.write(str(count))
        if (Reactions[count-1].reactant1 == ""):
            ivyFile.write("\n\tbefore check_guard_r")
            ivyFile.write(str(count))
            ivyFile.write(" {\n\t\tassert true\n\t}\n\n\t")
        elif(Reactions[count-1].reactant1 != "" and Reactions[count-1].reactant2 == ""):
            ivyFile.write("(reactant1:updater.num)\n\tbefore check_guard_r")
            ivyFile.write(str(count))
            ivyFile.write(" {\n\t\tassert reactant1 >= ")
            ivyFile.write(str(obj.reactant1Num))
            ivyFile.write("\n\t}\n\n\t")
        elif(Reactions[count-1].reactant1 != "" and Reactions[count-1].reactant2 != ""):
            ivyFile.write("(reactant1:updater.num,reactant2:updater.num)\n\tbefore check_guard_r")
            ivyFile.write(str(count))
            ivyFile.write(" {\n\t\tassert reactant1 >= ")
            ivyFile.write(str(obj.reactant1Num))
            ivyFile.write(" & reactant2 >= ")
            ivyFile.write(str(obj.reactant2Num))
            ivyFile.write("\n\t}\n\n\t")

        
ivyFile.write("\n}")

ivyFile.write("\n\nobject selector = {\n\t")

count = 0

for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write("individual r")
        ivyFile.write(str(count))
        ivyFile.write("_exec : updater.exec_var\n\t")

ivyFile.write("\n\t")
count = 0

for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write("individual r")
        ivyFile.write(str(count))
        ivyFile.write("_rate : updater.exec_var\n\t")

ivyFile.write("\n\t")

count = 0
for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write("individual r")
        ivyFile.write(str(count))
        ivyFile.write("_count : updater.exec_var\n\t")

ivyFile.write("\n\t")

count = 0
for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write("individual r")
        ivyFile.write(str(count))
        ivyFile.write("_count_rate : updater.exec_var\n\t")

ivyFile.write("\n\t")

count = 0
for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write("individual r")
        ivyFile.write(str(count))
        ivyFile.write("_stage : updater.exec_stage\n\t")

ivyFile.write("\n\n\tafter init {\n\t\t")

count = 0
for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write("r")
        ivyFile.write(str(count))
        ivyFile.write("_count := 0")
        ivyFile.write(";\n\t\t")

ivyFile.write("\n\n\t\t")
count = 0
for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write("r")
        ivyFile.write(str(count))
        ivyFile.write("_count_rate := 4")
        ivyFile.write(";\n\t\t")

ivyFile.write("\n\t}\n\n\t")

count = 0
for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write("action execute_r")
        ivyFile.write(str(count))
        ivyFile.write(" returns(y:bool) = {\n\t\tr")
        ivyFile.write(str(count))
        ivyFile.write("_exec := r")
        ivyFile.write(str(count))
        ivyFile.write("_exec + 1;\n\t\t")
        ivyFile.write("if r")
        ivyFile.write(str(count))
        ivyFile.write("_exec >= r")
        ivyFile.write(str(count))
        ivyFile.write("_rate {\n\t\t\ty := true;\n\t\t\tr")
        ivyFile.write(str(count))
        ivyFile.write("_exec := 0;\n\t\t\tr")
        ivyFile.write(str(count))
        ivyFile.write("_count := r")
        ivyFile.write(str(count))
        ivyFile.write("_count + 1\n\t\t}\n\t\telse {\n\t\t\ty := false\n\t\t};\n\t\tif r")
        ivyFile.write(str(count))
        ivyFile.write("_count >= r")
        ivyFile.write(str(count))
        ivyFile.write("_count_rate {\n\t\t\tr")
        ivyFile.write(str(count))
        ivyFile.write("_stage := r")
        ivyFile.write(str(count))
        ivyFile.write("_stage + 1;\n\t\t\tr")
        ivyFile.write(str(count))
        ivyFile.write("_count := 0\n\t\t};\n\t\t")
        if obj.priority >= 23:
            ivyFile.write("if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 0 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 1 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 2 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 3 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 4 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 5 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 6 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 7 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\telse {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_stage := 0\n\t\t}\n\t}\n\n\t")
        elif obj.priority >= 21:
            ivyFile.write("if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 0 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 1 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 2\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 2 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 3 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 3;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 2\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 4 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 5;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 5 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 2\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 6 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 7 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 2\n\t\t}\n\t\telse {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_stage := 0\n\t\t}\n\t}\n\n\t")
        elif obj.priority >= 19:
            ivyFile.write("if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 0 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 3;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 1 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 2\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 2 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 3\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 3 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 2\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 4 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 3;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 3\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 5 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 2\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 6 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 1;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 1\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 7 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 2\n\t\t}\n\t\telse {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_stage := 0\n\t\t}\n\t}\n\n\t")
        elif obj.priority == 18:
            ivyFile.write("if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 0 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 3\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 1 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 3;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 4\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 2 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 5\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 3 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 9;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 5\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 4 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 4\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 5 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 3;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 5\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 6 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 5;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 3\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 7 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 1;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 4\n\t\t}\n\t\telse {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_stage := 0\n\t\t}\n\t}\n\n\t")
        elif obj.priority == 17:
            ivyFile.write("if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 0 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 13\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 1 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 3;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 11\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 2 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 15\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 3 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 9;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 12\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 4 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 14\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 5 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 12\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 6 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 5;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 15\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 7 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 3;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 10\n\t\t}\n\t\telse {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_stage := 0\n\t\t}\n\t}\n\n\t")
        elif obj.priority == 16:
            ivyFile.write("if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 0 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 5;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 30\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 1 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 3;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 28\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 2 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 34\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 3 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 9;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 25\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 4 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 36\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 5 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 29\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 6 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 5;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 30\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 7 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 1;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 34\n\t\t}\n\t\telse {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_stage := 0\n\t\t}\n\t}\n\n\t")
        elif obj.priority <= 9 and obj.priority >= 7:
            ivyFile.write("if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 0 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 5;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 50\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 1 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 3;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 56\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 2 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 62\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 3 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 9;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 48\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 4 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 63\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 5 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 52\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 6 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 5;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 58\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 7 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 1;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 82\n\t\t}\n\t\telse {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_stage := 0\n\t\t}\n\t}\n\n\t")
        elif obj.priority <= 6:
            ivyFile.write("if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 0 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 5;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 250\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 1 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 3;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 250\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 2 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 250\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 3 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 9;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 250\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 4 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 4;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 250\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 5 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 2;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 250\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 6 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 5;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 250\n\t\t}\n\t\t")
            ivyFile.write("else if r")
            ivyFile.write(str(count))
            ivyFile.write("_stage = 7 {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_count_rate := 1;\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_rate := 250\n\t\t}\n\t\telse {\n\t\t\tr")
            ivyFile.write(str(count))
            ivyFile.write("_stage := 0\n\t\t}\n\t}\n\n\t")



ivyFile.write("\n}\n")

ivyFile.write("\nobject protocol = {\n\n\ttype 2bit\n\tinterpret 2bit -> bv[1]\n\tindividual idle : 2bit\n\n")

for obj in spec:
    ivyFile.write("\tindividual ")
    ivyFile.write("r_")
    ivyFile.write(obj)
    ivyFile.write(" : updater.num\n")

count = 0
for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write("\tindividual r")
        ivyFile.write(str(count))
        ivyFile.write("_executions : updater.num\n")

ivyFile.write("\n\tafter init {\n\t\t")

for obj in speciesList:
    ivyFile.write("r_")
    ivyFile.write(obj.name)
    ivyFile.write(" := ")
    ivyFile.write(str(obj.value))
    ivyFile.write(";\n\t\t")

count = 0
for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write("r")
        ivyFile.write(str(count))
        ivyFile.write("_executions := 0;\n\t\t")

ivyFile.write("idle := 0\n\t}\n\n\t")

count = 0
for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        if(obj.reactant1 == "" and obj.product1 != "" and obj.product2 == ""):
            ivyFile.write("action update_r")
            ivyFile.write(str(count))
            ivyFile.write(" = {\n\t\t")
            ivyFile.write("if selector.execute_r")
            ivyFile.write(str(count))
            ivyFile.write(" {\n\t\t\tcall inspector.check_guard_r")
            ivyFile.write(str(count))
            for x in range(obj.product1Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.product1)
                ivyFile.write(" := updater.incr(")
                ivyFile.write("r_")
                ivyFile.write(obj.product1)
                ivyFile.write(")")
            if obj.priority >= 25:
                ivyFile.write(";\n\t\t")
                ivyFile.write("\tif ")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                if upOrDown == "1":
                    ivyFile.write(" >= ")
                elif upOrDown == "2":
                    ivyFile.write(" > ")
                elif upOrDown == "3":
                    ivyFile.write(" <= ")
                elif upOrDown == "4":
                    ivyFile.write(" < ")
                ivyFile.write(str(targetNum))
                ivyFile.write(" {\n\t\t\t\tcall goal.achieved(")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                ivyFile.write(")\n\t\t\t}\n\t\t")
            else:
                ivyFile.write(";\n\t\t\tr")
                ivyFile.write(str(count))
                ivyFile.write("_executions := updater.incr(r")
                ivyFile.write(str(count))
                ivyFile.write("_executions)")
                ivyFile.write("\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 == "" and obj.product1 != "" and obj.product2 != ""):
            ivyFile.write("action update_r")
            ivyFile.write(str(count))
            ivyFile.write(" = {\n\t\t")
            ivyFile.write("if selector.execute_r")
            ivyFile.write(str(count))
            ivyFile.write(" {\n\t\t\tcall inspector.check_guard_r")
            ivyFile.write(str(count))
            for x in range(obj.product1Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.product1)
                ivyFile.write(" := updater.incr(")
                ivyFile.write("r_")
                ivyFile.write(obj.product1)
                ivyFile.write(")")
            for x in range(obj.product2Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.product2)
                ivyFile.write(" := updater.incr(")
                ivyFile.write("r_")
                ivyFile.write(obj.product2)
                ivyFile.write(")")
            if obj.priority >= 25:
                ivyFile.write(";\n\t\t")
                ivyFile.write("\tif ")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                if upOrDown == "1":
                    ivyFile.write(" >= ")
                elif upOrDown == "2":
                    ivyFile.write(" > ")
                elif upOrDown == "3":
                    ivyFile.write(" <= ")
                elif upOrDown == "4":
                    ivyFile.write(" < ")
                ivyFile.write(str(targetNum))
                ivyFile.write(" {\n\t\t\t\tcall goal.achieved(")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                ivyFile.write(")\n\t\t\t}\n\t\t")
            else:
                ivyFile.write(";\n\t\t\tr")
                ivyFile.write(str(count))
                ivyFile.write("_executions := updater.incr(r")
                ivyFile.write(str(count))
                ivyFile.write("_executions)")
                ivyFile.write("\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 != "" and obj.reactant2 == "" and obj.product1 == ""):
            ivyFile.write("action update_r")
            ivyFile.write(str(count))
            ivyFile.write(" = {\n\t\t")
            ivyFile.write("if selector.execute_r")
            ivyFile.write(str(count))
            ivyFile.write(" {\n\t\t\tcall inspector.check_guard_r")
            ivyFile.write(str(count))
            ivyFile.write("(")
            ivyFile.write("r_")
            ivyFile.write(obj.reactant1)
            ivyFile.write(")")
            for x in range(obj.reactant1Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant1)
                ivyFile.write(" := updater.decr(")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant1)
                ivyFile.write(")")
            if obj.priority >= 25:
                ivyFile.write(";\n\t\t")
                ivyFile.write("\tif ")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                if upOrDown == "1":
                    ivyFile.write(" >= ")
                elif upOrDown == "2":
                    ivyFile.write(" > ")
                elif upOrDown == "3":
                    ivyFile.write(" <= ")
                elif upOrDown == "4":
                    ivyFile.write(" < ")
                ivyFile.write(str(targetNum))
                ivyFile.write(" {\n\t\t\t\tcall goal.achieved(")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                ivyFile.write(")\n\t\t\t}\n\t\t")
            else:
                ivyFile.write(";\n\t\t\tr")
                ivyFile.write(str(count))
                ivyFile.write("_executions := updater.incr(r")
                ivyFile.write(str(count))
                ivyFile.write("_executions)")
                ivyFile.write("\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 != "" and obj.reactant2 == "" and obj.product1 != "" and obj.product2 == ""):
            ivyFile.write("action update_r")
            ivyFile.write(str(count))
            ivyFile.write(" = {\n\t\t")
            ivyFile.write("if selector.execute_r")
            ivyFile.write(str(count))
            ivyFile.write(" {\n\t\t\tcall inspector.check_guard_r")
            ivyFile.write(str(count))
            ivyFile.write("(")
            ivyFile.write("r_")
            ivyFile.write(obj.reactant1)
            ivyFile.write(")")
            for x in range(obj.reactant1Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant1)
                ivyFile.write(" := updater.decr(")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant1)
                ivyFile.write(")")
            for x in range(obj.product1Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.product1)
                ivyFile.write(" := updater.incr(")
                ivyFile.write("r_")
                ivyFile.write(obj.product1)
                ivyFile.write(")")
            if obj.priority >= 25:
                ivyFile.write(";\n\t\t")
                ivyFile.write("\tif ")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                if upOrDown == "1":
                    ivyFile.write(" >= ")
                elif upOrDown == "2":
                    ivyFile.write(" > ")
                elif upOrDown == "3":
                    ivyFile.write(" <= ")
                elif upOrDown == "4":
                    ivyFile.write(" < ")
                ivyFile.write(str(targetNum))
                ivyFile.write(" {\n\t\t\t\tcall goal.achieved(")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                ivyFile.write(")\n\t\t\t}\n\t\t")
            else:
                ivyFile.write(";\n\t\t\tr")
                ivyFile.write(str(count))
                ivyFile.write("_executions := updater.incr(r")
                ivyFile.write(str(count))
                ivyFile.write("_executions)")
                ivyFile.write("\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 != "" and obj.reactant2 == "" and obj.product1 != "" and obj.product2 != ""):
            ivyFile.write("action update_r")
            ivyFile.write(str(count))
            ivyFile.write(" = {\n\t\t")
            ivyFile.write("if selector.execute_r")
            ivyFile.write(str(count))
            ivyFile.write(" {\n\t\t\tcall inspector.check_guard_r")
            ivyFile.write(str(count))
            ivyFile.write("(")
            ivyFile.write("r_")
            ivyFile.write(obj.reactant1)
            ivyFile.write(")")
            for x in range(obj.reactant1Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant1)
                ivyFile.write(" := updater.decr(")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant1)
                ivyFile.write(")")
            for x in range(obj.product1Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.product1)
                ivyFile.write(" := updater.incr(")
                ivyFile.write("r_")
                ivyFile.write(obj.product1)
                ivyFile.write(")")
            for x in range(obj.product2Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.product2)
                ivyFile.write(" := updater.incr(")
                ivyFile.write("r_")
                ivyFile.write(obj.product2)
                ivyFile.write(")")
            if obj.priority >= 25:
                ivyFile.write(";\n\t\t")
                ivyFile.write("\tif ")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                if upOrDown == "1":
                    ivyFile.write(" >= ")
                elif upOrDown == "2":
                    ivyFile.write(" > ")
                elif upOrDown == "3":
                    ivyFile.write(" <= ")
                elif upOrDown == "4":
                    ivyFile.write(" < ")
                ivyFile.write(str(targetNum))
                ivyFile.write(" {\n\t\t\t\tcall goal.achieved(")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                ivyFile.write(")\n\t\t\t}\n\t\t")
            else:
                ivyFile.write(";\n\t\t\tr")
                ivyFile.write(str(count))
                ivyFile.write("_executions := updater.incr(r")
                ivyFile.write(str(count))
                ivyFile.write("_executions)")
                ivyFile.write("\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 != "" and obj.reactant2 != "" and obj.product1 == ""):
            ivyFile.write("action update_r")
            ivyFile.write(str(count))
            ivyFile.write(" = {\n\t\t")
            ivyFile.write("if selector.execute_r")
            ivyFile.write(str(count))
            ivyFile.write(" {\n\t\t\tcall inspector.check_guard_r")
            ivyFile.write(str(count))
            ivyFile.write("(")
            ivyFile.write("r_")
            ivyFile.write(obj.reactant1)
            ivyFile.write(",")
            ivyFile.write("r_")
            ivyFile.write(obj.reactant2)
            ivyFile.write(")")
            for x in range(obj.reactant1Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant1)
                ivyFile.write(" := updater.decr(")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant1)
                ivyFile.write(")")
            for x in range(obj.reactant2Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant2)
                ivyFile.write(" := updater.decr(")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant2)
                ivyFile.write(")")
            if obj.priority >= 25:
                ivyFile.write(";\n\t\t")
                ivyFile.write("\tif ")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                if upOrDown == "1":
                    ivyFile.write(" >= ")
                elif upOrDown == "2":
                    ivyFile.write(" > ")
                elif upOrDown == "3":
                    ivyFile.write(" <= ")
                elif upOrDown == "4":
                    ivyFile.write(" < ")
                ivyFile.write(str(targetNum))
                ivyFile.write(" {\n\t\t\t\tcall goal.achieved(")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                ivyFile.write(")\n\t\t\t}\n\t\t")
            else:
                ivyFile.write(";\n\t\t\tr")
                ivyFile.write(str(count))
                ivyFile.write("_executions := updater.incr(r")
                ivyFile.write(str(count))
                ivyFile.write("_executions)")
                ivyFile.write("\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 != "" and obj.reactant2 != "" and obj.product1 != "" and obj.product2 == ""):
            ivyFile.write("action update_r")
            ivyFile.write(str(count))
            ivyFile.write(" = {\n\t\t")
            ivyFile.write("if selector.execute_r")
            ivyFile.write(str(count))
            ivyFile.write(" {\n\t\t\tcall inspector.check_guard_r")
            ivyFile.write(str(count))
            ivyFile.write("(")
            ivyFile.write("r_")
            ivyFile.write(obj.reactant1)
            ivyFile.write(",")
            ivyFile.write("r_")
            ivyFile.write(obj.reactant2)
            ivyFile.write(")")
            for x in range(obj.reactant1Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant1)
                ivyFile.write(" := updater.decr(")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant1)
                ivyFile.write(")")
            for x in range(obj.reactant2Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant2)
                ivyFile.write(" := updater.decr(")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant2)
                ivyFile.write(")")
            for x in range(obj.product1Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.product1)
                ivyFile.write(" := updater.incr(")
                ivyFile.write("r_")
                ivyFile.write(obj.product1)
                ivyFile.write(")")
            if obj.priority >= 25:
                ivyFile.write(";\n\t\t")
                ivyFile.write("\tif ")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                if upOrDown == "1":
                    ivyFile.write(" >= ")
                elif upOrDown == "2":
                    ivyFile.write(" > ")
                elif upOrDown == "3":
                    ivyFile.write(" <= ")
                elif upOrDown == "4":
                    ivyFile.write(" < ")
                ivyFile.write(str(targetNum))
                ivyFile.write(" {\n\t\t\t\tcall goal.achieved(")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                ivyFile.write(")\n\t\t\t}\n\t\t")
            else:
                ivyFile.write(";\n\t\t\tr")
                ivyFile.write(str(count))
                ivyFile.write("_executions := updater.incr(r")
                ivyFile.write(str(count))
                ivyFile.write("_executions)")
                ivyFile.write("\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 != "" and obj.reactant2 != "" and obj.product1 != "" and obj.product2 != ""):
            ivyFile.write("action update_r")
            ivyFile.write(str(count))
            ivyFile.write(" = {\n\t\t")
            ivyFile.write("if selector.execute_r")
            ivyFile.write(str(count))
            ivyFile.write(" {\n\t\t\tcall inspector.check_guard_r")
            ivyFile.write(str(count))
            ivyFile.write("(")
            ivyFile.write("r_")
            ivyFile.write(obj.reactant1)
            ivyFile.write(",")
            ivyFile.write("r_")
            ivyFile.write(obj.reactant2)
            ivyFile.write(")")
            for x in range(obj.reactant1Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant1)
                ivyFile.write(" := updater.decr(")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant1)
                ivyFile.write(")")
            for x in range(obj.reactant2Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant2)
                ivyFile.write(" := updater.decr(")
                ivyFile.write("r_")
                ivyFile.write(obj.reactant2)
                ivyFile.write(")")
            for x in range(obj.product1Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.product1)
                ivyFile.write(" := updater.incr(")
                ivyFile.write("r_")
                ivyFile.write(obj.product1)
                ivyFile.write(")")
            for x in range(obj.product2Num):
                ivyFile.write(";\n\t\t\t")
                ivyFile.write("r_")
                ivyFile.write(obj.product2)
                ivyFile.write(" := updater.incr(")
                ivyFile.write("r_")
                ivyFile.write(obj.product2)
                ivyFile.write(")")
            if obj.priority >= 25:
                ivyFile.write(";\n\t\t")
                ivyFile.write("\tif ")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                if upOrDown == "1":
                    ivyFile.write(" >= ")
                elif upOrDown == "2":
                    ivyFile.write(" > ")
                elif upOrDown == "3":
                    ivyFile.write(" <= ")
                elif upOrDown == "4":
                    ivyFile.write(" < ")
                ivyFile.write(str(targetNum))
                ivyFile.write(" {\n\t\t\t\tcall goal.achieved(")
                ivyFile.write("r_")
                ivyFile.write(targetSpecies)
                ivyFile.write(")\n\t\t\t}\n\t\t")
            else:
                ivyFile.write(";\n\t\t\tr")
                ivyFile.write(str(count))
                ivyFile.write("_executions := updater.incr(r")
                ivyFile.write(str(count))
                ivyFile.write("_executions)")
                ivyFile.write("\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")

ivyFile.write("\n\n\taction idling = {}\n\n\t")
count = 0
for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write("before update_r")
        ivyFile.write(str(count))
        if (Reactions[count-1].reactant1 == ""):
            ivyFile.write(" {\n\t\tassert idle = 0;\n\t\tassert enabled_checker.is_enabled_r")
            ivyFile.write(str(count))
            count1 = 0
            count2 = 0
            if obj.priority <= 17:
                ivyFile.write(";\n\t\tassert false")
            if obj.priority < 25:
                for y in  reactions:
                    count1 += 1
                    if y.priority > 15 and y.priority < 25:
                        count2 += 1
                        if count2 == 1:
                            ivyFile.write(";\n\t\tassert (r")
                            ivyFile.write(str(count1))
                            ivyFile.write("_executions")
                            ivyFile.write(" * ")
                            for x in secondTargetList:
                                if y.product1 == x.name:
                                    ivyFile.write(str(y.product1Num))
                                elif y.product2 == x.name:
                                    ivyFile.write(str(y.product2Num))
                        if count2 >= 2:
                            ivyFile.write(" + r")
                            ivyFile.write(str(count1))
                            ivyFile.write("_executions")
                            ivyFile.write(" * ")
                            for x in secondTargetList:
                                if y.product1 == x.name:
                                    ivyFile.write(str(y.product1Num))
                                elif y.product2 == x.name:
                                    ivyFile.write(str(y.product2Num))
                    if count1 == numOfReactions:
                        ivyFile.write(") < ")
                        for x in secondTargetList:
                            if x.name == obj.product1 or x.name == obj.product2:
                                ivyFile.write(str(x.minAmount)) #this needs to modified to be universal
                if obj.priority <= 17:
                    ivyFile.write(";\n\t\tassert false")
            ivyFile.write("\n\t}\n\t")
        elif(Reactions[count-1].reactant1 != "" and Reactions[count-1].reactant2 == ""):
            ivyFile.write(" {\n\t\tassert idle = 0;\n\t\tassert enabled_checker.is_enabled_r")
            ivyFile.write(str(count))
            ivyFile.write("(")
            ivyFile.write("r_")
            ivyFile.write(Reactions[count-1].reactant1)
            ivyFile.write(")")
            count1 = 0
            count2 = 0
            if obj.priority <= 17:
                ivyFile.write(";\n\t\tassert false")
            if obj.priority < 25:
                for y in  reactions:
                    count1 += 1
                    if y.priority > 15 and y.priority < 25:
                        count2 += 1
                        if count2 == 1:
                            ivyFile.write(";\n\t\tassert (r")
                            ivyFile.write(str(count1))
                            ivyFile.write("_executions")
                            ivyFile.write(" * ")
                            for x in secondTargetList:
                                if y.product1 == x.name:
                                    ivyFile.write(str(y.product1Num))
                                elif y.product2 == x.name:
                                    ivyFile.write(str(y.product2Num))
                        if count2 >= 2:
                            ivyFile.write(" + r")
                            ivyFile.write(str(count1))
                            ivyFile.write("_executions")
                            ivyFile.write(" * ")
                            for x in secondTargetList:
                                if y.product1 == x.name:
                                    ivyFile.write(str(y.product1Num))
                                elif y.product2 == x.name:
                                    ivyFile.write(str(y.product2Num))
                    if count1 == numOfReactions:
                        ivyFile.write(") < ")
                        for x in secondTargetList:
                            if x.name == obj.product1 or x.name == obj.product2:
                                ivyFile.write(str(x.minAmount)) #this needs to modified to be universal
                if obj.priority <= 17:
                    ivyFile.write(";\n\t\tassert false")
            ivyFile.write("\n\t}\n\t")
        elif(Reactions[count-1].reactant1 != "" and Reactions[count-1].reactant2 != ""):
            ivyFile.write(" {\n\t\tassert idle = 0;\n\t\tassert enabled_checker.is_enabled_r")
            ivyFile.write(str(count))
            ivyFile.write("(")
            ivyFile.write("r_")
            ivyFile.write(Reactions[count-1].reactant1)
            ivyFile.write(",")
            ivyFile.write("r_")
            ivyFile.write(Reactions[count-1].reactant2)
            ivyFile.write(")")
            count1 = 0
            count2 = 0
            if obj.priority <= 17:
                ivyFile.write(";\n\t\tassert false")
            if obj.priority < 25:
                for y in  reactions:
                    count1 += 1
                    if y.priority > 15 and y.priority < 25:
                        count2 += 1
                        if count2 == 1:
                            ivyFile.write(";\n\t\tassert (r")
                            ivyFile.write(str(count1))
                            ivyFile.write("_executions")
                            ivyFile.write(" * ")
                            for x in secondTargetList:
                                if y.product1 == x.name:
                                    ivyFile.write(str(y.product1Num))
                                elif y.product2 == x.name:
                                    ivyFile.write(str(y.product2Num))
                        if count2 >= 2:
                            ivyFile.write(" + r")
                            ivyFile.write(str(count1))
                            ivyFile.write("_executions")
                            ivyFile.write(" * ")
                            for x in secondTargetList:
                                if y.product1 == x.name:
                                    ivyFile.write(str(y.product1Num))
                                elif y.product2 == x.name:
                                    ivyFile.write(str(y.product2Num))
                    if count1 == numOfReactions:
                        ivyFile.write(") < ")
                        for x in secondTargetList:
                            if x.name == obj.product1 or x.name == obj.product2:
                                ivyFile.write(str(x.minAmount)) #this needs to modified to be universal
                if obj.priority <= 17:
                    ivyFile.write(";\n\t\tassert false")
            ivyFile.write("\n\t}\n\n\t")


ivyFile.write("\n\n\tbefore idling {\n\t\tassert idle = 1\n\t}\n}\n")

#ivyFile.write("\n\n\tafter idling {\n\t\tassert idle = 0\n\t}\n}\n") #this causes assertion failure for the first run

count = 0
for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write("export protocol.update_r")
        ivyFile.write(str(count))
        ivyFile.write("\n")


ivyFile.write("export protocol.idling\nimport goal.achieved\n")

count = 0
for obj in  reactions:
    count= count + 1
    if obj.priority > 15:
        ivyFile.write("import inspector.check_guard_r")
        ivyFile.write(str(count))
        ivyFile.write("\n")

ivyFile.write("\nisolate iso_proto = protocol with enabled_checker, updater, goal, selector, inspector")

ivyFile.close()        #ivy model complete

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

for x in range(numOfReactions):
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
            for x in range(numOfReactions):
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

for x in range(numOfReactions):
    Total.append(0)

Totaliterlist = []
Totaltranlist = []

iterations = []
for x in range(numOfReactions):
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
        for x in range(numOfReactions):
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

for x in range(numOfReactions):
    print("\n\nAverage number of reaction", x+1, "executions in a trace is:", Total[x]/int(runswanted))
    print("\nThe biggest number of reaction", x+1, "executions recorded in a trace is:", max(iterations[x]))
    print("\nThe smallest number of reaction", x+1, "executions recorded in a trace is:", min(iterations[x]))

"""
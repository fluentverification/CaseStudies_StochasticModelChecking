import subprocess
import math
import os

class Reaction:
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

class Species:
    def __init__(self, value, name):
        self.value = value
        self.name = name

class SecondTarget:
    def __init__(self, name, minAmount):
        self.name = name
        self.minAmount = minAmount

class TargetReaction:
    def __init__(self, reaction, secondTargets):
        self.reaction = reaction
        self.secondTargets = secondTargets

numOfReactions = int(input("Number of reactions: "))

o = "{"
c = "}"

reactions = []
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
            exit(1)
        secondReactant = input("What is the second reactant (if no second reactant type 'NA' or leave blank): ")
        if(secondReactant.lower() == "na" or secondReactant == ""):
            secondReactant = ""
            secondReactantNum = 0
        else:
            secondReactantNum = int(input("What amount of this reactant is needed (type an integer): "))
            if (secondReactantNum == 0):
                print("Error, must be greater than 0, please start over")
                exit(1)
    firstProduct = input("What is the first product (if no products type 'NA' or leave blank): ")
    if(firstProduct.lower() == "na" or firstProduct == ""):
        if(firstReactant == ""):
            print("Error, this reaction has no reactants or products please start over")
            exit(1)
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
    reactions.append(Reaction(firstReactant,firstReactantNum,secondReactant,secondReactantNum,firstProduct,firstProductNum,secondProduct,secondProductNum,15))

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
    speciesList.append(Species(val, obj))

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


for obj in reactions:       #secondary target species identified and added to a list of secondary target species, also given minAmount value (amount needed for reaction to fire enough times to get to target state)
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

for obj in secondTargetList:
    print(f"{obj.name}, {obj.minAmount}\n")
            
 
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

ivyFile.write(f"""#lang ivy 1.7

object updater = {o}
    type num
    interpret num -> bv[10]
    type exec_var
    interpret exec_var -> bv[8]
    type exec_stage
    interpret exec_stage -> bv[3]
    
    action incr(x:num) returns(y:num) = {o}
        y := x + 1
    {c}
    
    action decr(x:num) returns(y:num) = {o}
        y := x - 1
    {c}
{c}

""")

if upOrDown == "1":
    equality = ">= "
elif upOrDown == "2":
    equality = "> "
elif upOrDown == "3":
    equality = "<= "
elif upOrDown == "4":
    equality = "< "

ivyFile.write(f"""
object goal = {o}
    action achieved(v:updater.num)
    object spec = {o}
        before achieved {o}
            assert v {equality} {targetNum};
            protocol.idle := 1
        {c}
    {c}
{c}

""")

ivyFile.write("object enabled_checker = {\n\n\t")

count = 0
for obj in  reactions:
    count += 1
    if obj.priority > 15:
        ivyFile.write(f"action is_enabled_r{count}") 
        if (reactions[count-1].reactant1 == ""):
            ivyFile.write(f""" returns(y:bool) = {o}
        y := true
    {c}
                
    """)
        elif(reactions[count-1].reactant1 != "" and reactions[count-1].reactant2 == ""):
            ivyFile.write(f"""(reactant1:updater.num) returns(y:bool) = {o}
        if reactant1 >= {obj.reactant1Num} {o}
            y:= true
        {c}
        else {o}
            y:= false
            {c}
        {c}
        
    """)
        elif(reactions[count-1].reactant1 != "" and reactions[count-1].reactant2 != ""):
            ivyFile.write(f"""(reactant1:updater.num,reactant2:updater.num) returns(y:bool) = {o}
        if reactant1 >= {obj.reactant1Num} & reactant2 >= {obj.reactant2Num} {o}
            y := true
        {c}
        else {o}
            y := false
        {c}
    {c}
                    
    """)
ivyFile.write("\n}\n\n")

ivyFile.write("object inspector = {\n\t")
count = 0
for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write(f"action check_guard_r{count}")
        if (reactions[count-1].reactant1 == ""):
            ivyFile.write(f"""
    before check_guard_r{count} {o}
        assert true
    {c}
    
    """)
        elif(reactions[count-1].reactant1 != "" and reactions[count-1].reactant2 == ""):
            ivyFile.write(f"""(reactant1:updater.num)\n\tbefore check_guard_r{count} {o}
        assert reactant1 >= {obj.reactant1Num}
    {c}
    
    """)
        elif(reactions[count-1].reactant1 != "" and reactions[count-1].reactant2 != ""):
            ivyFile.write(f"""(reactant1:updater.num,reactant2:updater.num)
    before check_guard_r{count} {o}
        assert reactant1 >= {obj.reactant1Num} & reactant2 >= {obj.reactant2Num}
    {c}
    
    """)
        
ivyFile.write("\n}")

ivyFile.write("\n\nobject selector = {\n\t")

count = 0

for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write(f"individual r{count}_exec : updater.exec_var\n\t")

ivyFile.write("\n\t")
count = 0

for obj in  reactions:
    count += 1
    if obj.priority > 15:
        ivyFile.write(f"individual r{count}_rate : updater.exec_var\n\t")

ivyFile.write("\n\t")

count = 0
for obj in  reactions:
    count += 1
    if obj.priority > 15:
        ivyFile.write(f"individual r{count}_count : updater.exec_var\n\t")

ivyFile.write("\n\t")

count = 0
for obj in  reactions:
    count += 1
    if obj.priority > 15:
        ivyFile.write(f"individual r{count}_count_rate : updater.exec_var\n\t")

ivyFile.write("\n\t")

count = 0
for obj in  reactions:
    count += 1
    if obj.priority > 15:
        ivyFile.write(f"individual r{count}_stage : updater.exec_stage\n\t")

ivyFile.write("\n\n\tafter init {\n\t\t")

count = 0
for obj in  reactions:
    count += 1
    if obj.priority > 15:
        ivyFile.write(f"r{count}_count := 0;\n\t\t")

ivyFile.write("\n\n\t\t")
count = 0
for obj in  reactions:
    count += 1
    if obj.priority > 15:
        ivyFile.write(f"r{count}_count_rate := 4;\n\t\t")

ivyFile.write("\n\t}\n\n\t")

count = 0
for obj in  reactions:
    count += 1
    if obj.priority > 15:
        ivyFile.write(f"""action execute_r{count} returns(y:bool) = {o}
        r{count}_exec := r{count}_exec + 1;
        if r{count}_exec >= r{count}_rate {o}
            y := true;
            r{count}_exec := 0;
            r{count}_count := r{count}_count + 1
        {c}
        else {o}
            y := false
        {c};
        if r{count}_count >= r{count}_count_rate {o}
            r{count}_stage := r{count}_stage + 1;
            r{count}_count := 0
        {c};
        """)
        if obj.priority >= 23:
            ivyFile.write(f"""if r{count}_stage = 0 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 1
        {c}
        else if r{count}_stage = 1 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 1
        {c}
        else if r{count}_stage = 2 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 1
        {c}
        else if r{count}_stage = 3 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 1
        {c}
        else if r{count}_stage = 4 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 1
        {c}
        else if r{count}_stage = 5 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 1
        {c}
        else if r{count}_stage = 6 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 1
        {c}
        else if r{count}_stage = 7 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 1
        {c}
        else {o}
            r{count}_stage := 0
        {c}
    {c}

    """)
        elif obj.priority >= 21:
            ivyFile.write(f"""if r{count}_stage = 0 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 1
        {c}
        else if r{count}_stage = 1 {o}
            r{count}_count_rate := 2;
            r{count}_rate := 2
        {c}
        else if r{count}_stage = 2 {o}
            r{count}_count_rate := 2;
            r{count}_rate := 1
        {c}
        else if r{count}_stage = 3 {o}
            r{count}_count_rate := 3;
            r{count}_rate := 2
        {c}
        else if r{count}_stage = 4 {o}
            r{count}_count_rate := 5;
            r{count}_rate := 1
        {c}
        else if r{count}_stage = 5 {o}
            r{count}_count_rate := 2;
            r{count}_rate := 2
        {c}
        else if r{count}_stage = 6 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 1
        {c}
        else if r{count}_stage = 7 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 2
        {c}
        else {o}
            r{count}_stage := 0
        {c}
    {c}

    """)
        elif obj.priority >= 19:
            ivyFile.write(f"""if r{count}_stage = 0 {o}
            r{count}_count_rate := 3;
            r{count}_rate := 3
        {c}
        else if r{count}_stage = 1 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 4
        {c}
        else if r{count}_stage = 2 {o}
            r{count}_count_rate := 2;
            r{count}_rate := 3
        {c}
        else if r{count}_stage = 3 {o}
            r{count}_count_rate := 3;
            r{count}_rate := 4
        {c}
        else if r{count}_stage = 4 {o}
            r{count}_count_rate := 3;
            r{count}_rate := 3
        {c}
        else if r{count}_stage = 5 {o}
            r{count}_count_rate := 2;
            r{count}_rate := 2
        {c}
        else if r{count}_stage = 6 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 3
        {c}
        else if r{count}_stage = 7 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 4
        {c}
        else {o}
            r{count}_stage := 0
        {c}
    {c}

    """)
        elif obj.priority == 18:
            ivyFile.write(f"""if r{count}_stage = 0 {o}
            r{count}_count_rate := 5;
            r{count}_rate := 30
        {c}
        else if r{count}_stage = 1 {o}
            r{count}_count_rate := 3;
            r{count}_rate := 28
        {c}
        else if r{count}_stage = 2 {o}
            r{count}_count_rate := 2;
            r{count}_rate := 34
        {c}
        else if r{count}_stage = 3 {o}
            r{count}_count_rate := 9;
            r{count}_rate := 25
        {c}
        else if r{count}_stage = 4 {o}
            r{count}_count_rate := 36;
            r{count}_rate := 5
        {c}
        else if r{count}_stage = 5 {o}
            r{count}_count_rate := 2;
            r{count}_rate := 29
        {c}
        else if r{count}_stage = 6 {o}
            r{count}_count_rate := 5;
            r{count}_rate := 30
        {c}
        else if r{count}_stage = 7 {o}
            r{count}_count_rate := 1;
            r{count}_rate := 34
        {c}
        else {o}
            r{count}_stage := 0
        {c}
    {c}

    """)
        elif obj.priority == 17:
            ivyFile.write(f"""if r{count}_stage = 0 {o}
            r{count}_count_rate := 1;
            r{count}_rate := 200
        {c}
        else if r{count}_stage = 1 {o}
            r{count}_count_rate := 3;
            r{count}_rate := 189
        {c}
        else if r{count}_stage = 2 {o}
            r{count}_count_rate := 2;
            r{count}_rate := 192
        {c}
        else if r{count}_stage = 3 {o}
            r{count}_count_rate := 9;
            r{count}_rate := 212
        {c}
        else if r{count}_stage = 4 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 192
        {c}
        else if r{count}_stage = 5 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 232
        {c}
        else if r{count}_stage = 6 {o}
            r{count}_count_rate := 5;
            r{count}_rate := 190
        {c}
        else if r{count}_stage = 7 {o}
            r{count}_count_rate := 3;
            r{count}_rate := 200
        {c}
        else {o}
            r{count}_stage := 0
        {c}
    {c}

    """)
        elif obj.priority == 16:
            ivyFile.write(f"""if r{count}_stage = 0 {o}
            r{count}_count_rate := 5;
            r{count}_rate := 1000
        {c}
        else if r{count}_stage = 1 {o}
            r{count}_count_rate := 3;
            r{count}_rate := 989
        {c}
        else if r{count}_stage = 2 {o}
            r{count}_count_rate := 2;
            r{count}_rate := 1190
        {c}
        else if r{count}_stage = 3 {o}
            r{count}_count_rate := 9;
            r{count}_rate := 1050
        {c}
        else if r{count}_stage = 4 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 942
        {c}
        else if r{count}_stage = 5 {o}
            r{count}_count_rate := 2;
            r{count}_rate := 1012
        {c}
        else if r{count}_stage = 6 {o}
            r{count}_count_rate := 5;
            r{count}_rate := 930
        {c}
        else if r{count}_stage = 7 {o}
            r{count}_count_rate := 1;
            r{count}_rate := 1000
        {c}
        else {o}
            r{count}_stage := 0
        {c}
    {c}

    """)

ivyFile.write("\n}\n")

ivyFile.write("\nobject protocol = {\n\n\ttype 2bit\n\tinterpret 2bit -> bv[1]\n\tindividual idle : 2bit\n\n")

for obj in spec:
    ivyFile.write(f"\tindividual r_{obj} : updater.num\n")

ivyFile.write("\n\tafter init {\n\t\t")

for obj in speciesList:
    ivyFile.write(f"r_{obj.name} := {obj.value};\n\t\t")

ivyFile.write("idle := 0\n\t}\n\n\t")

count = 0
for obj in  reactions:
    count += 1
    if obj.priority > 15:
        if(obj.reactant1 == "" and obj.product1 != "" and obj.product2 == ""):
            ivyFile.write(f"""action update_r{count} =  {o}
        if selector.execute_r{count} {o}
            call inspector.check_guard_r{count}""")
            for x in range(obj.product1Num):
                ivyFile.write(f";\n\t\t\tr_{obj.product1} := updater.incr(r_{obj.product1})")
            if obj.priority >= 25:
                ivyFile.write(f";\n\t\t\tif r_{targetSpecies} {equality} {targetNum} {o}\n\t\t\t\tcall goal.achieved(r_{targetSpecies})\n\t\t\t{c}\n\t\t")
            else:
                ivyFile.write("\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 == "" and obj.product1 != "" and obj.product2 != ""):
            ivyFile.write(f"""action update_r{count} = {o}
        if selector.execute_r{count} {o}
            call inspector.check_guard_r{count}""")
            for x in range(obj.product1Num):
                ivyFile.write(f";\n\t\t\tr_{obj.product1} := updater.incr(r_{obj.product1})")
            for x in range(obj.product2Num):
                ivyFile.write(f";\n\t\t\tr_{obj.product2} := updater.incr(r_{obj.product2})")
            if obj.priority >= 25:
                ivyFile.write(f";\n\t\t\tif r_{targetSpecies} {equality} {targetNum} {o}\n\t\t\t\tcall goal.achieved(r_{targetSpecies})\n\t\t\t{c}\n\t\t")
            else:
                ivyFile.write("\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 != "" and obj.reactant2 == "" and obj.product1 == ""):
            ivyFile.write(f"""action update_r{count} =  {o}
        if selector.execute_r{count} {o}
            call inspector.check_guard_r{count}(r_{obj.reactant1})""")
            for x in range(obj.reactant1Num):
                ivyFile.write(f";\n\t\t\tr_{obj.reactant1} := updater.decr(r_{obj.reactant1})")
            if obj.priority >= 25:
                ivyFile.write(f";\n\t\t\tif r_{targetSpecies} {equality} {targetNum} {o}\n\t\t\t\tcall goal.achieved(r_{targetSpecies})\n\t\t\t{c}\n\t\t")
            else:
                ivyFile.write("\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 != "" and obj.reactant2 == "" and obj.product1 != "" and obj.product2 == ""):
            ivyFile.write(f"""action update_r{count} =  {o}
        if selector.execute_r{count} {o}
            call inspector.check_guard_r{count}(r_{obj.reactant1})""")
            for x in range(obj.reactant1Num):
                ivyFile.write(f";\n\t\t\tr_{obj.reactant1} := updater.decr(r_{obj.reactant1})")
            for x in range(obj.product1Num):
                ivyFile.write(f";\n\t\t\tr_{obj.product1} := updater.incr(r_{obj.product1})")
            if obj.priority >= 25:
                ivyFile.write(f";\n\t\t\tif r_{targetSpecies} {equality} {targetNum} {o}\n\t\t\t\tcall goal.achieved(r_{targetSpecies})\n\t\t\t{c}\n\t\t")
            else:
                ivyFile.write("\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 != "" and obj.reactant2 == "" and obj.product1 != "" and obj.product2 != ""):
            ivyFile.write(f"""action update_r{count} =  {o}
        if selector.execute_r{count} {o}
            call inspector.check_guard_r{count}(r_{obj.reactant1})""")
            for x in range(obj.reactant1Num):
                ivyFile.write(f";\n\t\t\tr_{obj.reactant1} := updater.decr(r_{obj.reactant1})")
            for x in range(obj.product1Num):
                ivyFile.write(f";\n\t\t\tr_{obj.product1} := updater.incr(r_{obj.product1})")
            for x in range(obj.product2Num):
                ivyFile.write(f";\n\t\t\tr_{obj.product2} := updater.incr(r_{obj.product2})")
            if obj.priority >= 25:
                ivyFile.write(f";\n\t\t\tif r_{targetSpecies} {equality} {targetNum} {o}\n\t\t\t\tcall goal.achieved(r_{targetSpecies})\n\t\t\t{c}\n\t\t")
            else:
                ivyFile.write("\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 != "" and obj.reactant2 != "" and obj.product1 == ""):
            ivyFile.write(f"""action update_r{count} =  {o}
        if selector.execute_r{count} {o}
            call inspector.check_guard_r{count}(r_{obj.reactant1},r_{obj.reactant2})""")
            for x in range(obj.reactant1Num):
                ivyFile.write(f";\n\t\t\tr_{obj.reactant1} := updater.decr(r_{obj.reactant1})")
            for x in range(obj.reactant2Num):
                ivyFile.write(f";\n\t\t\tr_{obj.reactant2} := updater.decr(r_{obj.reactant2})")
            if obj.priority >= 25:
                ivyFile.write(f";\n\t\t\tif r_{targetSpecies} {equality} {targetNum} {o}\n\t\t\t\tcall goal.achieved(r_{targetSpecies})\n\t\t\t{c}\n\t\t")
            else:
                ivyFile.write("\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 != "" and obj.reactant2 != "" and obj.product1 != "" and obj.product2 == ""):
            ivyFile.write(f"""action update_r{count} =  {o}
        if selector.execute_r{count} {o}
            call inspector.check_guard_r{count}(r_{obj.reactant1},r_{obj.reactant2})""")
            for x in range(obj.reactant1Num):
                ivyFile.write(f";\n\t\t\tr_{obj.reactant1} := updater.decr(r_{obj.reactant1})")
            for x in range(obj.reactant2Num):
                ivyFile.write(f";\n\t\t\tr_{obj.reactant2} := updater.decr(r_{obj.reactant2})")
            for x in range(obj.product1Num):
                ivyFile.write(f";\n\t\t\tr_{obj.product1} := updater.incr(r_{obj.product1})")
            if obj.priority >= 25:
                ivyFile.write(f";\n\t\t\tif r_{targetSpecies} {equality} {targetNum} {o}\n\t\t\t\tcall goal.achieved(r_{targetSpecies})\n\t\t\t{c}\n\t\t")
            else:
                ivyFile.write("\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 != "" and obj.reactant2 != "" and obj.product1 != "" and obj.product2 != ""):
            ivyFile.write(f"""action update_r{count} =  {o}
        if selector.execute_r{count} {o}
            call inspector.check_guard_r{count}(r_{obj.reactant1},r_{obj.reactant2})""")
            for x in range(obj.reactant1Num):
                ivyFile.write(f";\n\t\t\tr_{obj.reactant1} := updater.decr(r_{obj.reactant1})")
            for x in range(obj.reactant2Num):
                ivyFile.write(f";\n\t\t\tr_{obj.reactant2} := updater.decr(r_{obj.reactant2})")
            for x in range(obj.product1Num):
                ivyFile.write(f";\n\t\t\tr_{obj.product1} := updater.incr(r_{obj.product1})")
            for x in range(obj.product2Num):
                ivyFile.write(f";\n\t\t\tr_{obj.product2} := updater.incr(r_{obj.product2})")
            if obj.priority >= 25:
                ivyFile.write(f";\n\t\t\tif r_{targetSpecies} {equality} {targetNum} {o}\n\t\t\t\tcall goal.achieved(r_{targetSpecies})\n\t\t\t{c}\n\t\t")
            else:
                ivyFile.write("\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")

ivyFile.write("\n\n\taction idling = {}\n\n\t")

ivyFile.write("\n\n\taction fail_test = {}\n\n\t")

count = 0
for obj in  reactions:
    count += 1
    if obj.priority > 15:
        ivyFile.write(f"before update_r{count}")
        if (reactions[count-1].reactant1 == ""):
            ivyFile.write(f" {o}\n\t\tassert idle = 0;\n\t\tassert enabled_checker.is_enabled_r{count}")
            if obj.priority <= 6:
                ivyFile.write(";\n\t\tassert false")
            ivyFile.write("\n\t}\n\t")
        elif(reactions[count-1].reactant1 != "" and reactions[count-1].reactant2 == ""):
            ivyFile.write(f" {o}\n\t\tassert idle = 0;\n\t\tassert enabled_checker.is_enabled_r{count}(r_{obj.reactant1})")
            if obj.priority <= 6:
                ivyFile.write(";\n\t\tassert false")
            ivyFile.write("\n\t}\n\t")
        elif(reactions[count-1].reactant1 != "" and reactions[count-1].reactant2 != ""):
            ivyFile.write(f" {o}\n\t\tassert idle = 0;\n\t\tassert enabled_checker.is_enabled_r{count}(r_{obj.reactant1},r_{obj.reactant2})")
            if obj.priority <= 6:
                ivyFile.write(";\n\t\tassert false")
            ivyFile.write("\n\t}\n\n\t")


ivyFile.write("\n\n\tbefore idling {\n\t\tassert idle = 1\n\t}\n")

ivyFile.write("\n\n\tafter idling {\n\t\tassert idle = 0\n\t}\n\n") #this causes assertion failure for the first run

ivyFile.write("\n\n\tbefore fail_test {\n\t\tassert idle = 0;\n\t\tassert (")

count = 0
count1 = 0
for obj in reactions:
    count += 1
    if obj.priority > 15:
        count1 += 1
        if count1 != 1:
            ivyFile.write(" & ")
        if obj.reactant1 == "":
            ivyFile.write(f"enabled_checker.is_enabled_r{count} = false")
        if obj.reactant1 != "" and obj.reactant2 == "":
            ivyFile.write(f"enabled_checker.is_enabled_r{count}(r_{obj.reactant1}) = false")
        if obj.reactant1 != "" and obj.reactant2 != "":
            ivyFile.write(f"enabled_checker.is_enabled_r{count}(r_{obj.reactant1},r_{obj.reactant2}) = false")
    if count == numOfReactions:
        ivyFile.write(")\n\t}")
    
ivyFile.write("\n\n\tafter fail_test {\n\t\tassert idle = 1\n\t}\n\n}\n")

ivyFile.write("\nexport protocol.fail_test\n")

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


ivy_to_cpp_command = subprocess.Popen(["ivy_to_cpp", "isolate=iso_proto", "target=test", "build=true", "test_v2.ivy"])
ivy_to_cpp_command.wait()

print("starting to run initial test")
os.system("./test_v2 seed=367 iters=10000 runs=1 >test_v2.txt")
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
        if line[11:20] == "fail_test":
            print("Error occurred during randomized testing!") #We need to decide what we want to do at this point

if first_iters >= 10000:
    print("Trace not found to specified target from randomized testing")
    exit(1)

print("The iters recorded for this initial example is", first_iters)

######
ivyFile = open("test_v3.ivy", "w") #an ivy model for the CRN is made without assertion failure at first idling action

ivyFile.write(f"""#lang ivy 1.7

object updater = {o}
    type num
    interpret num -> bv[10]
    type exec_var
    interpret exec_var -> bv[8]
    type exec_stage
    interpret exec_stage -> bv[3]
    
    action incr(x:num) returns(y:num) = {o}
        y := x + 1
    {c}
    
    action decr(x:num) returns(y:num) = {o}
        y := x - 1
    {c}
{c}

""")

ivyFile.write(f"""
object goal = {o}
    action achieved(v:updater.num)
    object spec = {o}
        before achieved {o}
            assert v {equality} {targetNum};
            protocol.idle := 1
        {c}
    {c}
{c}

""")

ivyFile.write("object enabled_checker = {\n\n\t")

count = 0
for obj in  reactions:
    count += 1
    if obj.priority > 15:
        ivyFile.write(f"action is_enabled_r{count}") 
        if (reactions[count-1].reactant1 == ""):
            ivyFile.write(f""" returns(y:bool) = {o}
        y := true
    {c}
                
    """)
        elif(reactions[count-1].reactant1 != "" and reactions[count-1].reactant2 == ""):
            ivyFile.write(f"""(reactant1:updater.num) returns(y:bool) = {o}
        if reactant1 >= {obj.reactant1Num} {o}
            y:= true
        {c}
        else {o}
            y:= false
            {c}
        {c}
        
    """)
        elif(reactions[count-1].reactant1 != "" and reactions[count-1].reactant2 != ""):
            ivyFile.write(f"""(reactant1:updater.num,reactant2:updater.num) returns(y:bool) = {o}
        if reactant1 >= {obj.reactant1Num} & reactant2 >= {obj.reactant2Num} {o}
            y := true
        {c}
        else {o}
            y := false
        {c}
    {c}
                    
    """)
ivyFile.write("\n}\n\n")

ivyFile.write("object inspector = {\n\t")
count = 0
for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write(f"action check_guard_r{count}")
        if (reactions[count-1].reactant1 == ""):
            ivyFile.write(f"""
    before check_guard_r{count} {o}
        assert true
    {c}
    
    """)
        elif(reactions[count-1].reactant1 != "" and reactions[count-1].reactant2 == ""):
            ivyFile.write(f"""(reactant1:updater.num)\n\tbefore check_guard_r{count} {o}
        assert reactant1 >= {obj.reactant1Num}
    {c}
    
    """)
        elif(reactions[count-1].reactant1 != "" and reactions[count-1].reactant2 != ""):
            ivyFile.write(f"""(reactant1:updater.num,reactant2:updater.num)
    before check_guard_r{count} {o}
        assert reactant1 >= {obj.reactant1Num} & reactant2 >= {obj.reactant2Num}
    {c}
    
    """)
        
ivyFile.write("\n}")

ivyFile.write("\n\nobject selector = {\n\t")

count = 0

for obj in  reactions:
    count = count + 1
    if obj.priority > 15:
        ivyFile.write(f"individual r{count}_exec : updater.exec_var\n\t")

ivyFile.write("\n\t")
count = 0

for obj in  reactions:
    count += 1
    if obj.priority > 15:
        ivyFile.write(f"individual r{count}_rate : updater.exec_var\n\t")

ivyFile.write("\n\t")

count = 0
for obj in  reactions:
    count += 1
    if obj.priority > 15:
        ivyFile.write(f"individual r{count}_count : updater.exec_var\n\t")

ivyFile.write("\n\t")

count = 0
for obj in  reactions:
    count += 1
    if obj.priority > 15:
        ivyFile.write(f"individual r{count}_count_rate : updater.exec_var\n\t")

ivyFile.write("\n\t")

count = 0
for obj in  reactions:
    count += 1
    if obj.priority > 15:
        ivyFile.write(f"individual r{count}_stage : updater.exec_stage\n\t")

ivyFile.write("\n\n\tafter init {\n\t\t")

count = 0
for obj in  reactions:
    count += 1
    if obj.priority > 15:
        ivyFile.write(f"r{count}_count := 0;\n\t\t")

ivyFile.write("\n\n\t\t")
count = 0
for obj in  reactions:
    count += 1
    if obj.priority > 15:
        ivyFile.write(f"r{count}_count_rate := 4;\n\t\t")

ivyFile.write("\n\t}\n\n\t")

count = 0
for obj in  reactions:
    count += 1
    if obj.priority > 15:
        ivyFile.write(f"""action execute_r{count} returns(y:bool) = {o}
        r{count}_exec := r{count}_exec + 1;
        if r{count}_exec >= r{count}_rate {o}
            y := true;
            r{count}_exec := 0;
            r{count}_count := r{count}_count + 1
        {c}
        else {o}
            y := false
        {c};
        if r{count}_count >= r{count}_count_rate {o}
            r{count}_stage := r{count}_stage + 1;
            r{count}_count := 0
        {c};
        """)
        if obj.priority >= 23:
            ivyFile.write(f"""if r{count}_stage = 0 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 1
        {c}
        else if r{count}_stage = 1 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 1
        {c}
        else if r{count}_stage = 2 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 1
        {c}
        else if r{count}_stage = 3 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 1
        {c}
        else if r{count}_stage = 4 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 1
        {c}
        else if r{count}_stage = 5 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 1
        {c}
        else if r{count}_stage = 6 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 1
        {c}
        else if r{count}_stage = 7 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 1
        {c}
        else {o}
            r{count}_stage := 0
        {c}
    {c}

    """)
        elif obj.priority >= 21:
            ivyFile.write(f"""if r{count}_stage = 0 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 1
        {c}
        else if r{count}_stage = 1 {o}
            r{count}_count_rate := 2;
            r{count}_rate := 2
        {c}
        else if r{count}_stage = 2 {o}
            r{count}_count_rate := 2;
            r{count}_rate := 1
        {c}
        else if r{count}_stage = 3 {o}
            r{count}_count_rate := 3;
            r{count}_rate := 2
        {c}
        else if r{count}_stage = 4 {o}
            r{count}_count_rate := 5;
            r{count}_rate := 1
        {c}
        else if r{count}_stage = 5 {o}
            r{count}_count_rate := 2;
            r{count}_rate := 2
        {c}
        else if r{count}_stage = 6 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 1
        {c}
        else if r{count}_stage = 7 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 2
        {c}
        else {o}
            r{count}_stage := 0
        {c}
    {c}

    """)
        elif obj.priority >= 19:
            ivyFile.write(f"""if r{count}_stage = 0 {o}
            r{count}_count_rate := 3;
            r{count}_rate := 3
        {c}
        else if r{count}_stage = 1 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 4
        {c}
        else if r{count}_stage = 2 {o}
            r{count}_count_rate := 2;
            r{count}_rate := 3
        {c}
        else if r{count}_stage = 3 {o}
            r{count}_count_rate := 3;
            r{count}_rate := 4
        {c}
        else if r{count}_stage = 4 {o}
            r{count}_count_rate := 3;
            r{count}_rate := 3
        {c}
        else if r{count}_stage = 5 {o}
            r{count}_count_rate := 2;
            r{count}_rate := 2
        {c}
        else if r{count}_stage = 6 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 3
        {c}
        else if r{count}_stage = 7 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 4
        {c}
        else {o}
            r{count}_stage := 0
        {c}
    {c}

    """)
        elif obj.priority == 18:
            ivyFile.write(f"""if r{count}_stage = 0 {o}
            r{count}_count_rate := 5;
            r{count}_rate := 30
        {c}
        else if r{count}_stage = 1 {o}
            r{count}_count_rate := 3;
            r{count}_rate := 28
        {c}
        else if r{count}_stage = 2 {o}
            r{count}_count_rate := 2;
            r{count}_rate := 34
        {c}
        else if r{count}_stage = 3 {o}
            r{count}_count_rate := 9;
            r{count}_rate := 25
        {c}
        else if r{count}_stage = 4 {o}
            r{count}_count_rate := 36;
            r{count}_rate := 5
        {c}
        else if r{count}_stage = 5 {o}
            r{count}_count_rate := 2;
            r{count}_rate := 29
        {c}
        else if r{count}_stage = 6 {o}
            r{count}_count_rate := 5;
            r{count}_rate := 30
        {c}
        else if r{count}_stage = 7 {o}
            r{count}_count_rate := 1;
            r{count}_rate := 34
        {c}
        else {o}
            r{count}_stage := 0
        {c}
    {c}

    """)
        elif obj.priority == 17:
            ivyFile.write(f"""if r{count}_stage = 0 {o}
            r{count}_count_rate := 1;
            r{count}_rate := 200
        {c}
        else if r{count}_stage = 1 {o}
            r{count}_count_rate := 3;
            r{count}_rate := 189
        {c}
        else if r{count}_stage = 2 {o}
            r{count}_count_rate := 2;
            r{count}_rate := 192
        {c}
        else if r{count}_stage = 3 {o}
            r{count}_count_rate := 9;
            r{count}_rate := 212
        {c}
        else if r{count}_stage = 4 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 192
        {c}
        else if r{count}_stage = 5 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 232
        {c}
        else if r{count}_stage = 6 {o}
            r{count}_count_rate := 5;
            r{count}_rate := 190
        {c}
        else if r{count}_stage = 7 {o}
            r{count}_count_rate := 3;
            r{count}_rate := 200
        {c}
        else {o}
            r{count}_stage := 0
        {c}
    {c}

    """)
        elif obj.priority == 16:
            ivyFile.write(f"""if r{count}_stage = 0 {o}
            r{count}_count_rate := 5;
            r{count}_rate := 1000
        {c}
        else if r{count}_stage = 1 {o}
            r{count}_count_rate := 3;
            r{count}_rate := 989
        {c}
        else if r{count}_stage = 2 {o}
            r{count}_count_rate := 2;
            r{count}_rate := 1190
        {c}
        else if r{count}_stage = 3 {o}
            r{count}_count_rate := 9;
            r{count}_rate := 1050
        {c}
        else if r{count}_stage = 4 {o}
            r{count}_count_rate := 4;
            r{count}_rate := 942
        {c}
        else if r{count}_stage = 5 {o}
            r{count}_count_rate := 2;
            r{count}_rate := 1012
        {c}
        else if r{count}_stage = 6 {o}
            r{count}_count_rate := 5;
            r{count}_rate := 930
        {c}
        else if r{count}_stage = 7 {o}
            r{count}_count_rate := 1;
            r{count}_rate := 1000
        {c}
        else {o}
            r{count}_stage := 0
        {c}
    {c}

    """)

ivyFile.write("\n}\n")

ivyFile.write("\nobject protocol = {\n\n\ttype 2bit\n\tinterpret 2bit -> bv[1]\n\tindividual idle : 2bit\n\n")

for obj in spec:
    ivyFile.write(f"\tindividual r_{obj} : updater.num\n")

count = 0
for obj in reactions:
    count += 1
    if obj.priority > 15:
        ivyFile.write(f"\tindividual r{count}_executions : updater.num\n")

ivyFile.write("\n\tafter init {\n\t\t")

for obj in speciesList:
    ivyFile.write(f"r_{obj.name} := {obj.value};\n\t\t")

count = 0
for obj in reactions:
    count += 1
    if obj.priority > 15:
        ivyFile.write(f"r{count}_executions := 0;\n\t\t")

ivyFile.write("idle := 0\n\t}\n\n\t")

count = 0
for obj in  reactions:
    count += 1
    if obj.priority > 15:
        if(obj.reactant1 == "" and obj.product1 != "" and obj.product2 == ""):
            ivyFile.write(f"""action update_r{count} =  {o}
        if selector.execute_r{count} {o}
            call inspector.check_guard_r{count}""")
            for x in range(obj.product1Num):
                ivyFile.write(f";\n\t\t\tr_{obj.product1} := updater.incr(r_{obj.product1})")
            if obj.priority >= 25:
                ivyFile.write(f";\n\t\t\tif r_{targetSpecies} {equality} {targetNum} {o}\n\t\t\t\tcall goal.achieved(r_{targetSpecies})\n\t\t\t{c}\n\t\t")
            else:
                ivyFile.write(f";\n\t\t\tr{count}_executions := updater.incr(r{count}_executions)\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 == "" and obj.product1 != "" and obj.product2 != ""):
            ivyFile.write(f"""action update_r{count} = {o}
        if selector.execute_r{count} {o}
            call inspector.check_guard_r{count}""")
            for x in range(obj.product1Num):
                ivyFile.write(f";\n\t\t\tr_{obj.product1} := updater.incr(r_{obj.product1})")
            for x in range(obj.product2Num):
                ivyFile.write(f";\n\t\t\tr_{obj.product2} := updater.incr(r_{obj.product2})")
            if obj.priority >= 25:
                ivyFile.write(f";\n\t\t\tif r_{targetSpecies} {equality} {targetNum} {o}\n\t\t\t\tcall goal.achieved(r_{targetSpecies})\n\t\t\t{c}\n\t\t")
            else:
                ivyFile.write(f";\n\t\t\tr{count}_executions := updater.incr(r{count}_executions)\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 != "" and obj.reactant2 == "" and obj.product1 == ""):
            ivyFile.write(f"""action update_r{count} =  {o}
        if selector.execute_r{count} {o}
            call inspector.check_guard_r{count}(r_{obj.reactant1})""")
            for x in range(obj.reactant1Num):
                ivyFile.write(f";\n\t\t\tr_{obj.reactant1} := updater.decr(r_{obj.reactant1})")
            if obj.priority >= 25:
                ivyFile.write(f";\n\t\t\tif r_{targetSpecies} {equality} {targetNum} {o}\n\t\t\t\tcall goal.achieved(r_{targetSpecies})\n\t\t\t{c}\n\t\t")
            else:
                ivyFile.write(f";\n\t\t\tr{count}_executions := updater.incr(r{count}_executions)\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 != "" and obj.reactant2 == "" and obj.product1 != "" and obj.product2 == ""):
            ivyFile.write(f"""action update_r{count} =  {o}
        if selector.execute_r{count} {o}
            call inspector.check_guard_r{count}(r_{obj.reactant1})""")
            for x in range(obj.reactant1Num):
                ivyFile.write(f";\n\t\t\tr_{obj.reactant1} := updater.decr(r_{obj.reactant1})")
            for x in range(obj.product1Num):
                ivyFile.write(f";\n\t\t\tr_{obj.product1} := updater.incr(r_{obj.product1})")
            if obj.priority >= 25:
                ivyFile.write(f";\n\t\t\tif r_{targetSpecies} {equality} {targetNum} {o}\n\t\t\t\tcall goal.achieved(r_{targetSpecies})\n\t\t\t{c}\n\t\t")
            else:
                ivyFile.write(f";\n\t\t\tr{count}_executions := updater.incr(r{count}_executions)\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 != "" and obj.reactant2 == "" and obj.product1 != "" and obj.product2 != ""):
            ivyFile.write(f"""action update_r{count} =  {o}
        if selector.execute_r{count} {o}
            call inspector.check_guard_r{count}(r_{obj.reactant1})""")
            for x in range(obj.reactant1Num):
                ivyFile.write(f";\n\t\t\tr_{obj.reactant1} := updater.decr(r_{obj.reactant1})")
            for x in range(obj.product1Num):
                ivyFile.write(f";\n\t\t\tr_{obj.product1} := updater.incr(r_{obj.product1})")
            for x in range(obj.product2Num):
                ivyFile.write(f";\n\t\t\tr_{obj.product2} := updater.incr(r_{obj.product2})")
            if obj.priority >= 25:
                ivyFile.write(f";\n\t\t\tif r_{targetSpecies} {equality} {targetNum} {o}\n\t\t\t\tcall goal.achieved(r_{targetSpecies})\n\t\t\t{c}\n\t\t")
            else:
                ivyFile.write(f";\n\t\t\tr{count}_executions := updater.incr(r{count}_executions)\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 != "" and obj.reactant2 != "" and obj.product1 == ""):
            ivyFile.write(f"""action update_r{count} =  {o}
        if selector.execute_r{count} {o}
            call inspector.check_guard_r{count}(r_{obj.reactant1},r_{obj.reactant2})""")
            for x in range(obj.reactant1Num):
                ivyFile.write(f";\n\t\t\tr_{obj.reactant1} := updater.decr(r_{obj.reactant1})")
            for x in range(obj.reactant2Num):
                ivyFile.write(f";\n\t\t\tr_{obj.reactant2} := updater.decr(r_{obj.reactant2})")
            if obj.priority >= 25:
                ivyFile.write(f";\n\t\t\tif r_{targetSpecies} {equality} {targetNum} {o}\n\t\t\t\tcall goal.achieved(r_{targetSpecies})\n\t\t\t{c}\n\t\t")
            else:
                ivyFile.write(f";\n\t\t\tr{count}_executions := updater.incr(r{count}_executions)\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 != "" and obj.reactant2 != "" and obj.product1 != "" and obj.product2 == ""):
            ivyFile.write(f"""action update_r{count} =  {o}
        if selector.execute_r{count} {o}
            call inspector.check_guard_r{count}(r_{obj.reactant1},r_{obj.reactant2})""")
            for x in range(obj.reactant1Num):
                ivyFile.write(f";\n\t\t\tr_{obj.reactant1} := updater.decr(r_{obj.reactant1})")
            for x in range(obj.reactant2Num):
                ivyFile.write(f";\n\t\t\tr_{obj.reactant2} := updater.decr(r_{obj.reactant2})")
            for x in range(obj.product1Num):
                ivyFile.write(f";\n\t\t\tr_{obj.product1} := updater.incr(r_{obj.product1})")
            if obj.priority >= 25:
                ivyFile.write(f";\n\t\t\tif r_{targetSpecies} {equality} {targetNum} {o}\n\t\t\t\tcall goal.achieved(r_{targetSpecies})\n\t\t\t{c}\n\t\t")
            else:
                ivyFile.write(f";\n\t\t\tr{count}_executions := updater.incr(r{count}_executions)\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")
        elif(obj.reactant1 != "" and obj.reactant2 != "" and obj.product1 != "" and obj.product2 != ""):
            ivyFile.write(f"""action update_r{count} =  {o}
        if selector.execute_r{count} {o}
            call inspector.check_guard_r{count}(r_{obj.reactant1},r_{obj.reactant2})""")
            for x in range(obj.reactant1Num):
                ivyFile.write(f";\n\t\t\tr_{obj.reactant1} := updater.decr(r_{obj.reactant1})")
            for x in range(obj.reactant2Num):
                ivyFile.write(f";\n\t\t\tr_{obj.reactant2} := updater.decr(r_{obj.reactant2})")
            for x in range(obj.product1Num):
                ivyFile.write(f";\n\t\t\tr_{obj.product1} := updater.incr(r_{obj.product1})")
            for x in range(obj.product2Num):
                ivyFile.write(f";\n\t\t\tr_{obj.product2} := updater.incr(r_{obj.product2})")
            if obj.priority >= 25:
                ivyFile.write(f";\n\t\t\tif r_{targetSpecies} {equality} {targetNum} {o}\n\t\t\t\tcall goal.achieved(r_{targetSpecies})\n\t\t\t{c}\n\t\t")
            else:
                ivyFile.write(f";\n\t\t\tr{count}_executions := updater.incr(r{count}_executions)\n\t\t")
            ivyFile.write("}\n\t}\n\n\t")

ivyFile.write("\n\n\taction idling = {}\n\n\t")

ivyFile.write("\n\n\taction fail_test = {}\n\n\t")

count = 0
for obj in  reactions:
    count += 1
    if obj.priority > 15:
        ivyFile.write(f"before update_r{count}")
        if (reactions[count-1].reactant1 == ""):
            ivyFile.write(f" {o}\n\t\tassert idle = 0;\n\t\tassert enabled_checker.is_enabled_r{count}")
            count1 = 0
            count2 = 0
            if obj.priority <= 17:
                ivyFile.write(";\n\t\tassert false")
            elif obj.priority < 25:
                for y in reactions:
                    count1 += 1
                    if y.priority > 15 and y.priority < 25:
                        count2 += 1
                        if count2 == 1:
                            ivyFile.write(f";\n\t\tassert (r{count1}_executions * ")
                            for x in secondTargetList:
                                if y.product1 == x.name:
                                    ivyFile.write(str(y.product1Num))
                                elif y.product2 == x.name:
                                    ivyFile.write(str(y.product2Num))
                        if count2 >= 2:
                            ivyFile.write(f" + r{count1}_executions * ")
                            for x in secondTargetList:
                                if y.product1 == x.name:
                                    ivyFile.write(str(y.product1Num))
                                elif y.product2 == x.name:
                                    ivyFile.write(str(y.product2Num))
                    if count1 == numOfReactions:
                        ivyFile.write(") < ")
                        for tar in secondTargetList:
                            if tar.name == obj.product1 or tar.name == obj.product2:
                                for tar2 in speciesList:
                                    if tar2.name == tar.name:
                                        needed_amount = round(tar.minAmount - tar2.value)
                                        ivyFile.write(str(needed_amount))
            ivyFile.write("\n\t}\n\t")
        elif(reactions[count-1].reactant1 != "" and reactions[count-1].reactant2 == ""):
            ivyFile.write(f" {o}\n\t\tassert idle = 0;\n\t\tassert enabled_checker.is_enabled_r{count}(r_{obj.reactant1})")
            count1 = 0
            count2 = 0
            if obj.priority <= 17:
                ivyFile.write(";\n\t\tassert false")
            elif obj.priority < 25:
                for y in reactions:
                    count1 += 1
                    if y.priority > 15 and y.priority < 25:
                        count2 += 1
                        if count2 == 1:
                            ivyFile.write(f";\n\t\tassert (r{count1}_executions * ")
                            for x in secondTargetList:
                                if y.product1 == x.name:
                                    ivyFile.write(str(y.product1Num))
                                elif y.product2 == x.name:
                                    ivyFile.write(str(y.product2Num))
                        if count2 >= 2:
                            ivyFile.write(f" + r{count1}_executions * ")
                            for x in secondTargetList:
                                if y.product1 == x.name:
                                    ivyFile.write(str(y.product1Num))
                                elif y.product2 == x.name:
                                    ivyFile.write(str(y.product2Num))
                    if count1 == numOfReactions:
                        ivyFile.write(") < ")
                        for tar in secondTargetList:
                            if tar.name == obj.product1 or tar.name == obj.product2:
                                for tar2 in speciesList:
                                    if tar2.name == tar.name:
                                        needed_amount = round(tar.minAmount - tar2.value)
                                        ivyFile.write(str(needed_amount))
            ivyFile.write("\n\t}\n\t")
        elif(reactions[count-1].reactant1 != "" and reactions[count-1].reactant2 != ""):
            ivyFile.write(f" {o}\n\t\tassert idle = 0;\n\t\tassert enabled_checker.is_enabled_r{count}(r_{obj.reactant1},r_{obj.reactant2})")
            count1 = 0
            count2 = 0
            if obj.priority <= 17:
                ivyFile.write(";\n\t\tassert false")
            elif obj.priority < 25:
                for y in reactions:
                    count1 += 1
                    if y.priority > 15 and y.priority < 25:
                        count2 += 1
                        if count2 == 1:
                            ivyFile.write(f";\n\t\tassert (r{count1}_executions * ")
                            for x in secondTargetList:
                                if y.product1 == x.name:
                                    ivyFile.write(str(y.product1Num))
                                elif y.product2 == x.name:
                                    ivyFile.write(str(y.product2Num))
                        if count2 >= 2:
                            ivyFile.write(f" + r{count1}_executions * ")
                            for x in secondTargetList:
                                if y.product1 == x.name:
                                    ivyFile.write(str(y.product1Num))
                                elif y.product2 == x.name:
                                    ivyFile.write(str(y.product2Num))
                    if count1 == numOfReactions:
                        ivyFile.write(") < ")
                        for tar in secondTargetList:
                            if tar.name == obj.product1 or tar.name == obj.product2:
                                for tar2 in speciesList:
                                    if tar2.name == tar.name:
                                        needed_amount = round(tar.minAmount - tar2.value)
                                        ivyFile.write(str(needed_amount))
            ivyFile.write("\n\t}\n\n\t")


ivyFile.write("\n\n\tbefore idling {\n\t\tassert idle = 1\n\t}\n")

ivyFile.write("\n\n\tbefore fail_test {\n\t\tassert idle = 0;\n\t\tassert (")

count = 0
count1 = 0
count2 = 0
count3 = 0
for obj in reactions:
    count += 1
    if obj.priority > 15:
        count1 += 1
        if count1 != 1:
            ivyFile.write(" & ")
        if obj.reactant1 == "":
            ivyFile.write(f"enabled_checker.is_enabled_r{count} = false")
        if obj.reactant1 != "" and obj.reactant2 == "":
            ivyFile.write(f"enabled_checker.is_enabled_r{count}(r_{obj.reactant1}) = false")
        if obj.reactant1 != "" and obj.reactant2 != "":
            ivyFile.write(f"enabled_checker.is_enabled_r{count}(r_{obj.reactant1},r_{obj.reactant2}) = false")
    if count == numOfReactions:
        ivyFile.write(") | ((")
        for y in reactions:
            count2 += 1
            if y.priority > 15 and y.priority < 25:
                count3 += 1
                if count3 == 1:
                    ivyFile.write(f"r{count2}_executions * ")
                    for x in secondTargetList:
                        if y.product1 == x.name:
                            ivyFile.write(str(y.product1Num))
                        elif y.product2 == x.name:
                            ivyFile.write(str(y.product2Num))
                if count3 >= 2:
                    ivyFile.write(f" + r{count2}_executions * ")
                    for x in secondTargetList:
                        if y.product1 == x.name:
                            ivyFile.write(str(y.product1Num))
                        elif y.product2 == x.name:
                            ivyFile.write(str(y.product2Num))
            if count2 == numOfReactions:
                ivyFile.write(") >= ")
                for tar in secondTargetList:
                    if tar.name == obj.product1 or tar.name == obj.product2:
                        for tar2 in speciesList:
                            if tar2.name == tar.name:
                                needed_amount = round(tar.minAmount - tar2.value)
                                ivyFile.write(f"{needed_amount})\n\t{c}\n\n")

    
ivyFile.write("\n\n\tafter fail_test {\n\t\tassert idle = 1\n\t}\n\n}\n")
ivyFile.write("\nexport protocol.fail_test\n")

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

ivy_to_cpp_command = subprocess.Popen(["ivy_to_cpp", "isolate=iso_proto", "target=test", "build=true", "test_v3.ivy"])
ivy_to_cpp_command.wait()

runswanted = input("How many traces do you want to the target specified? (Type an integer greater than 0): ") #Amount of traces desired is recorded

print("starting to run rest of tests")
firsthalf = "./test_v3 iters="
middle = str(first_iters*1.25)
middle2 = " runs="
secondhalf = " >test_v3.txt"
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

with open("test_v3.txt", "r") as f:
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
                if iters == math.floor(first_iters * 1.25):
                    print("Error!\tRun", count+1, "did not reach the target state\n")
                if line[11:20] == "fail_test":
                    print("Error occurred during randomized testing!")
                    exit(1)
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

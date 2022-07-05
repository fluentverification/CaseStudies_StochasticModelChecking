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

class chemical:
    def __init__(self, value, name):
        self.value = value
        self.name = name

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
chem = []

for obj in Reactions:
    if (obj.reactant1 not in chem and obj.reactant1 != ""):
        chem.append(obj.reactant1)
    if (obj.reactant2 not in chem and obj.reactant2 != ""):
        chem.append(obj.reactant2)
    if (obj.product1 not in chem and obj.product1 != ""):
        chem.append(obj.product1)
    if (obj.product2 not in chem and obj.product2 != ""):
        chem.append(obj.product2)

chemlist = []

for obj in chem:
    print("What is the initial value of", obj, "?")
    val = int(input())
    chemlist.append(chemical(val, obj))

print("The initial values reported are:")

for obj in chemlist:
    print(obj.name,"=",obj.value)

print("\n")

targetchem = input("Which chemical is going to be monitored? ")
if(targetchem not in chem):
    print("Error, chemical specified not found in the reactions reported please start over")
    exit()
targetnum = input("What is the target number for this chemical? ")

upordown = input("Are you interested in seeing when the chemical is above or below the specified number? (type either above or below): ")

for obj in chemlist:
    if obj.name == targetchem:
        if upordown.lower() == "above":
            if obj.value >= int(targetnum):
                print("\nSpecified target is already achieved in target state, please start over")
                exit()
        elif upordown.lower() == "below":
            if obj.value <= int(targetnum):
                print("\nSpecified target is already achieved in target state, please start over")
                exit()
        else:
            print("Problem with information entered (check spelling and make sure there are no spaces)")
            exit()

print("We will monitor when", targetchem, "reaches",targetnum,"\n")

secondtarget = []
if upordown.lower() == "above":
    for obj in Reactions:
        if obj.product1 == targetchem or obj.product2 == targetchem:
            obj.priority = obj.priority + 10
        elif obj.reactant1 == targetchem or obj.reactant2 == targetchem:
            obj.priority = obj.priority - 10
elif upordown.lower() == "below":
    for obj in Reactions:
        if obj.product1 == targetchem or obj.product2 == targetchem:
            obj.priority = obj.priority - 10
        elif obj.reactant1 == targetchem or obj.reactant2 == targetchem:
            obj.priority = obj.priority + 10


for obj in Reactions:
    if obj.priority >= 25:
        if obj.reactant1 != "" and obj.reactant2 != "":
            if obj.reactant1 != targetchem:
                secondtarget.append(obj.reactant1)
            if obj.reactant2 != targetchem:    
                secondtarget.append(obj.reactant2)
        elif obj.reactant1 != "" and obj.reactant2 == "":
            if obj.reactant1 != targetchem:
                secondtarget.append(obj.reactant1)

for obj in chemlist:
    if obj.name == targetchem:
        chemnum = abs(int(targetnum) - obj.value)
 
for obj in Reactions:
    if obj.priority < 25:
        for tar in secondtarget:
            for chemical in chemlist:
                if chemical.name == tar:
                    if chemical.value >= 2*chemnum:
                        if obj.reactant1 == tar:
                            obj.priority = obj.priority - 1
                        if obj.reactant2 == tar:
                            obj.priority = obj.priority - 1
                    elif chemical.value >= chemnum:
                        if obj.reactant1 == tar:
                            obj.priority = obj.priority - 2
                        if obj.reactant2 == tar:
                            obj.priority = obj.priority - 2
                    elif chemical.value >= (chemnum/2):
                        if obj.reactant1 == tar:
                            obj.priority = obj.priority - 3
                        if obj.reactant2 == tar:
                            obj.priority = obj.priority - 3
                    elif chemical.value >= (chemnum/4):
                        if obj.reactant1 == tar:
                            obj.priority = obj.priority - 4
                        if obj.reactant2 == tar:
                            obj.priority = obj.priority - 4
                    elif chemical.value < (chemnum/4):
                        if obj.reactant1 == tar:
                            obj.priority = obj.priority - 5
                        if obj.reactant2 == tar:
                            obj.priority = obj.priority - 5

        
for obj in Reactions:
    #if obj.priority < 25:
    for tar in secondtarget:
        for chemical in chemlist:
            if chemical.name == tar:
                if chemical.value >= (2*chemnum):
                    if obj.product1 == tar:
                        obj.priority = obj.priority + 1
                    if obj.product2 == tar:
                        obj.priority = obj.priority + 1
                elif chemical.value >= chemnum:
                    if obj.product1 == tar:
                        obj.priority = obj.priority + 2
                    if obj.product2 == tar:
                        obj.priority = obj.priority + 2
                elif chemical.value >= (chemnum/2):
                    if obj.product1 == tar:
                        obj.priority = obj.priority + 3
                    if obj.product2 == tar:
                        obj.priority = obj.priority + 3
                elif chemical.value >= (chemnum/4):
                    if obj.product1 == tar:
                        obj.priority = obj.priority + 4
                    if obj.product2 == tar:
                        obj.priority = obj.priority + 4
                elif chemical.value < (chemnum/4):
                    if obj.product1 == tar:
                        obj.priority = obj.priority + 5
                    if obj.product2 == tar:
                        obj.priority = obj.priority + 5

print("The following priorities have been noted for the reactions: \n")

count = 0
for obj in Reactions:
    count = count + 1
    print("reaction", str(count), ":", str(obj.priority))

"""
shortest = input("Do you want the shortest paths possible to the specified property (Yes or No): ")
if shortest == "Yes":
    alternate = input("Can we alternate two reactions to reach the specified property? (Yes or No): ")

    if (alternate == "Yes"):
        alternateone = input("What is the first reaction needed? (type the integer in front of the reaction when it was reported) ")
        alternatetwo = input("What is the second reaction needed? (type the integer in front of the reaction when it was reported) ")
    else:
        alternateone = "NA"
        alternatetwo = "NA"
"""
#ask for the reactions that you want to have priority

    

ivy_file = open("test_v2.ivy", "w")

ivy_file.write("#lang ivy 1.7\n\nobject inc_dec = {\n")
ivy_file.write("\ttype num\n\tinterpret num -> bv[10]\n\ttype exec_var\n\tinterpret exec_var -> bv[8]\n\ttype exec_stage\n\tinterpret exec_stage -> bv[3]\n\n\taction incr(x:num) returns(y:num) = {\n\t\ty := x + 1\n\t}\n\n\taction decr(x:num) returns(y:num) = {\n\t\ty := x - 1\n\t}\n}")
ivy_file.write("\n\nobject goal = {\n\taction achieved(v:inc_dec.num)\n\tobject spec = {\n\t\tbefore achieved {\n\t\t\tassert v ")
if upordown.lower() == "above":
    ivy_file.write(">= ")
elif upordown.lower() == "below":
    ivy_file.write("<= ")
ivy_file.write(targetnum)
ivy_file.write(";\n\t\t\tproto.idle := 1\n\t\t}\n\t}\n}\n\n")

ivy_file.write("object enabled = {\n\n\t")

count = 0
for obj in Reactions:
    count = count + 1
    ivy_file.write("action r") 
    ivy_file.write(str(count))
    if (Reactions[count-1].reactant1 == ""):
        ivy_file.write(" returns(y:bool) = {\n\t\ty := true\n\t}\n\n\t")
    elif(Reactions[count-1].reactant1 != "" and Reactions[count-1].reactant2 == ""):
        ivy_file.write("(reactant1:inc_dec.num) returns(y:bool) = {\n\t\tif reactant1 >= ")
        ivy_file.write(str(obj.reactant1num))
        ivy_file.write(" {\n\t\t\ty := true\n\t\t}\n\t\telse {\n\t\t\ty := false\n\t\t}\n\t}\n\n\t")
    elif(Reactions[count-1].reactant1 != "" and Reactions[count-1].reactant2 != ""):
        ivy_file.write("(reactant1:inc_dec.num,reactant2:inc_dec.num) returns(y:bool) = {\n\t\tif reactant1 >= ")
        ivy_file.write(str(obj.reactant1num))
        ivy_file.write(" & reactant2 >= ")
        ivy_file.write(str(obj.reactant2num))
        ivy_file.write(" {\n\t\t\ty := true\n\t\t}\n\t\telse {\n\t\t\ty := false\n\t\t}\n\t}\n\n\t")
ivy_file.write("\n}\n\n")

ivy_file.write("object monitor = {\n\t")
count = 0
for obj in Reactions:
    count = count + 1
    ivy_file.write("action r")
    ivy_file.write(str(count))
    if (Reactions[count-1].reactant1 == ""):
        ivy_file.write("\n\tbefore r")
        ivy_file.write(str(count))
        ivy_file.write(" {\n\t\tassert true\n\t}\n\n\t")
    elif(Reactions[count-1].reactant1 != "" and Reactions[count-1].reactant2 == ""):
        ivy_file.write("(reactant1:inc_dec.num)\n\tbefore r")
        ivy_file.write(str(count))
        ivy_file.write(" {\n\t\tassert reactant1 >= ")
        ivy_file.write(str(obj.reactant1num))
        ivy_file.write("\n\t}\n\n\t")
    elif(Reactions[count-1].reactant1 != "" and Reactions[count-1].reactant2 != ""):
        ivy_file.write("(reactant1:inc_dec.num,reactant2:inc_dec.num)\n\tbefore r")
        ivy_file.write(str(count))
        ivy_file.write(" {\n\t\tassert reactant1 >= ")
        ivy_file.write(str(obj.reactant1num))
        ivy_file.write(" & reactant2 >= ")
        ivy_file.write(str(obj.reactant2num))
        ivy_file.write("\n\t}\n\n\t")

        
ivy_file.write("\n}")

ivy_file.write("\n\nobject choose_reaction = {\n\t")

count = 0

for obj in Reactions:
    count = count + 1
    ivy_file.write("individual r")
    ivy_file.write(str(count))
    ivy_file.write("_exec : inc_dec.exec_var\n\t")

ivy_file.write("\n\t")
count = 0

for obj in Reactions:
    count = count + 1
    ivy_file.write("individual r")
    ivy_file.write(str(count))
    ivy_file.write("_rate : inc_dec.exec_var\n\t")

ivy_file.write("\n\t")

count = 0
for obj in Reactions:
    count = count + 1
    ivy_file.write("individual r")
    ivy_file.write(str(count))
    ivy_file.write("_count : inc_dec.exec_var\n\t")

ivy_file.write("\n\t")

count = 0
for obj in Reactions:
    count = count + 1
    ivy_file.write("individual r")
    ivy_file.write(str(count))
    ivy_file.write("_count_rate : inc_dec.exec_var\n\t")

ivy_file.write("\n\t")

count = 0
for obj in Reactions:
    count = count + 1
    ivy_file.write("individual r")
    ivy_file.write(str(count))
    ivy_file.write("_stage : inc_dec.exec_stage\n\t")

ivy_file.write("\n\n\tafter init {\n\t\t")
#import random
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
    ivy_file.write("action r")
    ivy_file.write(str(count))
    ivy_file.write("_execution returns(y:bool) = {\n\t\tr")
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

ivy_file.write("\nobject proto = {\n\n\ttype 2bit\n\tinterpret 2bit -> bv[1]\n\tindividual idle : 2bit\n\n")

for obj in chem:
    ivy_file.write("\tindividual ")
    ivy_file.write("r_")
    ivy_file.write(obj)
    ivy_file.write(" : inc_dec.num\n")

ivy_file.write("\n\tafter init {\n\t\t")

for obj in chemlist:
    ivy_file.write("r_")
    ivy_file.write(obj.name)
    ivy_file.write(" := ")
    ivy_file.write(str(obj.value))
    ivy_file.write(";\n\t\t")

ivy_file.write("idle := 0\n\t}\n\n\t")

#ivy_file.write("action updating = {\n\t\t")

count = 0
for obj in Reactions:
    count = count + 1
    if(obj.reactant1 == "" and obj.product1 != "" and obj.product2 == ""):
        ivy_file.write("action updating_r")
        ivy_file.write(str(count))
        ivy_file.write(" = {\n\t\t")
        ivy_file.write("if choose_reaction.r")
        ivy_file.write(str(count))
        ivy_file.write("_execution {\n\t\t\tcall monitor.r")
        ivy_file.write(str(count))
        for x in range(obj.product1num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.product1)
            ivy_file.write(" := inc_dec.incr(")
            ivy_file.write("r_")
            ivy_file.write(obj.product1)
            ivy_file.write(")")
        if obj.priority >= 25:
            ivy_file.write(";\n\t\t")
            ivy_file.write("\tif ")
            ivy_file.write("r_")
            ivy_file.write(targetchem)
            if upordown.lower() == "above":
                ivy_file.write(" >= ")
            elif upordown.lower() == "below":
                ivy_file.write(" <= ")
            ivy_file.write(str(targetnum))
            ivy_file.write(" {\n\t\t\t\tcall goal.achieved(")
            ivy_file.write("r_")
            ivy_file.write(targetchem)
            ivy_file.write(")\n\t\t\t}\n\t\t")
        else:
            ivy_file.write("\n\t\t")
        ivy_file.write("}\n\t}\n\n\t")
    elif(obj.reactant1 == "" and obj.product1 != "" and obj.product2 != ""):
        ivy_file.write("action updating_r")
        ivy_file.write(str(count))
        ivy_file.write(" = {\n\t\t")
        ivy_file.write("if choose_reaction.r")
        ivy_file.write(str(count))
        ivy_file.write("_execution {\n\t\t\tcall monitor.r")
        ivy_file.write(str(count))
        for x in range(obj.product1num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.product1)
            ivy_file.write(" := inc_dec.incr(")
            ivy_file.write("r_")
            ivy_file.write(obj.product1)
            ivy_file.write(")")
        for x in range(obj.product2num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.product2)
            ivy_file.write(" := inc_dec.incr(")
            ivy_file.write("r_")
            ivy_file.write(obj.product2)
            ivy_file.write(")")
        #ivy_file.write(")\n\t\t")
        if obj.priority >= 25:
            ivy_file.write(";\n\t\t")
            ivy_file.write("\tif ")
            ivy_file.write("r_")
            ivy_file.write(targetchem)
            if upordown.lower() == "above":
                ivy_file.write(" >= ")
            elif upordown.lower() == "below":
                ivy_file.write(" <= ")
            ivy_file.write(str(targetnum))
            ivy_file.write(" {\n\t\t\t\tcall goal.achieved(")
            ivy_file.write("r_")
            ivy_file.write(targetchem)
            ivy_file.write(")\n\t\t\t}\n\t\t")
        else:
            ivy_file.write("\n\t\t")
        ivy_file.write("}\n\t}\n\n\t")
    elif(obj.reactant1 != "" and obj.reactant2 == "" and obj.product1 == ""):
        ivy_file.write("action updating_r")
        ivy_file.write(str(count))
        ivy_file.write(" = {\n\t\t")
        ivy_file.write("if choose_reaction.r")
        ivy_file.write(str(count))
        ivy_file.write("_execution {\n\t\t\tcall monitor.r")
        ivy_file.write(str(count))
        ivy_file.write("(")
        ivy_file.write("r_")
        ivy_file.write(obj.reactant1)
        ivy_file.write(")")
        for x in range(obj.reactant1num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant1)
            ivy_file.write(" := inc_dec.decr(")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant1)
            ivy_file.write(")")
        #ivy_file.write(")\n\t\t")
        if obj.priority >= 25:
            ivy_file.write(";\n\t\t")
            ivy_file.write("\tif ")
            ivy_file.write("r_")
            ivy_file.write(targetchem)
            if upordown.lower() == "above":
                ivy_file.write(" >= ")
            elif upordown.lower() == "below":
                ivy_file.write(" <= ")
            ivy_file.write(str(targetnum))
            ivy_file.write(" {\n\t\t\t\tcall goal.achieved(")
            ivy_file.write("r_")
            ivy_file.write(targetchem)
            ivy_file.write(")\n\t\t\t}\n\t\t")
        else:
            ivy_file.write("\n\t\t")
        ivy_file.write("}\n\t}\n\n\t")
    elif(obj.reactant1 != "" and obj.reactant2 == "" and obj.product1 != "" and obj.product2 == ""):
        ivy_file.write("action updating_r")
        ivy_file.write(str(count))
        ivy_file.write(" = {\n\t\t")
        ivy_file.write("if choose_reaction.r")
        ivy_file.write(str(count))
        ivy_file.write("_execution {\n\t\t\tcall monitor.r")
        ivy_file.write(str(count))
        ivy_file.write("(")
        ivy_file.write("r_")
        ivy_file.write(obj.reactant1)
        ivy_file.write(")")
        for x in range(obj.reactant1num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant1)
            ivy_file.write(" := inc_dec.decr(")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant1)
            ivy_file.write(")")
        for x in range(obj.product1num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.product1)
            ivy_file.write(" := inc_dec.incr(")
            ivy_file.write("r_")
            ivy_file.write(obj.product1)
            ivy_file.write(")")
        #ivy_file.write(")\n\t\t")
        if obj.priority >= 25:
            ivy_file.write(";\n\t\t")
            ivy_file.write("\tif ")
            ivy_file.write("r_")
            ivy_file.write(targetchem)
            if upordown.lower() == "above":
                ivy_file.write(" >= ")
            elif upordown.lower() == "below":
                ivy_file.write(" <= ")
            ivy_file.write(str(targetnum))
            ivy_file.write(" {\n\t\t\t\tcall goal.achieved(")
            ivy_file.write("r_")
            ivy_file.write(targetchem)
            ivy_file.write(")\n\t\t\t}\n\t\t")
        else:
            ivy_file.write("\n\t\t")
        ivy_file.write("}\n\t}\n\n\t")
    elif(obj.reactant1 != "" and obj.reactant2 == "" and obj.product1 != "" and obj.product2 != ""):
        ivy_file.write("action updating_r")
        ivy_file.write(str(count))
        ivy_file.write(" = {\n\t\t")
        ivy_file.write("if choose_reaction.r")
        ivy_file.write(str(count))
        ivy_file.write("_execution {\n\t\t\tcall monitor.r")
        ivy_file.write(str(count))
        ivy_file.write("(")
        ivy_file.write("r_")
        ivy_file.write(obj.reactant1)
        ivy_file.write(")")
        for x in range(obj.reactant1num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant1)
            ivy_file.write(" := inc_dec.decr(")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant1)
            ivy_file.write(")")
        for x in range(obj.product1num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.product1)
            ivy_file.write(" := inc_dec.incr(")
            ivy_file.write("r_")
            ivy_file.write(obj.product1)
            ivy_file.write(")")
        for x in range(obj.product2num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.product2)
            ivy_file.write(" := inc_dec.incr(")
            ivy_file.write("r_")
            ivy_file.write(obj.product2)
            ivy_file.write(")")
        #ivy_file.write(")\n\t\t")
        if obj.priority >= 25:
            ivy_file.write(";\n\t\t")
            ivy_file.write("\tif ")
            ivy_file.write("r_")
            ivy_file.write(targetchem)
            if upordown.lower() == "above":
                ivy_file.write(" >= ")
            elif upordown.lower() == "below":
                ivy_file.write(" <= ")
            ivy_file.write(str(targetnum))
            ivy_file.write(" {\n\t\t\t\tcall goal.achieved(")
            ivy_file.write("r_")
            ivy_file.write(targetchem)
            ivy_file.write(")\n\t\t\t}\n\t\t")
        else:
            ivy_file.write("\n\t\t")
        ivy_file.write("}\n\t}\n\n\t")
    elif(obj.reactant1 != "" and obj.reactant2 != "" and obj.product1 == ""):
        ivy_file.write("action updating_r")
        ivy_file.write(str(count))
        ivy_file.write(" = {\n\t\t")
        ivy_file.write("if choose_reaction.r")
        ivy_file.write(str(count))
        ivy_file.write("_execution {\n\t\t\tcall monitor.r")
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
            ivy_file.write(" := inc_dec.decr(")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant1)
            ivy_file.write(")")
        for x in range(obj.reactant2num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant2)
            ivy_file.write(" := inc_dec.decr(")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant2)
            ivy_file.write(")")
        #ivy_file.write(")\n\t\t")
        if obj.priority >= 25:
            ivy_file.write(";\n\t\t")
            ivy_file.write("\tif ")
            ivy_file.write("r_")
            ivy_file.write(targetchem)
            if upordown.lower() == "above":
                ivy_file.write(" >= ")
            elif upordown.lower() == "below":
                ivy_file.write(" <= ")
            ivy_file.write(str(targetnum))
            ivy_file.write(" {\n\t\t\t\tcall goal.achieved(")
            ivy_file.write("r_")
            ivy_file.write(targetchem)
            ivy_file.write(")\n\t\t\t}\n\t\t")
        else:
            ivy_file.write("\n\t\t")
        ivy_file.write("}\n\t}\n\n\t")
    elif(obj.reactant1 != "" and obj.reactant2 != "" and obj.product1 != "" and obj.product2 == ""):
        ivy_file.write("action updating_r")
        ivy_file.write(str(count))
        ivy_file.write(" = {\n\t\t")
        ivy_file.write("if choose_reaction.r")
        ivy_file.write(str(count))
        ivy_file.write("_execution {\n\t\t\tcall monitor.r")
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
            ivy_file.write(" := inc_dec.decr(")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant1)
            ivy_file.write(")")
        for x in range(obj.reactant2num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant2)
            ivy_file.write(" := inc_dec.decr(")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant2)
            ivy_file.write(")")
        for x in range(obj.product1num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.product1)
            ivy_file.write(" := inc_dec.incr(")
            ivy_file.write("r_")
            ivy_file.write(obj.product1)
            ivy_file.write(")")
        #ivy_file.write(")\n\t\t")
        if obj.priority >= 25:
            ivy_file.write(";\n\t\t")
            ivy_file.write("\tif ")
            ivy_file.write("r_")
            ivy_file.write(targetchem)
            if upordown.lower() == "above":
                ivy_file.write(" >= ")
            elif upordown.lower() == "below":
                ivy_file.write(" <= ")
            ivy_file.write(str(targetnum))
            ivy_file.write(" {\n\t\t\t\tcall goal.achieved(")
            ivy_file.write("r_")
            ivy_file.write(targetchem)
            ivy_file.write(")\n\t\t\t}\n\t\t")
        else:
            ivy_file.write("\n\t\t")
        ivy_file.write("}\n\t}\n\n\t")
    elif(obj.reactant1 != "" and obj.reactant2 != "" and obj.product1 != "" and obj.product2 != ""):
        ivy_file.write("action updating_r")
        ivy_file.write(str(count))
        ivy_file.write(" = {\n\t\t")
        ivy_file.write("if choose_reaction.r")
        ivy_file.write(str(count))
        ivy_file.write("_execution {\n\t\t\tcall monitor.r")
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
            ivy_file.write(" := inc_dec.decr(")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant1)
            ivy_file.write(")")
        for x in range(obj.reactant2num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant2)
            ivy_file.write(" := inc_dec.decr(")
            ivy_file.write("r_")
            ivy_file.write(obj.reactant2)
            ivy_file.write(")")
        for x in range(obj.product1num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.product1)
            ivy_file.write(" := inc_dec.incr(")
            ivy_file.write("r_")
            ivy_file.write(obj.product1)
            ivy_file.write(")")
        for x in range(obj.product2num):
            ivy_file.write(";\n\t\t\t")
            ivy_file.write("r_")
            ivy_file.write(obj.product2)
            ivy_file.write(" := inc_dec.incr(")
            ivy_file.write("r_")
            ivy_file.write(obj.product2)
            ivy_file.write(")")
        #ivy_file.write(")\n\t\t")
        if obj.priority >= 25:
            ivy_file.write(";\n\t\t")
            ivy_file.write("\tif ")
            ivy_file.write("r_")
            ivy_file.write(targetchem)
            if upordown.lower() == "above":
                ivy_file.write(" >= ")
            elif upordown.lower() == "below":
                ivy_file.write(" <= ")
            ivy_file.write(str(targetnum))
            ivy_file.write(" {\n\t\t\t\tcall goal.achieved(")
            ivy_file.write("r_")
            ivy_file.write(targetchem)
            ivy_file.write(")\n\t\t\t}\n\t\t")
        else:
            ivy_file.write("\n\t\t")
        ivy_file.write("}\n\t}\n\n\t")

#ivy_file.write("\n\t}\n\n\t")
ivy_file.write("\n\n\taction idling = {}\n\n\t")
count = 0
for obj in Reactions:
    count = count + 1
    ivy_file.write("before updating_r")
    ivy_file.write(str(count))
    if (Reactions[count-1].reactant1 == ""):
        ivy_file.write(" {\n\t\tassert idle = 0;\n\t\tassert enabled.r")
        ivy_file.write(str(count))
        if obj.priority <= 6:
            ivy_file.write(";\n\t\tassert false")
        ivy_file.write("\n\t}\n\t")
    elif(Reactions[count-1].reactant1 != "" and Reactions[count-1].reactant2 == ""):
        ivy_file.write(" {\n\t\tassert idle = 0;\n\t\tassert enabled.r")
        ivy_file.write(str(count))
        ivy_file.write("(")
        ivy_file.write("r_")
        ivy_file.write(Reactions[count-1].reactant1)
        ivy_file.write(")")
        if obj.priority <= 6:
            ivy_file.write(";\n\t\tassert false")
        ivy_file.write("\n\t}\n\t")
    elif(Reactions[count-1].reactant1 != "" and Reactions[count-1].reactant2 != ""):
        ivy_file.write(" {\n\t\tassert idle = 0;\n\t\tassert enabled.r")
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
#export individual reactions

count = 0
for obj in Reactions:
    count = count + 1
    ivy_file.write("export proto.updating_r")
    ivy_file.write(str(count))
    ivy_file.write("\n")


ivy_file.write("export proto.idling\nimport goal.achieved\n")

count = 0
for obj in Reactions:
    count= count + 1
    ivy_file.write("import monitor.r")
    ivy_file.write(str(count))
    ivy_file.write("\n")

ivy_file.write("\nisolate iso_proto = proto with enabled, inc_dec, goal, choose_reaction, monitor")

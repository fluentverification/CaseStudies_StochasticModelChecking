
'''
Reaction objects store details about reactions.
'''

class Reaction:

	# Initialize a basic, empty reaction
	def __init__(self, name, rate):
		self.name = name
		self.rate = rate
		self.reactants = []
		self.products = []
		self.dependsOn = []
		self.dependCount = []
		self.executions = 0
		self.tier = -1
	
	# Add a reactant to the reaction
	def addReactant(self, reactant):
		self.reactants.append(reactant)

	# Add a product to the reaction
	def addProduct(self, product):
		self.products.append(product)

	# Custom tostring function for reactions
	def __str__(self) -> str:
		r = "\n" + self.name
		r = r + " - Rate " + str(self.rate)
		r = r + "\nReactants " + str(self.reactants)
		r = r + "\nProducts " + str(self.products)
		r = r + "\nRequired Executions " + str(self.executions) 
		r = r + "\nTier " + str(self.tier) + "\n"
		for d in range(len(self.dependsOn)):
			r = r + " - Depends On " + str(self.dependsOn[d].name) + " " + str(self.dependCount[d]) + " times\n"
		return r



'''
Recursive graph building function
Inputs: recursion depth, reaction array, chemical name array, initial values, 
	target values, reaction history, and parent reaction
Output: None
'''

def buildGraph(recdepth, reactions, chemicals, initials, targets, reaction_history, parent):
	
	deltaTarget = []
	needChems = []
	needChemQty = []
	numChems = len(chemicals)

	# Find difference between current (initial or modified initial) state and target
	for i in range(numChems):
		if targets[i] > -1:
			deltaR = targets[i] - initials[i]
			deltaTarget.append(deltaR)
			if deltaR > 0:
				needChems.append(chemicals[i])
				needChemQty.append(deltaR)
		else:
			deltaTarget.append(0)

	# Figure out what reactions we need to generate necessary chemicals
	needReactions = []
	for c in range(len(needChems)):
		for r in range(len(reactions)):
			if needChems[c] in reactions[r].products:
				needReactions.append(reactions[r])
	
	# For every required reaction
	for r in needReactions:
		
		# Print user-readable information
		print(80*"-")
		if parent:
			print("TIER", recdepth, "Checking", r.name,"From parent",parent.name)
		else:
			print("TIER", recdepth, "Checking", r.name,"From parent",parent)
		print(80*"-")
		print()
		print("Current Initial State\t",initials)
		print("Current Target State \t",targets)
		print("Delta Target-Initial \t",deltaTarget)
		print("Chemicals Required   \t",needChems)
		print("In these quantities  \t",needChemQty)

		# Check for cycles and alert user
		if r.name in reaction_history:
			print()
			print(r.name, "in reaction history. CYCLE DETECTED.\n")
			print()
			continue

		# Add current reaction to the reaction history (to look for cycles)
		r_hist = []
		for rh in reaction_history:
			r_hist.append(rh)
		r_hist.append(r.name)

		# Update required number of executions
		reqExec = 0
		for d in range(numChems):
			for p in range(len(r.products)):
				if chemicals[d] in r.products[p]:
					if deltaTarget[d] > reqExec:
						reqExec = deltaTarget[d]

		# Add to the required executions in the reaction object
		r.executions = r.executions + reqExec
		print("\nRequired Executions\t",r.executions)

		# Find out new "initial state" after reqExec executions
		new_initials = []
		for c in range(numChems):
			if chemicals[c] in r.products:
				new_initials.append(initials[c] + reqExec)
			else:
				new_initials.append(initials[c])

		# Find out new "target state" after reqExec executions
		new_targets = []
		for c in range(numChems):
			if chemicals[c] in r.reactants:
				new_targets.append(targets[c] + reqExec)
				if targets[c] == -1:
					new_targets[c] = new_targets[c] + 1
			else:
				new_targets.append(targets[c])
		
		# Print updated initial and target states, after r fires
		print("Initial After",reqExec,"Execs\t",new_initials)
		print("Target After",reqExec,"Execs\t",new_targets)

		# Update the parent to note this dependency
		if parent:
			parent.dependsOn.append(r)
			parent.dependCount.append(reqExec)

		# Set the tier to the recursion depth, if recursion depth is lower
		# or tier is not yet set
		if recdepth < r.tier or r.tier == -1:
			r.tier = recdepth

		# Print the updated reaction object
		print(r)

		# Recurse (find requirements for this reaction)
		buildGraph(recdepth+1, reactions, chemicals, new_initials, new_targets, r_hist, r)


'''
Master function to make the dependency graph
Input: File name (string) for reaction file in format from docs.md
Output: Array of reaction objects
'''

def makeDepGraph(infile):
	
	chemicals = [] # Stores string names of chemicals
	initials = [] # Stores initial values of chemicals
	targets = [] # Stores target values of chemicals
	reactions = [] # Array of ALL reaction objects

	with open(infile, 'r') as inpt:
		
		# Read the line of chemical names
		line = inpt.readline().strip()
		if not line or line == "":
			print("ERROR! CANNOT READ FIRST LINE")
			quit()
		for chem in line.split():
			chemicals.append(str(chem).strip())

		# Read the line of initial values
		line = inpt.readline().strip()
		if not line or line == "":
			print("ERROR! CANNOT READ SECOND LINE")
			quit()
		for val in line.split():
			initials.append(int(val))

		# Read the line of target values (-1 is don't care)
		line = inpt.readline().strip()
		if not line or line == "":
			print("ERROR! CANNOT READ THIRD LINE")
			quit()
		for val in line.split():
			targets.append(int(val))
		
		# Parse the reactions, don't process anything yet
		while True:
			line = inpt.readline().strip()
			if not line or line == "":
				break
			sline = line.split()
			rname = sline[0]
			rate = float(sline[len(sline)-1])
			react = Reaction(rname, rate)
			switchToProducts = False
			for i in range(1,len(sline)-1):
				if ">" in sline[i]: # Check if we need to switch to reading products
					switchToProducts = True
				elif "0" in sline[i]: # Case for null reactant or product
					continue
				elif switchToProducts:
					react.addProduct(sline[i]) # Add products second
				else:
					react.addReactant(sline[i]) # Add reactants first
			reactions.append(react) # Add to reaction matrix

	# Uncomment to print reactions at initialization for debugging:
	# for react in reactions:
	# 	print(react)

	reaction_history = []

	print(80*"=")

	# Recursively find the necessary reactions
	buildGraph(0, reactions, chemicals, initials, targets, reaction_history, None)

	# Print the list of necessary reactions and their dependencies
	print()
	print(80*"=")
	print("NECESSARY REACTIONS")
	print(80*"=")

	# Print only necessary reactions:
	for react in reactions:
		if react.tier > -1:
			print(react)

	# Uncomment to print all reactions instead:
	# for react in reactions:
	# 	print(react)
	
	print(80*"=")

	return reactions


# Main function... use 8-reaction file if 
# no other input is provided
if __name__=="__main__":
	makeDepGraph("8reaction_input.txt")
def man(name = "all"):
	manual = {
		"all": "Prints  the help text for all module_a functions",
		"solve": "help"
	}
	if name == "all":
		a = list(manual.keys())
		b = list(manual.values())
		for i in range(0, len(manual.keys())):
			return str(a[i] + ": ") + b[i]

	else:
		return str(name + ": ") + str(manual[name])

def solve(args):
	pass
class Solve:
	pass

print("Type 'man' for help")

def customPrint(value):
	if isinstance(value, list):
		for x in value:
			print(x)
	elif isinstance(value, str):
		print(value)

data = ""
while data not in ["q", "quit", "exit"]:
	data = input("type: ")
	partial = data.split(" ")

	#"is" does not work
	#Type incompatibility?
	if partial[0] == "man":
		man = getattr(__import__(partial[1]), "man")
		customPrint(man(partial[2]))

	if partial[0] == "solve":
		solve = getattr(__import__(partial[1]), "solve")
		solve(partial[1:])
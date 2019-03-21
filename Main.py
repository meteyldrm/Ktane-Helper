class Solve:
	pass

print("Type 'man' for help")
data = ""
while data not in ["q", "quit", "exit"]:
	data = input()
	partial = data.split(" ")
	if partial[0] is "man":
		man = __import__(partial[1] + ".man")
		
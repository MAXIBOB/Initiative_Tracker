def StartUp():
	global initiatives
	print("Welcome to Initiative Tracker!")
	choice = input("Would you like to use your previous initiatives? (y or n): ")
	if choice == "y":
		initiatives = open("Initiatives.txt","r")
		TurnOrder()
	else:
		initiatives = open("Initiatives.txt","w")
		NewNums()

def NewNums():
	while True:
		global initiatives
		name = input("Name of the character (q to end input): ")
		if name == "q":
			break
		ini = input("The initiative of the character: ")
		try:
			initiative = int(ini)
		except:
			print("You didn't input a number for the initiative. Try again.")
			NewNums()
		initiatives.write(name+"\n")
		initiatives.write(ini+"\n")
	initiatives.close()
	initiatives = open("Initiatives.txt","r")
	TurnOrder()		

def TurnOrder():
	global initiatives
	contents = initiatives.read()
	full_array = contents.splitlines()
	print(full_array)
	names = []
	nums = []
	for i in range(len(full_array)):
		if i%2 == 0:
			names.append(full_array[i])
		else:
			nums.append(int(full_array[i]))
	sorted_names = [x for _,x in sorted(zip(nums,names),reverse=True)]
	i=0
	while True:
		if i<len(sorted_names):
			print(sorted_names[i])
			i+=1
			x=input("")
		else:
			i=0
			print(sorted_names[i])
			x=input("")
			i+=1

StartUp()

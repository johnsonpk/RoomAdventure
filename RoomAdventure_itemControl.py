######################################################################
# Name:Matthew Louque
# Date:2/05/2016
# Description:Room adventure text based game
######################################################################
######################################################################
#blueprint for a room
#the room class
class Room(object):
	#constructor
	def __init__(self, name): 
		#rooms have a name, exits (ex south), exit locations
		#ex to the south is room n, items (ex table), 
		#item descriptions (for each item, and grabbables (things that can be taken into inventory)
		self.name = name
		self.exits = []
		self.exitLocations = []
		self.items = []
		self.itemDescriptions= []
		self.grabbables = []
		self.grabbablesDescriptions = []
		self.itemOriginalDescriptions = []
	
	#getters and setters
	#getter
	@property
	def name(self):
		return self._name
	
	#setter
	@name.setter
	def name(self, value):
		self._name = value
	
	@property
	def exits(self):
		return self._exits
	
	@exits.setter
	def exits(self, value):
		self._exits = value
	
	@property
	def exitLocations(self):
		return self._exitLocations
	
	@exitLocations.setter
	def exitLocations(self, value):
		self._exitLocations = value
		
	@property
	def items(self):
		return self._items
		
	@items.setter
	def items(self, value):
		self._items = value
		
	@property
	def itemDescriptions(self):
		return self._itemDescriptions
		
	@itemDescriptions.setter
	def itemDescriptions(self, value):
		self._itemDescriptions = value
		
	@property
	def grabbables(self):
		return self._grabbables
	
	@grabbables.setter
	def grabbables(self, value):
		self._grabbables = value
		
	@property
	def grabbablesDescriptions(self):
		return self._grabbablesDescriptions
		
	@grabbablesDescriptions.setter
	def grabbablesDescriptions(self, value):
		self._grabbablesDescriptions = value
		
	@property
	def itemOriginalDescriptions(self):
		return self._itemOriginalDescriptions
		
	@itemOriginalDescriptions.setter
	def itemOriginalDescriptions(self, value):
		self._itemOriginalDescriptions = value
		
	# adds an exit to the room
	# the exit is a string (e.g., north)
	# the room is an instance of a room	
	def addExit(self, exit, room):
		self._exits.append(exit)
		self._exitLocations.append(room)
	
	def addItem (self, name, desc, grab = ""):
		self._items.append(name)
		self._itemOriginalDescriptions.append(desc)
		if (grab != ""):
			desc = desc + " There is a {}".format(grab) + " on the {}".format(name)
		self.itemDescriptions.append(desc)
		
	# adds a grabbable to the room, appends to list
	def addGrabbable(self, item, description):
		self._grabbables.append(item)
		self.grabbablesDescriptions.append(description)
		
		
	# Deletes grabbable, removes grabbable description, fixes item description
	def delGrabbable(self, item):
		# Saves index of grabbable to i
		i = self._grabbables.index(item)
		# removes grabbable and grabbable description from proper lists
		self._grabbables.remove(item)
		del self._grabbablesDescriptions[i]
		# Iterate through itemDescriptions, looking for grabbable. If found, revert item to description
			# that is without the grabbable. 
		for a1 in self._itemDescriptions:
			if (item in a1):
				i = self._itemDescriptions.index(a1)
				self._itemDescriptions[i] = self._itemOriginalDescriptions[i]
				break
		
		
		
		
	
	#prints a string description of the room	
	def __str__(self):
		#the room name
		s = "You are in {}.\n".format(self.name)
		
		#items in room
		s += "You see: "
		for item in self.items:
			s += item + " "
		s += "\n"
		
		#exits from room
		s += "Exits: "
		for exit in self.exits:
			s += exit + " "
		return s
	


# displays an appropriate "message" when the player dies
# yes, this is intentionally obfuscated!
def death():
	print " " * 17 + "u" * 7
	print " " * 13 + "u" * 2 + "$" * 11 + "u" * 2
	print " " * 10 + "u" * 2 + "$" * 17 + "u" * 2
	print " " * 9 + "u" + "$" * 21 + "u"
	print " " * 8 + "u" + "$" * 23 + "u"
	print " " * 7 + "u" + "$" * 25 + "u"
	print " " * 7 + "u" + "$" * 25 + "u"
	print " " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3 +"\"" + " " * 3 + "\"" + "$" * 6 + "u"
	print " " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7+ "$" * 4 + "\""
	print " " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u" +"$" * 3
	print " " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" + "" * 6 + "u" + "$" * 3
	print " " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 +"$" * 3 + "u" * 2 + "$" * 4 + "\""
	print " " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" * 7+ "\""
	print " " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u"
	print " " * 13 + "u$\"$\"$\"$\"$\"$\"$u"
	print " " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" + "$"* 2 + " " * 7 + "u" * 3
	print " u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3 + "" * 7 + "u" + "$" * 4
	print " " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9 +"\"" + " " * 5 + "u" * 2 + "$" * 6
	print "u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " * 4 +"u" * 4 + "$" * 10
	print "$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 + "u" * 2+ "$" * 9 + "\"" * 3 + "$" * 3 + "\""
	print " " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" * 2 +" " + "\"" * 2 + "$" + "\"" * 3
	print " " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3
	print " " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2 +" \"\"" + "$" * 11 + "u" * 3 + "$" * 3
	print " " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" + "$" *11 + "\""
	print " " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" + "$" *4 + "\"\""
	print " " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\""


#creates the rooms
def createRooms():
	global currentRoom
	r1 = Room("Room 1")
	r2 = Room("Room 2")
	r3 = Room("Room 3")
	r4 = Room("Room 4")
	
	r1.addExit("east", r2)
	r1.addExit("south", r3)
	# add grabbables to room 1
	r1.addGrabbable("key", "A golden key.")
	r1.addGrabbable("glasses","An old pair of glasses.")
	# add items to room 1

	
	r1.addItem("table", "It is made of oak.", "key")
	r1.addItem("chair", "It is made of wicker and no one is sitting on it.", "glasses")
	
	
	r2.addExit("south", r4)
	r2.addExit("west", r1)
	#r2.addItem("rug", "Persian")
	#r2.addItem("fireplace", "Has Ashes")
	
	r3.addExit("north", r1)
	r3.addExit("east", r4)
	r3.addItem("bookshelves", "They are empty")
	r3.addItem("desk", "An old, worn down desk.", "book")
	r3.addGrabbable("book", "An introduction to Scratch, the only tool you'll ever need")
	
	r4.addExit("north", r2)
	r4.addExit("west", r3)
	r4.addExit("south", None) #DEATH
	#r4.addItem("rug", "It is made of wicker and no one is sitting on it.")
	#r4.addItem("table", "It is made of oak.")
	#r4.addGrabbable("knife")
	
	#start in room 1
	currentRoom = r1
	
#main part of program
inventory = []
inventoryDescriptions = []
createRooms()
#play forever
while (True):
	#set the status so the player has situational awareness
	#the status has room and inventory information
	status = "{}\nYou are carrying: {}\n".format(currentRoom, inventory)
	if (currentRoom == None ):
		death()
		break
	# display the status
	print "========================================================="
	print status
	# prompt for player input
	# the game supports a simple language of <verb> <noun>
	# valid verbs are go, look, and take
	# valid nouns depend on the verb
	# we use raw_input here to treat the input as a string instead of
	# an expression
	action = raw_input("What to do? ")
	# set the user's input to lowercase to make it easier to compare
	# the verb and noun to known values
	action = action.lower()
	# exit the game if the player wants to leave (supports quit,
	# exit, and bye)
	if (action == "quit" or action == "exit" or action == "bye"):
		break

	# set a default response
	response = "I don't understand. Try verb noun. Valid verbs are go, look, and take"
	# split the user input into words (words are separated by spaces)
	# and store the words in a list
	words = action.split()
	if (len(words) == 3):
		temp = words[1] + " " + words[2]
		words[1] = temp
		print words[1]
	# the game only understands two word inputs
	if (len(words) == 2):
		# isolate the verb and noun
		verb = words[0]
		noun = words[1]
	
		# the verb is: go
		if (verb == "go"):
			# set a default response
			response = "Invalid exit."
			
			# check for valid exits in the current room
			for i in range(len(currentRoom.exits)):
				# a valid exit is found
				if (noun == currentRoom.exits[i]):
				# change the current room to the one that is
				# associated with the specified exit
					currentRoom = currentRoom.exitLocations[i]
					# set the response (success)
					response = "Room changed."
					# no need to check any more exits
					break
		# the verb is: look
		elif (verb == "look"):
			
			# set a default response
			response = "I don't see that item."
			# check for valid items in the current room
			for i in range(len(currentRoom.items)):
				# a valid item is found
				if (noun == currentRoom.items[i]):
					# set the response to the item's description
					response = currentRoom.itemDescriptions[i]
					# no need to check any more items
					break
					# the verb is: take
			for i in range(len(inventory)):
				# a valid item is found
				if (noun == inventory[i]):
					# set the response to the item's description
					response = inventoryDescriptions[i]
					break
				
					
					
		elif (verb == "take"):
			# set a default response
			response = "I don't see that item."
			
			# check for valid grabbable items in the current room
			for grabbable in currentRoom.grabbables:
				# a valid grabbable item is found
				if (noun == grabbable):
					# add the grabbable item to the player's
					# inventory
					inventory.append(grabbable)
					i = currentRoom.grabbables.index(grabbable)
					
					inventoryDescriptions.append(currentRoom.grabbablesDescriptions[i])
		
					# remove the grabbable item from the room
					currentRoom.delGrabbable(grabbable)
		
					# set the response (success)
					response = "{} grabbed.".format(grabbable)
		
					# no need to check any more grabbable item
					break
	#display the response 
	print "\n{}".format(response)


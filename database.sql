DROP DATABASE IF EXISTS space;


# Creating new database.
CREATE DATABASE space;


# Using database.
USE space;

#CREATE USER 'spacecaptain'@'localhost' IDENTIFIED BY 'rocket';
#GRANT SELECT, INSERT, UPDATE, DELETE ON space.* TO spacecaptain@localhost;


# Creating NPC-table.
CREATE TABLE NPC (
		ID INTEGER NOT NULL,
		Name VARCHAR(50) NOT NULL,
		Description VARCHAR(500),
		Dialogues VARCHAR(1000) NOT NULL,
		
		# Setting primary key.
		PRIMARY KEY (ID));


# Creating Item-table.
CREATE TABLE Item (
		ID INTEGER NOT NULL,
		Name VARCHAR(50) NOT NULL,
		Description VARCHAR(500) NOT NULL,
		Interactive INTEGER NOT NULL,
		Ownership INTEGER NOT NULL,
		Relates INTEGER,
		Combines INTEGER,
		
		# Setting primary key.
		PRIMARY KEY (ID));


# Creating RoomState-table.
CREATE TABLE RoomState (
		RoomID INTEGER NOT NULL,
		ID INTEGER NOT NULL,
		Name VARCHAR(50) NOT NULL,
		Description VARCHAR(1000) NOT NULL,
		ImagePath VARCHAR(500),
		North INTEGER,
		East INTEGER,
		South INTEGER,
		West INTEGER,
		Item1 INTEGER,
		Item2 INTEGER,
		Item3 INTEGER,
		NPCID INTEGER,
		Keyword VARCHAR(500),
		KeyItem INTEGER,
		
		# Setting primary key.
		PRIMARY KEY (RoomID, ID),
		
		# Setting foreign keys.
		FOREIGN KEY (Item1) REFERENCES Item (ID),
		FOREIGN KEY (Item2) REFERENCES Item (ID),
		FOREIGN KEY (Item3) REFERENCES Item (ID),
		FOREIGN KEY (NPCID) REFERENCES NPC (ID),
		FOREIGN KEY (KeyItem) REFERENCES Item (ID));


# Creating Room-table.
CREATE TABLE Room (
		ID INTEGER NOT NULL,
		RoomStateID INTEGER NOT NULL,
		
		# Setting primary key.
		PRIMARY KEY (ID),
		
		# Setting foreign keys.
		FOREIGN KEY (ID, RoomStateID) REFERENCES RoomState (RoomID, ID));


# Creating Player-table.
CREATE TABLE Player (
		ID INTEGER NOT NULL,
		RoomID INTEGER NOT NULL,
		
		# Setting primary key.
		PRIMARY KEY (ID),
		
		# Setting foreign key.
		FOREIGN KEY (RoomID) REFERENCES Room (ID));


# Inserting data into NPC-table. (ID, Name, Description, Dialogues)
INSERT INTO NPC
		VALUES(1, "Captain", "Quite a scent this guy has.", "Well, that was a spicy meatball. Well, back to work.");
INSERT INTO NPC
		VALUES(2, "Pmurt", "Wants to build protective bubble around the Earth and run for overlord of the galaxy.", "No illegal migrants in this galaxy! We are making Mars great again! "
				"After Pmurt fulfills his plans to have a 55 feet thick protective bubble around the Earth, he will be elected as the new overlord of the galaxy! "
				"No more illegal weak, sick and deceiving earthlings with their insecure e-mails! And want to hear the best part of it? YOU ARE GOING TO PAY THE WHOLE FREAKING BUBBLE! "
				"Pmurt would kill you otherwise, but it would be way too much paperwork for Pmurt and his small hands to handle. NOT EVEN THE ONE WHO LOVED US ALL CAN SAVE YOU PESKY HUMANS NOW! "
				"\nBob: Oh dear… You need a miracle to go past this Pmurt guy… But miracles only happen in movies and games like this… Maybe you could give it a shot and start praying?");
INSERT INTO NPC
		VALUES(3, "Harambe", "Scout kid!", "Rrrrraarrrgggh!");


# Inserting data into Item-table. (ID, Name, Description, Interactive, Ownership, Relates, Combines)
INSERT INTO Item
		VALUES(1, "Paper note", "Welcome to Universe Mission. This is the last ditch effort of mankind. As you are aware, captain, the emergency override code for the dashboard is 1234.", 1, 0, null, null);
INSERT INTO Item
		VALUES(2, "Alerting Dashboard", "The dashboard is flashing red with unintelligible terms. By swiping left, the dashboard asks for an override code. What is it?", 0, 0, null, null);
INSERT INTO Item
		VALUES(3, "Dashboard", "The flashing stops and the dashboard allows you to unlock the bridge doors.", 0, 0, null, null);
INSERT INTO Item
		VALUES(4, "Wet mop", "Space or no space, mops are a vital part of a janitor’s toolset.", 1, 0, null, null);
INSERT INTO Item
		VALUES(5, "Graffiti", "“MAKE MARS GREAT AGAIN!” The 25th century has its own set of vandals. By the looks of it, the graffiti is made using a red marker pen.", 0, 0, null, null);
INSERT INTO Item
		VALUES(6, "Clean wall", "There, much better. A clean ship is a more comfortable ship for everyone.", 0, 0, null, null);
INSERT INTO Item
		VALUES(7, "Gooped keypad", "The keypad covered in goop seems to be of very little use.", 0, 0, null, null);
INSERT INTO Item
		VALUES(8, "Keybad", "It’s an elevator keypad. Pushing it opens the elevator.", 0, 0, null, null);
INSERT INTO Item
		VALUES(9, "Soap", "It’s a bar of soap.", 1, 0, 12, 13);
INSERT INTO Item
		VALUES(10, "Bucket", "It’s a standard issue Earth Federation bucket made out of galactic plastic.", 1, 0, 11, 12);
INSERT INTO Item
		VALUES(11, "Water tap", "It’s a water tap. What do you expect?", 0, 0, 10, 12);
INSERT INTO Item
		VALUES(12, "Bucket of water", "It’s a bucket with clear water.", 1, 0, 9, 13);
INSERT INTO Item
		VALUES(13, "Bucket with water and soap", "Don’t drink this. Soapy water isn’t good for you.", 1, 0, null, null);
INSERT INTO Item
		VALUES(14, "Vomit", "It’s a very disgusting looking pile of vomit. You wish someone else were the janitor here.", 0, 0, null, null);
INSERT INTO Item
		VALUES(15, "Picture", "It’s a very soothing picture of a gorilla. The letter H is engraved in gold on it.", 0, 0, null, null);
INSERT INTO Item
		VALUES(16, "Bag of crisps", "It’s a bag of crisps, the king of comfort food.", 1, 0, null, null);
INSERT INTO Item
		VALUES(17, "Master key", "It’s a master key. Hindsight 20/20 but maybe you should’ve had this with you all along.", 1, 0, null, null);
INSERT INTO Item
		VALUES(18, "Window", "Based on the window view, you’re very close to Uranus.", 0, 0, null, null);
INSERT INTO Item
		VALUES(19, "Button 1", "It's a button to the Bridge.", 0, 0, null, null);
INSERT INTO Item
		VALUES(20, "Button 2", "It's a button to the Engineering.", 0, 0, null, null);
INSERT INTO Item
		VALUES(21, "Button 3", "It's a button to the Deck 42.", 0, 0, null, null);
INSERT INTO Item
		VALUES(22, "Clothespin", "Somebody must have dropped this on the way to the laundry room.", 1, 0, null, null);
INSERT INTO Item
		VALUES(666, "Pentagram", "A sign of the end times", 0, 0, null, null);		


# Inserting data into RoomState-table. (RoomID, ID, Name, Description, ImagePath, North, East, South, West, Item1, Item2, Item3, NPCID, Keyword, KeyItem)
INSERT INTO RoomState
		VALUES(1, 1, "The Bridge", "As you enter the bridge, you're struck by a sudden dread. The bridge is that of your average Federation warship. "
				"Golden decorations, posters of Miss Multiverse 2421 and video games. But why is the bridge empty? Soon after, the emergency lockdown starts for no apparent reason. "
				"As you just cleaned the place, you only need to get out… no harm just disabling the emergency lockdown, right? There is a 'paper note' on this 'alerting dashboard'."
				"\nThere’s an exit to the south, but it is locked.", "bridge.png", null, null, null, null, 1, 2, null, null, "1234", null);
INSERT INTO RoomState
		VALUES(1, 2, "The Bridge", "There, much better. No flashing red lights, the 'dashboard' is stabilized. "
				"But now the double-double bacon burger with cheese you had for lunch is coming out fast and is its own emergency. Where’s the bathroom? \nThere’s an exit to the south.", "bridge.png", null, null, 2,
				null, 3, null, null, null, null, null);
INSERT INTO RoomState
		VALUES(2, 1, "Dirty Corridor", "Wait, what is this? This corridor was cleaned 30 minutes ago. Now someone has already ruined the walls with 'graffiti'. Luckily, there is a 'wet mop' on the floor. "
				"\nThe corridor continues to the south. There’s a door to the north.", "corridor.png", 1, null, 3, null, 4, 5, null, null, null, 4);
INSERT INTO RoomState
		VALUES(2, 2, "Dirty Corridor", "Wait, what is this? This corridor was cleaned 30 minutes ago. Now someone has already ruined the walls with 'graffiti'. \nThe corridor continues to the south. "
				"There’s a door to the north.", "corridor.png", 1, null, 3, null, 5, null, null, null, "clean graffiti", 4);
INSERT INTO RoomState
		VALUES(2, 3, "Just a plain Corridor", "You cleaned up the grafitti and all that is left is 'clean wall'. Clean corridors are a janitor’s best friend. "
				"You actually aren’t paid to do this but it soothes your soul nonetheless. \nThe corridor continues to the south. There’s a door to the north.", "corridor.png", 1, null, 3, null, 6, null, null, null, null,
				null);
INSERT INTO RoomState
		VALUES(3, 1, "Stinky Elevator Corridor", "Oh science, this smell! You can’t even think straight… There is a single 'clothespin' on the corridor floor.", "corridor2.png", 2, null, null, null, 7, 22, null, null, null,
				22);
INSERT INTO RoomState
		VALUES(3, 2, "Stinky Elevator Corridor", "Oh science, this smell! You can’t even think straight…", "corridor2.png", 2, null, null, null, 7, 22, null, null,
				"use clothespin", 22);
INSERT INTO RoomState
		VALUES(3, 3, "Stinky Elevator Corridor", "After plugging the 'clothespin' on your nose you can see the 'gooped keypad' before the elevator. \nThe corridor goes north. "
				"There’s a door to the east and an elevator to the west.", "corridor2.png", 2, 4, null, null, 7, null, null, null, "clean gooped keypad", 13);
INSERT INTO RoomState
		VALUES(3, 4, "Stinky Elevator Corridor", "Cleaning the yellow goop didn’t help much but at least there is a way out of this stinky corridor. \nThe corridor goes north. "
				"There’s a door to the east and an elevator to the west.", "corridor2.png", 2, 4, null, 5, 8, null, null, null, null, null);
INSERT INTO RoomState
		VALUES(4, 1, "The Broom Closet", "A broom closet in 25th century looks largely the same as a broom closet in the 21st century. It’s largely an unassuming place. "
				"On the floor there’s a 'bucket' and 'soap'. There’s also a 'water tap'... Maybe you should pick up a 'bucket'? \nThere’s a corridor to the west.", "broomcloset.png", null, null, null, 3, 9, 10, 11, null, null,
				10);
INSERT INTO RoomState
		VALUES(4, 2, "The Broom Closet", "A broom closet in 25th century looks largely the same as a broom closet in the 21st century. It’s largely an unassuming place. On the floor there’s 'soap'. "
				"There’s also a 'water tap'. \nThere’s a corridor to the west.", "broomcloset.png", null, null, null, 3, 9, 11, null, null, null, 9);
INSERT INTO RoomState
		VALUES(4, 3, "The Broom Closet", "A broom closet in 25th century looks largely the same as a broom closet in the 21st century. It’s largely an unassuming place. There’s also a 'water tap.' "
				"\nThere’s a corridor to the west.", "broomcloset.png", null, null, null, 3, 11, null, null, null, null, null);
INSERT INTO RoomState
		VALUES(5, 1, "The Elevator", "The elevator seems like the only clean place so far. There’s a control panel with three buttons. "
				"'Button 1' is for the bridge, 'Button 2' is for the engine room and 'Button 3' is for Deck 42. A curious amount of buttons for a ship with 50 decks. \nThere’s a corridor to the east.", "elevator.png",
				null, 3, null, null, 19, 20, 21, null, "press button 3", null);
INSERT INTO RoomState
		VALUES(5, 2, "The Elevator", "After the ride the elevator sits still. You smell smoke coming from the keypad buttons; the elevator is completely useless now. \nThe door is open to the east.", "elevator.png", null, 6, null, null, 19, 20, 21, null, null, null);
INSERT INTO RoomState
		VALUES(6, 1, "Bathroom Corridor", "The corridor looks largely the same as the corridor upstairs. Only the sound of sewers makes it seem any different."
				"\nThere’s a locked bathroom door to the east and the corridor continues north.", "corridor_mirrored.png", 7, null, null, null, null, null, null, null, "unlock door", 17);
INSERT INTO RoomState
		VALUES(6, 2, "Bathroom Corridor", "A faint whiff of a toilet fills the air. \nThere’s a bathroom door to the east and the corridor continues north.", "corridor_mirrored.png", 7, 10, null, null, null, null, null, null,
				null, null);
INSERT INTO RoomState
		VALUES(7, 1, "Disgusting Corridor", "Oh boy. This place is quite the mess. There’s 'vomit' on the window to space. It stinks and blocks the beautiful view. "
				"\nThere’s a door to the north and the corridor continues to the south.", "corridor2_mirrored.png", 8, null, 6, null, 14, null, null, null, "clean vomit", 13);
INSERT INTO RoomState
		VALUES(7, 2, "Just another Corridor", "Another cleaned corridor. The 'window' shows a very beautiful view of the space beyond. \nThere’s a door to the north and the corridor continues to the south.",
				"corridor2_mirrored.png", 8, null, 6, null, 18, null, null, null, null, null);
INSERT INTO RoomState
		VALUES(8, 1, "Living Quarters", "The living quarters have always been a miserably sterile place. As a janitor, you enjoy the cleanliness of the place but otherwise the place bores you to tears. "
				"This time, though, there’s an unusual sight to see. A green creature with a “Vote for 'Pmurt'” election pin is guarding the lobby. "
				"Another more interesting addition is a 'picture' of a gorilla on the lobby table with the letter H on it. "
				"\nThere’s a corridor to the south and an open door to the east but you need to get past the creature first.", "livingquarters.png", null, null, 7, null, 15, null, null, 2, "pray for harambe", null);
INSERT INTO RoomState
		VALUES(8, 2, "Living Quarters", "A wild Harambe appears and throws Pmurt out of the spaceship… it seemed as easy as throwing a baby into a gorilla pit. "
				"\nThere’s a corridor to the south but the Holy Gorilla is blocking the way. You feel compelled to 'thank' this mysterious saviour.", "harambe.png", null, 9, null, null, 15, null, null, 3, "thank", null);
INSERT INTO RoomState
		VALUES(8, 3, "Living Quarters", "The living quarters have always been a miserably sterile place. As a janitor, you enjoy the cleanliness of the place but otherwise the place bores you to tears. "
				"A strangely unassuming gorilla looks at you. He looks very similiar to the one in the 'picture'. \nThere’s a corridor to the south and an open door to the east.", "livingquarters.png", null, 9, 7, null, 15,
				null, null, 3, null, null);
INSERT INTO RoomState
		VALUES(9, 1, "Janitor's Room", "Ah, home sweet home. This is your castle. It has all the things a man needs, a 'bag of crisps', a desk and a picture of a dog. "
				"The desk has all of your important things including a 'master key'... That seems important, maybe you should have it with you? \nThere’s a door to the west.", "janitorsroom.png", null, null, null, 8, 16, 17,
				null, null, null, 17);
INSERT INTO RoomState
		VALUES(9, 2, "Janitor's Room", "Ah, home sweet home. This is your castle. There's a 'bag of crisps', a desk and a picture of a dog. \nThere’s a door to the west.", "janitorsroom.png", null, null, null, 8,
				16, null, null, null, null, 16);
INSERT INTO RoomState
		VALUES(9, 3, "Janitor's Room", "After emptying your room of all valuables, you don’t think there’s much here. \nThere’s a door to the west.", "janitorsroom.png", null, null, null, 8, null, null, null, null, null,
				null);
INSERT INTO RoomState
		VALUES(10, 1, "The Bathroom", "The smell of this room reminds you of a toilet. Maybe this is because that is what the room is. All of the stalls are locked. All you can do is wait. "
				"\nThere’s a door to the west.", "toilet.png", null, null, null, 6, null, null, null, null, "wait", null);
INSERT INTO RoomState
		VALUES(10, 2, "The Bathroom", "You're getting extremely impatient. So much so that you accidentally lock the bathroom door."
				"", "toilet.png", null,
				null, null, null, null, null, null, null, "wait", null);
INSERT INTO RoomState
		VALUES(10, 3, "The Bathroom", "The captain gets out of the toilet and quickly rushes out into the corridor. You quickly rush into the toilet and do your deed. As you're just finishing your deed, the emergency lockdown starts again with the captain of the ship bellowing 'WHO DISABLED THE LOCKDOWN?' from the ship's intercomm. You sigh and get out... waiting for your next adventure. [GAME ENDS]", "toilet.png", null, null, null, null, null, null, null, 1, null, 666);
		
# Inserting data into Room-table. (ID, RoomStateID)
INSERT INTO Room
		VALUES(1, 1);
INSERT INTO Room
		VALUES(2, 1);
INSERT INTO Room
		VALUES(3, 1);
INSERT INTO Room
		VALUES(4, 1);
INSERT INTO Room
		VALUES(5, 1);
INSERT INTO Room
		VALUES(6, 1);
INSERT INTO Room
		VALUES(7, 1);
INSERT INTO Room
		VALUES(8, 1);
INSERT INTO Room
		VALUES(9, 1);
INSERT INTO Room
		VALUES(10, 1);
		
# Inserting data into Player-table. (ID, RoomID)
INSERT INTO Player
		VALUES(1, 1);





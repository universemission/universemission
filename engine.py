import mysql.connector
import ui



#Introducing variables
gamecommands = ['move', 'look', 'examine', 'cry', 'end', 'combine','pick', 'pray', 'inventory']
crycount = 0
game = 0
keyword=False
keyitem=False
consoletext=""
consoletext_prev=""
#Returns information from database
def database(information):
   #Returns player position room
   if information == "room":
       sql="SELECT RoomID FROM player"
       cur.execute(sql)
       for result in cur:
           return result[0]
   elif information == "roomname":
       sql = "SELECT roomstate.name FROM roomstate,player, room WHERE roomstate.RoomID = player.RoomID AND Roomstate.Id = Room.RoomstateId AND roomstate.roomid = room.id"
       cur.execute(sql)
       for result in cur:
           return result[0]
   #Returns current roomstate from the room player is in
   elif information == "roomstate":
       sql = "SELECT RoomStateID FROM room"
       cur.execute(sql)
       for result in cur:
           return result[0]
   #Current roomstates open passages to north
   elif information == "north":
       sql = "SELECT roomstate.north FROM roomstate,player, room WHERE roomstate.RoomID = player.RoomID AND Roomstate.Id = Room.RoomstateId AND roomstate.roomid = room.id"
       cur.execute(sql)
       for result in cur:
           return result[0]
   # Current roomstates open passages to east
   elif information == "east":
       sql = "SELECT roomstate.east FROM roomstate,player, room WHERE roomstate.RoomID = player.RoomID AND Roomstate.Id = Room.RoomstateId AND roomstate.roomid = room.id"
       cur.execute(sql)
       for result in cur:
           return result[0]
   # Current roomstates open passages to south
   elif information == "south":
       sql = "SELECT roomstate.south FROM roomstate,player, room WHERE roomstate.RoomID = player.RoomID AND Roomstate.Id = Room.RoomstateId AND roomstate.roomid = room.id"
       cur.execute(sql)
       for result in cur:
           return result[0]
   # Current roomstates open passages to west
   elif information == "west":
       sql = "SELECT roomstate.west FROM roomstate,player, room WHERE roomstate.RoomID = player.RoomID AND Roomstate.Id = Room.RoomstateId AND roomstate.roomid = room.id"
       cur.execute(sql)
       for result in cur:
           return result[0]
   #Description of the current roomstate
   elif information == "description":
       sql = "SELECT roomstate.Description FROM roomstate,player, room WHERE roomstate.RoomID = player.RoomID AND Roomstate.Id = Room.RoomstateId AND roomstate.roomid = room.id"
       cur.execute(sql)
       for result in cur:
           return result[0]


   else:
       return 0


#Finds out if string is the same as roomstates keyword string
def iskeyword(information):


   global keyword
   keywordcheck = str
   item1 = ' '.join(information)


   sql = "SELECT keyword FROM roomstate, player,room WHERE roomstate.RoomID = player.RoomID AND Roomstate.Id = Room.RoomstateId AND roomstate.roomid = room.id"
   cur.execute(sql)
   for result in cur:
       keywordcheck = result[0]


   if keywordcheck == item1:


       keyword = True
       return True
   else:


       keyword = False
       return False


#Lists items player currently owns
def owneditemsmethod():
   playeritems = []
   sql = "SELECT ID FROM ITEM WHERE Ownership = 1"
   cur.execute(sql)
   for result in cur:
       playeritems.extend(result)


       if None in playeritems:
           playeritems.remove(None)


   return playeritems


#Lists items in same roomstate which are not owned by a player
def roomitemsmethod():
   roomitems = []
   playeritems = []
   sql = "SELECT roomstate.item1, roomstate.item2, roomstate.item3 FROM roomstate, player,room WHERE roomstate.RoomID = player.RoomID AND Roomstate.Id = Room.RoomstateId AND roomstate.roomid = room.id"
   cur.execute(sql)
   for results in cur:
       roomitems = list(results)


   if None in roomitems:
       roomitems.remove(None)


   return roomitems




#lists all available items. Owned by player + items on roomstate
def availableitems():
   roomitems = []
   playeritems = []
   temporarylist = []
   sql = "SELECT roomstate.item1, roomstate.item2, roomstate.item3 FROM roomstate, player,room WHERE roomstate.RoomID = player.RoomID AND Roomstate.Id = Room.RoomstateId AND roomstate.roomid = room.id"
   cur.execute(sql)
   for results in cur:
       roomitems = list(results)


   sql = "SELECT ID FROM ITEM WHERE Ownership = 1"
   cur.execute(sql)
   for result in cur:
       playeritems.extend(result)
   roomitems = roomitems + playeritems


   if None in roomitems:
       roomitems.remove(None)




   return roomitems


def itemsavailablelist():
   itemlist = owneditemsmethod()


   namelist = []
   if len(itemlist) > 0:
       for x in range(0,len(itemlist)):
           sql = "SELECT name FROM ITEM WHERE id ='" + str(itemlist[x]) +"'"
           cur.execute(sql)
           for result in cur:
               namelist.append(result)


       namelist = list(namelist)
       return ("          ".join([" ".join(x) for x in namelist]))
   else:
       return "None."


#Sees if there is also an keyitem in the room. If not, roomstate ++. If is and player owns item, roomstate ++
def situationcheck():
   global keyword
   keyitemcheck = str
   ownership = str
   sql = "SELECT keyitem FROM roomstate, player,room WHERE roomstate.RoomID = player.RoomID AND Roomstate.Id = Room.RoomstateId AND roomstate.roomid = room.id"
   cur.execute(sql)
   for result in cur:
       keyitemcheck = result[0]


   if keyitemcheck is None and keyword == True:
       sql = "UPDATE room, roomstate, player SET room.roomstateID = roomstateID +1 WHERE roomstate.RoomID = player.RoomID AND Roomstate.Id = Room.RoomstateId AND roomstate.roomid = room.id"
       cur.execute(sql)
       UpdateConsole(database("description"))
       keyword = False


   elif keyitemcheck is not None and keyword == True:
       sql = "SELECT ownership FROM item WHERE id ='"+str(keyitemcheck)+"'"
       cur.execute(sql)
       for result in cur:
           ownership = result[0]


       if ownership == 1:
           sql = "UPDATE room, roomstate, player SET room.roomstateID = roomstateID +1 WHERE roomstate.RoomID = player.RoomID AND Roomstate.Id = Room.RoomstateId AND roomstate.roomid = room.id"
           cur.execute(sql)
           UpdateConsole(database("description"))
           keyword = False












       else:


           keyword = False








   #ENDING THE GAME HAPPENS HERE


#Ends game. Value tells game why it was ended
def Endgame(value):
   global game
   if value == 1:
       game = 1
       UpdateConsole("YOu ended the game")
   if value == 2:
       UpdateConsole("You wept like a pussy you are too many times. Game over!")
       game = 1


#Command MOVE is processed here
def MoveRoom(direction):


   #Finds if provided direction is valid
   if direction == "north" or direction == "east" or direction == "south" or direction == "west":
       TryGoRoom = database(direction)


       #If there is passage to next room
       if  TryGoRoom!= None:
           UpdateConsole("You moved "+ str(direction))
           sql = "UPDATE PLAYER SET RoomID =" + str(TryGoRoom)
           cur.execute(sql)
           UpdateConsole(database("description"))
       #If you cant go there
       else:
           UpdateConsole("You cant go there! Banging your head to wall wont help!")


#Picking up items
def pick(information):
   #List "(pick,up,xxxx)" to string "xxxx"
   itemid = 0
   interactive = int
   information.pop(0)
   information.pop(0)
   item1 = ' '.join(information)


   sql = "SELECT ID FROM ITEM WHERE item.Name ='" + str(item1) + "'"
   cur.execute(sql)
   for result in cur:
       itemid = result[0]




   sql = "SELECT interactive FROM ITEM WHERE item.ID ='" + str(itemid) + "'"
   cur.execute(sql)
   for result in cur:
       interactive = result[0]




   roomitems = roomitemsmethod()
   owneditems = owneditemsmethod()




   if itemid is not None and itemid in roomitems and itemid not in owneditems and interactive == 1:
       sql = "UPDATE Item SET ownership = 1 WHERE id ='"+ str(itemid) + "'"
       cur.execute(sql)
       UpdateConsole("You picked up '"+ str(item1)+ "'.")


   elif itemid is not None and itemid in roomitems and itemid not in owneditems and interactive == 0:
       UpdateConsole("You cannot pick up that!")


   elif itemid is not None and itemid in owneditems and interactive == 1:
       UpdateConsole("You pick up'"+ str(item1) +"' from your pocket and place it in your other pocket.")
   else:
       UpdateConsole("There is no such item in here!")


#Reads item description
def look(information):
   information.pop(0)
   informationid = ' '.join(information)


   sql = "SELECT ID FROM ITEM WHERE item.Name ='" + str(informationid) + "'"
   cur.execute(sql)
   for result in cur:
       informationid = result[0]




   if informationid in availableitems():


       sql = "SELECT Description FROM ITEM WHERE id ='" + str(informationid) + "'"
       cur.execute(sql)
       for result in cur:
           UpdateConsole(result)




   else:
       UpdateConsole("Your eyes glaze over as you try to look at something that doesn't exist")


#Method for combining items
def combineitems(information):
   information.pop(0)
   item1list1 = []
   item1list2 = []
   informationid1 = 0
   informationid2 = 0
   combines = 0




   if "with" in information:
       #Finds the index of the word with from command
       splitter = information.index("with")


       #Makes all words before "with" to list and transforms it to string
       for x in range (0,splitter):
           item1list1.append(information[x])
       item1 = ' '.join(item1list1)




       #Makes all words after "with" to list and transforms it to string
       for x in range (splitter+1, len(information)):
           item1list2.append(information[x])
       item2 = ' '.join(item1list2)


       #Seeks item ID:s
       sql = "SELECT ID FROM ITEM WHERE item.Name ='" + str(item1) + "'"
       cur.execute(sql)
       for result in cur:
           informationid1 = result[0]


       sql = "SELECT ID FROM ITEM WHERE item.Name ='" + str(item2) + "'"
       cur.execute(sql)
       for result in cur:
           informationid2 = result[0]


       #Finds out if items exist and if not, creates errors according to what items are not available/not exist
       if informationid1 and informationid2 in availableitems():
           sql = "SELECT relates FROM ITEM WHERE item.ID ='" + str(informationid1) + "'"
           cur.execute(sql)
           for result in cur:
               combines = result[0]


           #If items can be combined, magic happens here
           if combines == informationid2:


               #Lets find the combining result item id and set its ownership to 1
               sql = "SELECT combines FROM ITEM WHERE item.ID ='" + str(informationid1) + "'"
               cur.execute(sql)
               for result in cur:
                   result = result[0]
               sql = "UPDATE item SET ownership = 1 WHERE item.ID ='" + str(result) + "'"
               cur.execute(sql)


               sql = "UPDATE item SET ownership = 0 WHERE item.ID ='" + str(informationid1) + "'"
               cur.execute(sql)
               sql = "UPDATE item SET ownership = 0 WHERE item.ID ='" + str(informationid2) + "'"
               cur.execute(sql)


               sql = "SELECT name FROM item WHERE ID ='" + str(result) + "'"
               cur.execute(sql)
               for result in cur:
                   finalproduct = result[0]


               UpdateConsole("Items '" + str(item1) + "' and '" + str(item2) + "' were combined succesfully to '" + str(finalproduct)+ "'.")


           else:
               UpdateConsole("These items cannot be combined together!")
           pass


       elif informationid1 in availableitems() and informationid2 not in availableitems():
           UpdateConsole("Item '"+ item2 + "' does not exist!")


       elif informationid1 not in availableitems() and informationid2 in availableitems():
           UpdateConsole("Item '"+ item1 + "' does not exist!")


       else:
           UpdateConsole("Item '" + item1 + "' nor '" + item2+ " 'exist you silly moron!")




   else:
       UpdateConsole("You pesky murloc should try to combine x WITH y")


#Method which prints out all console text in the game!
def UpdateConsole(text):
    global consoletext
    consoletext = str(text)
    ui.parseprint(str(text))

def returnConsoletext():
    global consoletext
    return consoletext

#Cry method. Cry 3 times and you are dead
def Cry():
   global crycount
   crycount = crycount+1
   UpdateConsole("You weep like a baby! Man up sir!")
   if crycount == 3:
       Endgame(2)


#Processing command happens here
def command(string):
   stringlower = string.lower()
   list = stringlower.split(' ')




   if iskeyword(list):
       pass


   elif list[0] in gamecommands:


       if list[0] == "move":
           if len(list)>1:
               MoveRoom(list[1])
           else:
               UpdateConsole("You should know the direction where to move before trying to do so!")


       elif list[0] == "cry":
           Cry()
       elif list[0] == "end":
           Endgame(1)
       elif list[0] == "look" or list[0] == "examine":
           if len(list) > 1:
               look(list)
           else:
               UpdateConsole(database("description"))
       elif list[0] == "combine":
           if len(list) > 1:
               combineitems(list)
           else:
               UpdateConsole("You combine emptiness with nothing.")


       elif list[0] == "pick":
           if len(list) >= 3 and list[1] == "up":
               pick(list)
           elif len(list) == 2 and list[1] == "up":
               UpdateConsole("You pick up nothing. Same applies for picking up women on this spaceship.")
           else:
               UpdateConsole("Maybe you should try to pick UP something")


       elif list[0] == "pray":
           if len(list) >=3 and list[0] =="pray" and list [1] == "for" and list[2] == "harambe":
               UpdateConsole("Harambe hears you and answers:'SCOUT around, KID.'")
           elif len(list) >=2 and list[1] =="pray" and list [2] == "for":
               UpdateConsole("Pray for what?")
           else:
               UpdateConsole("Who do you pray for?")
       elif list[0] == "inventory":
           UpdateConsole(itemsavailablelist())










   else:
       pass




   situationcheck()


#Game loop
def GAME():
   global db,cur
   db = mysql.connector.connect(host="localhost",user="root",passwd="juuri123",db="space",buffered=True)
   cur=db.cursor()
   return


GAME()



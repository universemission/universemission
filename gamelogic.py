import mysql.connector

pelikomennot = ['move', 'look', 'examine', 'cry', 'end']
crycount = 0
game = 0

def database(information):
   #Returns player position room
   if information == "room":
       sql="SELECT RoomID FROM player"
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
       sql = "SELECT North FROM roomstate"
       cur.execute(sql)
       for result in cur:
           return result[0]
   # Current roomstates open passages to north
   elif information == "east":
       sql = "SELECT east FROM roomstate"
       cur.execute(sql)
       for result in cur:
           return result[0]
   # Current roomstates open passages to north
   elif information == "south":
       sql = "SELECT south FROM roomstate"
       cur.execute(sql)
       for result in cur:
           return result[0]
   # Current roomstates open passages to north
   elif information == "west":
       sql = "SELECT west FROM roomstate"
       cur.execute(sql)
       for result in cur:
           return result[0]
   #Description of the current roomstate
   elif information == "description":
       sql = "SELECT Description FROM roomstate,player WHERE roomstate.RoomID = player.RoomID"
       cur.execute(sql)
       for result in cur:
           return result[0]




   else:
       return 0



def Updater():
   pass

#ENDING THE GAME HAPPENS HERE
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




def look(information):
   information.pop(0)
   informationid = ' '.join(information)

   sql = "SELECT ID FROM ITEM WHERE item.Name ='" + str(informationid) + "'"
   cur.execute(sql)
   for result in cur:
       informationid = result[0]


   sql = "SELECT roomstate.item1, roomstate.item2, roomstate.item3 FROM roomstate, player,room WHERE roomstate.RoomID = player.RoomID AND Roomstate.Id = Room.RoomstateId AND roomstate.roomid = room.id"
   cur.execute(sql)
   for result in cur:
       roomitems = list(result)

   sql = "SELECT ID FROM ITEM WHERE ownership = 1"
   cur.execute(sql)
   for result in cur:
       playeritems = list(result)
       roomitems.append(playeritems)


   if informationid in roomitems:

       sql = "SELECT Description FROM ITEM WHERE id ='" + str(informationid) + "'"
       cur.execute(sql)
       for result in cur:
           UpdateConsole(result)


   else:
       UpdateConsole("Your eyes glaze over as you try to look at something that doesn't exist")

import mysql.connector

pelikomennot = ['move', 'look', 'examine', 'cry', 'end']
crycount = 0
game = 0

def database(information):
    #Returns player position room
    if information == "room":
        sql="SELECT RoomID FROM player"
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
        sql = "SELECT North FROM roomstate"
        cur.execute(sql)
        for result in cur:
            return result[0]
    # Current roomstates open passages to north
    elif information == "east":
        sql = "SELECT east FROM roomstate"
        cur.execute(sql)
        for result in cur:
            return result[0]
    # Current roomstates open passages to north
    elif information == "south":
        sql = "SELECT south FROM roomstate"
        cur.execute(sql)
        for result in cur:
            return result[0]
    # Current roomstates open passages to north
    elif information == "west":
        sql = "SELECT west FROM roomstate"
        cur.execute(sql)
        for result in cur:
            return result[0]
    #Description of the current roomstate
    elif information == "description":
        sql = "SELECT Description FROM roomstate,player WHERE roomstate.RoomID = player.RoomID"
        cur.execute(sql)
        for result in cur:
            return result[0]




    else:
        return 0



def Updater():
    pass

#ENDING THE GAME HAPPENS HERE
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




def look(information):
    information.pop(0)
    informationid = ' '.join(information)

    sql = "SELECT ID FROM ITEM WHERE item.Name ='" + str(informationid) + "'"
    cur.execute(sql)
    for result in cur:
        informationid = result[0]


    sql = "SELECT roomstate.item1, roomstate.item2, roomstate.item3 FROM roomstate, player,room WHERE roomstate.RoomID = player.RoomID AND Roomstate.Id = Room.RoomstateId AND roomstate.roomid = room.id"
    cur.execute(sql)
    for result in cur:
        roomitems = list(result)

    sql = "SELECT ID FROM ITEM WHERE ownership = 1"
    cur.execute(sql)
    for result in cur:
        playeritems = list(result)
        roomitems.append(playeritems)


    if informationid in roomitems:

        sql = "SELECT Description FROM ITEM WHERE id ='" + str(informationid) + "'"
        cur.execute(sql)
        for result in cur:
            UpdateConsole(result)


    else:
        UpdateConsole("Your eyes glaze over as you try to look at something that doesn't exist")




def UpdateConsole(text):
    print (str(text))

def Cry():
    global crycount
    crycount = crycount+1
    UpdateConsole("You cried like a pussy you are!")
    if crycount == 3:
        Endgame(2)


def command(string):
    stringlower = string.lower()
    list = stringlower.split(' ')



    if list[0] in pelikomennot:

        if list[0] == "move":
            if len(list)>1:
                MoveRoom(list[1])
            else:
                UpdateConsole("Provide us the direction you want to go!")

        elif list[0] == "cry":
            Cry()
        elif list[0] == "end":
            Endgame(1)
        elif list[0] == "look" or list[0] == "examine":
            if len(list) > 1:
                look(list)
            else:
                UpdateConsole(database("description"))
    else:
        pass


def GAME():
    global db,cur
    db = mysql.connector.connect(host="localhost",user="Verkku",passwd="dbpass",db="space",buffered=True)
    cur=db.cursor()
    while game == 0:
        command(input(str("Anna Komento")))
    db.close()
    return

GAME()


def UpdateConsole(text):
   print (str(text))

def Cry():
   global crycount
   crycount = crycount+1
   UpdateConsole("You cried like a pussy you are!")
   if crycount == 3:
       Endgame(2)


def command(string):
   stringlower = string.lower()
   list = stringlower.split(' ')



   if list[0] in pelikomennot:

       if list[0] == "move":
           if len(list)>1:
               MoveRoom(list[1])
           else:
               UpdateConsole("Provide us the direction you want to go!")

       elif list[0] == "cry":
           Cry()
       elif list[0] == "end":
           Endgame(1)
       elif list[0] == "look" or list[0] == "examine":
           if len(list) > 1:
               look(list)
           else:
               UpdateConsole(database("description"))
   else:
       pass


def GAME():
   global db,cur
   db = mysql.connector.connect(host="localhost",user="Verkku",passwd="dbpass",db="space",buffered=True)
   cur=db.cursor()
   while game == 0:
       command(input(str("Anna Komento")))
   db.close()
   return

GAME()

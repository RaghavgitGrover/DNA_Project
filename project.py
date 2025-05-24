import subprocess as sp
import pymysql
import pymysql.cursors

# selct minimal functions

def get_pokemon(arg):
    try:
        q="SELECT * FROM pokemon WHERE Name = '%s'" % arg
        cur.execute(q)
        result = cur.fetchall()
        for row in result:
            # print all the moves of this pokemon
            print(row)
            sql = "SELECT * FROM pokemons_with_this_move WHERE Pokemon_Name = '%s'" % row["Name"]
            cur.execute(sql)
            result2 = cur.fetchall()
            print("Moves: ", end=' ')
            for row2 in result2:
                print(row2["Move_Name"], end=' ')
            print()
    except Exception as e:
        print("Error:", e)
    

def get_trainer(arg):
    try:
        q="SELECT * FROM trainer WHERE Trainer_ID = '%d'" % arg
        cur.execute(q)
        result = cur.fetchall()
        for row in result:
            print(row)
            q2="SELECT * FROM trainer_name WHERE Trainer_ID = '%d'" % row["Trainer_ID"]
            cur.execute(q2)
            result2 = cur.fetchall()
            print("Trainer Name: ", end=' ')
            for row2 in result2:
                print(row2["First_Name"], row2["Middle_Name"], row2["Last_Name"], end=' ')
            print()
            q3="SELECT * FROM trainer_number WHERE Trainer_ID = '%d'" % row["Trainer_ID"]
            cur.execute(q3)
            result2 = cur.fetchall()
            print("Phone Number: ", end=' ')
            for row2 in result2:
                print(row2["Country_Code"], row2["Phone_Number"], end=' ')
            # get pokemons owned by this trainer
            print()
            q4 = "SELECT * FROM pokemon_owned WHERE Trainer_ID = '%d'" % row["Trainer_ID"]
            cur.execute(q4)
            result2 = cur.fetchall()
            print("Pokemons Owned: ", end=' ')
            for row2 in result2:
                print(row2["Pokemon_Name"], end=' ')
            print()
    except Exception as e:
        print("Error:", e)
def get_tournament(arg):
    try:
        q="SELECT * FROM tournament WHERE Name = '%s'" % arg
        cur.execute(q)
        result = cur.fetchall()
        for row in result:
            print(row)
            q2="SELECT * FROM tournament_location WHERE Name = '%s'" % row["Name"]
            cur.execute(q2)
            result2 = cur.fetchall()
            print("Location of tournament : ", end=' ')
            for row2 in result2:
                print(row2["Region"], row2["City"], row2["Street"], end=' ')
            print()
    except Exception as e:
        print("Error:", e)
def get_gym(arg):
    try:
        q="SELECT * FROM gym WHERE Gym_Name = '%s'" % arg
        cur.execute(q)
        result = cur.fetchall()
        for row in result:
            print(row)
            q2="SELECT * from trainer_name WHERE Trainer_ID = '%d'" % row["Gym_Leader_ID"]
            cur.execute(q2)
            result2 = cur.fetchall()
            print("Leader Name: ", end=' ')
            for row2 in result2:
                print(row2["First_Name"], row2["Middle_Name"], row2["Last_Name"], end=' ')
            q3="SELECT * FROM gym_location WHERE Gym_Name = '%s'" % row["Gym_Name"]
            cur.execute(q3)
            result2 = cur.fetchall()
            print()
            print("Location of gym : ", end=' ')
            for row2 in result2:
                print(row2["Region"], row2["City"], row2["Street"], end=' ')
            print()
    except Exception as e:
        print("Error:", e)
def get_items(arg):
    try:
        q="SELECT * FROM items WHERE Item_Name = '%s'" % arg
        cur.execute(q)
        result = cur.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print("Error:", e)
def get_officials(arg):
    try:
        q="SELECT * FROM officials WHERE Official_ID = '%d'" % arg
        cur.execute(q)
        result = cur.fetchall()
        for row in result:
            print(row)
            q2="SELECT * FROM official_name WHERE Official_ID = '%d'" % row["Official_ID"]
            cur.execute(q2)
            result2 = cur.fetchall()
            print("Official Name: ", end=' ')
            for row2 in result2:
                print(row2["First_Name"], row2["Middle_Name"], row2["Last_Name"], end=' ')
            print()
            q3="SELECT * FROM official_location WHERE Official_ID = '%d'" % row["Official_ID"]
            cur.execute(q3)
            result2 = cur.fetchall()
            print("Official Location: ", end=' ')
            for row2 in result2:
                print(row2["Region"], row2["City"], end=' ')
            print()
    except Exception as e:
        print("Error:", e)
def get_event(arg):
    try:
        q="SELECT * FROM event WHERE Event_ID = '%d'" % arg
        cur.execute(q)
        result = cur.fetchall()
        for row in result:
            print(row)
            is_encounrt=True
            # print the associated entry, which is present in either Encounter or Battle
            sql2 = "SELECT * FROM encounter WHERE Event_ID = %d" % row["Event_ID"]
            cur.execute(sql2)
            row2 = cur.fetchone()
            # check if NULL, if it is the this was a battle
            if row2 is None:
                is_encounrt=False
                sql2 = "SELECT * FROM battle WHERE Event_ID = %d" % row["Event_ID"]
                cur.execute(sql2)
                row2 = cur.fetchone()
            if(is_encounrt):
                print("Pokemon Captured: ", end=' ')
                print( row2["Pokemon_Captured_Name"])
                q2 = "SELECT * FROM encounter_pokemons WHERE Event_ID = %d" % row["Event_ID"]
                cur.execute(q2)
                result2 = cur.fetchall()
                print("Pokemon Used: ", end=' ')
                for row2 in result2:
                    print(row2["Pokemon"], end=' ')
                print()
                q2 = "SELECT * FROM encounter_items_used WHERE Event_ID = %d" % row["Event_ID"]
                cur.execute(q2)
                result2 = cur.fetchall()
                print("Items Used: ", end=' ')
                for row2 in result2:
                    print(row2["Items"], end=' ')
                print()
                
            else:
                print("Battle: ", end=' ')
                print(row2["Trainer1_ID"], row2["Trainer2_ID"], end=' ')
                q2 = "SELECT * FROM battle_trainer1_items WHERE Event_ID = %d" % row["Event_ID"]
                cur.execute(q2)
                result2 = cur.fetchall()
                print("Items Used by Trainer 1: ", end=' ')
                for row2 in result2:
                    print(row2["Items"], end=' ')
                print()
                q2 = "SELECT * FROM battle_trainer2_items WHERE Event_ID = %d" % row["Event_ID"]
                cur.execute(q2)
                result2 = cur.fetchall()
                print("Items Used by Trainer 2: ", end=' ')
                for row2 in result2:
                    print(row2["Items"], end=' ')
                print()
                q2 = "SELECT * FROM battle_trainer1_pokemon_used WHERE Event_ID = %d" % row["Event_ID"]
                cur.execute(q2)
                result2 = cur.fetchall()
                print("Pokemon Used by Trainer 1: ", end=' ')
                for row2 in result2:
                    print(row2["Pokemon_Used"], end=' ')
                q2 = "SELECT * FROM battle_trainer2_pokemon_used WHERE Event_ID = %d" % row["Event_ID"]
                cur.execute(q2)
                result2 = cur.fetchall()
                print("Pokemon Used by Trainer 2: ", end=' ')
                for row2 in result2:
                    print(row2["Pokemon_Used"], end=' ')
            print()
    except Exception as e:
        print("Error:", e)  
def get_moves(arg):
    try:
        q="SELECT * FROM moves WHERE Move_Name = '%s'" % arg
        cur.execute(q)
        result = cur.fetchall()
        for row in result:
            print(row)
            sql2 = "SELECT * FROM types_of_move WHERE Move_Name = '%s'" % row["Move_Name"]
            cur.execute(sql2)
            result2 = cur.fetchall()
            print("Types: ", end=' ')
            for row2 in result2:
                print(row2["Move_Type"], end=' ')
            # get pokemons with this move
            q2 = "SELECT * FROM pokemons_with_this_move WHERE Move_Name = '%s'" % row["Move_Name"]
            cur.execute(q2)
            result2 = cur.fetchall()
            print()
            print("Pokemons with this move: ", end=' ')
            for row2 in result2:
                print(row2["Pokemon_Name"], end=' ')
            print()
    except Exception as e:
        print("Error:", e) 

# SELECT FUNCTIONS

def select_pokemon():
    try:
        sql = "SELECT * FROM pokemon"
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            print(row)
            # show the evolutions of this pokemon
            sql2 = "SELECT * FROM pokemon_evolves_to WHERE Pokemon_Name = '%s'" % row["Name"]
            cur.execute(sql2)
            result2 = cur.fetchall()
            print("Evolves to: ", end=' ')
            for row2 in result2:
                print(row2["Evolves_To"], end=' ')
            print()
            # show the types of this pokemon
            sql2 = "SELECT * FROM pokemon_types WHERE Pokemon_Name = '%s'" % row["Name"]
            cur.execute(sql2)
            result2 = cur.fetchall()
            print("Types: ", end=' ')
            for row2 in result2:
                print(row2["Type"], end=' ')
            print()
            # show the weaknesses of this pokemon
            sql2 = "SELECT * FROM pokemon_weaknesses WHERE Pokemon_Name = '%s'" % row["Name"]
            cur.execute(sql2)
            result2 = cur.fetchall()
            print("Weaknesses: ", end=' ')
            for row2 in result2:
                print(row2["Weakness"], end=' ')
            q2="SELECT * FROM pokemons_with_this_move WHERE Pokemon_Name = '%s'" % row["Name"]
            cur.execute(q2)
            result2 = cur.fetchall()
            print()
            print("Moves: ", end=' ')
            for row2 in result2:
                print(row2["Move_Name"], end=' ')
            
            print()
            
    except Exception as e:
        print("Error:", e)

def select_trainer():
    try:
        sql = "SELECT * FROM trainer" 
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            print(row)
            q2="SELECT * FROM trainer_name WHERE Trainer_ID = '%d'" % row["Trainer_ID"]
            cur.execute(q2)
            result2 = cur.fetchall()
            print("Trainer Name: ", end=' ')
            for row2 in result2:
                print(row2["First_Name"], row2["Middle_Name"], row2["Last_Name"], end=' ')
            print()
            # show the number of badges this trainer has
            sql2 = "SELECT Badges FROM trainer_badges WHERE Trainer_ID = '%d'" % row["Trainer_ID"]
            cur.execute(sql2)
            result2 = cur.fetchall()
            if len(result2) == 0:
                print("Badges: None")
            else:
                print("Badges: ", end=' ')
                for row2 in result2:
                    print(row2["Badges"], end=' ')
            print()
            # show the number
            sql2 = "SELECT Country_Code,Phone_Number FROM trainer_number WHERE Trainer_ID = '%d'" % row["Trainer_ID"]
            cur.execute(sql2)
            result2 = cur.fetchall()
            print("Phone Number: ", end=' ')
            for row2 in result2:
                print(row2["Country_Code"], row2["Phone_Number"], end=' ')
            print()
    except Exception as e:
        print("Error:", e)

def select_tournament():
    try:
        sql = "SELECT * FROM tournament"
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            print(row)
            # show the location of this tournament
            sql2 = "SELECT * FROM tournament_location WHERE Name = '%s'" % row["Name"]
            cur.execute(sql2)
            row2 = cur.fetchone()
            print("Location of tournament: ", end=' ')
            print(row2["Region"],row2["City"],row2["Street"], end=' ')
            print()
    except Exception as e:
        print("Error:", e)

def select_gym():
    try:
        sql = "SELECT * FROM gym"
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:

            print(row,end=' ')
            q3="SELECT * from trainer_name WHERE Trainer_ID = '%d'" % row["Gym_Leader_ID"]
            cur.execute(q3)
            result3 = cur.fetchall()
            print("Leader Name: ", end=' ')
            for row3 in result3:
                print(row3["First_Name"], row3["Middle_Name"], row3["Last_Name"], end=' ')
            sql2 = "SELECT * FROM gym_location WHERE Gym_Name = '%s'" % row["Gym_Name"]
            cur.execute(sql2)
            result2 = cur.fetchall()
            print("Location of gym : ", end=' ')
            for row2 in result2:
                print(row2["Region"], row2["City"], row2["Street"], end=' ')
            print()
    except Exception as e:
        print("Error:", e)  

def select_items():
    try:
        sql = "SELECT * FROM items"
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print("Error:", e)

def select_officials():
    try:
        sql = "SELECT * FROM officials"
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            print(row)
            q2="SELECT * FROM official_name WHERE Official_ID = '%d'" % row["Official_ID"]
            cur.execute(q2)
            result2 = cur.fetchall()
            print("Official Name: ", end=' ')
            for row2 in result2:
                print(row2["First_Name"], row2["Middle_Name"], row2["Last_Name"], end=' ')
            print()
            q3="SELECT * FROM official_location WHERE Official_ID = '%d'" % row["Official_ID"]
            cur.execute(q3)
            result2 = cur.fetchall()
            print("Official Location: ", end=' ')
            for row2 in result2:
                print(row2["Region"], row2["City"], end=' ')
            print()
    except Exception as e:
        print("Error:", e)

def select_event():
    try:
        sql = "SELECT * FROM event"
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            print(row, end=' ')
            is_encounrt=True
            # print the associated entry, which is present in either Encounter or Battle
            sql2 = "SELECT * FROM encounter WHERE Event_ID = %d" % row["Event_ID"]
            cur.execute(sql2)
            row2 = cur.fetchone()
            # check if NULL, if it is the this was a battle
            if row2 is None:
                is_encounrt=False
                sql2 = "SELECT * FROM battle WHERE Event_ID = %d" % row["Event_ID"]
                cur.execute(sql2)
                row2 = cur.fetchall()
            if(is_encounrt):
                print("Encounter\nPokemon Captured: ", end=' ')
                print(row2["Pokemon_Captured_Name"], end=' ')
                q2 = "SELECT * FROM encounter_pokemons WHERE Event_ID = %d" % row["Event_ID"]
                cur.execute(q2)
                result2 = cur.fetchall()
                print()
                print("Pokemon Used: ", end=' ')
                for row2 in result2:
                    print(row2["Pokemon"], end=' ')
                print()
                q2 = "SELECT * FROM encounter_items_used WHERE Event_ID = %d" % row["Event_ID"]
                cur.execute(q2)
                result2 = cur.fetchall()
                print("Items Used: ", end=' ')
                for row2 in result2:
                    print(row2["Items"], end=' ')
                print()
                
            else:
                print("Battle")
                # print(row2["Trainer1_ID"], row2["Trainer2_ID"], end=' ')
                q2 = "SELECT * FROM battle_trainer1_items WHERE Event_ID = %d" % row["Event_ID"]
                cur.execute(q2)
                result2 = cur.fetchall()
                print("Items Used by Trainer 1: ", end=' ')
                for row2 in result2:
                    print(row2["Items"], end=' ')
                print()
                q2 = "SELECT * FROM battle_trainer2_items WHERE Event_ID = %d" % row["Event_ID"]
                cur.execute(q2)
                result2 = cur.fetchall()
                print()
                print("Items Used by Trainer 2: ", end=' ')
                for row2 in result2:
                    print(row2["Items"], end=' ')
                print()
                q2 = "SELECT * FROM battle_trainer1_pokemon_used WHERE Event_ID = %d" % row["Event_ID"]
                cur.execute(q2)
                result2 = cur.fetchall()
                print("Pokemon Used by Trainer 1: ", end=' ')
                for row2 in result2:
                    print(row2["Pokemon_Used"], end=' ')
                print()
                q2 = "SELECT * FROM battle_trainer2_pokemon_used WHERE Event_ID = %d" % row["Event_ID"]
                cur.execute(q2)
                result2 = cur.fetchall()
                print("Pokemon Used by Trainer 2: ", end=' ')
                for row2 in result2:
                    print(row2["Pokemon_Used"], end=' ')   
                print()             
            print()
    except Exception as e:
        print("Error:", e)
def select_moves():
    try:
        sql = "SELECT * FROM moves"
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            print(row)
            sql2 = "SELECT * FROM types_of_move WHERE Move_Name = '%s'" % row["Move_Name"]
            cur.execute(sql2)
            result2 = cur.fetchall()
            print("Types: ", end=' ')
            for row2 in result2:
                print(row2["Move_Type"], end=' ')
            print()
    except Exception as e:
        print("Error:", e)

# INSERTION FUNCTIONS

def insert_pokemon():
    try:
        row = {}
        print("Enter new pokemon's details: ")
        row["name"] = input("Name: ")
        row["height"] = int(input("Height: "))
        row["weight"] = int(input("Weight: "))

        sql = "INSERT INTO pokemon(Name, Height, Weight) VALUES ('%s', '%d', '%d')" % (row["name"], row["height"], row["weight"])
        cur.execute(sql)
        
        print("Enter the types of this Pokemon, separated by commas: ")
        types = input()
        if len(types) == 0:
            # insert NULL type
            sql = "INSERT INTO pokemon_types(Pokemon_Name, Type) VALUES ('%s', NULL)" % row["name"]
            cur.execute(sql)
        else:
            types = types.split(',')
            for type in types:
                sql = "INSERT INTO pokemon_types(Pokemon_Name, Type) VALUES ('%s', '%s')" % (row["name"], type)
                cur.execute(sql)

        print("Enter Pokemon Weaknesses, separated by commas: ")
        weaknesses = input()
        if len(weaknesses) == 0:
            # insert NULL weakness
            sql = "INSERT INTO pokemon_weaknesses(Pokemon_Name, Weakness) VALUES ('%s', NULL)" % row["name"]
            cur.execute(sql)
        else:
            weaknesses = weaknesses.split(',')
            for weakness in weaknesses:
                sql = "INSERT INTO pokemon_weaknesses(Pokemon_Name, Weakness) VALUES ('%s', '%s')" % (row["name"], weakness)
                cur.execute(sql)
                
        print("Enter the names of the Pokemon this Pokemon can evolve into, separated by commas: ")
        evolutions = input()
        if len(evolutions) == 0:
            pass
        else:
            evolutions = evolutions.split(',')
            for evolution in evolutions:
                sql = "INSERT INTO pokemon_evolves_to(Pokemon_Name, Evolves_To) VALUES ('%s', '%s')" % (row["name"], evolution)
                cur.execute(sql)
        
        con.commit()        
        print("Inserted Into Database")        
        
    except Exception as e:
        # Rollback in case there is any error
        con.rollback()
        print("Error:", e)


def insertTrainer():
    try:
        # Takes emplyee details as input
        row = {}
        print("Enter new trainer's details: ")
        name = (input("Name (Fname Minit Lname): ")).split(' ')
        row["Fname"] = name[0]
        row["Mname"] = name[1]
        row["Lname"] = name[2]
        row["ID"] = input("ID: ")
        query = "INSERT INTO trainer_name(Trainer_ID,First_Name,Middle_Name,Last_Name) VALUES('%s', '%s', '%s', '%s')" % (row["Fname"], row["Mname"], row["Lname"], row["ID"])
        cur.execute(query)
        # con.commit() 
        row["Sex"] = input("Sex: ")
        row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")
        row["Jdate"] = input("Start of Journey Date (YYYY-MM-DD): ")
        query2= "INSERT INTO trainer(Trainer_ID,Gender,Date_of_Birth,Start_of_Journey) VALUES('%s', '%s', '%s', '%s')" % (row["ID"], row["Sex"], row["Bdate"], row["Jdate"])
        cur.execute(query2)
        # con.commit()
        row["Country Code"] = int((input("Country Code: ")))
        row["Phone Number"] = int(input("Phone Number: "))
        row["Start_of_Journey"] = input("Start of Journey Date (YYYY-MM-DD): ")      
        query3 = "INSERT INTO trainer_number(Trainer_ID,Country_Code,Phone_Number) VALUES('%s', '%d', '%d')" % (row["ID"], row["Country Code"], row["Phone Number"])
        cur.execute(query3)
        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def insert_tournament():
    try:
        row = {}
        print("Enter new tournament's details: ")
        row["name"] = input("Name: ")
        row["start_date"] = input("Date: ")
        row["end_date"] = input("End Date: ")
        row["No_of_participants"] = int(input("Number of Participants: "))
        row["badges"] = int(input("badges "))
        query= "INSERT INTO tournament(name, Start_Date, End_Date, No_of_participants, No_of_Badge_Required) VALUES('%s', '%s', '%s', '%d', '%d')" % (row["name"], row["start_date"], row["end_date"], row["No_of_participants"], row["badges"])
        cur.execute(query)
        row["Region"]= input("Region: ")
        row["City"]= input("City: ")
        row["Street"]= input("Street: ")
        query2= "INSERT INTO tournament_location(Name, Region, City, Street) VALUES('%s', '%s', '%s', '%s')" % (row["name"], row["Region"], row["City"], row["Street"])
        cur.execute(query2)
        con.commit()
    except Exception as e:
        # Rollback in case there is any error
        con.rollback()
        print("Error:", e)
        
def insertGym():
    try:
        row = {}
        print("Enter new Gym's details: ")
        row["name"] = input("Name : ")
        row["Type"] = input("Type: ")
        row["Gym_Leader_Id"]=int(input("Leader_ID: "))
        query = "INSERT INTO gym(Gym_Name,Type,Gym_Leader_ID) VALUES('%s', '%s', '%d')" % (row["name"], row["Type"], row["Gym_Leader_Id"])
        cur.execute(query) 
        row["Region"]= input("Region: ")
        row["City"]= input("City: ")
        row["Street"]= input("Street: ")
        query2= "INSERT INTO gym_location(Gym_Name, Region, City, Street) VALUES('%s', '%s', '%s', '%s')" % (row["name"], row["Region"], row["City"], row["Street"])
        cur.execute(query2)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Error:", e)

def insertItems():
    try:
        row = {}
        print("Enter new Item's details: ")
        row["name"] = input("Name : ")
        row["Effect"] = input("Effect: ")
        row["Target"]=input("Target: ")
        query = "INSERT INTO items(Item_Name,Effect,Target) VALUES('%s', '%s', '%s')" % (row["name"], row["Effect"], row["Target"])
        cur.execute(query) 
        con.commit()
    except Exception as e:
        con.rollback()
        print("Error:", e)
        
def insertEncounter(arg):
    try:
        # Takes emplyee details as input
        row = {}
        print("Enter new Encounter's details: ")
        row["Event_ID"] = arg
        row["Trainer_ID"] = int(input("Trainer_ID: "))
        row["Pokemon_Captured_Name"] = input("Pokemon_Captured_Name: ")
        query = "INSERT INTO encounter(Event_ID,Trainer_ID,Pokemon_Captured_Name) VALUES('%d', '%d', '%s')" % (row["Event_ID"], row["Trainer_ID"], row["Pokemon_Captured_Name"])
        cur.execute(query)
        row["Pokemon"] = input("Insert the names of Pokemon used, separated by commas: ")
        for pokemon in row["Pokemon"].split(','):
            query2= "INSERT INTO encounter_pokemons(Pokemon,Event_ID) VALUES('%s', '%d')" % (pokemon, row["Event_ID"])
            cur.execute(query2)
        row["Items"] = input("Enter the items used by the Trainer, separated by commas: ")
        if row["Items"] == "":
            query3= "INSERT INTO encounter_items_used(Items,Event_ID) VALUES(NULL, '%d')" % (row["Event_ID"])
            cur.execute(query3)
        else:
            for item in row["Items"].split(','):
                query3= "INSERT INTO encounter_items_used(Items,Event_ID) VALUES('%s', '%d')" % (item, row["Event_ID"])
                cur.execute(query3)
        # cur.execute(query3)
        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>pqr", e)

def insertBattle(arg):
    try:
        row = {}
        print("Enter new Battle's details: ")
        row["Event_ID"] = arg
        row["Trainer1_ID"] = int(input("Trainer 1 ID: "))
        row["Trainer2_ID"] = int(input("Trainer 2 ID: "))      
        query = "INSERT INTO battle(Event_ID, Trainer1_ID, Trainer2_ID) VALUES('%d', '%d', '%d')" % (row["Event_ID"], row["Trainer1_ID"], row["Trainer2_ID"])
        cur.execute(query)

        print("Enter the items used by Trainer 1, separated by commas: ")
        row["Items"] = input()
        if row["Items"] == "":
            query = "INSERT INTO battle_trainer1_items(Items, Event_ID) VALUES(NULL, '%d')" % (row["Event_ID"])
            cur.execute(query)
        else:
            data = row["Items"].split(',')
            for item in data:
                query = "INSERT INTO battle_trainer1_items(Items, Event_ID) VALUES('%s', '%d')" % (item, row["Event_ID"])
                cur.execute(query)
        
        print("Enter the items used by Trainer 2, separated by commas: ")  
        row["Items"] = input()
        if row["Items"] == "":
            query = "INSERT INTO battle_trainer2_items(Items, Event_ID) VALUES(NULL, '%d')" % (row["Event_ID"])
            cur.execute(query)
        else:
            data = row["Items"].split(',')
            for item in data:
                query = "INSERT INTO battle_trainer2_items(Items, Event_ID) VALUES('%s', '%d')" % (item, row["Event_ID"])
                cur.execute(query)
        
        print("Enter the Pokemon used by Trainer 1: ")
        data = input().split(',')
        for pokemon in data:
            query = "INSERT INTO battle_trainer1_pokemon_Used(Pokemon_Used, Event_ID) VALUES('%s', '%d')" % (pokemon, row["Event_ID"])
            cur.execute(query)

        print("Enter the Pokemon used by Trainer 2: ")
        data = input().split(',')
        for pokemon in data:
            query = "INSERT INTO battle_trainer2_pokemon_Used(Pokemon_Used, Event_ID) VALUES('%s', '%d')" % (pokemon, row["Event_ID"])
            cur.execute(query)

        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>xyz", e)


def updateTrainerBadge():
    try:
        row = {}
        print("Enter Trainer's ID and Gym name of the gym whose badge is earned: ")
        row["Trainer_ID"] = input("Trainer ID: ")
        row["Gym_Name"] = input("Gym Name: ")
        query = "INSERT INTO trainer_badges VALUES('%s', '%s')" % (row["Trainer_ID"], row["Gym_Name"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

def addMoves():
    try:
        row = {}
        print("Enter new move for the Pokemon: ")
        row["Move_Name"] = input("Move Name: ")
        row["Description"] = input("Description: ")
        row["Power"] = int(input("Power: "))
        row["Accuracy"] = int(input("Accuracy: "))
        row["PP"] = int(input("Power Points: "))
        row["Effect"] = input("Effect on opponent: ")

        query = "INSERT INTO moves(Move_Name, Description, Power, Accuracy, PP, Effect_on_Opponent)  VALUES('%s', '%s', '%d', '%d', '%d', '%s')" % (row["Move_Name"], row["Description"], row["Power"], row["Accuracy"], row["PP"], row["Effect"])
        cur.execute(query)

        print("Enter the types of this Move, separated by commas: ")
        row["Type"] = input()
        if row["Type"] == "":
            query = "INSERT INTO types_of_move(Move_Name, Move_Type) VALUES('%s', NULL)" % row["Move_Name"]
            cur.execute(query)
        else:
            types = row["Type"].split(',')
            for type in types:
                query = "INSERT INTO types_of_move(Move_Name, Move_Type) VALUES ('%s', '%s')" % (row["Move_Name"], type)
                cur.execute(query)

        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

def addPokemonToTrainer():
    try:
        row = {}
        print("Enter Trainer's ID")
        row["Trainer_ID"] = int(input("Trainer ID: "))
        print("Enter Pokemon's name: ")
        row["Pokemon_Name"] = input("Pokemon Name: ")
        print("Enter Pokemon's level: ")
        row["Level"] = int(input("Level: "))
        print("Enter Pokemon's Experience Points: ")
        row["Experience_Points"] = int(input("Experience Points: "))
        print("Enter Date of Capture: ")
        row["Date_of_Capture"] = input("Date of Capture (YYYY-MM-DD): ")
        
        query = "INSERT INTO pokemon_owned(Trainer_ID, Pokemon_Name, Level, Experience, Date_of_Capture) VALUES('%d', '%s', '%d', '%d', '%s')" % (row["Trainer_ID"], row["Pokemon_Name"], row["Level"], row["Experience_Points"], row["Date_of_Capture"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

def addMovesToPokemon():
    try:
        row = {}
        print("Enter Pokemon's name: ")
        row["Pokemon_Name"] = input("Pokemon Name: ")
        print("Enter new move for the Pokemon: ")
        row["Move_Name"] = input("Move Name: ")
        query = "INSERT INTO pokemons_with_this_move(Move_Name, Pokemon_Name) VALUES('%s', '%s')" % (row["Move_Name"], row["Pokemon_Name"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

def insert_officials():
    try:
        row = {}
        print("Enter new official's details: ")
        row["Official_ID"] = int(input("Official ID: "))
        row["First_Name"] = input("First Name: ")
        row["Middle_Name"] = input("Middle Name: ")
        row["Last_Name"] = input("Last Name: ")
       
        row["Role"]= input("Role: ")
        row["Start_of_Service"]= input("Start of Service Date (YYYY-MM-DD): ")
        query3= "INSERT INTO officials(Official_ID, Role, Start_of_Service) VALUES('%d', '%s', '%s')" % (row["Official_ID"], row["Role"], row["Start_of_Service"])
        cur.execute(query3)
        query= "INSERT INTO official_name(Official_ID, First_Name, Middle_Name, Last_Name) VALUES('%d', '%s', '%s', '%s')" % (row["Official_ID"], row["First_Name"], row["Middle_Name"], row["Last_Name"])
        row["Region"]= input("Region: ")
        row["City"]= input("City: ")
        query2= "INSERT INTO official_location(Official_ID, Region, City) VALUES('%d', '%s', '%s')" % (row["Official_ID"], row["Region"], row["City"])
        cur.execute(query2)
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
        
def insert_event():
    try:
        row = {}
        print("Enter new event's details: ")
        row["Event_ID"] = int(input("Event ID: "))
        row["Description"] = input("Description: ")
        row["Time_of_Occurrence"] = input("Time of Occurrence: ")
        row["Result"] = input("Result: ")
        if row["Result"] == "":
            row["Result"] = None
        query= "INSERT INTO event(Event_ID, Description, Time_of_Occurrence, Result) VALUES('%d', '%s', '%s', '%s')" % (row["Event_ID"], row["Description"], row["Time_of_Occurrence"], row["Result"])
        cur.execute(query)
        row["Region"]= input("Region: ")
        row["City"]= input("City: ")
        row["Street"]= input("Street: ")
        query2= "INSERT INTO event_location(Event_ID, Region, City, Street) VALUES('%d', '%s', '%s', '%s')" % (row["Event_ID"], row["Region"], row["City"], row["Street"])
        cur.execute(query2)
        con.commit()
        print("deone\n")
        a= int(input("Enter type of event: 1 for Battle  2 for Encounter"))
        if a==1:
            print("before insertBattle\n")
            insertBattle(row["Event_ID"])
            print("a== 1 done\n")
        elif a==2:
            print("before insertEncounter\n")
            insertEncounter(row["Event_ID"])
            print("a== 2 done\n")
        
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>abc", e)

# update functions

def update_pokemons_moves(arg1,arg2):
    try:
        q1 = "INSERT INTO pokemons_with_this_move(Move_Name, Pokemon_Name) VALUES('%s', '%s')" % (arg1, arg2)
        cur.execute(q1)
        con.commit()
        
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

def update_tournament_start_date(arg1,arg2):
    try:
        q1 = "UPDATE tournament SET Start_Date = '%s' WHERE Name = '%s'" % (arg1, arg2)
        cur.execute(q1)
        con.commit()
        
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
def update_tournament_end_date(arg1,arg2):
    try:
        q1 = "UPDATE tournament SET End_Date = '%s' WHERE Name = '%s'" % (arg1, arg2)
        cur.execute(q1)
        con.commit()
        
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
def update_gym_leader(arg1,arg2):
    try:
        q1 = "UPDATE gym SET Gym_Leader_ID = '%d' WHERE Gym_Name = '%s'" % (arg1, arg2)
        cur.execute(q1)
        con.commit()
        
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
def update_tournament_location(arg1,arg2,arg3,arg4):
    try:
        q1 = "UPDATE tournament_location SET Region = '%s', City = '%s', Street = '%s' WHERE Name = '%s'" % (arg2, arg3, arg4, arg1)
        cur.execute(q1)
        con.commit()
        
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
        
def update_trainer_phone(arg1,arg2,arg3):
    try:
        q1 = "UPDATE trainer_number SET Country_Code = '%d', Phone_Number = '%d' WHERE Trainer_ID = '%d'" % (arg2, arg3, arg1)
        cur.execute(q1)
        con.commit()
        
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

# analysis functions

def get_top_5_used_moves(arg1,arg2):
   # get the top arg2 moves of type arg1 used by pokemions

    try:
        sql="SELECT Move_Name, COUNT(*) as count FROM pokemons_with_this_move WHERE Move_Name IN (SELECT Move_Name FROM types_of_move WHERE Move_Type = '%s') GROUP BY Move_Name ORDER BY count DESC LIMIT %d" % (arg1,arg2)
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print("Error:", e)
def get_top_5_most_used_itemsused_in_any_event():
    try:
        # write an sql query to get the top 5 most used items in any event which is a battle or encounter 

        sql = "SELECT ItemName as ItemName, COUNT(ItemName) AS TotalUsage FROM (SELECT Items as ItemName, COUNT(*) AS ItemCount FROM encounter_items_used GROUP BY ItemName UNION ALL SELECT Items as ItemName, COUNT(*) AS ItemCount FROM battle_trainer1_items GROUP BY ItemName UNION ALL SELECT Items as ItemName, COUNT(*) AS ItemCount FROM battle_trainer2_items GROUP BY ItemName) AS CombinedItems GROUP BY ItemName ORDER BY TotalUsage DESC LIMIT 5"

        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print("Error:", e)

def get_most_used_pokemon():
    try:
        # write the query to get the most used pokemon across all events like battles and encounters, there is a master event table which refers to two tables for battle and encounter. If it is a battle, there are two pokemon used table in total, else if it is an encounter, there is a single pokemon used table for the trainer who captured the pokemon, so count across all these pokemon used tables and get the most used pokemon

        sql = "SELECT Pokemon_Name, COUNT(*) as count FROM (SELECT Pokemon as Pokemon_Name FROM encounter_pokemons UNION ALL SELECT Pokemon_Used as Pokemon_Name FROM battle_trainer1_pokemon_used UNION ALL SELECT Pokemon_Used as Pokemon_Name FROM battle_trainer2_pokemon_used) AS CombinedPokemon GROUP BY Pokemon_Name ORDER BY count DESC LIMIT 1"

        cur.execute(sql)
        result = cur.fetchall()
        for row in result:  
            print(row)
    except Exception as e:
        print("Error:", e)

# deletion functions

def delete_pokemon():
    try:
        row = {}
        print("Enter name of the pokemon to be deleted: ")
        row["name"] = input("Pokemon Name: ")
        query = "DELETE FROM pokemon WHERE name = '%s'" % row["name"]
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

def delete_trainer():
    try:
        row = {}
        print("Enter ID of the trainer to be deleted: ")
        row["ID"] = int(input("Trainer ID: "))
        query = "DELETE FROM trainer WHERE ID = '%d'" % row["ID"]
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

def delete_officials():
    try:
        row = {}
        print("Enter ID of the official to be deleted: ")
        row["ID"] = int(input("Official ID: "))
        query = "DELETE FROM officials WHERE Official_ID = '%d'" % row["ID"]
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

def delete_pokemon_owned():
    try:
        row = {}
        print("Enter Trainer's ID and Pokemon's name to be deleted: ")
        row["Trainer_ID"] = int(input("Trainer ID: "))
        row["Pokemon_Name"] = input("Pokemon Name: ")
        query = "DELETE FROM pokemon_owned WHERE Trainer_ID = '%d' AND Pokemon_Name = '%s'" % (row["Trainer_ID"], row["Pokemon_Name"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

def delete_event():
    try:
        row = {}
        print("Enter Event ID to be deleted: ")
        row["Event_ID"] = int(input("Event ID: "))

        # first delete from correspoding batlle or encounter table
        query = "DELETE FROM encounter WHERE Event_ID = '%d'" % row["Event_ID"]
        cur.execute(query)
        query = "DELETE FROM battle WHERE Event_ID = '%d'" % row["Event_ID"]
        cur.execute(query)
        
        query = "DELETE FROM event WHERE Event_ID = '%d'" % row["Event_ID"]
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    

# functions for calling other functions

def dispatch1(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        insert_pokemon()
    elif(ch == 2):
        insert_officials()
    elif(ch == 3):
        insertGym()
    elif(ch == 4):
        insertTrainer()
    elif(ch == 5):
        insert_tournament()
    elif(ch == 6):
        insert_event()
    elif(ch == 7):
        insertItems()
    elif (ch == 8):
        addMoves()
    elif (ch == 9):
        addMovesToPokemon()
    elif (ch == 10):
        addPokemonToTrainer()
    elif (ch == 11):
        updateTrainerBadge()
    else:
        print("Error: Invalid Option")

def dispatch2(ch):
    """
    Function that maps helper functions to option entered
    """
    if(ch == 1):
        select_pokemon()
    elif(ch == 2):
        select_trainer()
    elif(ch == 3):
        select_tournament()
    elif(ch == 4):
        select_gym()
    elif(ch == 5):
        select_items()
    elif(ch == 6):
        select_officials()
    elif(ch == 7):
        select_event()
    elif(ch == 8):
        select_moves()
    else:
        print("Error: Invalid Option")
def dispatch3(ch):
    if(ch == 1):
        updateTrainerBadge()
    elif(ch == 2):
        print("Enter the move and the pokemon")
        arg1 = input("Move Name: ")
        arg2 = input("Pokemon Name: ")
        update_pokemons_moves(arg1,arg2)
    elif(ch == 3):
        print("Enter the new date and the tournament name")
        arg1 = input("New Start Date: ")
        arg2 = input("Tournament Name: ")
        update_tournament_start_date(arg1,arg2)
    elif(ch == 4):
        print("Enter the new date and the tournament name")
        arg1 = input("New End Date: ")
        arg2 = input("Tournament Name: ")
        update_tournament_end_date(arg1,arg2)
    elif(ch == 5):
        print("Enter the new leader's ID and the gym name")
        arg1 = int(input("Leader ID: "))
        arg2 = input("Gym Name: ")
        update_gym_leader(arg1,arg2)
    elif(ch == 6):
        print("Enter the new location details and the tournament name")
        arg1 = input("Tournament Name: ")
        arg2 = input("Region: ")
        arg3 = input("City: ")
        arg4 = input("Street: ")
        update_tournament_location(arg1,arg2,arg3,arg4)
    elif(ch == 7):
        print("Enter the new phone number details and the trainer's ID")
        arg1 = int(input("Trainer ID: "))
        arg2 = int(input("Country Code: "))
        arg3 = int(input("Phone Number: "))
        update_trainer_phone(arg1,arg2,arg3)
    else:
        print("Error: Invalid Option")
    
def dispatch4(ch):
    if(ch == 1):
        delete_pokemon()
    elif(ch == 2):
        delete_trainer()
    elif(ch == 3):
        delete_officials()
    elif(ch == 4):
        delete_pokemon_owned()
    elif(ch == 5):
        delete_event()
    else:
        print("Error: Invalid Option")

def dispatch5(ch):
    if(ch == 1):
        print("Enter Event ID")
        arg = int(input("Event ID: "))
        get_event(arg)
    elif(ch == 2):
        print("Enter Pokemon Name")
        arg = input("Pokemon Name: ")
        get_pokemon(arg)
    elif(ch == 3):
        print("Enter Trainer ID")
        arg = int(input("Trainer ID: "))
        get_trainer(arg)
    elif(ch == 4):
        print("Enter Gym Name")
        arg = input("Gym Name: ")
        get_gym(arg)
    elif(ch == 5):
        print("Enter Item Name")
        arg = input("Item Name: ")
        get_items(arg)
    elif(ch == 6):
        print("Enter Official ID")
        arg = int(input("Official ID: "))
        get_officials(arg)
    elif(ch == 7):
        print("Enter Tournament Name")
        arg = input("Tournament Name: ")
        get_tournament(arg)
    elif(ch == 8):
        print("Enter Move Name")
        arg = input("Move Name: ")
        get_moves(arg)
    else:
        print("Error: Invalid Option")
def dispatch6(ch):
    if(ch == 1):
        print("Enter type of move and number of moves")
        arg1 = input("Move Type: ")
        arg2 = int(input("Number of Moves: "))
        get_top_5_used_moves(arg1,arg2)
    elif(ch == 2):
        get_top_5_most_used_itemsused_in_any_event()
    # else:
    #     print("Error: Invalid Option")
    elif(ch == 3):
        get_most_used_pokemon()
    
# Global
while(1):
    tmp = sp.call('clear', shell=True)

    try:
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              user="root",
                              password="",
                              db='dna',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                print("Select functionlity: ")
                print(""" \t1. Insertion Fnctions\n\t2. Select Functions\n\t3. Update Functions\n\t4. Delete Functions\n\t5. Minimal Select\n\t6. Functional Requirements\n\t7. Exit""")
                type = int(input("Enter choice> "))
                if(type==1):
                # Here taking example of Employee Mini-world
                    print("1. Insert a New Pokemon ")  
                    print("2. Insert a New Official ")  
                    print("3. Insert a New Gym")  
                    print("4. Insert a New Trainer")  
                    print("5. Insert a New Tournament")
                    print("6. Insert a New Event")
                    print("7. Insert a New Item")
                    print("8 Insert a New Move")
                    print("9. Add a new move to a pokemon")
                    print("10. Add a new pokemon to a trainer")
                    print("11. Update the badges of a trainer")
                    print("12. Logout")
                    ch = int(input("Enter choice> "))
                    tmp = sp.call('clear', shell=True)
                    if ch == 12:
                        exit()
                    else:
                        dispatch1(ch)
                        tmp = input("Enter any key to CONTINUE>")
                elif(type==2):
                    print("1. Select Pokemon")
                    print("2. Select Trainer")
                    print("3. Select Tournament")
                    print("4. Select Gym")
                    print("5. Select Items")
                    print("6. Select Officials")
                    print("7. Select Event")
                    print("8. Select Moves")
                    print("9. Exit")
                    ch = int(input("Enter choice> "))
                    tmp = sp.call('clear', shell=True)
                    if ch == 9:
                        exit()
                    else:
                        dispatch2(ch)
                        tmp = input("Enter any key to CONTINUE>")
                elif(type==3):
                    print("1. Update Trainer's Badges")
                    print("2. Update Pokemon's Moves")
                    print("3. Update Tournament's start date ")
                    print("4. Update Tournament's end date")
                    print("5. Update Gym's Leader")
                    print("6. Update Tournament's location")
                    print("7. Update Trainers Phone Number")
                    print("8. Exit")

                    ch = int(input("Enter choice> "))
                    tmp = sp.call('clear', shell=True)
                    if(ch==8):
                        exit()
                    else:
                        dispatch3(ch)
                        tmp = input("Enter any key to CONTINUE>")
                elif(type==4):
                    print("1. Delete a Pokemon")
                    print("2. Delete a Trainer")
                    print("3. Delete an Official")
                    print("4. Delete a Pokemon Owned")
                    print("5. Delete an Event") 
                    print("6. Exit")
                    ch = int(input("Enter choice> "))
                    tmp = sp.call('clear', shell=True)
                    if(ch==6):
                        exit()
                    else:
                        dispatch4(ch)
                        tmp = input("Enter any key to CONTINUE>")
                
                elif(type==5):
                    print("1. View an Event")
                    print("2. Get pokemon details")
                    print("3. Get Trainer details")
                    print("4. Get Gym details")
                    print("5. Get Items details")
                    print("6. Get Official details")
                    print("7. Get Tournament details")
                    print("8. Get Moves details")
                    print("9. Exit")
                    ch = int(input("Enter choice> "))
                    tmp = sp.call('clear', shell=True)
                    if(ch==9):
                        exit()
                    else:
                        dispatch5(ch)
                        tmp = input("Enter any key to CONTINUE>")
                    
                elif(type==6):
                    print("1. Get top  most used moves by pokemons of a particular type")
                    print("2 Get top most used item in all events")
                    print("3. Get the name of the most used pokemons in events")
                    print("4. Exit")
                    ch = int(input("Enter choice> "))
                    tmp = sp.call('clear', shell=True)
                    if(ch==4):
                        exit()
                    else:
                        dispatch6(ch)
                        tmp = input("Enter any key to CONTINUE>")


    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")

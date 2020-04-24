import logging
import sqlite3
from os import path

def GenerateDB():
    if not path.exists("discordBotDB.db"):
        print("DB not found. Generating new DB")
        conn = sqlite3.connect('discordBotDB.db') # generate the db.
        cursor = conn.cursor()
        # Create table - USERS
        cursor.execute('''CREATE TABLE USERS
                     ([ID] INTEGER PRIMARY KEY AUTOINCREMENT,[USERNAME] text, [DISCORD_ID] integer, [COMMON_NAME] text unique)''')


        examples = [('Prophecies', 9660, 'CJ'),
                    ('JamesDebt', 4815, 'James'),
                    ('TheKarmoable', 1732, 'Mason'),
                    ('seamonsterpasta', 5554, 'Maisano'),
                    ('Noobmeister', 9588, 'Mericle')]
        cursor.executemany("""INSERT INTO USERS
                                 ( USERNAME, DISCORD_ID, COMMON_NAME) 
                                  VALUES 
                                 (?, ?, ?)
                                 """, examples)


        conn.commit()

        ### Generate DND Character Table ###

        cursor = conn.cursor()
        # Create table - USERS
        cursor.execute('''CREATE TABLE DND_CHARACTERS
                             ([CHARACTER_ID] INTEGER PRIMARY KEY AUTOINCREMENT, 
                             [CHARACTER_NAME] TEXT UNIQUE NOT NULL, 
                             [CREATOR_USER_ID] INTEGER, 
                             [CAMPAIGN] TEXT,
                             [STRENGTH] INTEGER,
                             [DEXTERITY] INTEGER,
                             [CONSTITUTION] INTEGER,
                             [INTELLIGENCE] INTEGER,
                             [WISDOM] INTEGER,
                             [CHARISMA] INTEGER,
                             [PROFICIENCY] INTEGER,
                             [WALKING_SPEED] INTEGER, 
                             [AC] INTEGER, 
                             [INITIATIVE] INTEGER, 
                             [ACROBATICS] INTEGER, 
                             [ANIMAL_HANDLING] INTEGER, 
                             [ARCANA] INTEGER, 
                             [ATHLETICS] INTEGER, 
                             [DECEPTION] INTEGER,
                             [HISTORY] INTEGER,
                             [INSIGHT] INTEGER, 
                             [INTIMIDATION] INTEGER, 
                             [INVESTIGATION] INTEGER, 
                             [MEDICINE] INTEGER, 
                             [NATURE] INTEGER, 
                             [PERCEPTION] INTEGER, 
                             [PERFORMANCE] INTEGER, 
                             [PERSUASION] INTEGER, 
                             [RELIGION] INTEGER, 
                             [SLEIGHT_OF_HAND] INTEGER, 
                             [STEALTH] INTEGER, 
                             [SURVIVAL] INTEGER, 
                             [ACTIVE] INTEGER 
                             )''')

        # set up a foreign key here eventually

        dndCharacters = [(1, 'Kerrigan', 1, 'Torn Asunder', 1, 2, 1, 1, 3, 1, 3, 55, 15, 2, 2, 3, 1, 4, 1, 4, 3, 4, 1, 3, 1, 3, 1, 1, 4, 2, 2, 3, 1),
                         (2, 'Valamour', 1, 'Being Nice to Goblins', 1, 3, 1, 0, 2, 4, 3, 30, 14, 7, 6, 2, 0, 1, 19, 0, 2, 7, 3, 2, 0, 8, 7, 7, 0, 6, 3, 2, 0)]




        cursor.executemany("""INSERT INTO DND_CHARACTERS
                                          VALUES 
                                         (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                                          , ?, ?, ?, ?, ?, ?)
                                         """, dndCharacters)

        conn.commit()




        return conn
    return sqlite3.connect('discordBotDB.db')
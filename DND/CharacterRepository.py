import sqlite3


class CharacterRepository:
    def __init__(self, characterDB, connection):
        self.datasource = characterDB
        self.conn = connection

    def refresh(self):
        dict = {}
        cur = self.conn.cursor()

        try:
            cur.execute("SELECT * FROM DND_CHARACTERS")
        except sqlite3.OperationalError as e:
            return e

        rows = cur.fetchall()

        for row in rows:
            dict[str(row[1]).lower()] = {'characterid': row[0],
                                 'charactername': row[1],
                                 'creatoruserid': row[2],
                                 'campaign': row[3],
                                 'strength': row[4],
                                 'dexterity': row[5],
                                 'constitution': row[6],
                                 'intelligence': row[7],
                                 'wisdom': row[8],
                                 'charisma': row[9],
                                 'proficiency': row[10],
                                 'walkingspeed': row[11],
                                 'ac': row[12],
                                 'initiative': row[13],
                                 'acrobatics': row[14],
                                 'animalhandling': row[15],
                                 'arcana': row[16],
                                 'athletics': row[17],
                                 'deception': row[18],
                                 'history': row[19],
                                 'insight': row[20],
                                 'intimidation': row[21],
                                 'investigation': row[22],
                                 'medicine': row[23],
                                 'nature': row[24],
                                 'perception': row[25],
                                 'performance': row[26],
                                 'persuasion': row[27],
                                 'religion': row[28],
                                 'sleightofhand': row[29],
                                 'stealth': row[30],
                                 'survival': row[31],
                                 'active': row[32]
                                 }

        self.datasource = dict

        return dict

    def getModifierByAttributeAndCharacterName(self, attributeName, characterName):
        tmp = self.datasource[characterName][attributeName]
        return tmp

    def loadCharacter(self, characterName, userId):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT * FROM DND_CHARACTERS WHERE lower(CHARACTER_NAME) = \"{0}\" AND CREATOR_USER_ID  = {1}".format(characterName.lower(), userId))
            rows = cur.fetchall()
            self.conn.commit()
            if not rows:
                return ('No Records Found with name {0} belonging to user_ID: {1}'.format(characterName, userId))
        except sqlite3.OperationalError as e:
            return e




        cur = self.conn.cursor()
        try:
            cur.execute("UPDATE DND_CHARACTERS SET ACTIVE = 0 WHERE CREATOR_USER_ID  = {0}".format(userId)) #deactivate all characters from the person
            print(str(len(cur.fetchall())) + ' deactivated')
            self.conn.commit()
            cur.execute("UPDATE DND_CHARACTERS SET ACTIVE = 1 WHERE CREATOR_USER_ID  = {0} AND lower(CHARACTER_NAME) = '{1}'".format(userId,characterName.lower()))
            print(str(len(cur.fetchall())) + ' activated')
            self.conn.commit()
        except sqlite3.OperationalError as e:
            return e

        for record in self.datasource.values(): #deactivate all records
            if record['creatoruserid'] == userId:
                record['active'] = 0

        self.datasource[characterName]['active'] = 1 #activate the one with the correct name


        return characterName + ' loaded.'

    def uploadCharacter(self, character):
        cursor = self.conn.cursor()

        tupilized = character.toTuple()
        cursor.execute("""INSERT INTO DND_CHARACTERS
                                        (CHARACTER_NAME, CREATOR_USER_ID, CAMPAIGN, STRENGTH, DEXTERITY, CONSTITUTION, INTELLIGENCE,
                                        WISDOM, CHARISMA, PROFICIENCY, WALKING_SPEED, AC, INITIATIVE, ACROBATICS, ANIMAL_HANDLING, 
                                        ARCANA, ATHLETICS, DECEPTION, HISTORY, INSIGHT, INTIMIDATION, INVESTIGATION, MEDICINE,
                                        NATURE, PERCEPTION, PERFORMANCE, PERSUASION, RELIGION, SLEIGHT_OF_HAND, STEALTH, SURVIVAL, ACTIVE)
                                           VALUES 
                                          (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                                           , ?, ?, ?, ?, ?)
                                          """, tupilized)

        self.refresh()



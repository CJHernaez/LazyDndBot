import sqlite3

class DBHelper:
        def __init__(self, conn):
            self.conn = conn

        basepadding = 1

        def setBasePadding(self, basepadding):
            self.basepadding = basepadding
        def setUserHelper(self, userHelper):
            self.userHelper = userHelper

        def setValarantHelper(self, valarantHelper):
            self.valarantHelper = valarantHelper

        def getUserIdByDiscordTag(self, discordTag):
            self.userHelper.getUserIdByDiscordTag(discordTag)

        def getAllFromTable(self, message):
            tokenizedMessage = message.content.split(' ')
            if (len(tokenizedMessage) < self.basepadding+1):
                return message.channel.send('Must include Table name')
            cur = self.conn.cursor()

            try:
                cur.execute("SELECT * FROM " + tokenizedMessage[self.basepadding+1].upper())
            except sqlite3.OperationalError as e:
                return e

            rows = cur.fetchall()

            for row in rows:
                print(row)

            messageBuilder = ''
            for row in rows:
                messageBuilder = messageBuilder + str(row) + '\n'


            return message.channel.send(messageBuilder)



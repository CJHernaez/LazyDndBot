from DND.CharacterRepository import CharacterRepository
import random

class CharacterHelper:
    def __init__(self, characterDB, connection):
        self.characterRepository = CharacterRepository(characterDB, connection)

    userHelper = ''

    def setUserHelper(self, userHelper):
        self.userHelper = userHelper

    basepadding = 1


    def setBasePadding(self, basepadding):
        self.basepadding = basepadding

    def refresh(self):
        return self.characterRepository.refresh()

    def getCharacterStatsByName(self, characterName):
        return self.characterRepository.datasource[characterName]

    def getModifierByAttributeAndCharacterName(self, attributeName, characterName):
        self.characterRepository.getModifierByAttributeAndCharacterName(attributeName, characterName)

        return
    def Handle(self, message):
        tokenizedMessage = message.content.split(' ')
        optionCommand = self.basepadding
        if len(tokenizedMessage) > optionCommand:
            if (tokenizedMessage[optionCommand].lower() == 'view' or tokenizedMessage[optionCommand].lower() == 'show') and len(tokenizedMessage) >= optionCommand + 1: # view {name}
                return message.channel.send(str(self.getCharacterStatsByName(tokenizedMessage[optionCommand + 1].lower())).replace(', ', '\n').replace('\'','').replace('{', '').replace('}', '')) #3rd element is characterName

            if tokenizedMessage[optionCommand].lower() == 'refresh' and tokenizedMessage[optionCommand+1].lower() == 'characters':
                try:
                    self.characterRepository.refresh()
                    return message.channel.send('Character Refresh Successful')
                except:
                    return message.channel.send('Character Refresh Failed')

            if tokenizedMessage[optionCommand].lower() == 'stat' and len(tokenizedMessage) >= optionCommand + 1:
                return message.channel.send(str(self.characterRepository.getModifierByAttributeAndCharacterName(tokenizedMessage[optionCommand+2].lower(), tokenizedMessage[optionCommand+1].lower()))) #3rd element is characterName

            if tokenizedMessage[optionCommand].lower() == 'load' and len(tokenizedMessage) >= optionCommand + 1: # view {name}
                return message.channel.send(str(self.loadCharacter(tokenizedMessage[optionCommand + 1], self.userHelper.getUserIdByMessage(message))))

            if tokenizedMessage[optionCommand].lower() == 'roll':  # if the second word is view
                return message.channel.send(self.roll(tokenizedMessage[optionCommand + 1], self.userHelper.getUserIdByMessage(message)))

            if tokenizedMessage[optionCommand].lower() == 'check':  # if the second word is view
                return message.channel.send(
                    self.check(tokenizedMessage[optionCommand + 1], self.userHelper.getUserIdByMessage(message)))

            if tokenizedMessage[optionCommand].lower() == 'getid':  # if the second word is view
                if '#' in tokenizedMessage[optionCommand+1]:
                    return message.channel.send(self.getUserIdByDiscordTag(tokenizedMessage[optionCommand + 1]))
                else:
                    return message.channel.send(self.getUserIdByNickname(tokenizedMessage[optionCommand + 1]))

        return message.channel.send('Options: Add, View, Delete, Update, Refresh, Help')

    def loadCharacter(self, characterName, userId):
        return self.characterRepository.loadCharacter(characterName, userId)



    def getActiveCharacterByUserId(self, userId):
        for record in self.characterRepository.datasource.values():
            if record['creatoruserid'] == userId and record['active'] == 1:
                return record
        return

    def roll(self, attribute, userID):
        activeChar = self.getActiveCharacterByUserId(userID)
        if activeChar == '':
            return 'No Active Character Found for userID: ' + userID

        modifier = activeChar[str(attribute)]
        roll = random.randrange(1, 20)
        return 'Rolling {0} for {1}. Modifier = {2}\nRoll: {3}\nTotal: {4}'.format(attribute, activeChar['charactername'], modifier, roll, modifier+roll)

    def check(self, attribute, userID):
        activeChar = self.getActiveCharacterByUserId(userID)
        if activeChar == '':
            return 'No Active Character Found for userID: ' + userID

        modifier = activeChar[str(attribute)]
        roll = random.randrange(1, 20)
        return '{0} check for {1}: {2}'.format(attribute,activeChar['charactername'],modifier)


    def uploadCharacter(self, character):
        return self.characterRepository.uploadCharacter(character)
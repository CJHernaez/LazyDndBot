
class MessageHelper:
        def __init__(self, userHelper):
            self.userHelper = userHelper


        def getDiscordTagByMessage(self, message):
            #generate the full discord name
            return message.author.name + '#' + message.author.discriminator

        def checkUserTriggerValues(self, message):
             #first check to see if that user is in the DB
            if self.userHelper.getUserIdByMessage(message) == 'User Id Not Found':
                return False

            potentialTriggerWords = self.getTriggerWordsByMessage(message)
            tokenizedMessage = message.content.replace(',','').split(' ')
            if [x for x in potentialTriggerWords if x.lower() == tokenizedMessage[0].lower()]:
                return True

            return False

        def getTriggerWordsByMessage(self, message):
            return self.userHelper.getTriggerWordsByDiscordTag(self.getDiscordTagByMessage(message))


        def getNicknameByMessage(self, message):
            return self.userHelper.getNicknameByDiscordTag(self.getDiscordTagByMessage(message))
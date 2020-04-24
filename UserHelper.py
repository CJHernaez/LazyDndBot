import sqlite3

from Repositories.UserRepository import UserRepository


class UserHelper:
    def __init__(self, userDB, connection):
        self.userRepository = UserRepository(userDB, connection)

    basepadding = 1

    def setBasePadding(self, basepadding):
        self.basepadding = basepadding

    def Handle(self, message):
        tokenizedMessage = message.content.split(' ')
        optionCommand = self.basepadding + 1
        if len(tokenizedMessage) > self.basepadding:
            if tokenizedMessage[optionCommand].lower() == 'add':  # if the second word is view
                return message.channel.send(self.addUser(tokenizedMessage[optionCommand + 1], tokenizedMessage[optionCommand + 2]))

            if tokenizedMessage[optionCommand].lower() == 'refresh':  # if the second word is view
                try:
                    self.userRepository.refresh()
                    return message.channel.send('Refresh Successful')
                except :
                    return message.channel.send('Refresh Failed')

            if tokenizedMessage[optionCommand].lower() == 'view':  # if the second word is view
                print (len(tokenizedMessage))
                if len(tokenizedMessage) == optionCommand + 1: #view all
                    return message.channel.send(self.viewAll(self.userRepository.datasource))
                else:
                    return message.channel.send(self.view(tokenizedMessage[optionCommand + 1]))

            if tokenizedMessage[optionCommand].lower() == 'delete':  # if the second word is view
                return message.channel.send(self.deleteUserbyDiscordTag(tokenizedMessage[optionCommand + 1]))

            if tokenizedMessage[optionCommand].lower() == 'getid':  # if the second word is view
                if '#' in tokenizedMessage[optionCommand + 1]:
                    return message.channel.send(self.getUserIdByDiscordTag(tokenizedMessage[optionCommand + 1]))
                else:
                    return message.channel.send(self.getUserIdByNickname(tokenizedMessage[optionCommand + 1]))

        return message.channel.send('Options: Add, View, Delete, Update, Refresh, Help')



    def getUserIdByDiscordTag(self, discordTag):
            return self.userRepository.getUserIdByDiscordTag(discordTag)

    def getNicknameByDiscordTag(self, discordTag):
        return self.userRepository.datasource[discordTag][3]

    def getUserIdByNickname(self, nickname):
        return self.userRepository.getUserIdByNickname(nickname)

    def addUser(self, discordTag, nickname):
            discordTagTokens = discordTag.split('#')
            return self.userRepository.add(discordTagTokens[0], discordTagTokens[1], nickname)

    def getUserIdByMessage(self, message):
        return self.getUserIdByDiscordTag(message.author.name + '#' + message.author.discriminator)

    def getTriggerWordsByDiscordTag(self, discordTag):
        return self.userRepository.getTriggerWordsByDiscordTag(discordTag)
    def deleteUserbyDiscordTag(self, discordTag):
            return self.userRepository.deleteUserByDiscordTag(discordTag)

    def refresh(self):
        return self.userRepository.refresh()

    def view(self, nickname):
        return self.userRepository.getDiscordTagByNickname(nickname)

    def viewAll(self, users):
        stringbuilder = ''
        for discordTag, (userID, name, discordId, nickname) in users.items():
            stringbuilder = stringbuilder + str(userID) + ' : ' + name + ' : ' + str(
                discordId) + ' : ' + discordTag + '\n'

        return stringbuilder

import random
class Roller:
        def __init__(self):
            pass


        def setMessageHelper(self, messageHelper):
            self.messageHelper = messageHelper

        def roll (self, message):
            # message will look something like this .. roll 3d8 + 7
            #managle the .roll to push the roll to its own word.
            message.content = message.content.replace('.', 'spacer ')
            message.content = message.content.replace('roll d', 'roll 1d')

            tokenized = message.content.split(' ')
            if 'd' not in message.content.lower():
                diceSize = int(tokenized[2])
                return 'Rolling a d{0} for {1}:\nResult: {2}'.format(diceSize,
                                                                    self.messageHelper.getNicknameByMessage(message),
                                                                     random.randint(1, int(tokenized[2])))

            valueModifier = 0
            if '-' in message.content:
                #reparse to remove -
                tokenized = message.content.replace('-',' ').split()
                valueModifier = -tokenized[3]


            elif '+' in message.content:
                # reparse to remove +
                tokenized = message.content.replace('+', ' ').split()
                valueModifier = int(tokenized[3])


            #take the 5d4 portion

            section1tokenized = tokenized[2].split('d')

            numRolls = int(section1tokenized[0])
            dieSize = int(section1tokenized[1])
            rolls = []
            for roll in range(numRolls):
                rolls.append(random.randint(1, dieSize))

            messageBuilder = 'Rolling {0}d{1}'.format(numRolls, dieSize)
            if valueModifier != 0:
                if valueModifier > 0:
                    messageBuilder = messageBuilder + ' + {0}'.format(str(valueModifier))
                else:
                    messageBuilder = messageBuilder + ' - {0}'.format(str(abs(valueModifier)))

            messageBuilder = messageBuilder + ' for {0}.\n\n'.format(self.messageHelper.getNicknameByMessage(message))

            messageBuilder = messageBuilder + 'Rolls:\n\n'

            sum = 0
            rollcount = 1
            for roll in rolls:
                messageBuilder = messageBuilder + 'Roll {0}: {1}\n'.format(rollcount, str(roll))
                rollcount = rollcount + 1
                sum = sum + roll

            if (valueModifier != 0):
                messageBuilder = messageBuilder + '\nModifier: {0}\n'.format(str(valueModifier))

            messageBuilder = messageBuilder + '\nTotal: {0}'.format(sum + valueModifier)

            return messageBuilder

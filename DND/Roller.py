
import random
class Roller:
        def __init__(self):
            pass


        def setMessageHelper(self, messageHelper):
            self.messageHelper = messageHelper

        def roll (self, message):
            # message will look something like this .. roll 3d8 + 7

            tokenized = message.content.split(' ')
            if 'd' not in message.content.lower():
                diceSize = int(tokenized[2])
                return 'Rolling a d{0} for {1}:\nResult: {2}'.format(diceSize,
                                                                    self.messageHelper.getNicknameByMessage(message),
                                                                     random.randint(1, int(tokenized[2])))

            elif True:
                pass
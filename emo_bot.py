#!/usr/bin/env python

class EmoBot:
    def __init__(self, message = '', moodboard = ''):
        self.message = message
        if moodboard == '':
            self.moodboard = [
            'sad', 'crying', 'lonely',
            'bored', 'tired', 'ok',
            'good', 'happy', 'excited',
            'anxious', 'frustrated', 'angry'];
        else:
            self.moodboard = moodboard

    def get_reply(self):
        score = 0
        count = 0
        for i in self.moodboard:
            if i in self.message:
                score = score + self.moodboard.index(i) + 1
                count = count + 1
        if count > 0:
            return round(score/count)
        else:
            return 99



if __name__ == '__main__':
    #tests
    hi = MessageBot('I\'m feeling bored today...')
    reply = hi.get_reply()
    print(reply)

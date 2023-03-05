#!/usr/bin/env python

class EmoBot:
    def __init__(self, message = ''):
        self.message = message
        moodboard1 = [
        'sad', 'cry', 'lonely',
        'bored', 'tired', 'ok',
        'good', 'happy', 'excite',
        'anxious', 'frustrate', 'angry']
        moodboard2 = [
        'depressed', 'upset', 'alone',
        'dull', 'fatigue', 'average',
        'great', 'joy', 'inspire',
        'agitate', 'annoy', 'mad']
        moodboard3 = [
        'bad', 'distress', 'isolate',
        'not much', 'sleep', 'normal',
        'well', 'cheer', 'can\'t wait',
        'nervous', 'irritate', 'rage']
        self.moodboards = [moodboard1, moodboard2, moodboard3]


    def get_reply(self):
        score = 0
        count = 0
        for i in self.moodboards:
            for j in range(12):
                if i[j] in self.message:
                    score = score + j + 1
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

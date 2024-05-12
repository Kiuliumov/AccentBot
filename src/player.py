from __init__ import *


class Player:
    ID = 1

    def __init__(self):
        print('New player ID {}'.format(str(self.ID)))
        self.ID += 1
        self.queue = deque()
        self.effects = []

    def add_song(self, song):
        self.queue.append(song)

    def add_effect(self, effect):
        self.effects.append(effect)

    def play_song(self):
        song = self.queue.popleft()
        pass

    def skip(self):
        self.play_song()

    def clear_queue(self):
        self.queue.clear()


from __init__ import *




class Playlist:

    def __init__(self, user_id):
        self.user_id = user_id

    @property
    def playlist(self) -> list[str]:
        pass

    def add_song_id_to_playlist(self, song_id):
        pass

    def get_all_song_ids_from_a_playlist(self):
        pass


from __init__ import *

class SearchView(View):

    def __init__(self, *, timeout=180, songs):
        self.songs: CustomSearch = songs
        self.current_index = 0
        super().__init__(timeout=timeout)

    @property
    def current_song(self):
        return self.songs[self.current_index]

    @discord.ui.button(label='', style=discord.ButtonStyle.green, emoji='<:arrowleft:1210243998384652308> ')
    async def play(self, interaction: discord.Interaction, button: discord.ui.Button):
        pl

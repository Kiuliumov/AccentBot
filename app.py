from client import client
from src import fetcher, builder


@client.event
async def on_ready() -> None:
    print(f'Logged in as {client.user}')


@client.command(name='search', description='Search for a song!')
async def search(interaction, song) -> None:

    songs = await fetcher.Fetcher.fetch(song)


    await interaction.response.send_message(builder.Builder.search_song(song))

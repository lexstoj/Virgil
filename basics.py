import discord

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
  print("Bot is ready!")

client.run("MTA2MDcyMjE0NTI0MTYwODIzMg.GizrWy.JNFTLQuSHlLBgvIF4_QFGwCkL-VdvYorFGuBLU")

import requests

def search_song(query):
  url = "https://www.googleapis.com/youtube/v3/search"
  params = {
    "key": "AIzaSyBfmZlahbMlyCNI_saX81Uee5r-GCMEJHg",
    "q": query,
    "type": "video",
    "part": "id",
    "maxResults": 1
  }
  r = requests.get(url, params=params)
  results = r.json()
  if results["items"]:
    return results["items"][0]["id"]["videoId"]
  return None

@client.command()
async def play(ctx, *, query):
  # Search for the song
  video_id = search_song(query)
  if video_id is None:
    await ctx.send("Sorry, I couldn't find that song.")
    return
  # Join the voice channel
  channel = ctx.author.voice.channel
  voice = await channel.connect()
  # Play the song
  player = await voice.create_ytdl_player(f"https://www.youtube.com/watch?v={video_id}")
  player.start()
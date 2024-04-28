import os
from dotenv import load_dotenv
from discord import Intents
from discord.ext import commands
import qbittorrentapi
import discord
from functions import *


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
USERNAME = os.getenv('username')
PASSWORD = os.getenv('password')
HOST = os.getenv('host')
PORT = os.getenv('port')

intents = Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.hybrid_command()
async def downloading(ctx: commands.Context):
    MovieList = []
    TVList = []
    OtherList = []
    count=0
    for torrent in qbt_client.torrents.info.active():
        if torrent.category == 'radarr':
            count = count+1
            TempList = []
            TempList.append(torrent.name + '\nProgress: ' + str(round(torrent.progress * 100, 2)) + "%" + '\n' + convertTime(torrent.eta))
            MovieList.append(TempList)
        if torrent.category == 'tv-sonarr':
            count = count+1
            TempList = []
            TempList.append(torrent.name + '\nProgress: ' + str(round(torrent.progress * 100, 2)) + "%" + '\n' + convertTime(torrent.eta))
            TVList.append(TempList)
        if torrent.category != 'tv-sonarr' and torrent.category != 'radarr':
            count = count+1
            TempList = []
            TempList.append(torrent.name + '\nProgress: ' + str(round(torrent.progress * 100, 2)) + "%" + '\n' + convertTime(torrent.eta))
            OtherList.append(TempList)

    embed = discord.Embed(
        title="**Torrents**",
        description="Currently Downloading Torrents",
        color=ctx.author.colour
    )
    if count == 0:
        await ctx.send("No Torrents Currently Downloading!")
    else:
        for item in MovieList:
            embed.add_field(name="Movie", value=item[0])
        for item in TVList:
            embed.add_field(name="TV Show", value=item[0])
        for item in OtherList:
            embed.add_field(name="Other" ,value=item[0])
        await ctx.send(embed=embed)

@bot.hybrid_command()
async def all(ctx: commands.Context):
    MovieList = []
    TVList = []
    OtherList = []
    count=0
    for torrent in qbt_client.torrents.info.all():
        if torrent.category == 'radarr':
            count = count+1
            TempList = []
            TempList.append(torrent.name + '\nProgress: ' + str(round(torrent.progress * 100, 2)) + "%" + '\n' + convertTime(torrent.eta))
            MovieList.append(TempList)
        if torrent.category == 'tv-sonarr':
            count = count+1
            TempList = []
            TempList.append(torrent.name + '\nProgress: ' + str(round(torrent.progress * 100, 2)) + "%" + '\n' + convertTime(torrent.eta))
            TVList.append(TempList)
        if torrent.category != 'tv-sonarr' and torrent.category != 'radarr':
            count = count+1
            TempList = []
            TempList.append(torrent.name + '\nProgress: ' + str(round(torrent.progress * 100, 2)) + "%" + '\n' + convertTime(torrent.eta))
            OtherList.append(TempList)

    embed = discord.Embed(
        title="**Torrents**",
        description="All Torrents",
        color=ctx.author.colour
    )
    if count == 0:
        await ctx.send("No Torrents Currently Downloading!")
    else:
        for item in MovieList:
            embed.add_field(name="Movie", value=item[0])
        for item in TVList:
            embed.add_field(name="TV Show", value=item[0])
        for item in OtherList:
            embed.add_field(name="Other" ,value=item[0])
        await ctx.send(embed=embed)

@bot.event
async def on_ready():
    print(f'{bot.user} is now running! \nMade By @SavnoorSamra')
    await bot.tree.sync()

# qBIT setup
conn_info = dict(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD
)
qbt_client = qbittorrentapi.Client(**conn_info)

try:
    qbt_client.auth_log_in()
except qbittorrentapi.LoginFailed as e:
    print(e)

print(f"qBittorrent: {qbt_client.app.version}")
print(f"qBittorrent Web API: {qbt_client.app.web_api_version}")
for k, v in qbt_client.app.build_info.items():
    print(f"{k}: {v}")

def main():
    bot.run(TOKEN)


if __name__ == '__main__':
    main()
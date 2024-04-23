import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, app_commands
from discord.ext import commands
import qbittorrentapi
import discord


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
USERNAME = os.getenv('username')
PASSWORD = os.getenv('password')
HOST = os.getenv('host')

# BOT SETUP

intents = Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

# MESSAGES

# BOT PARAMETERS

@bot.hybrid_command()
async def hello(ctx: commands.Context):
    await ctx.send('bye')

@bot.hybrid_command()
async def torrents(ctx: commands.Context):
    TorrentList = []
    count=0

    #for torrent in qbt_client.torrents_info():
    for torrent in qbt_client.torrents.info.active():
        count=count+1
        TempList=[]
        TempList.append(torrent.name + "\n" + convertTime(torrent.eta))
        #TempList.append(torrent.category)
        #TempList.append(str(round(torrent.progress*100,2))+"%")
        #TempList.append(torrent.state)
        #TempList.append(convertTime(torrent.eta))
        TorrentList.append(TempList)

    embed = discord.Embed(
        title="**TORRENTS**",
        description="Currently Downloading Torrents",
        color=ctx.author.colour
    )
    if count == 0:
        await ctx.send("No Torrents Currently Downloading!")
    else:
        for item in TorrentList:
            embed.add_field(name="Name", value=item[0])
        await ctx.send(embed=embed)

def convertTime(seconds):
    intervals = (
    ('weeks', 604800),  # 60 * 60 * 24 * 7
    ('days', 86400),    # 60 * 60 * 24
    ('hours', 3600),    # 60 * 60
    ('minutes', 60),
    ('seconds', 1),)
    if seconds!=8640000:
        result = []
        for name, count in intervals:
            value = seconds // count
            if value:
                seconds -= value * count
                if value == 1:
                    name = name.rstrip('s')
                result.append("{} {}".format(value, name))
        return 'ETA: '+', '.join(result[:])
    else:
        return "N/A"

@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')
    await bot.tree.sync()

# qBIT setup
conn_info = dict(
    host=HOST,
    port=8181,
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

@bot.event
async def on_message(message: Message):
    if message.author == bot.user:
        return

    username = message.author
    user_message = message.content
    channel = message.channel

    print(username, user_message, channel)

def main():
    bot.run(TOKEN)

if __name__ == '__main__':
    main()
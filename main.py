import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, app_commands
from discord.ext import commands
from responses import getResponse

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# BOT SETUP

intents = Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

# MESSAGES

# BOT PARAMETERS
@bot.hybrid_command()
async def hello(ctx: commands.Context):
    await ctx.send('bye')


@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')
    await bot.tree.sync()

@bot.event
async def on_message(message: Message):
    if message.author == bot.user:
        return
    username = message.author
    user_message = message.content
    channel = message.channel

    print(username, user_message, channel)

def main():
    bot.run(token=TOKEN)

if __name__ == '__main__':
    main()
# Static variables
host = '142.4.204.26'
port = 42500
password = "secretRCON"

# Import libraries
import mcrcon
import chat_parser
import time
import discord
import datetime
# Setup
rcon = mcrcon.MCRcon()
chatParser = chat_parser.ChatParser()
rcon.connect(host, port, password)
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.', description="description")

async def update_chat():
    chatParser.get_log()
    messages = chatParser.read_log()
    for msg in messages:
        channel = bot.get_channel(576508966532677632)
        await channel.send(msg)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name + " Chat")
    print(bot.user.id)
    print('------')
    first_start = True
    if first_start:
        await clear_channel(bot.get_channel(576508966532677632))
        first_start = False
    while True:
        await update_chat()

async def clear_channel(channel):
    history = []
    history = await channel.history().flatten()
    await channel.purge(limit=len(history))

bot.run('NTc2NTAyNDk0Mzg2MTkyMzg0.XNXiJA.mKSzyyRc59smbIfCQnN7BHbaS3I')

print("passed")

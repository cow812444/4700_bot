import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import has_role
from discord import Member
from discord.utils import get
import os

bot = commands.Bot(command_prefix='$$')
bot.load_extension(f'cmds.Lilipoints')
bot.load_extension(f'cmds.Summoning')
bot.load_extension(f'cmds.NewsPush')
@bot.event
async def on_ready():
    print('>> 岡田Bot is online')


if __name__ == "__main__":
    print("token be used is : {}".format(str(os.environ.get('DISCORD_TOKEN'))))
    bot.run(str(os.environ.get('DISCORD_TOKEN')))
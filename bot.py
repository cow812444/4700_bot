import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import has_role
from discord import Member
from discord.utils import get
from env import load_env
import json
import os
import pymysql
pymysql.install_as_MySQLdb()
mydb = pymysql.connect(
    host='us-cdbr-iron-east-05.cleardb.net',
    user='b8167bd3b0485f',
    passwd='8042a225',
    db='heroku_e3fdeb125d50ac6'
)

#TOKEN = os.environ.get("DISCORD_BOT_SECRET","")
TOKEN = "NjQyNDIyMDUzMjIzNTMwNTA2.Xd-8oQ.gyxaw9gsxRjOcIT8Y--B_1SO8BI"

with open('setting.json','r',encoding='utf-8') as jsonFile:
    jsonData = json.load(jsonFile)

bot = commands.Bot(command_prefix='$$')

@bot.event
async def on_ready():
    print('>> Bot is online')

@bot.event
async def on_member_join(member):
    print(f'{member} join!')
    channel = bot.get_channel(649210703718383616)
    await channel.send(f'{member} 加入囉!')

#@bot.event
#async def on_member_remove(member):
#    print(f'{member} leave!')
#    channel = bot.get_channel(642458050300608513)
#    await channel.send(f'{member} leave!')

#for fileName in os.listdir('./cmds'):
#    if(fileName.endswith('.py')):
#        bot.load_extension(f'cmds.{fileName[:-3]}')

bot.load_extension(f'cmds.Lilipoints')
bot.load_extension(f'cmds.Summoning')
bot.load_extension(f'cmds.NewsPush')

if __name__ == "__main__":
    bot.run(TOKEN)
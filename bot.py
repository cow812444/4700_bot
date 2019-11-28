import asyncio
import discord
from discord.ext import commands
import json
import os
import pymysql
pymysql.install_as_MySQLdb()

mydb = pymysql.connect(
    host='us-cdbr-iron-east-05.cleardb.net',
    user='b481207a7d96b0',
    passwd='8d2c2f0e',
    db='heroku_8559373c0824ae1'
)

with open('setting.json','r',encoding='utf-8') as jsonFile:
    jsonData = json.load(jsonFile)

bot = commands.Bot(command_prefix='$$')

@bot.event
async def on_ready():
    print('>> Bot is online')

@bot.event
async def on_member_join(member):
    print(f'{member} join!')
    channel = bot.get_channel(642457848340807693)
    await channel.send(f'{member} join!')

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
    bot.run(jsonData['TOKEN'])
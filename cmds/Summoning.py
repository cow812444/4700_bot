import discord
from discord.ext import commands
import json

with open('setting.json','r',encoding='utf-8') as jsonFile:
    jsonData = json.load(jsonFile)
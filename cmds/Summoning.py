import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json','r',encoding='utf-8') as jsonFile:
    jsonData = json.load(jsonFile)


class Summoning(Cog_Extension):
    
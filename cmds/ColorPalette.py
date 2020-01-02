import asyncio
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import re
import os

class ColorPalette(Cog_Extension):
    self.colorPlt = {'<:green_square:bb7aa875fe442f8c2c79e5b8b1e8c7c9>':'color_1',
                    '<:red_square:395a4608ed021406b8f0ad4506081996>':'color_2',
                    '<:yellow_square:0ca363e545e2f490cf4b852f5c8e0404>':'color_3',
                    '<:color_4:585654238432985124>':'color_4',
                    '<:color_5:585654238432985124>':'color_5',
                    '<:color_6:585654238432985124>':'color_6',
                    '<:color_7:585654238432985124>':'color_7',
                    '<:color_8:585654238432985124>':'color_8',
                    '<:color_9:585654238432985124>':'color_9',
                    '<:color_10:585654238432985124>':'color_10',
                    '<:color_11:585654238432985124>':'color_11',
                    '<:color_12:585654238432985124>':'color_12',
                    '<:color_13:585654238432985124>':'color_13',
                    '<:color_14:585654238432985124>':'color_14',
                    '<:color_15:585654238432985124>':'color_15',
                    '<:color_16:585654238432985124>':'color_16',
                    '<:color_17:585654238432985124>':'color_17',
                    '<:color_18:585654238432985124>':'color_18',
                    '<:color_19:585654238432985124>':'color_19',
                    '<:color_20:585654238432985124>':'color_20',
                    '<:color_21:585654238432985124>':'color_21',
                    '<:color_22:585654238432985124>':'color_22',
                    '<:color_23:585654238432985124>':'color_23',
                    '<:color_24:585654238432985124>':'color_24',
                    '<:color_25:585654238432985124>':'color_25',
                    '<:color_26:585654238432985124>':'color_26',
                    '<:color_27:585654238432985124>':'color_27',
                    '<:color_28:585654238432985124>':'color_28',
                    '<:color_29:585654238432985124>':'color_29',
                    '<:color_30:585654238432985124>':'color_30',
                    '<:color_31:585654238432985124>':'color_31',
                    '<:color_32:585654238432985124>':'color_32',
                    '<:color_33:585654238432985124>':'color_33',
                    '<:color_34:585654238432985124>':'color_34',
                    '<:color_35:585654238432985124>':'color_35',
                    '<:color_36:585654238432985124>':'color_36',
                    '<:color_37:585654238432985124>':'color_37',
                    '<:color_38:585654238432985124>':'color_38',
                    '<:color_39:585654238432985124>':'color_39',
                    '<:color_40:585654238432985124>':'color_40',
                    '<:color_41:585654238432985124>':'color_41',
                    '<:color_42:585654238432985124>':'color_42',
                    '<:color_43:585654238432985124>':'color_43',
                    '<:color_44:585654238432985124>':'color_44',
                    '<:color_45:585654238432985124>':'color_45',
    }
    self.emoji_id =[]
    self.role_name=[]
    for self.key, self.value in self.colorPlt.items():   #dict轉list
        self.emoji_id.append(key)
        self.role_name.append(value)
    @commands.Cog.listener()
    async def on_reaction_add(self,reaction, user):
        channel_Change_Color = self.bot.get_channel(648922785716109323)
        if reaction.message.channel.id != channel_Change_Color:
            return
        if reaction.emoji in self.emoji_id:
            idx = self.emoji_id(reaction.emoji)
            role = discord.utils.get(user.server.roles, name=self.role_name(idx))
            await self.bot.add_roles(user, role)
            pass
        '''
        if reaction.emoji == '<:color_1:585654238432985124>':  #color 1
            role = discord.utils.get(user.server.roles, name="color_1")
            await self.bot.add_roles(user, role)
            pass
        '''
    pass
def setup(bot):
    bot.add_cog(ColorPalette(bot))
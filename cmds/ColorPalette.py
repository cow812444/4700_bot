import asyncio
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import re
import os

class ColorPalette(Cog_Extension):
    colorPlt = {'🟩':'color_1',
                    '🟥':'color_2',
                    '🟨':'color_3',
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
    emoji_id =[]
    role_name=[]
    for key, value in colorPlt.items():   #dict轉list
        emoji_id.append(key)
        role_name.append(value)
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        colorPlt = {'0ca363e545e2f490cf4b852f5c8e0404':'color_1',
                    'red_square':'color_2',
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
        print('偵測到reaction from {}'.format(payload))
        channel_Change_Color = self.bot.get_channel(648922785716109323)
        if not payload.guild_id:
            print('not payload.guild_id, 直接return')
            return
        if payload.message_id != 662185247785353217:
            return
        guild = self.bot.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        print(payload.emoji.name)
        role_N = colorPlt.get(payload.emoji.name)
        print('guild ={}, member ={}, role_N ={}'.format(guild,member,role_N))
        if role_N:
            print('YES')
            role = discord.utils.get(guild.roles, name=role_N)
            await member.add_roles(role, reason='Reaction role')
    pass
def setup(bot):
    bot.add_cog(ColorPalette(bot))

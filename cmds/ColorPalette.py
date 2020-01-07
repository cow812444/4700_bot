import asyncio
import discord
from discord.ext import commands
from discord.utils import get
from core.classes import Cog_Extension
import re
import os

class ColorPalette(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self, msg):
        channel_Change_color = self.bot.get_channel(648922785716109323)
        text_str = re.search(r'(#([A-Z0-9]{6}))', msg.content)
        # and msg.channel == channel_Change_color
        if text_str:
            guild = msg.guild
            colour_value = text_str.group(2)
            to_int = int(colour_value, 16)
            colour_value = to_int
            role = get(guild.roles, name=msg.author.display_name)
            user = msg.author
            if role:
                #change roles color
                await self.bot.edit_role(guild, role, colour=discord.Colour(colour_value))
            else:
                await guild.create_role(name=msg.author.display_name, colour=discord.Colour(colour_value))
                await user.add_roles(role)
        #msg.author
        pass
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        colorPlt = {'🟩':'color_1',
                    '🟥':'color_2',
                    '🟨':'color_3'
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
        #print(payload.emoji.name)
        role_N = colorPlt.get(payload.emoji.name)
        '''
        print('guild ={}, member ={}, role_N ={}'.format(guild,member,role_N))
        if role_N:
            print('YES')
            role = discord.utils.get(guild.roles, name=role_N)
            await member.add_roles(role, reason='Reaction role')
        '''
    pass
def setup(bot):
    bot.add_cog(ColorPalette(bot))

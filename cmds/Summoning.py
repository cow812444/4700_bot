import asyncio
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import time
import os
import re
import random
import math


class Summoning(Cog_Extension):
    def set_Chance(self,fs1=1,fs2=0.8,fs3=1,fs4=1.2,increase_If_Fail=[0,0,0,0]):  #初始機率 4%
        five_Star_1 = fs1 + increase_If_Fail[0]
        five_Star_2 = fs2 + fs1 + increase_If_Fail[1]
        five_Star_3 = fs3 + fs1 + fs2 + increase_If_Fail[2]
        five_Star_4 = fs4 + fs1 + fs2 + fs3 + increase_If_Fail[3]
        total_range = (five_Star_1 * 4)
    @commands.Cog.listener()
    async def on_message(self, msg):
        five_Star_1 = 1
        five_Star_2 = 0.8 + 1
        five_Star_3 = 1 + 1 + 0.8
        five_Star_4 = 1.2 + 1 + 1 + 0.8
        total_range = (five_Star_1 * 4)
        #每10連增加機率 0.5%
        five_Star_1_fail = 0.125
        five_Star_2_fail = 0.105
        five_Star_3_fail = 0.125
        five_Star_4_fail = 0.145
        folder_dict = {'精選_1':['5★光秀[光]','5★信長[火]'],'精選_2':'5★大黑天[光]','五星':[u'5★納杰夫[火]','5★里亞[火]','5★尊[火]','5★雷吉娜[火]','5★葉潔莉特[火]','5★羅吉娜[火]','5★雀兒喜[火]','5★梅莉貝爾(花樣笑顏ver.)[火]','5★亞雷克西斯[水]','5★榭葉拉(夏日ver.)[水]','5★茱莉葉塔(夏日ver.)[水]','5★賽因福蘭德[水]','5★拉拉諾亞[水]','5★莉莉[水]','5★耶魯菲莉絲(花嫁ver.)[風]','5★維克多[風]','5★葵(花嫁ver.)[風]','5★燐由[風]','5★夏思特[風]','5★路易潔[風]','5★霍克[風]','5★梅莉貝爾[風]','5★阿迦奢[風]','5★阿爾貝爾[光]','5★夏迪(時尚美艷ver.)[光]','5★朱莉葉塔[光]','5★安妮里耶[光]','5★克菈兒(夏日ver.)[光]','5★露克雷齊亞[光]','5★赫德德[光]','5★夜天[暗]','5★夏實[暗]','5★德菲[暗]','5★庫豹[暗]','5★菈特妮[暗]','5★涅法莉耶[暗]','5★卡珊德拉[暗]','5★海因沃爾德[暗]','5★薇兒謝拉(夏日ver.)[暗]','5★太公望[水]'],'五星龍':['5★阿耆尼[火]','5★可魯[火]','5★普羅[火]','5★木花開[火]','5★阿波羅[火]','5★火熊[火]','5★加具土[火]','5★雷鷹[風]','5★+66[風]','5★龍龍[風]','5★怕祖祖[風]','5★伐由[風]','5★哈斯塔[風]','5★芙蕾雅[風]','5★波賽東[水]','5★利維坦[水]','5★賽蓮[水]','5★泡泡雞[水]','5★丘比特[光]','5★基加美修[光]','5★建御雷[光]','5★貞德[光]','5★萊德[光]','5★賽蓮[光]','5★忍[暗]','5★奈亞[暗]','5★尼德霍格[暗]','5★普魯托[暗]']}
        #初始機率 4%
        self.set_Chance()

        ###  >>>   (10[連抽]|十[連抽]|[單一]抽)?(\d?\d?\d|抽到有)?[連次抽]?    <<<   11/27
        channel_Num1 = int(os.environ.get('CHANNEL_SUMMONROOM_FROM_4700'))
        channel_Num2 = int(os.environ.get('CHANNEL_SUMMONROOM_FROM_DISH'))
        channel1 = self.bot.get_channel(channel_Num1)  ##4700 抽卡區
        channel2 = self.bot.get_channel(channel_Num2)  ##餐廳 曬卡區
        pattern = re.search(r'(\d?\d?\d(?=連|次|抽)|抽到有)',msg.content.lower())
        if pattern and msg.author != self.bot.user and (channel1 == msg.channel or channel2 == msg.channel):
            user = msg.author.display_name
            group1 = pattern.group(1)
            controlTrigger = 0
            counts = 0
            numbers = 0
            result = []
            if group1 == '抽到有':
                while True:
                    ran_Num = round(random.random() * 100,4)
                    controlTrigger = 0
                    numbers = numbers + 1
                    if total_range == 9:
                        five_Star_1 = five_Star_1 + (five_Star_1_fail * 182)
                        five_Star_2 = five_Star_2 + (five_Star_2_fail * 182) + five_Star_1
                        five_Star_3 = five_Star_3 + (five_Star_3_fail * 182) + five_Star_1 + five_Star_2
                        five_Star_4 = five_Star_4 + (five_Star_4_fail * 182) + five_Star_1 + five_Star_2 + five_Star_3
                        total_range = (five_Star_1 * 4)
                    if ran_Num <= five_Star_1:
                        random_pu = random.randint(0,(len(folder_dict['精選_1'])-1))
                        print(ran_Num,' ',folder_dict['精選_1'][random_pu])
                        controlTrigger = 1
                        result.append(folder_dict['精選_1'][random_pu])
                        break
                        counts = counts + 1
                        #await msg.channel.send('{} {}'.format(ran_Num,folder_dict['精選_2']))
                    elif ran_Num <= five_Star_2:
                        print(ran_Num,' ',folder_dict['精選_2'])
                        controlTrigger = 1
                        result.append(folder_dict['精選_2'])
                        break
                        counts = counts + 1
                        #await msg.channel.send('{} {}'.format(ran_Num,folder_dict['精選_2']))
                    elif ran_Num <= five_Star_3:
                        random_char = random.randint(0,(len(folder_dict['五星'])-1))
                        print(ran_Num,' ',random_char,' ',folder_dict['五星'][random_char])
                        controlTrigger = 1
                        result.append(folder_dict['五星'][random_char])
                        counts = counts + 1
                        #await msg.channel.send('{} {}'.format(ran_Num,folder_dict['五星']))
                    elif ran_Num <= five_Star_4:
                        random_dra = random.randint(0,(len(folder_dict['五星龍'])-1))
                        print(ran_Num,' ',random_dra,' ',folder_dict['五星龍'][random_dra])
                        controlTrigger = 1
                        result.append(folder_dict['五星龍'][random_dra])
                        counts = counts + 1
                        #await msg.channel.send('{} {}'.format(ran_Num,folder_dict['五星龍']))
                    else:
                        print(ran_Num,' ','nothing')
                        counts = counts + 1
                        #result.append([ran_Num,'nothing'])
                        #await msg.channel.send('{} nothing'.format(ran_Num))
                        if counts % 10 == 0 and counts != 0 :
                            self.set_Chance(fs1=five_Star_1,fs2=five_Star_2,fs3=five_Star_3,fs4=five_Star_4,increase_If_Fail=[0.125,0.105,0.125,0.145])
                    if controlTrigger == 1:
                        self.set_Chance()
                        #counts = abs(counts - rounds)
                        counts = 0
                    controlTrigger = 0
                    #counts = counts + 1
                if len(result) == 0:
                    await msg.channel.send('{}總共花了 {} 抽,然而什麼都沒有,ㄏㄏ'.format(user,numbers))
                else:
                    await msg.channel.send('{}總共花了 {} 抽,抽到: {}% '.format(user,numbers,result))
                #print('目前機率: {}%'.format(total_range))
            else:
                summon_Times = int(group1)
                tenFold_Count = int(math.floor(summon_Times/10))
                oneShot_Count = summon_Times%10
                summonNum = tenFold_Count * 10 + oneShot_Count
                for rounds in range(0,summonNum):
                    ran_Num = round(random.random() * 100,3)
                    controlTrigger = 0
                    if total_range == 9:
                        five_Star_1 = five_Star_1 + (five_Star_1_fail * 182)
                        five_Star_2 = five_Star_2 + (five_Star_2_fail * 182) + five_Star_1
                        five_Star_3 = five_Star_3 + (five_Star_3_fail * 182) + five_Star_1 + five_Star_2
                        five_Star_4 = five_Star_4 + (five_Star_4_fail * 182) + five_Star_1 + five_Star_2 + five_Star_3
                        total_range = (five_Star_1 * 4)
                    if ran_Num <= five_Star_1:
                        print(ran_Num,' ',folder_dict['精選_1'])
                        controlTrigger = 1
                        result.append(folder_dict['精選_1'])
                        counts = counts + 1
                        #await msg.channel.send('{} {}'.format(ran_Num,folder_dict['精選_2']))
                    elif ran_Num <= five_Star_2:
                        print(ran_Num,' ',folder_dict['精選_2'])
                        controlTrigger = 1
                        result.append(folder_dict['精選_2'])
                        counts = counts + 1
                        #await msg.channel.send('{} {}'.format(ran_Num,folder_dict['精選_2']))
                    elif ran_Num <= five_Star_3:
                        random_char = random.randint(0,(len(folder_dict['五星'])-1))
                        print(ran_Num,' ',random_char,' ',folder_dict['五星'][random_char])
                        controlTrigger = 1
                        result.append(folder_dict['五星'][random_char])
                        counts = counts + 1
                        #await msg.channel.send('{} {}'.format(ran_Num,folder_dict['五星']))
                    elif ran_Num <= five_Star_4:
                        random_dra = random.randint(0,(len(folder_dict['五星龍'])-1))
                        print(ran_Num,' ',random_dra,' ',folder_dict['五星龍'][random_dra])
                        controlTrigger = 1
                        result.append(folder_dict['五星龍'][random_dra])
                        counts = counts + 1
                        #await msg.channel.send('{} {}'.format(ran_Num,folder_dict['五星龍']))
                    else:
                        print(ran_Num,' ','nothing')
                        counts = counts + 1
                        #result.append([ran_Num,'nothing'])
                        #await msg.channel.send('{} nothing'.format(ran_Num))
                        if counts % 10 == 0 and counts != 0 :
                            self.set_Chance(fs1=five_Star_1,fs2=five_Star_2,fs3=five_Star_3,fs4=five_Star_4,increase_If_Fail=[0.125,0.105,0.125,0.145])
                    if controlTrigger == 1:
                        self.set_Chance()
                        #counts = abs(counts - rounds)
                        counts = 0
                    controlTrigger = 0
                    #counts = counts + 1
                if len(result) == 0:
                    await msg.channel.send('{}總共花了 {} 抽,然而什麼都沒有'.format(user,summon_Times))
                else:
                    await msg.channel.send('{}總共花了 {} 抽,抽到: {} '.format(user,summon_Times,result))
                print('目前機率: {}%'.format(total_range))
            
def setup(bot):
    bot.add_cog(Summoning(bot))

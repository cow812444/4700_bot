import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import re
import os
import random
import pymysql
pymysql.install_as_MySQLdb()

mydb = pymysql.connect(
    host='localhost',
    user='root',
    passwd='4510',
    db='userpoints'
)


user_dict={'齊木':'1','黑貓':'2','yoyo':'3','盆栽':'4','咲夜':'5','火花':'6','蟑螂':'7','變態':'8','三寶':'9','香香':'10','幕容':'11','木子':'12','小白':'13','月海':'14','草哥':'15','四月':'16','dula':'17','可魯':'18','卡打':'19','lza':'20','月月':'21','somes':'22','wewa':'23','亡音':'24','夏音':'25','奧迪':'26','鱈魚':'27','kk':'28','voc':'29','恰恰':'30','腐貓':'31','詩詩':'32','那歐':'33','霜降':'34','peco':'35','女僕丸':'36','max':'37','岡田':'38','松浦':'39','sky':'40','maple':'41','海瀨':'42','米國':'43','滑水':'44','zz':'45'}
user_nName=[['齊木黑昀','齊ㄇ'],['黒猫','黑貓','黒貓'],['null'],['盤栽'],['消夜','宵夜','笑夜'],['泡泡雞','雷鷹','ㄆㄆ雞','泡雞'],['壞壞蟑螂'],['null'],['3寶','ㄌㄌㄎ','yutami'],['今天不行了','ㄌㄌㄎ'],['慕蓉','慕容','幕蓉'],['null'],['白白雞','白白'],['粵海','倉鼠'],['草尼馬','草尼瑪','草泥瑪','草泥馬'],['april','apr','4月'],['賭拉','杜拉','肚拉','度拉'],['fly'],['katar','卡達'],['版主'],['moon'],['null'],['null'],['亡88','音88','亡爸爸','音爸爸'],['導遊'],['null'],['雪魚'],['null'],['null'],['chacha'],['null'],['國軍'],['nao'],['ㄌㄌㄎ'],['佩扣','佩口','珮口','珮扣'],['妹斗','妹抖'],['null'],['二號','2號'],['一號','1號'],['null'],['null'],['null'],['null'],['null'],['莉莉']]
user_name =[]
user_dbId=[]
for key, value in user_dict.items():   #dict轉list
    user_name.append(key)
    user_dbId.append(value)

with open('setting.json','r',encoding='utf-8') as jsonFile:
    jsonData = json.load(jsonFile)

class Lilipoints(Cog_Extension):
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} leave!')
        channel = self.bot.get_channel(642458050300608513)
        await channel.send(f'{member} leave!')

 

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content =='二號下台' and msg.author != self.bot.user:
            if random.randint(0,12) ==11:
                await msg.channel.send('我對不起大家 <:prison:585652892627894288>')
            if random.randint(0,12) == 1:
                await msg.channel.send('明日贈送十連券*10 <:cryfrog:585653534461132800>')
            if random.randint(0,12) == 5:
                await msg.channel.send('我就喜歡看著你討厭我卻又幹不掉我的樣子')
                await msg.channel.send('<:PepeHappy:585654238432985124>')


        for name in user_name:
            #countingPattern = re.search(r'^.*(({}).*((\+|\-)(\d+)(?!.*(劍|法|補|槍|短|刀|斧|弓))).*$'.format(name), msg.content.lower())  #regex
            countingPattern = re.search(r'^.*(('+name+').*((\+|\-)(\d{1,3}))(?!.*(劍|法|補|槍|短|刀|斧|弓))).*$', msg.content.lower())  #regex
            showPoints = re.search(r'(^\$)({}$)'.format(name), msg.content.lower())
            resetPoints = re.search(r'(^\$reset )({}$)'.format(name), msg.content.lower())
            organizeBoard = re.search(r'(^\$)('+name+')([A-Za-z]{1,4}|[\u4E00-\u9FA5]{2})([A-Za-z]{1,4}|[\u4E00-\u9FA5]{2})([A-Za-z]{1,4}|[\u4E00-\u9FA5]{2})',msg.content.lower())
            ##########################加減分計算Start#####################################
            if(countingPattern and msg.author != self.bot.user):
                print('整句: ' + countingPattern.group(0))   #整句
                #print('從id開始到最後: ' + m1.group(1))  #從id開始到最後
                print('得到id: ' + countingPattern.group(2))   #得到id
                userName_get = countingPattern.group(2)    #抓取開頭兩字得到name
                #print('分數加分/減分全部: ' + m1.group(3))
                points_ChangedStatus = countingPattern.group(4)   #分數加分/減分
                print('分數加分/減分: ' + points_ChangedStatus)
                userPoints_get = countingPattern.group(5)  #得到分數變化,存進pnt_get
                print('分數變化: ' + userPoints_get)
                if userPoints_get == '0':
                    await msg.channel.send('不要戲弄岡田 <:prison:585652892627894288>  , {}是想被揍嗎'.format(countingPattern.group(3)))
                    continue
                if len(userPoints_get) >= 3 and points_ChangedStatus == '+':
                    await msg.channel.send('不要欺負{} <:cjm:641920055092838400>'.format(userName_get))
                    continue   
                if int(userPoints_get) > 99 and points_ChangedStatus == '-':
                    await msg.channel.send('減這麼多分，你484偷偷喜歡{}'.format(userName_get))
                if userName_get in user_dict:
                    print('db編號: ' + user_dict[userName_get]+' get!')
                    #await msg.channel.send('目標: ' + userName_get + '\n分數變化: ' + countingPattern.group(3) + '\nDB編號: ' + user_dict[userName_get])
                    cursor = mydb.cursor()
                    cursor.execute('SELECT * FROM users WHERE user_id = %s',user_dict[userName_get])
                    result = cursor.fetchall()
                    current_UserPoints = result[0][1]
                    print('目前計分: {}'.format(current_UserPoints))
                    #print('原本db分數: ' + (str)(current_UserPoints))
                    if points_ChangedStatus == '+':
                        if int(current_UserPoints) + int(userPoints_get) > 2147483647:
                            await msg.channel.send('{}已經爆掉了,放過他好ㄇ'.format(userName_get))
                            continue
                        new_UserPoints = str(current_UserPoints + (int)(userPoints_get))
                    if points_ChangedStatus == '-':
                        if int(current_UserPoints) + int(userPoints_get) < -2147483648:
                            await msg.channel.send('{}已經爆掉了,放過他好ㄇ'.format(userName_get))
                            continue
                        new_UserPoints = str(current_UserPoints - (int)(userPoints_get))
                    print('最新分數: {}'.format(new_UserPoints))
                    sql = 'UPDATE users SET user_points = {} WHERE user_id = {}'.format(new_UserPoints, user_dict[userName_get])
                    cursor.execute(sql)
                    mydb.commit()
                    #print('目前db分數: ' + (str)(new_UserPoints))
                    #msg_toSend = '目標 : {}\n原本莉莉點數: {}\n分數變化: {}\n目前莉莉點數: {}'.format(userName_get,current_UserPoints,countingPattern.group(3),new_UserPoints)
                    msg_toSend = '{}{} (原本計分: {} // 目前計分: {})'.format(userName_get,countingPattern.group(3),current_UserPoints,new_UserPoints)
                    #print('目標 : {}\n原本莉莉點數: {}\n分數變化: {}\n目前莉莉點數: {}'.format(userName_get,current_UserPoints,countingPattern.group(3),new_UserPoints))
                    print('{}{} (原本計分: {} // 目前計分: {})'.format(userName_get,countingPattern.group(3),current_UserPoints,new_UserPoints))
                    channel1 = self.bot.get_channel(547075157693562913)
                    if msg.channel != channel1:
                        await msg.channel.send(msg_toSend)
                else:
                    print("fail!")
                    await msg.channel.send('沒抓到綽號,請換一個試試')

            ##########################顯示目前分數#####################################
            if(showPoints and msg.author != self.bot.user):
                #print('整句: ' + showPoints.group(0))   #整句
                #print('得到id: ' + showPoints.group(2))   #得到id
                userName_get = showPoints.group(2)
                cursor = mydb.cursor()
                cursor.execute('SELECT * FROM users WHERE user_id = %s',user_dict[userName_get])
                result = cursor.fetchall()
                current_UserPoints = result[0][1]
                msg_toSend = '{}(累積計分: {})'.format(userName_get,current_UserPoints)
                print('{}(累積計分: {})'.format(userName_get,current_UserPoints))
                await msg.channel.send(msg_toSend)
            
            ##########################重置分數#########################################
            if(resetPoints and msg.author != self.bot.user):
                #print('整句: ' + resetPoints.group(0))   #整句
                #print('得到id: ' + resetPoints.group(2))   #得到id
                userName_get = resetPoints.group(2)
                cursor = mydb.cursor()
                cursor.execute('SELECT * FROM users WHERE user_id = %s',user_dict[userName_get])
                result = cursor.fetchall()
                current_UserPoints = result[0][1]
                new_UserPoints = '0'
                sql = 'UPDATE users SET user_points = {} WHERE user_id = {}'.format(new_UserPoints, user_dict[userName_get])
                cursor.execute(sql)
                mydb.commit()
                msg_toSend = '已重置 {} 的分數(累積計分: {})'.format(userName_get,new_UserPoints)
                await msg.channel.send(msg_toSend)

            ##########################組隊顯示分數#####################################
            if(organizeBoard and msg.author != self.bot.user):
                #print('整句: ' + organizeBoard.group(0))   #整句
                #print('得到\$: ' + organizeBoard.group(1))   #得到$

                #print('得到id_1: ' + organizeBoard.group(2))
                #print('得到id_2: ' + organizeBoard.group(3))
                #print('得到id_3: ' + organizeBoard.group(4))
                #print('得到id_4: ' + organizeBoard.group(5))

                usersName_get = [organizeBoard.group(2),organizeBoard.group(3),organizeBoard.group(4),organizeBoard.group(5)]
                cursor = mydb.cursor()
                current_usersPoints = []
                n=0
                for id_ in usersName_get:
                    if id_ in user_dict:
                        cursor.execute('SELECT * FROM users WHERE user_id = %s',user_dict[id_])
                        result = cursor.fetchall()
                        current_usersPoints.append(result[0][1])
                        n=n+1
                    else:
                        await msg.channel.send('有人的名字打錯囉！')
                        continue
                channel1 = self.bot.get_channel(547075157693562913)
                if len(current_usersPoints) == 4 and msg.channel != channel1:
                    #await msg.channel.send(dict(zip(usersName_get,current_usersPoints)))
                    await msg.channel.send('{}: {}\n{}: {}分\n{}: {}分\n{}: {}分'.format(organizeBoard.group(2),current_usersPoints[0],organizeBoard.group(3),current_usersPoints[1],organizeBoard.group(4),current_usersPoints[2],organizeBoard.group(5),current_usersPoints[3]))
                    print('記分板: {}'.format(dict(zip(usersName_get,current_usersPoints))))                







def setup(bot):
    bot.add_cog(Lilipoints(bot))
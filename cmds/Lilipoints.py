import asyncio
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import re
import os
import random
import pymysql
pymysql.install_as_MySQLdb()

user_dict={'齊木':'1','黑貓':'2','yoyo':'3','盆栽':'4','咲夜':'5','火花':'6','蟑螂':'7','變態':'8','三寶':'9','香香':'10','幕容':'11','木子':'12','小白':'13','月海':'14','草哥':'15','四月':'16','dula':'17','可魯':'18','卡打':'19','lza':'20','月月':'21','somes':'22','wewa':'23','亡音':'24','夏音':'25','奧迪':'26','鱈魚':'27','kk':'28','voc':'29','恰恰':'30','腐貓':'31','詩詩':'32','那歐':'33','霜降':'34','peco':'35','女僕丸':'36','max':'37','岡田':'38','松浦':'39','sky':'40','maple':'41','海瀨':'42','米國':'43','滑水':'44','zz':'45'}
user_nName={'齊木':['齊木','齊ㄇ','7ㄇ','7木'],'黑貓':['黑貓','黒猫','黑貓','黒貓'],'yoyo':['yoyo'],'盆栽':['盤栽','盆栽'],'咲夜':['咲夜','消夜','宵夜','笑夜'],'火花':['火花','泡泡雞','雷鷹','ㄆㄆ雞','泡雞'],'蟑螂':['壞壞蟑螂','蟑螂'],'變態':['變態'],'三寶':['三寶','3寶','ㄌㄌㄎ','yutami'],'香香':['香香','今天不行了','ㄌㄌㄎ'],'幕容':['幕容','慕蓉','慕容','幕蓉'],'木子':['木子'],'小白':['小白','白白雞','白','siro'],'月海':['月海','粵海','倉鼠'],'草哥':['草哥','草尼馬','草尼瑪','草泥瑪','草泥馬','馬哥','尼哥'],'四月':['四月','april','apr','4月'],'dula':['dula','賭拉','杜拉','肚拉','度拉'],'可魯':['可魯','fly'],'卡打':['卡打','katar','卡達'],'lza':['lza','版主'],'月月':['moon','月月'],'somes':['somes'],'wewa':['wewa'],'亡音':['亡音','亡88','音88','亡爸爸','音爸爸'],'夏音':['夏音','導遊'],'奧迪':['奧迪'],'鱈魚':['鱈魚','雪魚'],'kk':['kk'],'voc':['voc'],'恰恰':['恰恰','chacha'],'腐貓':['腐貓'],'詩詩':['詩詩','國軍'],'那歐':['那歐','nao'],'霜降':['霜降','ㄌㄌㄎ'],'peco':['peco','佩扣','佩口','珮口','珮扣'],'女僕丸':['女僕丸','妹斗','妹抖'],'max':['max'],'岡田':['岡田','二號','2號'],'松浦':['松浦','一號','1號'],'sky':['sky'],'maple':['maple'],'海瀨':['海瀨','海獺'],'米國':['米國'],'滑水':['滑水'],'zz':['zz','莉莉']}
user_name =[]
user_dbId=[]
for key, value in user_dict.items():   #dict轉list
    user_name.append(key)
    user_dbId.append(value)
user_nName1 =[]
user_dDbId=[]
for key, value in user_nName.items():   #dict轉list
    user_dDbId.append(key)
    user_nName1.append(value)

class Lilipoints(Cog_Extension):
    def connect(self):
        self.mydb = pymysql.connect(
        host=os.environ.get('DB_HOST'),
        user=os.environ.get('DB_USER'),
        passwd=os.environ.get('DB_PASSWD'),
        db=os.environ.get('DB_NAME')
        )
    def query(self, sql):
        try:
            cursor = self.mydb.cursor()
            cursor.execute(sql)
        except:
            self.connect()
            cursor = self.mydb.cursor()
            cursor.execute(sql)
        return cursor
    @commands.Cog.listener() 
    async def on_message(self, msg):
        self.connect()
        channel_Num1 = int(os.environ.get('CHANNEL_TEXTLOBBY_FROM_DISH'))
        channel_TextLobby = self.bot.get_channel(os.environ.get('CHANNEL_TEXTLOBBY_FROM_DISH'))
        text_str = re.search(r'(二號|岡田)下台', msg.content)
        #if ((msg.content =='二號下台' or msg.content =='岡田下台') and msg.author != self.bot.user):
        if text_str and msg.author != self.bot.user:
            ranNum = random.randint(0,12)
            if ranNum <= 1:
                await msg.channel.send('我對不起大家 <:prison:585652892627894288>')
            elif ranNum < 6 and ranNum >= 4:
                await msg.channel.send('明日贈送十連券 <:cryfrog:661231166464065547>')
                await msg.channel.send('但是卡打沒有')
            elif ranNum >= 11:
                await msg.channel.send('我就喜歡看著你討厭我卻又幹不掉我的樣子')
                await msg.channel.send('<:PepeHappy:661231204409802776>')
        text_katar = re.search(r'(工讀)', msg.content)
        if msg.author.display_name == 'Katar' and text_katar:
            ranNun = random.randint(0,10)
            if ranNun <=1:
                await msg.channel.send('你才工讀生，你全家都工讀生')
                await msg.channel.send('<:dog~1:661230606843117589>')
            elif ranNun <6 and ranNun >= 4:
                await msg.channel.send('工作真的很辛苦，薪水又少，給點牡蠣好ㄇ')
            elif ranNun >=11:
                await msg.channel.send('卡打')
                time.sleep(2)
                await msg.channel.send('掐')
        tmp = 0
        for name in user_name:
            for nameList in user_nName1:
                for personList in nameList:
                    #countingPattern = re.search(r'^.*(({}).*((\+|\-)(\d+)(?!.*(劍|法|補|槍|短|刀|斧|弓))).*$'.format(name), msg.content.lower())  #regex
                    countingPattern = re.search(r'^.*(('+personList+').*((\+|\-)(\d{1,3}))(?!.*(劍|法|補|槍|短|刀|斧|弓))).*$', msg.content.lower())  #regex
                    showPoints = re.search(r'(^\$)({}$)'.format(personList), msg.content.lower())
                    resetPoints = re.search(r'(^\$reset )({}$)'.format(personList), msg.content.lower())
                    organizeBoard = re.search(r'(^\$)('+personList+')\s([A-Za-z]{1,5}|[\u4E00-\u9FA5]{2})\s([A-Za-z]{1,5}|[\u4E00-\u9FA5]{2})\s([A-Za-z]{1,5}|[\u4E00-\u9FA5]{2})',msg.content.lower())
                    ##########################加減分計算Start#####################################
                    if(countingPattern and msg.author != self.bot.user and tmp == 0 and channel_TextLobby != msg.channel):    
                    ##pattern get and 防機器人自己偵測自己 and 重複判定 and 禁止小餐廳-文字大廳使用(防洗頻)
                        tmp = tmp + 1
                        print('整句: ' + countingPattern.group(0))   #整句
                        print('得到id: ' + countingPattern.group(2))   #得到id 
                        userName_get = [k for k, v in user_nName.items() if v == nameList][0]
                        points_ChangedStatus = countingPattern.group(4)   #分數加分/減分
                        print('分數加分/減分: ' + points_ChangedStatus)
                        userPoints_get = countingPattern.group(5)  #得到分數變化,存進pnt_get
                        print('分數變化: ' + userPoints_get)
                        if userPoints_get == '0':
                            await msg.channel.send('不要戲弄岡田 <:18:661231588511580180>  , {}是想被揍嗎'.format(countingPattern.group(3)))
                            continue
                        if len(userPoints_get) >= 3 and points_ChangedStatus == '+':
                            await msg.channel.send('不要欺負{} <:dedene5:661231368864530434>'.format(userName_get))
                            continue   
                        if int(userPoints_get) > 10 and points_ChangedStatus == '-':
                            await msg.channel.send('減這麼多分，你484偷偷喜歡{}'.format(userName_get))
                            continue
                        if userName_get in user_dict:
                            print('db編號: ' + user_dict[userName_get]+' get!')
                            sql = "SELECT * FROM users WHERE users_id = '{}'".format(user_dict[userName_get])
                            cursor = self.query(sql)
                            #cursor.execute('SELECT * FROM users WHERE users_id = %s',user_dict[userName_get])
                            result = cursor.fetchall()
                            current_UserPoints = result[0][1]
                            print('目前計分: {}'.format(current_UserPoints))
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
                            sql = 'UPDATE users SET user_points = {} WHERE users_id = {}'.format(new_UserPoints, user_dict[userName_get])
                            cursor = self.query(sql)
                            self.mydb.commit()
                            msg_toSend = '{}{} (原本計分: {} // 目前計分: {})'.format(userName_get,countingPattern.group(3),current_UserPoints,new_UserPoints)
                            print('{}{} (原本計分: {} // 目前計分: {})'.format(userName_get,countingPattern.group(3),current_UserPoints,new_UserPoints))
                            await msg.channel.send(msg_toSend)
                        else:
                            print("fail!")
                            await msg.channel.send('沒抓到綽號,請換一個試試')

                    ##########################顯示目前分數#####################################
                    if(showPoints and msg.author != self.bot.user and tmp == 0):
                        tmp = tmp + 1
                        #print('整句: ' + showPoints.group(0))   #整句
                        #print('得到id: ' + showPoints.group(2))   #得到id
                        userName_get = [k for k, v in user_nName.items() if v == nameList][0]
                        #cursor = mydb.cursor()
                        #cursor.execute('SELECT * FROM users WHERE users_id = %s',user_dict[userName_get])
                        sql = "SELECT * FROM users WHERE users_id = '{}'".format(user_dict[userName_get])
                        cursor = self.query(sql)
                        result = cursor.fetchall()
                        current_UserPoints = result[0][1]
                        msg_toSend = '{}(累積計分: {})'.format(userName_get,current_UserPoints)
                        print('{}(累積計分: {})'.format(userName_get,current_UserPoints))
                        await msg.channel.send(msg_toSend)
                    
                    ##########################重置分數#########################################
                    #if(resetPoints and msg.author != self.bot.user and tmp == 0):
                    #    tmp = tmp + 1
                    #    #print('整句: ' + resetPoints.group(0))   #整句
                        #print('得到id: ' + resetPoints.group(2))   #得到id
                        #userName_get = resetPoints.group(2)
                    #    userName_get = [k for k, v in user_nName.items() if v == nameList][0]
                    #    cursor = mydb.cursor()
                    #    cursor.execute('SELECT * FROM users WHERE users_id = %s',user_dict[userName_get])
                    #    result = cursor.fetchall()
                    #    current_UserPoints = result[0][1]
                    #    new_UserPoints = '0'
                    #    sql = 'UPDATE users SET user_points = {} WHERE users_id = {}'.format(new_UserPoints, user_dict[userName_get])
                    #    cursor.execute(sql)
                    #    mydb.commit()
                    #    msg_toSend = '已重置 {} 的分數(累積計分: {})'.format(userName_get,new_UserPoints)
                    #    await msg.channel.send(msg_toSend)

                    ##########################組隊顯示分數#####################################
                    if(organizeBoard and msg.author != self.bot.user and tmp == 0 and msg.channel != channel_TextLobby):
                        tmp = tmp + 1
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
                                sql = "SELECT * FROM users WHERE users_id = '{}'".format(user_dict[id_])
                                #cursor.execute('SELECT * FROM users WHERE users_id = %s',user_dict[id_])
                                cursor = self.query(sql)
                                result = cursor.fetchall()
                                current_usersPoints.append(result[0][1])
                                n=n+1
                            else:
                                await msg.channel.send('有人的名字打錯囉！')
                                continue
                        if len(current_usersPoints) == 4:
                            embed=discord.Embed(title='記分板', color=0x0080c0)
                            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/576863956879015983/642711388162228225/WorrySurrounded.gif')
                            embed.add_field(name=organizeBoard.group(2), value=current_usersPoints[0], inline=True)
                            embed.add_field(name=organizeBoard.group(3), value=current_usersPoints[1], inline=True)
                            embed.add_field(name=organizeBoard.group(4), value=current_usersPoints[2], inline=True)
                            embed.add_field(name=organizeBoard.group(5), value=current_usersPoints[3], inline=True)
                            await msg.channel.send(embed=embed)
                            #await msg.channel.send('{}: {}分\n{}: {}分\n{}: {}分\n{}: {}分'.format(organizeBoard.group(2),current_usersPoints[0],organizeBoard.group(3),current_usersPoints[1],organizeBoard.group(4),current_usersPoints[2],organizeBoard.group(5),current_usersPoints[3]))
                            print('記分板: {}'.format(dict(zip(usersName_get,current_usersPoints))))                







def setup(bot):
    bot.add_cog(Lilipoints(bot))
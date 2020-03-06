import asyncio
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import time
import os
import re
from selenium import webdriver
from bs4 import BeautifulSoup
import pymysql
pymysql.install_as_MySQLdb()

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=chrome_options)
class NewsPush(Cog_Extension):
    @commands.Cog.listener()
    async def on_ready(self):
        dateRange = []
        info = []
        char_1 = []
        char_2 = []
        char_3 = []
        pnts = []
        typess = ''
        status = "有新資料"
        channel_Num = int(os.environ.get('CHANNEL_NEWSBOARD_FROM_4700'))
        while True:
            self.connect()
            channel_newsBoard = self.bot.get_channel(channel_Num)
            full_result = await self.crawler()
            for resultF in full_result:
                if resultF is not None:
                    info = resultF[0]
                    char_1 = resultF[1]
                    char_2 = resultF[2]
                    char_3 = resultF[4]
                    pnts = [char_1,char_2,char_3]
                    dateRange = resultF[3]
                    typess = resultF[5]
                if typess == '開始舉辦' or typess == '':
                    continue
                for pnt in pnts:
                    if len(pnt) == 20:
                        embed=discord.Embed(title="{} ~ {}".format(dateRange[0],dateRange[1]), url=info[2], description=pnt[19])
                        embed.set_author(name=info[0], url=info[2])
                        embed.set_image(url=pnt[0])
                        #embed.set_thumbnail(url=char_1[0])
                        embed.add_field(name="Lv.", value=pnt[2], inline=True)
                        embed.add_field(name="HP.", value=pnt[4], inline=True)
                        embed.add_field(name="ATK.", value=pnt[6], inline=True)
                        embed.add_field(name="EX", value=pnt[9], inline=False)
                        embed.add_field(name="S1.{}".format(pnt[7]), value=pnt[13], inline=False)
                        embed.add_field(name="S2.{}".format(pnt[8]), value=pnt[14], inline=False)
                        embed.add_field(name="被動1.{}".format(pnt[10]), value=pnt[16], inline=False)
                        embed.add_field(name="被動2.{}".format(pnt[11]), value=pnt[17], inline=False)
                        embed.add_field(name="被動3.{}".format(pnt[12]), value=pnt[18], inline=False)
                        embed.set_image(url=pnt[0])
                        await channel_newsBoard.send(embed=embed)
                    if len(pnt) == 12:
                        embed=discord.Embed(title="{} ~ {}".format(dateRange[0],dateRange[1]), url=info[2], description=pnt[11])
                        embed.set_author(name=info[0], url=info[2])
                        embed.set_image(url=pnt[0])
                        #embed.set_thumbnail(url=char_1[0])
                        embed.add_field(name="Lv.", value=pnt[2], inline=True)
                        embed.add_field(name="HP.", value=pnt[4], inline=True)
                        embed.add_field(name="ATK.", value=pnt[6], inline=True)
                        embed.add_field(name="主動技能.{}".format(pnt[7]), value=pnt[9], inline=False)
                        embed.add_field(name="被動.{}".format(pnt[8]), value=pnt[10], inline=False)
                        embed.set_image(url=pnt[0])
                        await channel_newsBoard.send(embed=embed)
                    if len(pnt) == 14:
                        embed=discord.Embed(title="{} ~ {}".format(dateRange[0],dateRange[1]), url=info[2], description=pnt[13])
                        embed.set_author(name=info[0], url=info[2])
                        embed.set_image(url=pnt[0])
                        #embed.set_thumbnail(url=char_1[0])
                        embed.add_field(name="Lv.", value=pnt[2], inline=True)
                        embed.add_field(name="HP.", value=pnt[4], inline=True)
                        embed.add_field(name="ATK.", value=pnt[6], inline=True)
                        embed.add_field(name="主動技能.{}".format(pnt[7]), value=pnt[10], inline=False)
                        embed.add_field(name="被動1.{}".format(pnt[8]), value=pnt[11], inline=False)
                        embed.add_field(name="被動2.{}".format(pnt[9]), value=pnt[12], inline=False)
                        embed.set_image(url=pnt[0])
                        await channel_newsBoard.send(embed=embed)

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
        self.mydb.commit()
        return cursor

    async def crawler(self):
        #緩衝時間
        await asyncio.sleep(2)

        #default set-up
        dateRange = []
        info = []
        char_1 = []
        char_2 = []
        char_3 = []
        cnt = 0
        info = []
        types = ''
        status = "有新資料"
        channel_lobby_Num = int(os.environ.get('CHANNEL_LOBBY_FROM_4700'))
        channel_lobby = self.bot.get_channel(channel_lobby_Num)
        path_ = 'https://dragalialost.com/cht/news/information/'
        driver.get(path_)
        await asyncio.sleep(5)
        soup = BeautifulSoup(driver.page_source,'lxml')
        '''  
        開始爬蟲
        #cnt作用為定位
        #regex的group(2)拿取舉辦公告/開始舉辦區分卡池是否進行中,
         舉辦公告先行爬蟲並po相關資料至dc並於大廳告知,
         開始舉辦不進行爬蟲但會於dc大廳公告卡池已開始進行

        #TODO:cnt整合info改為dict:關聯性,可減少cnt,cnt1這類的變數宣告,直接用key-value形式獲取相應位置 ex.{2:'卡池title',3:'維護公告'}
        '''

        sixResult = []

        for i in soup.select('li a p.title'):
            #reset default set-up
            #driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=chrome_options)
            dateRange = []
            info = []
            char_1 = []
            char_2 = []
            char_3 = []
            info = []
            types = ''
            status = "有新資料"
            channel_lobby_Num = int(os.environ.get('CHANNEL_LOBBY_FROM_4700'))
            channel_lobby = self.bot.get_channel(channel_lobby_Num)
            path_ = 'https://dragalialost.com/cht/news/information/'
            driver.get(path_)
            await asyncio.sleep(5)
            soup = BeautifulSoup(driver.page_source,'lxml')

            #獲取公告標題
            texts = i.text.strip()
            info.append(texts)

            #獲取公告日期
            n=0
            for data in soup.select('li a div.time'):
                if n == cnt:
                    info.append(data.text.split('公告')[0].strip())
                n=n+1
            
            #爬取相應標題網址以及編號
            cnt1 = 0
            for i in soup.select('div ul#news-list li a'):
                if cnt1 == cnt:
                    path_ = 'https://dragalialost.com' + i.get('href')
                    info.append(path_)
                    tmp = path_.split('/')
                    info.append(tmp[len(tmp)-1])
                cnt1 = cnt1 +1

            #判斷是否是卡池公告
            group1 = re.search(r'(失落龍絆日|傳說召喚|精選召喚).*(舉辦公告|開始舉辦)',texts)
            if group1:
                types = group1.group(2) #用舉辦公告/開始舉辦區分

                #網址導向卡池頁面內
                ###測試用driver.get('https://dragalialost.com/cht/news/detail/935')
                print('info = {}'.format(info))
                driver.get(path_) #info[2]
                await asyncio.sleep(3)
                soup = BeautifulSoup(driver.page_source,'lxml')

                #獲取卡池開始及結束時間
                dateRange = []
                for date in soup.select('div span.local_date'):
                    if date.text not in dateRange:
                        dateRange.append(date.text)
                dateRange

                #檢驗卡池是否已存在於資料庫(已爬過)
                #TODO:local -> mysql 改為 local -> redis -> mysql , 提升處理速率 , 減少伺服器負荷
                #cons:可能會導致內存使用量增高不少 , 不確定heroku免費額度夠不夠
                print("開始檢驗是否重複")
                try:
                    titleName = info[0]
                    titleTimeStart = dateRange[0]
                    titleTimeEnd = dateRange[1]
                except:
                    titleName = ''
                    titleTimeStart = ''
                    titleTimeEnd = ''
                sql = "SELECT titleName FROM titletable WHERE titleName = '{}'".format(titleName)
                cursor = self.query(sql)
                result = cursor.fetchall()


                print("抓到資料庫中的 titleName = {}".format(result))
                if result is not None:
                    try:
                        result = "".join(result[0])
                        print("抓到資料庫中的 titleName(after join) = {}".format(result))
                        result = result.split('\'')[0]
                    except:
                        pass
                    sql = "SELECT titleTimeStart FROM titletable WHERE titleName = '{}'".format(titleName)
                    cursor = self.query(sql)
                    resultTime = cursor.fetchall()

                    if resultTime is not None:
                        try:
                            resultTime = "".join(resultTime[0])
                            print("抓到資料庫中的 titleTimeStart(after join) = {}".format(resultTime))
                            resultTime = resultTime.split('\'')[0]
                        except:
                            resultTime = ''

                    print("抓到資料庫中的 titleTimeStart = '{}', 目前現有的 dateRange[0] = '{}', 開始進行比對".format(resultTime,titleTimeStart))
                    if resultTime == titleTimeStart:
                        print("已存在資料庫 , 不進行爬蟲 , 等待 5 秒後略過")
                        await asyncio.sleep(5)
                        print("正在前往下一個標題")
                        status = "無新資料"

                if status == "有新資料":
                    #目前最多支援三隻角色
                    print("From NewsPush.py : 已爬到卡池資訊,未重複,開始爬資料")
                    sql = "INSERT INTO titletable (titleName,titleTimeStart,titleTimeEnd) VALUE ('{}','{}','{}')".format(titleName,titleTimeStart,titleTimeEnd)
                    cursor = self.query(sql)

                    charskillTitle_1 = []
                    charskillTitle_2 = []
                    charskillTitle_3 = []
                    tmp = 0
                    #技能&被動名稱
                    for skillTitle in soup.select('dl dt span'):
                        if skillTitle.text.strip() != '':
                            if tmp < 6 :
                                charskillTitle_1.append(skillTitle.text.strip())
                            elif tmp < 12:
                                charskillTitle_2.append(skillTitle.text.strip())
                            else:
                                charskillTitle_3.append(skillTitle.text.strip())
                            tmp = tmp +1

                    skillExAbility_1 = []
                    skillExAbility_2 = []
                    skillExAbility_3 = []
                    tmp = 0
                    #技能&ex&被動描述
                    for skillParam in soup.select('dl dd div'):
                        if tmp < 6 :
                            skillExAbility_1.append(skillParam.text.strip())
                        elif tmp < 12:
                            skillExAbility_2.append(skillParam.text.strip())
                        else:
                            skillExAbility_3.append(skillParam.text.strip())
                        tmp = tmp +1

                    charLv_1 = []
                    charLv_2 = []
                    charLv_3 = []
                    tmp = 0
                    #等級
                    for lv in soup.select('div ul li.lv'):
                        a = lv.text.split('\n')[1]
                        b = lv.text.split('\n')[2]
                        if tmp <1 :
                            charLv_1.append(a)
                            charLv_1.append(b)
                        elif tmp == 1:
                            charLv_2.append(a)
                            charLv_2.append(b)
                        else:
                            charLv_3.append(a)
                            charLv_3.append(b)
                        tmp = tmp +1

                    charHp_1 = []
                    charHp_2 = []
                    charHp_3 = []
                    tmp = 0
                    #hp
                    for hp in soup.select('div ul li.hp'):
                        a = hp.text.split('\n')[1]
                        b = hp.text.split('\n')[2]
                        if tmp <1 :
                            charHp_1.append(a)
                            charHp_1.append(b)
                        elif tmp ==1:
                            charHp_2.append(a)
                            charHp_2.append(b)
                        else:
                            charHp_3.append(a)
                            charHp_3.append(b)
                        tmp = tmp +1

                    charAtk_1 = []
                    charAtk_2 = []
                    charAtk_3 = []
                    tmp = 0
                    #atk
                    for atk in soup.select('div ul li.atk'):
                        a = atk.text.split('\n')[1]
                        b = atk.text.split('\n')[2]
                        if tmp <1 :
                            charAtk_1.append(a)
                            charAtk_1.append(b)
                        elif tmp == 1:
                            charAtk_2.append(a)
                            charAtk_2.append(b)
                        else:
                            charAtk_3.append(a)
                            charAtk_3.append(b)
                        tmp = tmp +1

                    charParam_1 = []
                    charParam_2 = []
                    charParam_3 = []
                    tmp = 0
                    #角色介紹
                    for charParam in soup.select('div section div div div div div div.param ul li'):
                        if tmp <1:
                            charParam_1.append(charParam.text.strip())
                        elif tmp == 1:
                            charParam_2.append(charParam.text.strip())
                        else:
                            charParam_3.append(charParam.text.strip())
                        tmp = tmp +1

                    charPhoto_1 = []
                    charPhoto_2 = []
                    charPhoto_3 = []
                    tmp = 0
                    #角色圖片
                    for photo in soup.select('div.mainImage img'):
                        if tmp < 1:
                            charPhoto_1.append(photo.get('src'))
                        elif tmp ==1:
                            charPhoto_2.append(photo.get('src'))
                        else:
                            charPhoto_3.append(photo.get('src'))
                        tmp = tmp +1

                    #關閉webdriver
                    #driver.close()

                    print(charPhoto_1)
                    print(charPhoto_2)
                    print(charPhoto_3)

                    #資料處理 & 彙整
                    all_Status_1 = [charPhoto_1,charLv_1,charHp_1,charAtk_1,charskillTitle_1,skillExAbility_1,charParam_1]
                    all_Status_2 = [charPhoto_2,charLv_2,charHp_2,charAtk_2,charskillTitle_2,skillExAbility_2,charParam_2]
                    all_Status_3 = [charPhoto_3,charLv_3,charHp_3,charAtk_3,charskillTitle_3,skillExAbility_3,charParam_3]
                    tmp_all = [all_Status_1,all_Status_2,all_Status_3]

                    #將tmp_all內資料彙整放入tmp_final
                    char_1 = []
                    char_2 = []
                    char_3 = []
                    tmp_final = [char_1,char_2,char_3]
                    n=0
                    for i in tmp_all:
                        for q in i:
                            for p in q:
                                tmp_final[n].append(p)
                        n=n+1

                    #2019/11/12 14:00  example
                    #傳說召喚「太糟糕啦☆愛之火☆乘車襲來」舉辦公告  example
                    print(info,'\n')
                    print(dateRange,'\n')
                    print(char_1,'\n\n')
                    print(char_2,'\n\n')
                    print(char_3,'\n\n')
                    pnts = [char_1,char_2,char_3]

                    #print結果皆會show在heroku.log , 故不另寫log.py
                    print('角色照片:{}'.format(char_1[0]))
                    print('角色介紹.{}'.format(char_1[19]))
                    print('Lv.{}'.format(char_1[2]))
                    print('HP.{}'.format(char_1[4]))
                    print('ATK.{}'.format(char_1[6]))
                    print('S1.{}'.format(char_1[7]))
                    print('S1效果.{}'.format(char_1[13]))
                    print('S2.{}'.format(char_1[8]))
                    print('S2效果.{}'.format(char_1[14]))
                    print('EX.{}'.format(char_1[9]))
                    print('EX效果.{}'.format(char_1[15]))
                    print('被動1.{}'.format(char_1[10]))
                    print('被動1效果.{}'.format(char_1[16]))
                    print('被動2.{}'.format(char_1[11]))
                    print('被動2效果.{}'.format(char_1[17]))
                    print('被動3.{}'.format(char_1[12]))
                    print('被動3效果.{}'.format(char_1[18]))

                    resultF = [info,char_1,char_2,dateRange,char_3,types]
                    if types == '開始舉辦':
                        await channel_lobby.send('{}！相關卡池資訊已經po到更新資訊區了，歡迎查看！'.format(info[0]))
                    if types == '舉辦公告':
                        await channel_lobby.send('{}！相關卡池資訊可於更新資訊區查看！'.format(info[0]))
                    sixResult.append(resultF)
            else:
                #非卡池公告處理
                #關閉webdriver
                #driver.close()
                #網址導向卡池頁面內
                ###測試用driver.get('https://dragalialost.com/cht/news/detail/935')
                print('info = {}'.format(info))

                #檢驗卡池是否已存在於資料庫(已爬過)
                #TODO:local -> mysql 改為 local -> redis -> mysql , 提升處理速率 , 減少伺服器負荷
                #cons:可能會導致內存使用量增高不少 , 不確定heroku免費額度夠不夠
                print("開始檢驗是否重複")
                try:
                    titleName = info[0]
                    titleTimeStart = info[1]
                    titleTimeEnd = titleTimeStart
                except:
                    titleName = ''
                    titleTimeStart = ''
                    titleTimeEnd = ''
                sql = "SELECT titleName FROM titletable WHERE titleName = '{}'".format(info[0])
                cursor = self.query(sql)
                result = cursor.fetchall()


                print("抓到資料庫中的 titleName = {}".format(result))
                if result is not None:
                    try:
                        result = "".join(result[0])
                        print("抓到資料庫中的 titleName(after join) = {}".format(result))
                        result = result.split('\'')[0]
                    except:
                        result = ''

                    print("抓到資料庫中的 titleName = '{}', 目前現有的 titleName = '{}', 開始進行比對".format(result,titleName))
                    if result == info[0]:
                        print("已存在資料庫 , 不進行爬蟲 , 等待 5 秒後略過")
                        await asyncio.sleep(5)
                        print("正在前往下一個標題")
                        status = "無新資料"

                if status == "有新資料":
                    
                    sql = "INSERT INTO titletable (titleName,titleTimeStart,titleTimeEnd) VALUE ('{}','{}','{}')".format(info[0],info[1],info[1])
                    cursor = self.query(sql)
                    channel_news_num = int(os.environ.get('CHANNEL_NEWS_FROM_4700'))
                    channel_news_storage = self.bot.get_channel(channel_news_num)
                    #目前最多支援三隻角色
                    #await channel_lobby.send('『公告』{title} 於 {dt} 發佈在官網囉！\r\n網址已同步發佈至『news』頻道'.format(title=info[0], dt=info[1]))
                    await channel_news_storage.send('『公告』{title} 於 {dt} 發佈在官網囉！\r\n{url}'.format(title=info[0], dt=info[1], url=info[2]))
 
            cnt = cnt +1

        return sixResult

        

def setup(bot):
    bot.add_cog(NewsPush(bot))

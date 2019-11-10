import re
import os
import pymysql
pymysql.install_as_MySQLdb()

mydb = pymysql.connect(
    host='localhost',
    user='root',
    passwd='4510',
    db='userpoints'
)

user_id1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,
31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,
46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,
61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,
76,77,78,79,80]
user_dict={'齊木':'1','黑貓':'2','yoyo':'3','盆栽':'4','咲夜':'5','火花':'6','蟑螂':'7','變態':'8','三寶':'9','香香':'10','幕容':'11','木子':'12','小白':'13','月海':'14','草哥':'15','四月':'16','dula':'17','可魯':'18','卡打':'19','lza':'20','月月':'21','somes':'22','wewa':'23','亡音':'24','夏音':'25','奧迪':'26','鱈魚':'27','kk':'28','voc':'29','恰恰':'30','腐貓':'31','詩詩':'32','那歐':'33','霜降':'34','peco':'35','女僕丸':'36','max':'37','岡田':'38','松浦':'39','sky':'40','maple':'41','海瀨':'42','米國':'43','滑水':'44','zz':'45'}
#user_nName=[['齊木黑昀','齊ㄇ'],['黒猫','黑貓','黒貓'],['null'],['盤栽'],['消夜','宵夜','笑夜'],['泡泡雞','雷鷹','ㄆㄆ雞','泡雞'],['壞壞蟑螂'],['null'],['3寶','ㄌㄌㄎ','yutami'],['今天不行了','ㄌㄌㄎ'],['慕蓉','慕容','幕蓉'],['null'],['白白雞','白白'],['粵海','倉鼠'],['草尼馬','草尼瑪','草泥瑪','草泥馬'],['april','apr','4月'],['賭拉','杜拉','肚拉','度拉'],['fly'],['katar','卡達'],['版主'],['moon'],['null'],['null'],['亡88','音88','亡爸爸','音爸爸'],['導遊'],['null'],['雪魚'],['null'],['null'],['chacha'],['null'],['國軍'],['nao'],['ㄌㄌㄎ'],['佩扣','佩口','珮口','珮扣'],['妹斗','妹抖'],['null'],['二號','2號'],['一號','1號'],['null'],['null'],['null'],['null'],['null'],['莉莉']]
user_nName={'齊木':['齊木','齊ㄇ'],'黑貓':['黑貓','黒猫','黑貓','黒貓'],'yoyo':['yoyo'],'盆栽':['盤栽','盆栽'],'咲夜':['咲夜','消夜','宵夜','笑夜'],'火花':['火花','泡泡雞','雷鷹','ㄆㄆ雞','泡雞'],'蟑螂':['壞壞蟑螂','蟑螂'],'變態':['變態'],'三寶':['三寶','3寶','ㄌㄌㄎ','yutami'],'香香':['香香','今天不行了','ㄌㄌㄎ'],'幕容':['幕容','慕蓉','慕容','幕蓉'],'木子':['木子'],'小白':['小白','白白雞','白白'],'月海':['月海','粵海','倉鼠'],'草哥':['草哥','草尼馬','草尼瑪','草泥瑪','草泥馬'],'四月':['四月','april','apr','4月'],'dula':['dula','賭拉','杜拉','肚拉','度拉'],'可魯':['可魯','fly'],'卡打':['卡打','katar','卡達'],'lza':['lza','版主'],'月月':['moon','月月'],'somes':['somes'],'wewa':['wewa'],'亡音':['亡音','亡88','音88','亡爸爸','音爸爸'],'夏音':['夏音','導遊'],'奧迪':['奧迪'],'鱈魚':['鱈魚','雪魚'],'kk':['kk'],'voc':['voc'],'恰恰':['恰恰','chacha'],'腐貓':['腐貓'],'詩詩':['詩詩','國軍'],'那歐':['那歐','nao'],'霜降':['霜降','ㄌㄌㄎ'],'peco':['peco','佩扣','佩口','珮口','珮扣'],'女僕丸':['女僕丸','妹斗','妹抖'],'max':['max'],'岡田':['岡田','二號','2號'],'松浦':['松浦','一號','1號'],'sky':['sky'],'maple':['maple'],'海瀨':['海瀨'],'米國':['米國'],'滑水':['滑水'],'zz':['zz','莉莉']}
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
m1 = ''
print('{}{}'.format(user_nName1,user_dDbId))
s = '但是莉莉還是要-100'   #on_message測試
print(user_name[1])
tmp = 0
for name in user_name:
    for nameList in user_nName1:
        for personList in nameList:
            m1 = re.search(r'^.*(({}).*((\+|\-)(\d+))(?!.*(劍|法|補|槍|短|刀|斧|弓))).*$'.format(personList), s)  #regex 
            if(m1 and tmp == 0):
                tmp = tmp + 1
                print([k for k, v in user_nName.items() if v == nameList][0])
                print('整句: ' + m1.group(0))   #整句
                #print('從id開始到最後: ' + m1.group(1))  #從id開始到最後
                print('得到id: ' + m1.group(2))   #得到id
                #userName_get = m1.group(2)    #抓取開頭兩字得到name
                userName_get = [k for k, v in user_nName.items() if v == nameList][0]
                #print('分數加分/減分全部: ' + m1.group(3))
                points_ChangedStatus = m1.group(4)   #分數加分/減分
                print('分數加分/減分: ' + points_ChangedStatus)
                userPoints_get = m1.group(5)  #得到分數變化,存進pnt_get
                print('分數變化: ' + userPoints_get)
                if userName_get in user_dict:
                    #print(user_dict[userName_get]+' get!')
                    print('目標: ' + userName_get + '\n分數變化: ' + m1.group(3) + '\nDB編號: ' + user_dict[userName_get])
                    cursor = mydb.cursor()
                    cursor.execute('SELECT * FROM users WHERE user_id = %s',user_dict[userName_get])
                    result = cursor.fetchall()
                    current_UserPoints = result[0][1]
                    print('原本db分數: ' + (str)(current_UserPoints))
                    if points_ChangedStatus == '+':
                        new_UserPoints = str(current_UserPoints + (int)(userPoints_get))
                    if points_ChangedStatus == '-':
                        new_UserPoints = str(current_UserPoints - (int)(userPoints_get))
                    #sql = 'UPDATE users SET user_points = {} WHERE user_id = {}'.format(new_UserPoints, user_dict[userName_get])
                    #cursor.execute(sql)
                    #mydb.commit()
                    print('目前db分數: ' + (str)(new_UserPoints))
                else:
                    print("fail!")
                continue
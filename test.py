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
user_dict={'測試':'0','齊木':'1','黑貓':'2','yoyo':'3','盆栽':'4','咲夜':'5','火花':'6','蟑螂':'7','變態':'8','三寶':'9','香香':'10','幕容':'11','木子':'12','小白':'13','月海':'14','草哥':'15','四月':'16','dula':'17','可魯':'18','卡打':'19','lza':'20','月月':'21','somes':'22','wewa':'23','亡音':'24','夏音':'25','奧迪':'26','鱈魚':'27','kk':'28','voc':'29','恰恰':'30','腐貓':'31','詩詩':'32','那歐':'33','霜降':'34','peco':'35','女僕丸':'36'}
user_name =[]
user_dbId=[]
abc = '火花'
print(abc.lower())
for key, value in user_dict.items():   #dict轉list
    user_name.append(key)
    user_dbId.append(value)
s = '但是火花還是要-100'   #on_message測試
print(user_name[1])
for name in user_name:
    m1 = re.search(r'^.*(({}).*((\+|\-)(\d+))(?!.*(劍|法|補|槍|短|刀|斧|弓))).*$'.format(name), s)  #regex 
    if(m1):
        print('整句: ' + m1.group(0))   #整句
        #print('從id開始到最後: ' + m1.group(1))  #從id開始到最後
        print('得到id: ' + m1.group(2))   #得到id
        userName_get = m1.group(2)    #抓取開頭兩字得到name
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
            sql = 'UPDATE users SET user_points = {} WHERE user_id = {}'.format(new_UserPoints, user_dict[userName_get])
            cursor.execute(sql)
            mydb.commit()
            print('目前db分數: ' + (str)(new_UserPoints))
        else:
            print("fail!")
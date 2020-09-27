from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re
driver = webdriver.Chrome('./chromedriver')
driver.get('https://dragalialost.com/cht/news/information/')
time.sleep(5)
soup = BeautifulSoup(driver.page_source,'lxml')
#p =driver.find_element_by_id('news-list')
cnt = 0
info = []
for i in soup.select('li a p.title'):
    texts = i.text.strip()
    print(texts)
    group1 = re.search(r'(失落龍絆日|傳說召喚|精選召喚)',texts)
    if group1:
        p=texts
        info.append(p)
        break
    cnt = cnt +1
n=0
for data in soup.select('li a div.time'):
    #if(n>=2):
    #    break
    if n == cnt:
        info.append(data.text.split('公告')[0].strip())
    n=n+1
print(info)
cnt1 = 0
for i in soup.select('div ul#news-list li a'):
    #print(i.get('href'))
    if cnt1 == cnt:
        path_ = 'https://dragalialost.com' + i.get('href')
        info.append(path_)
        tmp = path_.split('/')
        info.append(tmp[len(tmp)-1])
        break
    cnt1 = cnt1 +1
print(info)
#path_ = 'https://dragalialost.com' + soup.select_one('div ul#news-list li a').get('href')
#info.append(path_)
#tmp = path_.split('/')
#info.append(tmp[len(tmp)-1])
#info
#driver.get('https://dragalialost.com/cht/news/detail/892')
driver.get(info[2])
time.sleep(3)
soup = BeautifulSoup(driver.page_source,'lxml')
dateRange = []
for date in soup.select('div span.local_date'):
    if date.text not in dateRange:
        dateRange.append(date.text)
dateRange
charskillTitle_1 = []
charskillTitle_2 = []
tmp = 0
for skillTitle in soup.select('dl dt span'):  #技能&被動名稱
    if skillTitle.text.strip() != '':
        if tmp < 6 :
            charskillTitle_1.append(skillTitle.text.strip())
        else:
            charskillTitle_2.append(skillTitle.text.strip())
        tmp = tmp +1
    #print(skillParam.text.strip())
print(charskillTitle_1)
print(charskillTitle_2)
print('\n\n')

skillExAbility_1 = []
skillExAbility_2 = []
tmp = 0
for skillParam in soup.select('dl dd div'):   #技能&ex&被動描述
    if tmp < 6 :
        skillExAbility_1.append(skillParam.text.strip())
    else:
        skillExAbility_2.append(skillParam.text.strip())
    tmp = tmp +1
    #print(skillParam.text.strip())
print(skillExAbility_1)
print(skillExAbility_2)
print('\n\n')

charLv_1 = []
charLv_2 = []
tmp = 0
for lv in soup.select('div ul li.lv'):        #等級
    a = lv.text.split('\n')[1]
    b = lv.text.split('\n')[2]
    if tmp <1 :
        charLv_1.append(a)
        charLv_1.append(b)
    else:
        charLv_2.append(a)
        charLv_2.append(b)
    tmp = tmp +1
    #print(lv.text.strip())
print(charLv_1)
print(charLv_1)
print('\n\n')

charHp_1 = []
charHp_2 = []
tmp = 0
for hp in soup.select('div ul li.hp'):        #hp
    a = hp.text.split('\n')[1]
    b = hp.text.split('\n')[2]
    if tmp <1 :
        charHp_1.append(a)
        charHp_1.append(b)
    else:
        charHp_2.append(a)
        charHp_2.append(b)
    tmp = tmp +1
    #print(hp.text.strip())
print(charHp_1)
print(charHp_2)
print('\n\n')

charAtk_1 = []
charAtk_2 = []
tmp = 0
for atk in soup.select('div ul li.atk'):        #atk
    a = atk.text.split('\n')[1]
    b = atk.text.split('\n')[2]
    if tmp <1 :
        charAtk_1.append(a)
        charAtk_1.append(b)
    else:
        charAtk_2.append(a)
        charAtk_2.append(b)
    tmp = tmp +1
    #print(hp.text.strip())
print(charAtk_1)
print(charAtk_2)
print('\n\n')

charParam_1 = []
charParam_2 = []
tmp = 0
for charParam in soup.select('div section div div div div div div.param ul li'): #角色介紹
    if tmp <1:
        charParam_1.append(charParam.text.strip())
    else:
        charParam_2.append(charParam.text.strip())
    tmp = tmp +1
print(charParam_1)
print(charParam_2)
print('\n\n')

charPhoto_1 = []
charPhoto_2 = []
tmp = 0
for photo in soup.select('div.mainImage img'):
    if tmp < 1:
        charPhoto_1.append(photo.get('src'))
    else:
        charPhoto_2.append(photo.get('src'))
    tmp = tmp +1
print(charPhoto_1)
print(charPhoto_2)

all_Status_1 = [charPhoto_1,charLv_1,charHp_1,charAtk_1,charskillTitle_1,skillExAbility_1,charParam_1]
all_Status_2 = [charPhoto_2,charLv_2,charHp_2,charAtk_2,charskillTitle_2,skillExAbility_2,charParam_2]
tmp_all = [all_Status_1,all_Status_2]
char_1 = []
char_2 = []
tmp_final = [char_1,char_2]
n=0
for i in tmp_all:
    for q in i:
        for p in q:
            tmp_final[n].append(p)
            #print(p)
    n=n+1
#2019/11/12 14:00
#傳說召喚「太糟糕啦☆愛之火☆乘車襲來」舉辦公告
print(info,'\n')
print(dateRange,'\n')
print(char_1,'\n\n')
print(char_2,'\n\n')

print('角色照片:{}\n'.format(char_1[0]))
print('角色介紹.{}\n'.format(char_1[19]))
print('Lv.{}\n'.format(char_1[2]))
print('HP.{}\n'.format(char_1[4]))
print('ATK.{}\n'.format(char_1[6]))
print('S1.{}\n'.format(char_1[7]))
print('S1效果.{}\n'.format(char_1[13]))
print('S2.{}\n'.format(char_1[8]))
print('S2效果.{}\n'.format(char_1[14]))
print('EX.{}\n'.format(char_1[9]))
print('EX效果.{}\n'.format(char_1[15]))
print('被動1.{}\n'.format(char_1[10]))
print('被動1效果.{}\n'.format(char_1[16]))
print('被動2.{}\n'.format(char_1[11]))
print('被動2效果.{}\n'.format(char_1[17]))
print('被動3.{}\n'.format(char_1[12]))
print('被動3效果.{}\n'.format(char_1[18]))

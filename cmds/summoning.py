# -*- coding: UTF-8 -*-
import time
import os
import re
import random

class Summoning():
    folder_dict = {u'精選_1':'mcrree',u'精選_2':'krlu',u'五星':['mikoto','ejlit'],u'五星龍':['5StarDragon1','5StarDragon2']}
    up_Char1 = 'asd'
    up_Char2 = 'asd2'
    #初始機率 4%
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

    #if m1.group(1) and m1.group(2):  
    #    case1 which like 'tenfold 2 times','singlefold 4 times'
	#    continue
    #elif m1.group(1):
    #    case2 which like 'tenfold','singlefold'
	#    continue
    #elif m1.group(2):
    #    case3 which like '99 times','summon until get pu5*'
	#    continue
    ###  >>>   (10[連抽]|十[連抽]|[單一]抽)?(\d?\d?\d|抽到有)?[連次抽]?    <<<   11/27
    
    while True:
        inputs = input('plz typing after this: ')
        #a = re.search('^(?:.*(十連|單抽|一次))(?:.*(十連|單抽|(([一二兩三四五六七八九十]|(\d+))次|發|抽到有)))[^嗎]?.*$',inputs)
        b = re.search('\$抽\s(\d?\d?\d)',inputs)   #testing pattern

        print('group0: ',b.group(1))
        summon_Times = int(b.group(1))
        tenFold_Count = int(round(summon_Times/10,0))
        oneShot_Count = summon_Times%10
        ran_Num = random.random() * 1000
        summonNum = tenFold_Count * 10 + oneShot_Count
        controlTrigger = 0
        counts = 0
        for rounds in range(0,summonNum):
            ran_Num = round(random.random() * 100,3)
            if ran_Num <= five_Star_1:
                print(ran_Num,' ',folder_dict['精選_1'])
                controlTrigger = 1
            elif ran_Num <= five_Star_2:
                print(ran_Num,' ',folder_dict['精選_2'])
                controlTrigger = 1
            elif ran_Num <= five_Star_3:
                print(ran_Num,' ',folder_dict['五星'][random.randint(0,1)])
                controlTrigger = 1
            elif ran_Num <= five_Star_4:
                print(ran_Num,' ',folder_dict['五星龍'][random.randint(0,1)])
                controlTrigger = 1
            else:
                print(ran_Num,' ','nothing')
                if counts % 10 == 0:
                    five_Star_1 = five_Star_1 + five_Star_1_fail
                    five_Star_2 = five_Star_2 + five_Star_2_fail
                    five_Star_3 = five_Star_3 + five_Star_3_fail
                    five_Star_4 = five_Star_4 + five_Star_4_fail
                    total_range = (five_Star_1 * 4)
            if controlTrigger == 1:
                five_Star_1 = 1
                five_Star_2 = 0.8 + 1
                five_Star_3 = 1 + 1 + 0.8
                five_Star_4 = 1.2 + 1 + 1 + 0.8
                total_range = (five_Star_1 * 4)
                counts = abs(counts - rounds)
            controlTrigger = 0
            counts = counts + 1
        print(u'目前機率: {}%'.format(total_range))
        #if tenFold_Count == 0 and oneShot_Count == 0:
        #   smn = 10
            #抽到有
        #elif tenFold_Count > 0:
        #    tenFold_Summon(tenFold_Count, oneShot_Count)
            #10連抽
        #elif oneShot_Count > 0:
            #oneShot_Suoong()
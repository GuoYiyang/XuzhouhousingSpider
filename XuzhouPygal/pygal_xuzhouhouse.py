import json
import pygal

filename='Xuzhouhouse.json'
with open(filename,'r',True,'utf-8') as f:
    house_list=json.load(f)
adict0 = {'1室1厅1卫':0,'2室1厅1卫':0,'2室2厅1卫':0,'3室2厅1卫':0,'其他':0}
adict1 = {'小于50平米':0,'50-75平米':0,'75-100平米':0,'大于100平米':0,'其他':0}
adict2 = {'南向':0,'南北向':0,'北向':0,'其他':0}
adict3 = {'毛坯':0,'简单装修':0,'中等装修':0,'精装修':0,'豪华装修':0,'其他':0}
adict4 = {'小于1000':0,'1000-1500':0,'1500-2000':0,'大于2000':0,'其他':0}

#房间数
for house_dict in house_list:
    str_size0=""
    try:
        for size0 in house_dict['size'][0]:
            str_size0+=size0
        if str_size0 == '1室1厅1卫':
            adict0['1室1厅1卫']+=1
        elif str_size0 == '2室1厅1卫':
            adict0['2室1厅1卫']+=1
        elif str_size0 == '2室2厅1卫':
            adict0['2室2厅1卫']+=1
        elif str_size0 =='3室2厅1卫':
            adict0['3室2厅1卫']+=1 
        else:
            adict0['其他']+=1
    except:
        print('装修有误')

pie0 = pygal.Pie()
for k in adict0.keys():
    pie0.add(k , adict0[k])
pie0.title="二手房屋房间数"
pie0.legend_at_bottom = True
pie0.render_to_file('房间数.svg')

#平方占比
for house_dict in house_list:
    str_size1=""
    try:
        for size1 in house_dict['size'][1][:-1]:
            if size1 == '.':
                break
            str_size1+=size1
        int_size1 = int(str_size1)
        if int_size1 < 50:
            adict1['小于50平米']+=1
        elif 50 <= int_size1 < 75:
            adict1['50-75平米']+=1
        elif 75 <= int_size1 < 100:
            adict1['75-100平米']+=1
        elif 100 <= int_size1 :
            adict1['大于100平米']+=1
        else:
            adict1['其他']+=1
    except:
        print("平方有误")

pie1 = pygal.Pie()
for k in adict1.keys():
    pie1.add(k , adict1[k])
pie1.title="二手房屋平米"
pie1.legend_at_bottom = True
pie1.render_to_file('房屋平米.svg')   


#朝向占比
for house_dict in house_list:
    str_size2=""
    try:
        for size2 in house_dict['size'][2]:
            str_size2+=size2
        if str_size2 == '南向':
            adict2['南向']+=1
        elif str_size2 == '南北向':
            adict2['南北向']+=1
        elif str_size2 =='北向':
            adict2['北向']+=1
        else:
            adict2['其他']+=1
    except:
        print('朝向有误')

pie2 = pygal.Pie()
for k in adict2.keys():
    pie2.add(k , adict2[k])
pie2.title="二手房屋朝向"
pie2.legend_at_bottom = True   
pie2.render_to_file('房屋朝向.svg')


#装修占比
for house_dict in house_list:
    str_size3=""
    try:
        for size3 in house_dict['size'][3]:
            str_size3+=size3
        if str_size3 == '毛坯':
            adict3['毛坯']+=1
        elif str_size3 == '简单装修':
            adict3['简单装修']+=1
        elif str_size3 == '中等装修':
            adict3['中等装修']+=1
        elif str_size3 =='精装修':
            adict3['精装修']+=1
        elif str_size3 =='豪华装修':
            adict3['豪华装修']+=1 
        else:
            adict3['其他']+=1
    except:
        print('装修有误')

pie3 = pygal.Pie()
for k in adict3.keys():
    pie3.add(k , adict3[k])
pie3.title="二手房屋装修"
pie3.legend_at_bottom = True
pie3.render_to_file('房屋装修.svg')


#价格占比
for house_dict in house_list:
    int_price=0
    try:
        for price in house_dict['price']:
            int_price=int(price)
            if int_price < 1000:
                adict4['小于1000']+=1
            elif 1000 <= int_price < 1500:
                adict4['1000-1500']+=1
            elif 1500 <= int_price < 2000:
                adict4['1500-2000']+=1
            elif 2000 <= int_price :
                adict4['大于2000']+=1
            else:
                adict4['其他']+=1
    except:
        print("价格有误")

pie4 = pygal.Pie()
for k in adict4.keys():
    pie4.add(k , adict4[k])
pie4.title="二手房屋价格"
pie4.legend_at_bottom = True
pie4.render_to_file('房屋价格.svg')

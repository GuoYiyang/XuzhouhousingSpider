import json
import pygal

filename='Xuzhouhouse.json'
with open(filename,'r',True,'utf-8') as f:
    house_list=json.load(f)
house_dict={}
for house in house_list:
    for price in house['price']:
        if(price in house_dict):
            house_dict[price]+=1
        else:
            house_dict[price]=1


pie=pygal.Pie()
for k in house_dict.keys():
    pie.add(k,house_dict[k])
pie.legend =True
pie.render_to_file('Xuzhouhouse.svg')

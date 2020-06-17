#coding:utf-8
"""
综合项目:世行历史数据基本分类及其可视化
作者：李长鸿
日期：6月14日

"""

import csv
import math
import pygal
import pygal_maps_world  #导入需要使用的库
wm = pygal_maps_world.maps.World()

def read_csv_as_nested_dict(filename,keyfield,separator,quote): #读取原始csv文件的数据，格式为嵌套字典
    """
    输入参数:
      filename:csv文件名
      keyfield:键名
      separator:分隔符
      quote:引用符

    输出:
      读取csv文件数据，返回嵌套字典格式，其中外层字典的键对应参数keyfiled，内层字典对应每行在各列所对应的具体值
    """
    result={}
    with open(filename,newline="")as csvfile:
        csvreader=csv.DictReader(csvfile,delimiter=separator,quotechar=quote)
        for row in csvreader:
            rowid=row[keyfield]
            result[rowid]=row

    return result
    
pygal_countries = pygal.maps.world.COUNTRIES #读取pygal.maps.world中国家代码信息（为字典格式），其中键为pygal中各国代码，值为对应的具体国名(建议将其显示在屏幕上了解具体格式和数据内容）
#gdp_countries = gdp.maps.world.COUNTRIES
#print(pygal_countries)
def reconcile_countries_by_name(plot_countries, gdp_countries): #返回在世行有GDP数据的绘图库国家代码字典，以及没有世行GDP数据的国家代码集合
  
  a1=set()
  b1={}
  for k,v in gdp_countries.items():
	  crusial=set(v.values())
	  if len(crusial)==5:
		  a1.add(form_value_to_key(k))
  for key,value in plot_countries.items():
	  if value not in a1:
		  b1[key]=value
  c1=(a1,b1)
  return c1

def form_value_to_key(value):
	for k,v in pygal_countries.items():
		if v==value:
			return k
def form_key_to_value(key):
	for k,v in pygal_countries.items():
		if k==key:
			return v
	
	
	"""
    输入参数:
    plot_countries: 绘图库国家代码数据，字典格式，其中键为绘图库国家代码，值为对应的具体国名
    gdp_countries:世行各国数据，嵌套字典格式，其中外部字典的键为世行国家代码，值为该国在世行文件中的行数据（字典格式)
    
    输出：
    返回元组格式，包括一个字典和一个集合。其中字典内容为在世行有GDP数据的绘图库国家信息（键为绘图库各国家代码，值为对应的具体国名),
    集合内容为在世行无GDP数据的绘图库国家代码
    """

    
    


def build_map_dict_by_name(gdpinfo, plot_countries, year):
	a2=set()
	b2={}
	for key,value in gdpinfo.items():
		if form_value_to_key(key) in plot_countries[0]:
			if value[year]!='':
				xe=float(value[year])
				b2[form_value_to_key(key)]=math.log(xe)
			else:
				a2.add(form_value_to_key)
	c2=(b2,a2,plot_countries[1])
	return c2
    



def render_world_map(gdpinfo, plot_countries, year, map_file):#将具体某年世界各国的GDP数据(包括缺少GDP数据以及只是在该年缺少GDP数据的国家)以地图形式可视化
	a3={}
	a4={}
	d1=list(gdpinfo[1])
	d2=list(gdpinfo[2])
	for values in d1:
		a3[values]='1'

	
	wm.title='全球gdp分布图'
	wm.add('%s'%year,gdpinfo[0])
	wm.add('missing form word bank',a3)
	wm.add('no data at this year',a4)
	wm.render_to_file(map_file)

"""
Inputs:
gdpinfo:gdp信息字典
plot_countires:绘图库国家代码数据，字典格式，其中键为绘图库国家代码，值为对应的具体国名
year:具体年份数据，以字符串格式程序，如"1970"
map_file:输出的图片文件名
    
目标：将指定某年的世界各国GDP数据在世界地图上显示，并将结果输出为具体的的图片文件
提示：本函数可视化需要利用pygal.maps.world.World()方法
     

"""

pygal_countries = pygal.maps.world.COUNTRIES# 获得绘图库pygal国家
# 测试时可以1970年为例，对函数继续测试，将运行结果与提供的svg进行对比，其它年份可将文件重新命名
print("欢迎使用世行GDP数据可视化查询")
print("----------------------")
year=input("请输入需查询的具体年份:")
q=read_csv_as_nested_dict("isp_gdp.csv","Country Name",',','"')
n = reconcile_countries_by_name(pygal_countries,q)
m=build_map_dict_by_name(q,n,year)
render_world_map(m,pygal_countries,year,"isp_gdp_world_name%s.svg"%year)



#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：植物生产类04班李长鸿
日期：4月12日
"""

import random
number=random.randint(0,4)



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
	if name=='石头':
		name_to_number=0
	elif name=='史波克':
		name_to_number=1
	elif name=='纸':
		name_to_number=2
	elif name=='蜥蜴':
		name_to_number=3
	elif name=='剪刀':
		name_to_number=4
	else:
		name_to_number=5
	return name_to_number
		
	
	
	
	


def number_to_name(number):
	if number<1:
		number_to_name='石头'
	elif 0<number<2:
		number_to_name='史波克'
	elif 1<number<3:
		number_to_name='纸'
	elif 2<number<4:
		number_to_name="蜥蜴"
	elif 3<number<5:
		number_to_name='剪刀'
	return number_to_name
   

    # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
    # 不要忘记返回结果




def rpsls(n,number):
	if n==0 and number==0:
		rpsls=0
	elif n==0 and number==1:
		rpsls=1
	elif n==0 and number==2:
		rpsls=1
	elif n==0 and number==3:
		rpsls=2
	elif n==0 and number==4:
		rpsls=2
	elif n==1 and number==0:
		rpsls=2
	elif n==1 and number==1:
		rpsls=0
	elif n==1 and number==2:
		rpsls=1
	elif n==1 and number==3:
		rpsls=1
	elif n==1 and number==4:
		rpsls=2
	elif n==2 and number==0:
		rpsls=2
	elif n==2 and number==1:
		rpsls=2
	elif n==2 and number==2:
		rpsls=0
	elif n==2 and number==3:
		rpsls=1
	elif n==2 and number==4:
		rpsls=1
	elif n==3 and number==0:
		rpsls=1
	elif n==3 and number==1:
		rpsls=2
	elif n==3 and number==2:
		rpsls=2
	elif n==3 and number==3:
		rpsls=0
	elif n==3 and number==4:
		rpsls=1
	elif n==4 and number==0:
		rpsls=1
	elif n==4 and number==1:
		rpsls=1
	elif n==4 and number==2:
		rpsls=2
	elif n==4 and number==3:
		rpsls=2
	elif n==4 and number==4:
		rpsls=0
	elif n>4:
		rpsls=5
	
	return rpsls
		
	
	
   


    # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    # 在屏幕上显示计算机选择的随机对象

    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”

    


# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
name=input()
m=number_to_name(number)
n=name_to_number(name)
a=rpsls(n,number)
if a>4:
	print('Error: No Correct Name')
else:
	print('--------------------')
	print('您的选择为：',name)
	print('计算机的选择为：',m)
	if a==0:
		print("很可惜，你们的选择是一样的")
	elif a==1:
		print("很抱歉，这次是您的计算机赢了")
	elif a==2:
		print("恭喜您，您猜赢了您的计算机")


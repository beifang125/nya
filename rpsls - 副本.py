#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�ֲ��������04�����
���ڣ�4��12��
"""

import random
number=random.randint(0,4)



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
	if name=='ʯͷ':
		name_to_number=0
	elif name=='ʷ����':
		name_to_number=1
	elif name=='ֽ':
		name_to_number=2
	elif name=='����':
		name_to_number=3
	elif name=='����':
		name_to_number=4
	else:
		name_to_number=5
	return name_to_number
		
	
	
	
	


def number_to_name(number):
	if number<1:
		number_to_name='ʯͷ'
	elif 0<number<2:
		number_to_name='ʷ����'
	elif 1<number<3:
		number_to_name='ֽ'
	elif 2<number<4:
		number_to_name="����"
	elif 3<number<5:
		number_to_name='����'
	return number_to_name
   

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��




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
		
	
	
   


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

    


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
name=input()
m=number_to_name(number)
n=name_to_number(name)
a=rpsls(n,number)
if a>4:
	print('Error: No Correct Name')
else:
	print('--------------------')
	print('����ѡ��Ϊ��',name)
	print('�������ѡ��Ϊ��',m)
	if a==0:
		print("�ܿ�ϧ�����ǵ�ѡ����һ����")
	elif a==1:
		print("�ܱ�Ǹ����������ļ����Ӯ��")
	elif a==2:
		print("��ϲ��������Ӯ�����ļ����")


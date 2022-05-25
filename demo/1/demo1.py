# author: zong
# date: 2022/5/20 20:35

'''一、使用print方式进行输出（输出的目的地是文件）'''
fp = open('test.txt', 'w', encoding='utf-8')
print('奋斗成就更好的你', file=fp)
fp.close()

'''二、使用文件读写操作'''
with open('test.txt', 'w', encoding='utf-8') as file:
    file.write('奋斗成就更好的你')
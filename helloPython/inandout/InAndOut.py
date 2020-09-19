# print('{0}和{1}'.format('hello','Python'))
# print('{0} {1}'.format('Hello', 'Python'))
# print('{1} {0}'.format('Hello', 'Python'))

# print('{name}网址：{site}'.format(name='Python技术', site='www.justdopython.com'))
# print('电商网站 {0}, {1}, {other}。'.format('淘宝', '京东', other='拼多多'))
# print("repr() shows quotes: {!a}; str() doesn't: {!s}".format('test1', 'test2'))

import math
# print('The value of PI is approximately {0:.3f}.'.format(math.pi))

# table = {'Sjoerd': 123, 'Jack': 456, 'Dcab': 789}
# for name, phone in table.items():print('{0:10} ==> {1:10d}'.format(name, phone))
# table = {'Sjoerd': 123, 'Jack': 456, 'Dcab': 789789789789}
# print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ' 'Dcab: {0[Dcab]:d}'.format(table))
# print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

# 键盘输入
# str = input("请输入：");
# print ("输入的内容是: ", str)

# 文件操作
# f = open('E:\\temp.txt','r')
# firstLine = f.readline()
# print(firstLine)
# string = f.read()
# print(string)
# str = f.readlines(1)
# print(str)
# f.close()

# f = open('E:\\temp.txt', 'w')
# num = f.write('Hello Python')
# print(num)
# f.close()

# f = open('E:\\temp.txt', 'rb+')
# f.write(b'0123456789abcdef')
# f.seek(5)
# print(f.read())
# f.close()

# f = open('E:\\temp.txt', 'r')
# f.seek(5)
# print(f.tell())
# f.close()

# 操作 json 格式数据
import json
data = {'id':'1', 'name':'jhon', 'age':12}
with open('t.json','w') as f:
    json.dump(data,f)
with open('t.json','r') as f:
    d = json.load(f)
print(d)





















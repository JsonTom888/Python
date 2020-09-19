from math import factorial
from functools import reduce

def high_func(f,arr):
    return [f(x) for x in arr]

def square(n):
    return n ** 2

# print(high_func(factorial,list(range(10))))
# print(high_func(square,list(range(10))))

facMap = map(factorial,list(range(10)))
# print(list(facMap))

squareMqp = map(square,list(range(10)))
# print(list(squareMqp))

lamMqp = map(lambda x:x * 2,list(range(10)))
# print(list(lamMqp))

mutiMqp = map(lambda x,y:x+y,list(range(10)),list(range(11,15)))
# print(list(mutiMqp))
# print(list(range(11,15)))

result = reduce(lambda x,y:x + y, [1, 2, 3, 4, 5])
# print(result)

s = reduce(lambda x, y: x + y, ['1', '2', '3', '4', '5'], "数字 = ")

# print(s)

def boy(n):
    if n % 2 == 0:
        return True
    return False
filterList = filter(boy, list(range(20)))
# print(list(filterList))
filterList2 = filter(lambda n: n % 2 == 0, list(range(20)))
# print(list(filterList2))
list01 = [5, -1, 3, 6, -7, 8, -11, 2]
list02 = ['apple', 'pig', 'monkey', 'money']
# print(sorted(list01))
# print(sorted(list01, key=abs))
# print(sorted(list01,reverse=True))

# print(sorted(list02))
# print(sorted(list02, reverse=True))
# 匿名函数排序
print(sorted(list02, key=lambda x: len(x), reverse=True))
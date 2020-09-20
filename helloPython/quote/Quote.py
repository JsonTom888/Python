# a = 10000
# print(id(a))
# a = 1335456
# print(id(a))

# a = 10000
# print(id(a))
# a = 10000
# print(id(a))

# a = [1,2]
# print(id(a))
# a = [1,2]
# print(id(a))

# for b in range(300):
#     if b is not range(300)[b]:
#         print("常量池最大值为：", (b - 1))
#         break

# a = 10000
# print(id(a))
# a = a + 1
# print(a)
# print(id(a))

# a = [1,2]
# print(id(a))
# a = a + [4]
# print(a)
# print(id(a))

# c = [1, 2, 3]
# print(id(c))
# c[2] = 5
# print(c)
# print(id(c))
# c.append(3)
# print(c)
# print(id(c))


# c = [1, 2, 3]
# cc = c
# print(id(c))
# print(id(cc))
# c[2] = 5
# print(cc)
# print(id(c))
# print(id(cc))
# c.append(3)
# print(c)
# print(cc)
# print(id(c))
# print(id(cc))
# del c[3]
# print(c)
# print(id(c))
# print(id(cc))

# num = 10000
# print(id(num))
# num += 1
# print(id(num))

# li = [1, 2, 3]
# print(id(li))
# li += [4]
# print(id(li))
# print(li)

a = 10000
print(a == 10000)
print(a is 10000)
print(id(a))
print(id(10000))

from sys import getrefcount
print(getrefcount(a))
print(getrefcount(10000))


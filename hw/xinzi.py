#-------------------矩阵乘法--------------------------------
class Matrix(object):
    def __init__(self):
        self.matrix = []
        self.row = 0
        self.col = 0
        self.init_matrix()  # 矩阵对象初始化
    
    def init_matrix(self):
        self.get_rowcol()
        self.add_number()

    def get_rowcol(self):
        while True:
            try:
                self.row = int(input("请输入矩阵行数："))
                self.col = int(input("请输入矩阵列数："))
                break
            except Exception:
                print("听话，输入数字。。。")
                continue


    def add_number(self):
        # 填充矩阵
        temp = []
        for i in range(self.row):
            for j in range(self.col):
                while True:
                    try:
                        temp.append(int(input("请输入%d行%d列数字："%(i + 1, j + 1))))
                        break
                    except ValueError as e:
                        print(e)
                        continue
            self.matrix.append(temp)
            temp = []

    @staticmethod
    def multiply(matrix01, matrix02):  # O(n^3)
        # 与矩阵02相乘
        # return 计算结果
        if matrix01.row != matrix02.col:        
            a = "这事儿成不了"
            return a
        elif not matrix01.matrix or not matrix02.matrix:
            a = "空矩阵无法相乘"
            return a
        else:
            result = []
            temp_number = []
            temp = []
            for i in range(matrix01.row):  # 确定M1行
                for a in range(matrix02.col):  # 确定M2的列
                    for j in range(matrix01.col):
                        temp_number.append(matrix01.matrix[i][j] * matrix02.matrix[j][a])                    
                    temp.append(sum(temp_number))
                    temp_number = []
                result.append(temp)
                temp = []
            return result

    @staticmethod
    def show(matrix):
        # 输出任意矩阵
        for array in matrix:
            for item in array:
                print(item, end=" ")
            print()

def main():
    # 创建矩阵对象M1并初始化
    print("设置矩阵对象M1，并初始化")
    M1 = Matrix()
    if M1.matrix:
        print("矩阵M1如下：")
        Matrix.show(M1.matrix)
    else:
        print("矩阵M1为空")

    # 创建矩阵对象M2并初始化
    print("设置矩阵对象M2，并初始化")
    M2 = Matrix()
    if M2.matrix:
        print("矩阵M2如下：")
        Matrix.show(M2.matrix)
    else:
        print("矩阵M2为空")

    a = Matrix.multiply(M1,M2)  # 矩阵对象乘积
    if isinstance(a, list):
        print("矩阵M1与M2乘积如下")        
        Matrix.show(a)
    else:
        print(a)

if __name__ == "__main__":
    main()

"""
测试结果：
（1）空矩阵相乘                 
    设置矩阵对象M1，并初始化
    请输入矩阵行数：0
    请输入矩阵列数：0
    矩阵M1为空
    设置矩阵对象M2，并初始化
    请输入矩阵行数：0
    请输入矩阵列数：0
    矩阵M2为空
    空矩阵无法相乘  # 判断结果正确
（2）数字和结构阳间一点的矩阵
    设置矩阵对象M1，并初始化 
    ...输入数据...
    矩阵M1如下：
    1 2
    2 1
    设置矩阵对象M2，并初始化
    ...输入数据...
    矩阵M2如下：
    -1 -2
    -2 -1
    矩阵M1与M2乘积如下  # 判断结果正确
    -5 -4
    -4 -5
（3）数字和结构阴间一点的矩阵  
    ......
    矩阵M1如下：
    1 2
    3 4
    5 6
    设置矩阵对象M2，并初始化
    ......
    矩阵M2如下：
    6 5 4
    3 2 1
    矩阵M1与M2乘积如下  # 判断结果正确
    12 9 6
    30 23 16
    48 37 26
"""

# -----------------洗牌算法------------------
"""
洗牌原理：
设一游标i从前向后扫描原始数据的拷贝，在[0, i]之间随机一个下标j，
然后用位置j的元素替换掉位置i的数字，再用原始数据位置i的元素替换掉拷贝数据位置j的元素。
其作用相当于在拷贝数据中交换i与j位置处的值。
"""
import random
def shuffle(target_list):  # O(n)
    def shuffle01(target_list, i):
        if i >= len(target_list):
            return target_list
        else:
            j = random.randint(0, i)
            change(target_list, i, j)
            shuffle01(target_list, i + 1)
    shuffle01(target_list, 0)
    return target_list
def change(target_list, i, j):
    target_list[i], target_list[j] = \
        target_list[j], target_list[i]
# 测试
# print(shuffle([1]))
# print(shuffle([]))
# print(shuffle([1, 2, 3, 4, 5]))
# print(shuffle([1, 3, 4, 2, 2, 1234]))
# print(shuffle([1123, 0, 423554, 21]))
"""
标准差计算：
规定一个数组[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
def shuffletest(time, shuffle):
    # time:测试次数
    # 返回统计结果和方差
    results = []
    for i in range(time):
        array = shuffle([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        results.append(array)

    # 统计
    stats = [[0]*10,[0]*10,[0]*10,[0]*10,[0]*10,[0]*10,[0]*10,[0]*10,[0]*10,[0]*10,]
    for item in results:
        for j in range(len(item)):
            stats[j][item[j]] += 1

    # 求平均数
    temp_sum = 0
    for item in stats:
        temp_sum += sum(item)
    avg = temp_sum / 100

    # 求方差
    temp = 0
    for item in stats:
        for i in item:
            temp += (i - avg)**2
    s = temp /100 /time
    return stats,s

# 打印二维数组
def show(target_list):
    for item in target_list:
        for number in item:
            print(number,end = "\t")
        print()

stats, s = shuffletest(1000, shuffle)
show(stats)
print(s)

#-------------------链表--------------------
class Node:
    def __init__(self, val = None):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self):
        # 链表头部始终不存储元素，链表第一元素从self.head.next开始
        self.head = Node()

    def show(self):
        p = self.head.next
        while p:
            print(p.value, end=" ")
            p = p.next
        print()

    def append(self, element):
        def appendx(p, element):
            if p.next is None:
                p.next = Node(element)
            else:
                p = p.next
                appendx(p, element)
        p = self.head
        appendx(p, element)

    def append_head(self, element):
        p = self.head
        node = Node(element)
        node.next = p.next
        p.next = node

    def insert(self, element, index):
        if index < 0 or index > self.length():
            raise IndexError("LinkedList index out of the range")
        def insertx(p, count):
            if count == index:
                node = Node(element)
                node.next = p.next
                p.next = node
            else:
                p = p.next
                count += 1
                insertx(p, count)
        p = self.head
        insertx(p,0)

        
    def length(self):
        p = self.head.next
        count = 0
        while p:
            p = p.next
            count += 1
        return count


# 这里的复杂度都是O(n)
link = LinkedList()
link.append(1)
link.append(2)
link.append(3)
link.append_head(5)  # 5 1 2 3
link.insert(2, 1)  # 5 2 1 2 3
# link.insert(5,9)  # 报错
link.show()
print(link.length())

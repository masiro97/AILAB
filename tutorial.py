# a = 3
# b = 4
# print(a+b)
# print('a+b')
# print('a+b=%d'%(a+b))
# print('%d+%d=%d'%(a,b,a+b))

# a = 10.3
# b = 10.7
# c = int(a)
# d = int(b)
# print(c)
# print(d)

# a = 'string'
# b = 35
# c = str(b)
# print(a+c)

# c = float(input("centigrade : "))
# f = ((9/5) * c) + 32
# print("centigrade : %.2f, Fahrenheit: %.2f"%(c,f))

test_list = [1,2,3,4,5]

# test_list.insert(1,10)
# print(test_list)
#
# test_list.append(11)
# print(test_list)
#
# del test_list[4]
# print(test_list)
#
# test_list.sort()
# print(test_list)
#
# test_list.reverse()
# print(test_list)
#
# print(test_list.index(10))

# marks = [90,25,67,45,80]
#
# number = 0
# for mark in marks:
#     number = number + 1
#     if mark < 60:
#         continue
#     print("%d번 학생 축하합니다. 합격입니다" %number)

# while(True):
#     var = int(input("Enter (1~9)? "))
#     if(var ==0):
#        print("Message : Quit")
#        break
#     else:
#         for i in range(0,10):
#             print("%dx%d=%d"%(var,i,var*i))

# def c2f(c):
#     return float((9/5)*c + 32)
#
# ce = float(input("centigrade : "))
# print("centigrade: %.2f, Fahrenheit: %.2f"%(ce,c2f(ce)))

class Ball:
    def __init__(self,size,color,direction):
        self.size = size
        self.color = color
        self.direction = direction
    def throw(self):
        print("Throw %s" %self.direction)



myBall = Ball(5,'red','down')
print(myBall.color)
myBall.color = 'blue'
print(myBall.color)
myBall.throw()
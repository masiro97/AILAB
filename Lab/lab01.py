# datas = [-23,97,18,21,5,-86,64,0,-37]
# target = int(input("input a target value: "))
# a=0
# for data in datas:
#     if data == target:
#         a = a+1
#         print(datas.index(target))
#         break
# if a ==0:
#     print("no data")


datas = [1,2,3,4,5,6,7,8,9]
target = 3
low = 0
high = len(datas)
while(True):
    middle = int((low + high)/2)
    if low >= high:
        print("Not Found")
        break
    elif datas[middle] == target:
        print("the index of target value is %d"%middle)
        break
    elif datas[middle] > target:
        high = middle -1
    else:
        low = middle + 1




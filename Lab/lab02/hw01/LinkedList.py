def hash_function(id): #Hash Function
    return id % 100

def store(slot,key,data):
    list = []
    if(len(slot[key]) == 0): #현재 slot이 비어있을 때
        list.append(data)
    else: #slot에 이미 값이 있을 때
        list = slot[key] #list에 이미 있던 값을 추가
        list.append(data) #저장할 데이터를 추가
    print("the hash address is [%d,%d]" %(key,len(list)))
    return list

def search(slot,key,data):
    idx = 0 #찾을 데이터의 index
    check = 0 #찾을 데이터가 hash에 존재하는지 check
    if(len(slot[key]) == 0): #slot에 아무것도 안들어 있을 때
        print("The value that you find is none")

    else: #slot에 데이터가 존재할 때
        for i in range(0,len(slot[key])): #slot에 있는 모든 값을 확인하면서 같은 값이 있는지 확인
            temp = slot[key][i]
            if (temp[0] == data): #데이터가 존재할 때
                check =1
                idx = i
                break
        if(check ==0):
            print("The value that you find is none")
        else:
            print("The target value is [%d, '%s']"%(slot[key][idx][0],slot[key][idx][1]))
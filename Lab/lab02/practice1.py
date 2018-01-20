import numpy as np
student_group =[0] *100

while(True):
    mode = int(input("mode를 선택하세요( 1:store 2:search 0:exit ) : "))
    if(mode ==1):

        student_number = int(input("학번을 입력해주세요 : "))
        student_name = input("이름을 입력해주세요 : ")
        index = student_number % 100
        student_group[index] = [student_number, student_name]

    elif(mode ==2):

        student_number = int(input("학번을 입력해주세요 : "))
        index = student_number % 100
        if(student_group[index] == 0):
            print("없는 학번입니다. 학번과 이름을 등록해주세요\n")
        else:
            print("index = %d" %index)
            print("name = %s"%student_group[index][1])
            print("id = %d"%student_group[index][0])

    else:
        break



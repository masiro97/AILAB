import LinkedList

slot = [[]] * 100 #100개의 empty slot

while True:
    e_input = input("input mode (1:store 2:search 3:show_hash_table 4:end) : ")
    if (e_input.isdigit() and 0 <= int(e_input) <= 5):
        mode = int(e_input)
        if(mode ==1): #store mode
            while(True):
                e_student_id = input("enter student ID (key) : ")
                if (e_student_id.isdigit()):
                    student_id = int(e_student_id)
                    student_name = input("enter student name (value) : ")
                    student = [student_id,student_name] #student의 id와 이름으로 list를 만든다.
                    hash_key = LinkedList.hash_function(student_id)
                    slot[hash_key] = LinkedList.store(slot,hash_key,student) #구한 hash key의 slot에 데이터 저장
                    break
                else: #잘못된 input이 들어올 때
                    print("wrong input. Please re-input")

        elif(mode ==2): #search mode
            while(True):
                e_find_id = input("enter ID that you find : ")
                if(e_find_id.isdigit()):
                    find_id = int(e_find_id)
                    hash_key = LinkedList.hash_function(find_id)
                    LinkedList.search(slot,hash_key,find_id) #hash key로 데이터 찾기
                    break
                else: #잘못된 input이 들어올 때
                    print("wrong input. Please re-input")

        elif(mode ==3): #show_hash_table
            print("show hash table")
            for i in range(0,100):
                print(slot[i])
        else: #exit
            break


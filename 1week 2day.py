import random
list_seven=[]
for i in range(1,8): # 7개의 요소를 생성 
    n = random.randint(1,99)
    list_seven.append(n)
    result = sum(list_seven)
    if result == 100:
        list_seven.sort() # list_seven.sort는 메서드 참조일뿐 호출 되지 않음 list_seven.sort()
        print(list_seven)
        break
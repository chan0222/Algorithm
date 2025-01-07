import random
list_nine = []
for i in range (1,9):
    n= random.randint(1,100)
    list_nine.append(n)
print(list_nine) # 리스트의 최종상태(9개의 요소를 한번만 출력하고 싶다면,print문을 루프 바깥으로 이동해야함함)
import random
while True:
    list_nine = [20,7,23,19,10,15,25,8,13]
    # for i in range (1,10):
    #     n = random.randint(1,99)
    #     list_nine.append(n)
    # print(list_nine) # 리스트의 최종상태(9개의 요소를 한번만 출력하고 싶다면,print문을 루프 바깥으로 이동해야함함)

# 여기서 9개애서 7개를 뽑고 나서 그 합이 100인걸 찾아야함

    list_seven = random.sample(list_nine,7)

    # print(list_seven)

    result = sum(list_seven) 
    # print(result)
    if result == 100:
        list_seven.sort()
        print(list_seven)
        break
# 합의 값이 100이 아니면 맨처음부터 반복하려면 ? 반복문 안에 반복문이 있는 형태
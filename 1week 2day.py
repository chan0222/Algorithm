import random
list_seven=[]
for i in range(1,7):
    n = random.randint(1,99)
    list_seven.append(n)
    result = sum(list_seven)
    if result == 100:
        list_seven.sort
        print(list_seven)
        break
import sys # 프로그램을 강제로 종료하기 위해 사용
dwarfs = [20,7,23,19,10,15,25,8,13] # 숫자 있는 곳에 int(input()) for _ in range (9 넣었음) >> 리스트 컴프리 헨션: 반복문을 이용해 리스트를 간단하게 생성하는 방식  
total = sum(dwarfs) # 9명 난쟁이 키의 총합을 구함 

for i in range(9):
    for j in range(i+1,9): # 이중루프를 사용해 9명 중에서 두명을 선택한다. i + 1 부터 j를 순회하도록 해 i != j 조건을 자동으로 만족 시킨다. 
        if total - dwarfs[i] - dwarfs[j] == 100: # 두명의 난쟁이를 제외한 나머지 7명의 키의 합이 100이 되는 지 확인인
            result = [dwarfs[k] for k in range(9) if k != i and k !=j] # 리스트 컴프리 헨션을 사용해 i와 j를 제외한 7명의 난쟁이 리스트에 추가한다. 
            result.sort() # 오름차순으로 정렬
            for dwarf in result: # 정답인 난쟁이 7명의 키를 한줄씩 출력한다. 
                print(dwarf)
            sys.exit() # 정답을 찾은 후 프로그램을 종료 



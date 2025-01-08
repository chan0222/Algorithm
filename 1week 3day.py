def triangular_numbers(limit): # 삼각수는 1-n 까지의 자연수를 더한 값// k이하의 모든 삼각수를 리스트로 생성하여 반환함함
    t_nums =[]
    n = 1
    while True:
        t = n * (n+1) // 2  # 삼각수 공식식
        if t> limit: # 삼각수가 k 보다 커지면 종료료
            break
        t_nums.append(t)
        n += 1
    return t_nums  # k 이하의 삼각수 리스트를 반환 

def check_tri(k): # 삼각수의 합으로 표현 여부를 확인 하는 함수// 자연수 k를 매개변수로 받아 k가 3개의 삼각수의 합으로 표현 가능한지 여부 판단 
    t_nums = triangular_numbers(k) # 여기서 k는 확인 하고자 하는 자연수 
    for i in t_nums:
        for j in t_nums:
            for m in t_nums:
                if i + j + m == k: # 중첩 반복문을 사용하여(3중 루프) 삼각수 리스트에서 3개의 숫자를 골라 합을 계산함
                    return 1  # 만족하는 조합이 발견되면 바로 즉시 1을 반환
    return 0 # 어떠한 조합을 찾지 못하면 0을 반환환
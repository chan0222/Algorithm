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
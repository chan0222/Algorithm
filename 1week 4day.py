def calculate_win_probability(A, B):
    # 전체 카드 덱 초기화
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 2
    cards.remove(A)
    cards.remove(B)

    # 영학이 족보 계산
    if A == B:  # 땡인 경우
        my_score = A
    else:  # 끗인 경우
        my_score = 10 + (A + B) % 10

    # 상대방 족보 계산 및 승리 경우의 수 세기
    win_count = 0
    total_cases = 0

    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            total_cases += 1
            C, D = cards[i], cards[j]
            if C == D:  # 땡인 경우
                opponent_score = C
            else:  # 끗인 경우
                opponent_score = 10 + (C + D) % 10
            
            if my_score > opponent_score:
                win_count += 1

    # 승리 확률 계산
    win_probability = win_count / total_cases
    return f"{win_probability:.3f}"
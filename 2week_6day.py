# 수의 개수 입력받기
N = int(input())
# 수열 입력받기
nums = list(map(int, input().split()))
# 연산자 개수 입력받기
op = list(map(int, input().split()))

# 최댓값, 최솟값 초기화하기
max_value = -1e9
min_value = 1e9

# dfs 함수 정의
def solution(num, idx, add, sub, mul, div):
    global max_value, min_value

    # 연산자를 모두 사용했을 경우, 최대/최소 값 갱신
    if idx == N:
        max_value = max(max_value, num)
        min_value = min(min_value, num)
        return

    # 연산자 사용
    if add > 0:
        solution(num + nums[idx], idx + 1, add - 1, sub, mul, div)
    if sub > 0:
        solution(num - nums[idx], idx + 1, add, sub - 1, mul, div)
    if mul > 0:
        solution(num * nums[idx], idx + 1, add, sub, mul - 1, div)
    if div > 0:
        # 정수 나눗셈 (나눗셈의 결과는 양수/음수 부호를 유지해야 함)
        if num < 0:
            solution(-(-num // nums[idx]), idx + 1, add, sub, mul, div - 1)
        else:
            solution(num // nums[idx], idx + 1, add, sub, mul, div - 1)

# dfs 함수 호출
solution(nums[0], 1, op[0], op[1], op[2], op[3])

# 최댓값과 최솟값 결과 출력
print(max_value)
print(min_value)

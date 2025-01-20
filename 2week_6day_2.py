import sys

# 수의 개수 입력받기
n = int(input())
# 수열 입력받기
data = list(map(int, input().split()))
# 연산자 개수 입력받기
add, sub, mul, div = map(int, input().split())

# 최댓값, 최솟값 초기화하기
max_value = -1e9
min_value = 1e9

# dfs 함수 정의
def dfs(i, arr):
    global add, sub, mul, div, max_value, min_value
		# 연산자를 모두 사용했을 경우, 다 탐색했기 때문에 최대최소 비교
		# 종료 조건에 해당
    if i == n:
        max_value = max(max_value, arr)
        min_value = min(min_value, arr)
        return 
    else: 
    # 연산자, 모든 경우 고려
		# 더하기
        if add > 0:
            add -= 1
            dfs(i+1, arr + data[i])
            add += 1
		# 빼기
        if sub > 0:
            sub -= 1
            dfs(i+1, arr - data[i])
            sub += 1        
        # 곱하기
        if mul > 0:
            mul -= 1
            dfs(i+1, arr * data[i])
            mul += 1		
        # 나누기
		if div > 0:
            div -= 1
            dfs(i+1, int(arr / data[i]))
            div += 1

# dfs 함수 호출
dfs(1, data[0])

# 최댓값과 최솟값 결과 출력
print(max_value)
print(min_value)
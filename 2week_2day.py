# 준현이 vs 성민이

Money = int(input())    # 초기자금 입력값 // input()은 기본적으로 문자열을 반환하기 때문에 숫자 데이터로 변환 해야함  그래서 int()
MachineDuck = list(map(int,input().split())) # 특정기간 동안의 주식 가격 목록 split()=> 입력 받은 문자열을 공백 기준으로 나눠 리스트로 변환하기 위해 //map(int,) => 문자열 리스트를 정수형 리스트로 변환하기 위해 사용// list() => map 객체를 리스트로 변환(why? 나중에 반복문에서 인텍스와 값을 쉽게 처리할수 있도록 리스트 형태태)

# 준현이
money_bnp = Money
count_bnp = 0

# 성민이
money_timing = Money
count_timing = 0

for num, price in enumerate(MachineDuck): # for => 리스트의 모든 주식 가격에 대해 순회하기 위해 사용// enumerate(): 현제 요소의 인택스와 값을 동시에 사용할수 있게 함(num,price) // 투자전략에서 연속적인 가격 변동(4일치)을 처리하기 위해 인텍스와 값을 동시에 활용

    #준현
    count_bnp += (money_bnp // price)
    money_bnp %= price

    #성민
    temp = MachineDuck[num:num+4] # 슬라이싱 => 특정구간(4일치)의 데이터를 가져오기 위해 사용 주식 가격의 연속적인 상승/ 하락 여부를 판단하기 위해 

    if len(temp) < 4:
        continue

    if temp[0] < temp[1] < temp[2] < temp[3] and count_timing > 0: # 수식 가격의 연속적인 상승 여부를 확인  count_timing > 0 은 주식이 있을 때만 매도 가능하도록 조건 추가 상승장일때 주식을 매도하고 이익 실현
        money_timing += (count_timing * temp[3])
        count_timing = 0
    elif temp[0] > temp[1] > temp[2] > temp[3]: # 주식 가격의 연속적인 하락 여부를 확인//  하락장에서 주식을 매수해 가격이 오를때를 대비비
        count_timing += (money_timing // temp[3])
        money_timing %= temp[3]

answer_bnp = money_bnp + count_bnp * MachineDuck[-1]
answer_timing = money_timing + count_timing * MachineDuck[-1]

if answer_bnp < answer_timing:
    print("TIMING")
elif answer_bnp > answer_timing:
    print("BNP")
else:
    print("SAMESAME")

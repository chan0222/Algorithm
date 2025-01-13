import sys;input = sys.stdin.readline

m = int(input())
arr=[0,1,2,3]
tmp_x=0
flag=False
for _ in range(m):
    x,y =map(int,input().split())

# x 위치 먼저 찾기
    for i in range(len(arr)):
        if arr[i]==x:
            # x가 있는 위치의 값을 tmp_x 변수에 저장해 둘
            tmp_x=arr[i]

            # 이후 y의 위치 찾기
            for j in range(len(arr)):
                #x,y가 있는 위치의 값을 서로 리버스. 이때 탬_x변수에 저장해둔 값 사용용
                if arr[j]==y:
                    arr[i]=arr[j]
                    arr[j]=tmp_x
                    flag=True
                    break
            # x,y의 위치 찾기가 끝났다면 루프를 종료     
            if flag:break

print(arr[1])
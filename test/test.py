import sys
sys.stdin = open('input_test.txt')

ts=int(input())
for t in range(1, ts+1):
    arr=[]
    answer=1
    for i in range(9):
        arr.append(list(map(int, input().split())))
    for row in arr:
        if [1,2,3,4,5,6,7,8,9]!=sorted(row):
            answer=0
            break
    for i in range(9):
        temp=[]
        for col in arr:
            temp.append(col[i])
        if [1,2,3,4,5,6,7,8,9]!=sorted(temp):
            answer=0
            break
    print(f'#{t} {answer}')
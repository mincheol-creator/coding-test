import sys
sys.stdin = open('input_test.txt')

N = int(input())
answer=''
for tc in range(1,N+1):
    if N % tc == 0 :
        answer+=str(tc)
        if tc!=N:
            answer+=' '
print(answer)
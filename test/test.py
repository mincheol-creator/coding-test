import sys
sys.stdin = open('input_test.txt')

N=int(input())
count_2=0
count_3=0
count_5=0
count_7=0
count_11=0

for i in range(1,N+1):
    input_number=int(input())
    while input_number!=1:
        if input_number%2==0:
            input_number=input_number/2
            count_2+=1
        elif input_number%3==0:
            input_number=input_number/3
            count_3+=1
        elif input_number%5==0:
            input_number=input_number/5
            count_5+=1
        elif input_number%7==0:
            input_number=input_number/7
            count_7+=1
        elif input_number%11==0:
            input_number=input_number/11
            count_11+=1
    print(f'#{i} {count_2} {count_3} {count_5} {count_7} {count_11}')
    count_2=0
    count_3=0
    count_5=0
    count_7=0
    count_11=0
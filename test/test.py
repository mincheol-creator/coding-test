import sys
sys.stdin = open('input_test.txt')

Numbers=int(input())
for Number in range(1, Numbers+1):
    print(f'#{Number}')

    Counts=int(input())
    enter_count=0
    for Count in range(0,Counts):
        input_arr=[]
        input_arr=list(input().split())
        for i in range(int(input_arr[1])):
            print(input_arr[0], end="")
            enter_count+=1
            if enter_count==10:
                print()
                enter_count=0
    print()
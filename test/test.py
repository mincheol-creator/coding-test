import sys
sys.stdin = open('input_test.txt')

import datetime

N=int(input())
string=''
for i in range(1,N+1):
    string=str(input())
    try:
        date=datetime.datetime(int(string[:4]), int(string[4:6]), int(string[6:]))
        print(f"#{i} {string[:4]}/{string[4:6]}/{string[6:]}")
    except:
        print(f"#{i} {-1}")
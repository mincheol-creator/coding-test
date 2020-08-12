import sys
sys.stdin = open('input_test.txt')

ts=int(input())
for t in range(1, ts+1):
    Ns=int(input())
    row=1
    col=Ns-1
    direct=1
    arr=[[i for i in range(1,Ns+1)]]
    for i in range(Ns-1):
        arr.append([0]*Ns)
    for N in range(Ns+1,Ns*2):
        arr[row][col]=N
        if row!=(Ns-1):
            row+=1
    for N in range(Ns*2,Ns*3-1):
        if col!=0:
            col-=1
        arr[row][col]=N
    for N in range(Ns*3-1,(Ns)**2+1):
        if direct==1:
            if arr[row-1][col]==0:
                arr[row-1][col]=N
                row-=1
            elif arr[row][col+1]==0:
                arr[row][col+1]=N
                col+=1
            else:
                direct=2
        if direct==2:
            if arr[row+1][col]==0:
                arr[row+1][col]=N
                row+=1
            elif arr[row][col-1]==0:
                arr[row][col-1]=N
                col-=1
            else:
                direct=1
    print(f'#{t}')
    for i in range(Ns):
        for j in range(Ns):
            print(arr[i][j], end=" ")
        print()
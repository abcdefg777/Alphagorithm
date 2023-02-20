import sys

n = int(sys.stdin.readline())

if n >=1 and n <= 50 :
    A_list = list(map(int, sys.stdin.readline().split()))
    B_list = list(map(int, sys.stdin.readline().split()))

sorted_A = sorted(A_list)
sorted_B = sorted(B_list, reverse = True)
#B를 재배열해서 엄연히 정답은 X...
temp = 0
for i in range(n) :
    temp = temp + sorted_A[i] * sorted_B[i]


print(temp)
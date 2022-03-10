# 3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.

num = list(map(int, input().split()))

for i in num:
    result = 'even' if i % 2 == 0 else 'odd'
    print(result)
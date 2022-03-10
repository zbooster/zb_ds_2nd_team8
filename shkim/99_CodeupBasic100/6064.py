# 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
# 단, 3항 연산을 사용한다.

num = list(map(int, input().split()))
print((num[0] if num[0] < num[2] else num[2]) if num[0] < num[1] else (num[1] if num[1] < num[2] else num[2]))
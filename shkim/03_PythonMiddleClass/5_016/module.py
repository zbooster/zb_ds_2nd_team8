# 수학 관련 함수

# 합
listVar = [2, 5, 3.14, 58, 10, 2]
print(f'sum(listVar): {sum(listVar)}')

print(f'max(listVar): {max(listVar)}')

print(f'min(listVar): {min(listVar)}')

# 거듭제곱
print(f'pow(13, 2): {pow(13, 2)}')

# 반올림
print(f'round(3.141592, 2): {round(3.141592, 2)}')

import math

# 절대값
print(f'math.fabs(-10): {math.fabs(-10)}')

# 올림
print(f'math.ceil(-5.21): {math.ceil(-5.21)}')

# 내림
print(f'math.floor(-5.21): {math.floor(-5.21)}')

# 버림
print(f'math.trunc(-5.21): {math.trunc(-5.21)}')

# 최대공약수
print(f'math.gcd(14, 21): {math.gcd(14, 21)}')

# 팩토리얼
print(f'math.factorial(10): {math.factorial(10)}')

# 제곱근
print(f'math.sqrt(10): {math.sqrt(10)}')

import time
lt = time.localtime()
print(f'time.localtime(): {lt}')

print(f'lt.tm_year: {lt.tm_year}')
print(f'lt.tm_mon: {lt.tm_mon}')
print(f'lt.tm_mday: {lt.tm_mday}')
print(f'lt.tm_hour: {lt.tm_hour}')
print(f'lt.tm_min: {lt.tm_min}')
print(f'lt.tm_sec: {lt.tm_sec}')
print(f'lt.tm_wday: {lt.tm_wday}')
# # 리스트에서 가장 앞에 있는 숫자 '7'을 검색하고 위치(인덱스)를 출력하자.
# nums = [4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9]
# searchNum = 7
# searchIdx = -1
#
# n = 0
# while n < len(nums):
#
#     if nums[n] == 7:
#         searchIdx = n
#         break
#
#     n += 1
#
# print(f'{searchNum}의 위치(인덱스)는 {searchIdx} 입니다.')

# 리스트에서 숫자 '7'을 모두 검색하고 각각의 위치(인덱스)와 검색 개수를 출력하자.
nums = [4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9]
searchNum = 7
searchIdx = []

n = 0
while n < len(nums):

    if nums[n] == 7:
        searchIdx.append(n)

    n += 1

print(f'{searchNum}의 위치(인덱스)는 {searchIdx} 이고, 개수는 {len(searchIdx)} 입니다.')




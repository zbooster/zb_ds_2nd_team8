nums = [4, 10 , 22, 5, 0, 17, 7, 11, 9, 61, 88]

print(f'nums: {nums}')
nums.sort()
print(f'nums: {nums}')

searchData = int(input('찾으려는 숫자 입력: '))
searchResultIdx = -1

staIdx = 0
endIdx = len(nums) - 1
midIdx = (staIdx + endIdx) // 2
midVal = nums[midIdx]
print(f'midIdx: {midIdx}')
print(f'midVal: {midVal}')

while searchData >= nums[0] and searchData <= nums[len(nums) - 1]:
    if searchData == midVal:
        searchResultIdx = midIdx
        break

    elif searchData < midVal:
        endIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = nums[midIdx]
        print(f'midIdx: {midIdx}')
        print(f'midVal: {midVal}')

    elif searchData > midVal:
        staIdx = midIdx + 1
        midIdx = (staIdx + endIdx) // 2
        midVal = nums[midIdx]
        print(f'midIdx: {midIdx}')
        print(f'midVal: {midVal}')

print(f'searchResultIdx: {searchResultIdx}')

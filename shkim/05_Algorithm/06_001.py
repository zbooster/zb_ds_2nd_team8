datas = [3, 2, 5, 7, 9, 1, 0, 8, 6, 4]
print(f'datas: {datas}')
print(f'datas length: {len(datas)}')

searchData = int(input('찾으려는 숫자 입력: '))
searchResultIdx = -1

datas.append(searchData)

n = 0
while True:

    if datas[n] == searchData:
        if n != len(datas) - 1:
            searchResultIdx = n
        break

    n += 1

print(f'datas: {datas}')
print(f'datas length: {len(datas)}')
print(f'searchResultIdx: [{searchResultIdx}]')
# group1 = ['홍길동', '박찬호', '이용규']
# group2 = ['김지은', '박승철', '강호동']
# print('group1: {}'.format(group1))
# print('group2: {}'.format(group2))

# group1.extend(group2)
# print('group1: {}'.format(group1))
# print('group2: {}'.format(group2))

# result = group1 + group2
# print('result: {}'.format(result))
# print('group1: {}'.format(group1))
# print('group2: {}'.format(group2))

myFavoriteNumbers = [1, 3, 5, 6, 7]
friendFavoriteNumbers = [2, 3, 5, 8, 10]

print('myFavoriteNumbers: {}'.format(myFavoriteNumbers))
print('friendFavoriteNumbers: {}'.format(friendFavoriteNumbers))

addList = myFavoriteNumbers + friendFavoriteNumbers
print('addList: {}'.format(addList))

result = myFavoriteNumbers

for number in friendFavoriteNumbers:
    if number not in result:
        result.append(number)

print('result: {}'.format(result))



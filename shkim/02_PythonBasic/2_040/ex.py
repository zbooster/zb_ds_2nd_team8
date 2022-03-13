import random
import datetime

custName = '홍길동'
productName = '야구글러브'


print('{} 고객님 안녕하세요.'.format(custName))
print('{} 고객님의 주문이 완료되었습니다.'.format(custName))
print('다음은 주문건에 대한 상세 내역입니다.')
print('-'*35)
print('상품명 \t: {}'.format(productName))
print('주문번호\t: {}'.format(random.randint(1000000, 9999999)))
print('결제방법\t: 신용카드')
print('상품금액\t: {} 원'.format(110000))
print('결제금액\t: {} 원'.format(100000))
print('포인트 \t: {} P'.format(10000))
print('결제일시\t: {}'.format(datetime.datetime.now()))
print('할부 \t: {} 개월'.format(6))
print('할부유형\t: {}'.format('무'))
print('문의 : 02-1234-5678')
print('-'*35)
print('저희 사이트를 이용해 주셔서 감사합니다.')


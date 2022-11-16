* 정합성의 확보는 데이터의 오류를 파악하는 것부터 시작한다.
<br>

* 상품 가격의 오류를 수정한다.<br>
~~~python
(참고) 측정 시점동안 상품의 가격은 변동되지 않는다.

flg_is_null = uriage['item_price'].isnull() # item_price 가 결측치인 정보를 flg_is_null 에 설정한다.

for trg in list(uriage.loc[flg_is_null, 'item_name'].unique()):
# item_price 가 결측치이면서 item_name 이 유일한 정보를 리스트형으로 변환하여 trg 에 설정한다.
    price = uriage.loc[(~flg_is_null) & (uriage['item_name'] == trg), 'item_price'].max()
    # item_price 가 결측치가 아닌 trg 에 해당하는 item_price 를 price 에 설정한다.
    uriage.loc[(flg_is_null) & (uriage['item_name'] == trg), 'item_price'] = price  
    # item_price 가 결측치인 trg 에 price 를 반영한다.
~~~
<br>

* 날짜의 형식을 일치화시킨다.<br>
~~~python
flg_is_serial = kokyaku_daicho['등록일'].astype('str').str.isdigit()
# 고객 정보의 등록일이 숫자인지 아닌지를 str.isdigit() 로 판정.
# 판정 결과, 숫자로 된 정보를 flg_is_serial 에 저장.

fromSerial = pd.to_timedelta(kokyaku_daicho.loc[flg_is_serial, '등록일'].astype('float'), unit='D') + pd.to_datetime('1900/01/01')
# loc() 를 이용하여 flg_is_serial 조건으로 데이터를 추출.
# to_timedelta(이름.astype('float'), unit='D') 을 이용하여 숫자 데이터를 '~일' 데이터로 변환.
# unit='D' 는 'days' 를 의미. '~일' 로 바꾸는 것.
# 42782 를 날짜 형태로 나타내면 '1900/01/01' 을 기준으로 42782 일을 더한, '2017/02/16' 이 된다.
~~~
<br>

* 두 개의 테이블을 합친다.
~~~python
join_data = pd.merge(uriage, kokyaku_daicho, left_on = 'customer_name', right_on = '고객이름', how = 'left')
# 서로 다른 열을 지정하여 두 개의 테이블을 합친다.

dump_data = join_data[['purchase_date', 'purchase_month', 'item_name', 'item_price', '고객이름', '지역', '등록일']]
# join_data 칼럼의 배치를 조정하여 dump_data 에 저장한다.

dump_data.to_csv('dump_data.csv', index = False)
# 수정한 dump_data 를 to_csv() 를 이용하여 파일로 저장한다.
~~~

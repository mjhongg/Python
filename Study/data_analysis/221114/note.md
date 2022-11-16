* 가시화 과정은 먼저 데이터를 집계하고, 집계된 데이터를 이용해 그래프를 그린다.

* matplotlib 을 이용해서 데이터를 집계한다.<br>
~~~python
import matplotlib.pyplot as plt
matplotilb inline # matplotlib 그래프는 가로축, 세로축의 순서로 지정.
plt.plot(list(graph_data.index), graph_data['PC-A'], label='PC-A')  # 가로축은 payment_month 를 표시해야 하므로 graph_data.index 를 리스트형으로 변환.
plt.plot(list(graph_data.index), graph_data['PC-B'], label='PC-B')  # 세로축은 상품별 매출이므로 graph_data 칼럼을 지정.
plt.plot(list(graph_data.index), graph_data['PC-C'], label='PC-C')
plt.plot(list(graph_data.index), graph_data['PC-D'], label='PC-D')
plt.plot(list(graph_data.index), graph_data['PC-E'], label='PC-E')
plt.legend()  # label 로 범례를 표시.
~~~


![image](https://user-images.githubusercontent.com/88098995/202056932-0ca4f9b8-b480-4d3a-9c8b-d243750162fd.png)<br><br>


* 날짜를 연월 형태로 변환한다.<br>
~~~python
uriage['purchase_date'] = pd.to_datetime(uriage['purchase_date'])
uriage['purchase_month'] = uriage['purchase_month'].dt.strftime("%Y%m")
~~~

* 데이터명 오류를 수정한다.<br>
~~~python
uriage['item_name'] = uriage['item_name'].str.upper()
uriage['item_name'] = uriage['item_name'].str.replace(' ','')
~~~

* pivot_table 로 집계 처리한다.<br>
~~~python
uriage.pivot_table(index = 'purchase_month', columns = 'item_name', values = 'item_price', aggfunc = 'sum', fill_value = 0)
~~~

![image](https://user-images.githubusercontent.com/88098995/202059654-95a96d07-9ffa-4089-81e8-9f493a45f4eb.png)

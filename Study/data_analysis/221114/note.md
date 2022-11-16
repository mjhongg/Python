* 가시화 과정은 먼저 데이터를 집계하고, 집계된 데이터를 이용해 그래프를 그린다.

* matplotlib 을 이용해서 데이터를 집계한다.<br>
~~~python
import matplotlib.pyplot as plt
matplotilb inline
plt.plot(list(graph_data.index), graph_data['PC-A'], label='PC-A')
plt.plot(list(graph_data.index), graph_data['PC-B'], label='PC-B')
plt.plot(list(graph_data.index), graph_data['PC-C'], label='PC-C')
plt.plot(list(graph_data.index), graph_data['PC-D'], label='PC-D')
plt.plot(list(graph_data.index), graph_data['PC-E'], label='PC-E')
plt.legend()
~~~


![image](https://user-images.githubusercontent.com/88098995/202056932-0ca4f9b8-b480-4d3a-9c8b-d243750162fd.png)


1. matplotlib 그래프는 가로축, 세로축의 순서로 지정.
2. 가로축은 payment_month 를 표시해야 하므로 graph_data.index 를 리스트형으로 변환.
3. 세로축은 상품별 매출이므로 graph_data 칼럼을 지정.
4. label 로 범례를 표시.

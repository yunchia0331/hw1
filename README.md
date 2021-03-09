# hw1
* 用for迴圈跑，將PRES數據為-99.000和-999.000的刪掉<br>
>for i in data:
>>   if i['PRES'] == '-99.000' or i['PRES'] == '-999.000':
>>>     i['PRES'] = '0'

* s表總和，a計算總個數，先初始化他們(以s1 a1為例)
>s1 = 0
>a1 = 0

* 用for迴圈跑，找出要的station_id的PRES值，並做總和和計算次數(0的不算一筆資料)
>for j in data:
>>   if j['station_id'] == 'C0A880' and j['PRES'] != '0':
>>>      a1 = a1 + 1 
>>>      s1 = s1 + float(j['PRES'])
>>   elif j['station_id'] == 'C0F9A0' and j['PRES'] != '0' :
>>>      a2 = a2 + 1 
>>>      s2 = s2 + float(j['PRES'])

* 計算平均<br>
>mean1 = s1 / a1

* 建一空的list
>alist = []

* 大的list內存小的list
** 若平均為0，輸出NONE(以round函數四捨五入至小數點下第2位)
>if mean1 == 0:
>>   alist.append(['C0A880', 'None'])
>else: 
>>   alist.append(['C0A880', round(mean1, 2)])

* 印出整個list
>print(alist)
* 結果為:[['C0A880', 1016.36], ['C0F9A0', 968.4], ['C0G640', 1017.25], ['C0R190', 1012.0], ['C0X260', 1012.63]]

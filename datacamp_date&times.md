## **Today**

Datacamp: Handling dates and times 공부하기

## **Datacamp_handling Dates and Time**

```python
'''From string to datetime
1) datetime module is part of the Python standard library
2) Use the datetime type from inside the datetime module
3) .strptime() method coverts from a string to a datetime object'''

from datetime import datetime 
print(parking_violations_date)
```

2021-06-10

```python
date_dt = datetime.strptime(parking_violations_date, '%m/%d/%Y')
```

## **Time Format Settings**

%d: 01,02,...,31

%m:  01,02....,12

%Y: 0001,0002,....9999

## **Datetime to String**

- .strftime() method uses a format string to convert a datetime object to a string date_dt.strftime('%m/%d/%Y')

'06/11/2016'

- isoformat() method outputs a datetime as an ISO standard string

```python
from datetime import datetime
for date_str in dates_list:
	date_dt = datetime.strptime(date_str, '%m/%d/%Y')

print(date_dt)
```

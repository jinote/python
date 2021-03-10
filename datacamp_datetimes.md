## **Today 21.3.10**

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

- .strftime() method uses a format string to convert a datetime object to a string

```python
date_dt.strftime('%m/%d/%Y')
```

06/11/2016

- isoformat() method outputs a datetime as an ISO standard string

```python
from datetime import datetime
for date_str in dates_list:
	date_dt = datetime.strptime(date_str, '%m/%d/%Y')

print(date_dt)
```

## Datetime  Components

- day, month, year, hour, minute, second, and more are available from a datetime instance
- Great for grouping data

```python
daily_violations =  defaultdict(int)
for violation in parking_violations:
	violation_date = datetime.strptime(violation[4],'%m/%d/%Y')

	daily_violations[violation_date.day]+=1

print(sorted(daily_violations.items()))
```

## What is the deal with now

- .now() method returns the current local datetime
- .utcnow() method returns the current UTC datetime

```python
from datetime import datetime
local_dt = datetime.now()
print(local_dt)
```

2017-05-05 12:30:00.740415

## What is the deal with utcnow

```python
utc_dt = datetime.utcnow()
print(utc_dt)
```

2017-05-05 17:30:05. 467221

## Timezones

- Naive datetime objects have no timezone date
- Aware datetime objects have a  timezone
- Timezone data is available via the 'pytz' module via the 'timezone' object
- Aware objects have '.astimezone()' so you can get the time in another timezone

## Timezones in action

```python
from pytz import timezone
record_dt = datetime.strptime('07/12/2016 04:39PM', .....: '%m/%d/%Y %H:%M%p')

ny_tz = timezone('US/Eastern')
a_tx = timezone('US/Pacific')
ny_dt = record_dt.replace(tzinfo=ny_tz)
la_dt = ny_dt.astimezone(la_tz)
print(ny_dt)
print(la_dt)
```

2016-07-12 04:39:00-04:00

2016-07-12 01:39:00-07:00

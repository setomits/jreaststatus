# What is this?

This is a python3 library to fetch service statuses of JR lines.


# How to use

```
>>> from pprint import pprint
>>> from jreast import JREast
>>> jr = JREast()

>>> pprint.pprint(jr.status('京葉線'))
{'area': 'kanto', 'line': '京葉線', 'statuses': [{'status': '平常運転'}]}

>>> pprint.pprint(jr.status('石巻線'))
{'area': 'tohoku',
 
 'line': '石巻線',
 'statuses': [{'detail': '石巻線は、大雨の影響で、石巻～女川駅間の上下線で運転を見合わせています。',
               'publishedAt': '2016年6月9日4時1分 配信',
               'status': '運転見合わせ'}]}

>>> pprint(jr.status('山田'))
{'area': None, 'line': '山田', 'status': None}
```

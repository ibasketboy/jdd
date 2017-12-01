# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


##   数据切分并输出
a = t_click.copy()
a['click_time_date'] = a.click_time.apply(lambda x:pd.to_datetime(x))
a['month'] = a.click_time_date.apply(lambda x:x.month)
click_Aug = a[a.month==8][['uid','click_time','pid','param']]
click_Sep = a[a.month==9][['uid','click_time','pid','param']]
click_Oct = a[a.month==10][['uid','click_time','pid','param']]
click_Nov = a[a.month==11][['uid','click_time','pid','param']]
del a


a = t_loan.copy()
a['loan_time_date'] = a.loan_time.apply(lambda x:pd.to_datetime(x))
a['month'] = a.loan_time_date.apply(lambda x:x.month)
loan_Aug = a[a.month==8][['uid','loan_time','loan_amount','plannum']]
loan_Sep = a[a.month==9][['uid','loan_time','loan_amount','plannum']]
loan_Oct = a[a.month==10][['uid','loan_time','loan_amount','plannum']]
loan_Nov = a[a.month==11][['uid','loan_time','loan_amount','plannum']]
del a

a = t_order.copy()
a['buy_time_date'] = a.buy_time.apply(lambda x:pd.to_datetime(x))
a['month'] = a.buy_time_date.apply(lambda x:x.month)
order_Aug = a[a.month==8][['uid','buy_time','price','qty','cate_id','discount']]
order_Sep = a[a.month==9][['uid','buy_time','price','qty','cate_id','discount']]
order_Oct = a[a.month==10][['uid','buy_time','price','qty','cate_id','discount']]
order_Nov = a[a.month==11][['uid','buy_time','price','qty','cate_id','discount']]
del a


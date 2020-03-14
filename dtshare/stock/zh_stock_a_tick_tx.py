# -*- coding:utf-8 -*-
# /usr/bin/env python
"""
Author: Tong Du
date: 2019/11/16 20:39
contact: dtshare@126.com
desc: 腾讯-股票-实时行情-成交明细
下载成交明细-每个交易日16:00提供当日数据
该列表港股报价延时15分钟
"""
from io import StringIO

import pandas as pd
import requests


def stock_zh_a_tick(code="sh600848", trade_date="20191011"):
    """
    成交明细-每个交易日16:00提供当日数据
    :param code: 带市场标识的股票代码
    :type code: str
    :param trade_date: 需要提取数据的日期
    :type trade_date: str
    :return: 返回当日股票成交明细的数据
    :rtype: pandas.DataFrame
    """
    url = "http://stock.gtimg.cn/data/index.php"
    params = {
        "appn": "detail",
        "action": "download",
        "c": code,
        "d": trade_date,
    }
    res = requests.get(url, params=params)
    res.encoding = "gbk"
    temp_df = pd.read_table(StringIO(res.text))
    return temp_df


if __name__ == "__main__":
    date_list = pd.date_range(start="20190801", end="20191111").tolist()
    date_list = [item.strftime("%Y%m%d") for item in date_list]
    for item in date_list:
        data = stock_zh_a_tick(code="sh601872", trade_date=f"{item}")
        if not data.empty:
            print(data)

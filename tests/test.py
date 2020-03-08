# -*- coding:utf-8 -*-
# /usr/bin/env python
"""
Author: Tong Du
Data:2019/10/12 18:16
Email: dtshare@126.com
desc: To test intention, just write test code here!
"""
from dtshare.cost.cost_living import cost_living


# def test_franchise_china():
#     """
#
#     :return:
#     :rtype: None
#     """
#     franchise_china_df = franchise_china()
#     assert franchise_china_df.shape[0] > 0


def test_cost_living():
    """

    :return:
    :rtype:
    """
    cost_living_df = cost_living()
    assert cost_living_df.shape[0] > 0


# def test_weibo_index():
#     """
#     test weibo_index interface
#     :return: weibo_index_df
#     :rtype: pandas.DataFrame
#     """
#     weibo_index_df = weibo_index(word="口罩", time_type="3month")
#     assert weibo_index_df.shape[0] > 0


if __name__ == "__main__":
    # test_weibo_index()
    # test_franchise_china()
    test_cost_living()

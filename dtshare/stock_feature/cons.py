# -*- coding:utf-8 -*-
# /usr/bin/env python
"""
Author: Tong Du
Data:2019/10/30 21:02
contact: dtshare@126.com
desc: 
"""
stock_em_sy_js = """
    function getCode(num) {
            var str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
            var codes = str.split('');
            num = num || 6;
            var code = "";
            for (var i = 0; i < num; i++) {
                code += codes[Math.floor(Math.random() * 52)]
            }
            return code
        }
    """

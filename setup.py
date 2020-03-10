# -*- coding:utf-8 -*-
# /usr/bin/env python
"""
@Author: Tony Yu
@Date: 2019-05-02 
@Contact: dtshare@126.com
@Group:DTShare Data
"""
import re
import ast
import setuptools

def get_version_string():
    with open("dtshare/__init__.py", "rb") as _f:
        version_line = re.search(
            r"__version__\s+=\s+(.*)", _f.read().decode("utf-8")
        ).group(1)
        return str(ast.literal_eval(version_line))

long_description = """
DTShare
===============

Target Users
--------------

* financial market analyst of China
* learners of financial data analysis with pandas/NumPy
* people who are interested in China financial data

Installation
--------------

    pip install dtshare
    
Upgrade
---------------

    pip install dtshare --upgrade
    
Quick Start
--------------

::

    import dtshare as dt
    
    dt.get_hist_data('600848')
    
return::

                open    high   close     low     volume    p_change  ma5 \
    
    date
    2012-01-11   6.880   7.380   7.060   6.880   14129.96     2.62   7.060
    2012-01-12   7.050   7.100   6.980   6.900    7895.19    -1.13   7.020
    2012-01-13   6.950   7.000   6.700   6.690    6611.87    -4.01   6.913
    2012-01-16   6.680   6.750   6.510   6.480    2941.63    -2.84   6.813
    2012-01-17   6.660   6.880   6.860   6.460    8642.57     5.38   6.822
    2012-01-18   7.000   7.300   6.890   6.880   13075.40     0.44   6.788
    2012-01-19   6.690   6.950   6.890   6.680    6117.32     0.00   6.770
    2012-01-20   6.870   7.080   7.010   6.870    6813.09     1.74   6.832
    
"""

setuptools.setup(
    name="dtshare",
    version=get_version_string(),
    author="Tony Du",
    license="MIT",
    description="Open financial data",
    long_description=long_description,
    url="https://github.com/DTShare/dtshare",
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy>=1.15.4",
        "pandas>=0.24",
        "requests>=2.22.0",
        "demjson>=2.2.4",
        "pyexecjs>=1.5.1",
        "pillow>=6.2.0",
        "pypinyin>=0.35.0",
        "websocket-client>=0.56.0",
        "pycryptodomex>=3.9.4",
        "html5lib>=1.0.1",
        "requests-html>=0.10.0",
        "scikit-learn>=0.22",
        "fonttools>=4.2.2",
        "xlrd>=1.2.0",
        "bs4>=0.0.1",
        "lxml>=4.2.1",
        "matplotlib>=3.1.1",
    ],
    package_data={"": ["*.py", "*.json", "*.csv"]},
    keywords=[
        "big data",
        "stock",
        "option",
        "futures",
        "fund",
        "bond",
        "finance index",
        "finance",
        "quant",
        "quantitative",
        "trading",
        "algotrading",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
)

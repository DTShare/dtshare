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

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

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

# -*- coding:utf-8 -*-
# /usr/bin/env python

__version__ = "1.0.1"
__author__ = "Tony Du"


"""
股票行情
"""

from dtshare.stock.trading import (
    get_tick_data,
    get_k_data,
    get_hist_data,
    get_index,
)


"""
期货日线情数据
"""
from dtshare.futures.daily_bar import (
    get_cffex_daily,
    get_czce_daily,
    get_shfe_v_wap,
    get_shfe_daily,
    get_dce_daily,
    get_futures_daily,
)


"""
微博舆情报告
"""
from dtshare.stock.stock_weibo_nlp import stock_js_weibo_nlp_time, stock_js_weibo_report

"""
金融期权-新浪
"""
from dtshare.option.option_finance_sina import (
    option_sina_cffex_hs300_list,
    option_sina_cffex_hs300_spot,
    option_sina_cffex_hs300_daily,
    option_sina_sse_list,
    option_sina_sse_expire_day,
    option_sina_sse_codes,
    option_sina_sse_spot_price,
    option_sina_sse_underlying_spot_price,
    option_sina_sse_greeks,
    option_sina_sse_minute,
    option_sina_sse_daily,
)

"""
中国-慈善
"""
from dtshare.charity.charity_china import (
    charity_china_organization,
    charity_china_plan,
    charity_china_platform,
    charity_china_progress,
    charity_china_report,
    charity_china_trust,
)

"""
中国-特许经营数据
"""
from dtshare.event.franchise import franchise_china

"""
债券-沪深债券
"""
from dtshare.bond.zh_bond_sina import bond_zh_hs_daily, bond_zh_hs_spot
from dtshare.bond.zh_bond_cov_sina import bond_zh_hs_cov_daily, bond_zh_hs_cov_spot



from dtshare.currency.currency import (
    currency_convert,
    currency_currencies,
    currency_history,
    currency_latest,
    currency_time_series,
)


"""
债券质押式回购成交明细数据
"""
from dtshare.bond.china_repo import bond_repo_zh_tick

"""
新型肺炎
"""
from dtshare.event.sos import (
    epidemic_area_search,
    epidemic_area_all,
    epidemic_area_detail,
    epidemic_trip,
    epidemic_history,
)

"""
基金数据接口
"""
from dtshare.fund.fund_em import fund_em_daily, fund_em_info

"""
百度迁徙地图接口
"""
from dtshare.event.sos import migration_area_baidu, migration_scale_baidu

"""
新增-事件接口新型冠状病毒接口
"""
from dtshare.event.sos import (
    epidemic_163,
    epidemic_dxy,
    epidemic_baidu,
    epidemic_hist_all,
    epidemic_hist_city,
    epidemic_hist_province,
)

"""
英为财情-外汇-货币对历史数据
"""
from dtshare.fx.currency_investing import (
    currency_hist,
    currency_name_code,
)

"""
商品期权-郑州商品交易所-期权-历史数据
"""
from dtshare.option.czce_option import option_czce_hist

"""
宏观-经济数据-银行间拆借利率
"""
from dtshare.interest_rate.interbank_rate_em import rate_interbank

"""
东方财富网-经济数据-银行间拆借利率
"""
from dtshare.interest_rate.interbank_rate_em import rate_interbank

"""
金十数据中心-外汇情绪
"""
from dtshare.economic.macro_other import macro_fx_sentiment

"""
金十数据中心-经济指标-欧元区
"""
from dtshare.economic.macro_euro import (
    macro_euro_gdp_yoy,
    macro_euro_cpi_mom,
    macro_euro_cpi_yoy,
    macro_euro_current_account_mom,
    macro_euro_employment_change_qoq,
    macro_euro_industrial_production_mom,
    macro_euro_manufacturing_pmi,
    macro_euro_ppi_mom,
    macro_euro_retail_sales_mom,
    macro_euro_sentix_investor_confidence,
    macro_euro_services_pmi,
    macro_euro_trade_balance,
    macro_euro_unemployment_rate_mom,
    macro_euro_zew_economic_sentiment,
)

"""
金十数据中心-经济指标-央行利率-主要央行利率
"""
from dtshare.economic.macro_bank import (
    macro_bank_australia_interest_rate,
    macro_bank_brazil_interest_rate,
    macro_bank_china_interest_rate,
    macro_bank_brazil_interest_rate,
    macro_bank_english_interest_rate,
    macro_bank_euro_interest_rate,
    macro_bank_india_interest_rate,
    macro_bank_japan_interest_rate,
    macro_bank_newzealand_interest_rate,
    macro_bank_russia_interest_rate,
    macro_bank_switzerland_interest_rate,
    macro_bank_usa_interest_rate,
)

"""
交易法门-工具-席位分析
"""
from dtshare.futures_derivative.jyfm_tools_func import jyfm_tools_position_structure

"""
交易法门-工具-套利分析
"""
from dtshare.futures_derivative.jyfm_tools_func import (
    jyfm_tools_futures_spread,
    jyfm_tools_futures_ratio,
    jyfm_tools_futures_customize,
    jyfm_exchange_symbol_dict,
    jyfm_tools_futures_full_carry,
)

"""
交易法门-工具-资讯汇总
"""
from dtshare.futures_derivative.jyfm_tools_func import (
    jyfm_tools_research_query,
    jyfm_tools_trade_calendar,
)

"""
交易法门-工具-持仓分析
"""
from dtshare.futures_derivative.jyfm_tools_func import (
    jyfm_tools_position_detail,
    jyfm_tools_position_seat,
    jyfm_tools_position_season,
)

"""
交易法门-工具-资金分析
"""
from dtshare.futures_derivative.jyfm_tools_func import (
    jyfm_tools_position_fund_direction,
    jyfm_tools_position_fund_down,
    jyfm_tools_position_fund_season,
    jyfm_tools_position_fund_deal,
)

"""
交易法门-工具-仓单分析
"""
from dtshare.futures_derivative.jyfm_tools_func import (
    jyfm_tools_warehouse_receipt_daily,
    jyfm_tools_warehouse_receipt_query,
    jyfm_tools_warehouse_virtual_fact_ratio,
    jyfm_tools_warehouse_virtual_fact_daily,
)

"""
交易法门-工具-期限分析
"""
from dtshare.futures_derivative.jyfm_tools_func import (
    jyfm_tools_futures_basis_daily,
    jyfm_tools_futures_basis_daily_area,
    jyfm_tools_futures_basis_analysis,
    jyfm_tools_futures_basis_structure,
    jyfm_tools_futures_basis_rule,
)

"""
交易法门-工具-交易规则
"""
from dtshare.futures_derivative.jyfm_tools_func import (
    jyfm_tools_receipt_expire_info,
    jyfm_tools_position_limit_info,
    jyfm_tools_symbol_handbook,
)

"""
义乌小商品指数
"""
from dtshare.index.index_yw import index_yw

"""
股票指数-股票指数-成份股
"""
from dtshare.index.index_cons import (
    index_stock_info,
    index_stock_cons,
)

"""
交易法门-工具-数据-黑色系
"""
from dtshare.futures_derivative.jyfm_data_func import (
    jyfm_data_cocking_coal,
    jyfm_data_coke,
)

"""
东方财富-股票账户
"""
from dtshare.stock_feature.stock_em_account import stock_em_account

"""
期货规则
"""
from dtshare.futures.futures_rule import futures_rule

"""
东方财富-商誉专题
"""
from dtshare.stock_feature.stock_em_sy import (
    stock_em_sy_profile,
    stock_em_sy_yq_list,
    stock_em_sy_jz_list,
    stock_em_sy_list,
    stock_em_sy_hy_list,
)

"""
东方财富-股票质押
"""
from dtshare.stock_feature.stock_em_gpzy import (
    stock_em_gpzy_pledge_ratio,
    stock_em_gpzy_profile,
    stock_em_gpzy_distribute_statistics_bank,
    stock_em_gpzy_distribute_statistics_company,
    stock_em_gpzy_industry_data,
    stock_em_gpzy_pledge_ratio_detail,
)

"""
东方财富-机构调研
"""
from dtshare.stock_feature.stock_em_jgdy import stock_em_jgdy_tj, stock_em_jgdy_detail

"""
新浪主力连续接口
"""
from dtshare.fortune.it_juzi import death_company, maxima_company, nicorn_company

"""
新浪主力连续接口
"""
from dtshare.futures_derivative.sina_futures_index import (
    futures_main_sina,
    futures_display_main_sina,
)

"""
中国宏观杠杆率数据
"""
from dtshare.economic.marco_cnbs import macro_cnbs

"""
大宗商品-现货价格指数
"""
from dtshare.index.index_spot import spot_goods

"""
成本-世界各大城市生活成本
"""
from dtshare.cost.cost_living import cost_living

"""
能约-碳排放权
"""
from dtshare.energy.energy_carbon import energy_carbon

"""
猫眼电影实时票房
"""
from dtshare.movie.movie_maoyan import box_office_spot

"""
中国证券投资基金业协会-信息公示
"""
from dtshare.fund.fund_amac import (
    amac_manager_info,
    amac_member_info,
    amac_member_sub_info,
    amac_aoin_info,
    amac_fund_account_info,
    amac_fund_info,
    amac_fund_sub_info,
    amac_futures_info,
    amac_manager_cancelled_info,
    amac_securities_info,
    amac_fund_abs,
    amac_manager_classify_info,
    amac_manager_xxgs_cxdj,
    amac_manager_xxgs_hmd,
    amac_manager_xxgs_jlcf,
    amac_person_org_list,
    amac_person_org_list_ext,
)

"""
世界五百强公司排名接口
"""
from dtshare.fortune.fortune_500 import fortune_rank, fortune_rank_eng

"""
AQI空气质量接口
"""
from dtshare.air.aqi_study import air_all_city, air_city_list, air_daily, air_hourly

"""
申万行业一级
"""
from dtshare.index.index_sw import (
    sw_index_spot,
    sw_index_cons,
    sw_index_daily,
    sw_index_daily_indicator,
)

"""
交易法门-数据-农产品
"""
from dtshare.futures_derivative.jyfm_data_func import (
    jyfm_data_palm,  # 棕榈
    jyfm_data_soybean_meal,  # 豆粕
    jyfm_data_sugar,  # 白糖
    jyfm_data_usa_bean,  # 美豆
    jyfm_data_soybean_oil,  # 豆油
)

"""
交易法门-工具
"""
from dtshare.futures_derivative.jyfm_tools_func import (
    jyfm_tools_futures_customize,  # 棕榈
    jyfm_tools_futures_ratio,  # 豆粕
    jyfm_tools_futures_spread,  # 白糖
    jyfm_tools_receipt_expire_info,  # 美豆
)

"""
交易法门-登录
"""
from dtshare.futures_derivative.jyfm_login_func import jyfm_login

"""
谷歌指数
"""
from dtshare.index.index_google import google_index

"""
百度指数
"""
from dtshare.index.index_baidu import (
    baidu_search_index,
    baidu_info_index,
    baidu_media_index,
)

"""
微博指数
"""
from dtshare.index.index_weibo import weibo_index

"""
经济政策不确定性指数
"""
from dtshare.article.epu_index import article_epu_index

"""
南华期货-南华指数
"""
from dtshare.futures_derivative.nh_index_return import nh_return_index
from dtshare.futures_derivative.nh_index_price import nh_price_index
from dtshare.futures_derivative.nh_index_volatility import nh_volatility_index

"""
空气-河北
"""
from dtshare.air.air_hebei import air_hebei

"""
timeanddate-日出和日落
"""
from dtshare.air.time_and_date import weather_daily, weather_monthly


"""
新浪-指数实时行情和历史行情
"""
from dtshare.stock.zh_stock_a_tick_tx import stock_zh_a_tick

"""
新浪-指数实时行情和历史行情
"""
from dtshare.index.zh_stock_index_sina import (
    stock_zh_index_daily,
    stock_zh_index_spot,
    stock_zh_index_daily_tx,
)

"""
外盘期货实时行情
"""
from dtshare.futures.hf_futures_sina import (
    futures_hf_spot,
    hf_subscribe_exchange_symbol,
)

"""
FF多因子数据接口
"""
from dtshare.article.ff_factor import article_ff_crr

"""
Realized Library 接口
"""
from dtshare.article.risk_rv import (
    article_oman_rv,
    article_oman_rv_short,
    article_rlab_rv,
)

"""
银保监分局本级行政处罚数据
"""
from dtshare.bank.bank_cbirc_2020 import bank_fjcf_table_detail

"""
科创板股票
"""
from dtshare.stock.zh_stock_kcb_sina import stock_zh_kcb_spot, stock_zh_kcb_daily

"""
A股
"""
from dtshare.stock.zh_stock_a_sina import stock_zh_a_spot, stock_zh_a_daily

"""
A+H股
"""
from dtshare.stock.zh_stock_ah_tx import (
    stock_zh_ah_spot,
    stock_zh_ah_daily,
    stock_zh_ah_name,
)

"""
数字货币
"""
from dtshare.economic.macro_other import get_js_dc_current

"""
金融期权
"""
from dtshare.option.option_finance import (
    option_finance_board,
    option_finance_underlying,
)

"""
新浪-美股实时行情数据和历史行情数据(前复权)
"""
from dtshare.stock.us_stock_sina import stock_us_daily, stock_us_spot, get_us_stock_name

"""
新浪-港股实时行情数据和历史数据(前复权和后复权因子)
"""
from dtshare.stock.hk_stock_sina import stock_hk_daily, stock_hk_spot

"""
新浪-期货实时数据
"""
from dtshare.futures.zh_futures_sina import futures_zh_spot, match_main_contract

"""
西本新干线-指数数据
"""
from dtshare.futures_derivative.xgx_data import get_code_pic, xgx_data

"""
生意社-商品与期货-现期图数据
"""
from dtshare.futures_derivative.sys_spot_futures import (
    get_sys_spot_futures,
    get_sys_spot_futures_dict,
)

"""
交易法门-套利工具-跨期价差(自由价差)
"""
from dtshare.futures_derivative.jyfm_tools_func import (
    jyfm_tools_futures_ratio,
    jyfm_tools_futures_customize,
    jyfm_tools_futures_spread,
)

"""
和讯财经-行情及历史数据
"""
from dtshare.stock.us_zh_stock_hx import stock_us_zh_spot, stock_us_zh_daily

"""
和讯财经-企业社会责任
"""
from dtshare.stock.zh_stock_zrbg_hx import stock_zh_a_scr_report

"""
期货-仓单有效期
"""
from dtshare.futures.receipt_period import get_receipt_date

"""
全球宏观-机构宏观
"""
from dtshare.economic.macro_constitute import (
    macro_cons_gold_amount,
    macro_cons_gold_change,
    macro_cons_gold_volume,
    macro_cons_opec_month,
    macro_cons_opec_near_change,
    macro_cons_silver_amount,
    macro_cons_silver_change,
    macro_cons_silver_volume,
)

"""
全球宏观-美国宏观
"""
from dtshare.economic.macro_usa import (
    macro_usa_eia_crude_rate,
    macro_usa_non_farm,
    macro_usa_unemployment_rate,
    macro_usa_adp_employment,
    macro_usa_core_pce_price,
    macro_usa_cpi_monthly,
    macro_usa_crude_alaska,
    macro_usa_crude_inner,
    macro_usa_crude_state,
    macro_usa_gdp_monthly,
    macro_usa_initial_jobless,
    macro_usa_lmci,
    macro_usa_api_crude_stock,
    macro_usa_building_permits,
    macro_usa_business_inventories,
    macro_usa_cb_consumer_confidence,
    macro_usa_core_cpi_monthly,
    macro_usa_core_ppi,
    macro_usa_current_account,
    macro_usa_durable_goods_orders,
    macro_usa_trade_balance,
    macro_usa_spcs20,
    macro_usa_services_pmi,
    macro_usa_rig_count,
    macro_usa_retail_sales,
    macro_usa_real_consumer_spending,
    macro_usa_ppi,
    macro_usa_pmi,
    macro_usa_personal_spending,
    macro_usa_pending_home_sales,
    macro_usa_nfib_small_business,
    macro_usa_new_home_sales,
    macro_usa_nahb_house_market_index,
    macro_usa_michigan_consumer_sentiment,
    macro_usa_exist_home_sales,
    macro_usa_export_price,
    macro_usa_factory_orders,
    macro_usa_house_price_index,
    macro_usa_house_starts,
    macro_usa_import_price,
    macro_usa_industrial_production,
    macro_usa_ism_non_pmi,
    macro_usa_ism_pmi,
    macro_usa_job_cuts,
)

"""
全球宏观-中国宏观
"""
from dtshare.economic.macro_china import (
    macro_china_cpi_monthly,
    macro_china_cpi_yearly,
    macro_china_m2_yearly,
    macro_china_fx_reserves_yearly,
    macro_china_cx_pmi_yearly,
    macro_china_pmi_yearly,
    macro_china_daily_energy,
    macro_china_non_man_pmi,
    macro_china_rmb,
    macro_china_gdp_yearly,
    macro_china_ppi_yearly,
    macro_china_cx_services_pmi_yearly,
    macro_china_market_margin_sh,
    macro_china_market_margin_sz,
    macro_china_au_report,
    macro_china_ctci_detail,
    macro_china_ctci_detail_hist,
    macro_china_ctci,
    macro_china_exports_yoy,
    macro_china_hk_market_info,
    macro_china_imports_yoy,
    macro_china_trade_balance,
    macro_china_shibor_all,
    macro_china_industrial_production_yoy,
)

"""
全球期货
"""
from dtshare.futures.international_futures import get_sector_futures

"""
外汇
"""
from dtshare.fx.fx_quote import fx_pair_quote, fx_spot_quote, fx_swap_quote

"""
债券行情
"""
from dtshare.bond.china_bond import bond_spot_quote, bond_spot_deal, bond_china_yield

"""
商品期权
"""
from dtshare.option.option_commodity import (
    get_dce_option_daily,
    get_czce_option_daily,
    get_shfe_option_daily,
)

"""
英为财情-债券
"""
from dtshare.bond.investing_bond import get_country_bond  # 债券-全球政府债券行情与收益率

"""
英为财情-指数
"""
from dtshare.index.index_investing import get_country_index  # 股票指数-全球股指与期货指数数据接口

"""
99期货数据
"""
from dtshare.futures.futures_inventory import get_inventory_data

"""
私募指数
"""
from dtshare.fund.fund_zdzk import zdzk_fund_index

"""
中国银行间市场交易商协会
"""
from dtshare.bond.bond_bank import get_bond_bank

"""
大宗商品现货价格及基差
"""
from dtshare.futures.basis import get_spot_price_daily, get_spot_price

"""
期货持仓成交排名数据
"""
from dtshare.futures.cot import (
    get_rank_sum_daily,
    get_rank_sum,
    get_shfe_rank_table,
    get_czce_rank_table,
    get_dce_rank_table,
    get_cffex_rank_table,
)

"""
大宗商品仓单数据
"""
from dtshare.futures.receipt import get_receipt

"""
大宗商品展期收益率数据
"""
from dtshare.futures.roll_yield import get_roll_yield_bar, get_roll_yield

"""
配置文件
"""
from dtshare.futures import cons
from dtshare.fund import cons


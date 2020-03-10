# DTShare

----------

DT时代的数据共享和应用，为用户提供优质便捷的数据。

首先，要感谢金融开放数据的“鼻祖”项目——[Tushare](http://github.com/waditu/tushare)，为开放的金融数据开辟了道路提供了思路，引领数据逐步走向开放，同时也为业界提供了足够多的开源代码够业界学习和参考。更多Tushare信息请访问[Tushare官网](https://tushare.pro "Tushare")。

其次，感谢所有DTShare用户的关注。我们将继续努力，为数据事业贡献力量。同时也欢迎更多小伙伴一起加入我们，为数据，为AI落地，为实现自己的价值，共同努力。


![](http://dt-share.com/img/dtshare-logo.png)

DTShare是一个完全开源免费的数据开放项目。
在DT和AI时代，数据是最宝贵的资源，是驱动信息智能化的第一生产资料。我们立志收集和整理各行各业的开放数据，为用户实现数据便捷的获取。截至到目前，我们主要从证券金融作为为出发点，提供了包括股票、期货、基金和宏观经济等方面的数据，在不久的将来，将会提供更多的数据。竭诚为用户服务！


详细的使用说明和文档，请访问官网地址：[http://dt-share.com](http://dt-share.com)

# 安装 #

> pip install dtshare

# 升级 #

> pip install dtshare --upgrade


# 使用示例1 ：获取实时tick行情（包含集合竞价）

> import dtshare as dt
> 
> 
> df = dt.get\_tick_data('600868')
> 
> print(df)

             time  price  vol type
	0     091503  21.64   29    -
	1     091509  21.65   93    -
	2     091536  21.64  129    -
	3     092427  21.63  295    -
	4     092442  21.62  295    -
	...      ...    ...  ...  ...
	2105  145652  21.46   16   买入
	2106  145655  21.46   52   买入
	2107  145658  21.46    3   买入
	2108  145702  21.47    2   卖出
	2109  150059  21.46  415   买入

可以获取到个股的实时tick数据，指标分别为：

- time ：交易时间
- price：成交价格
- vol：成交量
- type：买卖方向

# 使用示例2： 获取指数实时行情和列表

> import dtshare as dt
> 
> df = dt.get_index()
> print(df)

          code   name    change  ...        low       volume     amount
	0   000001   上证指数   -1.21  ...  3029.4632    362061533  3773.8854
	1   000002   Ａ股指数   -1.21  ...  3174.6675    361838944  3772.7966
	2   000003   Ｂ股指数   -0.21  ...   241.3628       222589     1.0889
	3   000008   综合指数   -1.45  ...  2820.4868     71442864   719.6169
	4   000009  上证380   -0.72  ...  5013.0374     73600788   764.3923
	..     ...    ...     ...  ...        ...          ...        ...
	21  399106   深证综指   -0.74  ...  1902.6370  53885674076  5801.0435
	22  399107   深证Ａ指   -0.74  ...  1990.7430  53861659420  5800.1456
	23  399108   深证Ｂ指   -0.41  ...   940.0110     24014656     0.8979
	24  399333   中小板R   -0.89  ...  8466.0090   4774643669   841.8404
	25  399606   创业板R   -0.75  ...  2294.6250   2790377749   628.8269




# 数据来源  #

感谢以下优秀的网站提供的公开披露数据：

[上海证券交易所网站](http://www.sse.com.cn/assortment/options/price/)：市场数据;

[深证证券交易所网站](http://www.szse.cn/)：市场数据;

[中国金融期货交易所网站](http://www.cffex.com.cn/)：期货数据;

[上海期货交易所网站](http://www.shfe.com.cn/)：期货数据;

[大连商品交易所网站](http://www.dce.com.cn/)：期货数据;

[郑州商品交易所网站](http://www.czce.com.cn/)：期货数据;

[上海国际能源交易中心网站](http://www.ine.com.cn/)：期货数据;

[中国外汇交易中心暨全国银行间同业拆借中心网站](http://www.chinamoney.com.cn/chinese/)：外汇数据;

[中国证券投资基金业协会](http://gs.amac.org.cn/)：私募基金数据;

[新浪财经网站](https://finance.sina.com.cn/)：综合金融数据;

[东方财富网站](http://data.eastmoney.com/jgdy/)：市场数据;

[生意社网站](http://www.100ppi.com/)：有色金属数据;

[中国银行间市场交易商协会网站](http://www.nafmii.org.cn/)：银行间交易数据;

[99期货网站](http://www.99qh.com/)：期货数据;

[英为财情网站](https://cn.investing.com/)：行情数据;

[金十数据网站](https://www.jin10.com/)：新闻资讯数据;

[交易法门网站](https://www.jiaoyifamen.com/)：行情数据;

[和讯财经网站](http://www.hexun.com/)：行情数据;

[智道智科网站](https://www.ziasset.com/)：指数市场数据;

[timeanddate网站](https://www.timeanddate.com/)：日出和日落数据;

[河北省空气质量预报信息发布系统网站](http://110.249.223.67/publish/)：河北省空气质量数据;

[南华期货网站](http://www.nanhua.net/nhzc/varietytrend.html)：期货指数数据;

[Economic Policy Uncertainty网站](http://www.nanhua.net/nhzc/varietytrend.html)经济政策不确定性(EPU)指数数据;

[微博指数](https://data.weibo.com/index/newindex)：微博指数数据;

[义乌小商品指数网站](http://www.ywindex.com/Home/Product/index/)：小商品交易数据;

[中国国家发展和改革委员会网站](http://jgjc.ndrc.gov.cn/dmzs.aspx?clmId=741)：宏观数据;

[网易新闻](https://news.163.com/special/epidemic/)：新闻资讯数据;

[丁香园网站](http://3g.dxy.cn/newh5/view/pneumonia?scene=2&clicktime=1579615030&enterid=1579615030&from=groupmessage&isappinstalled=0)：疫情数据;

[百度网站](https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_1)：大数据;

[百度迁徙网站](https://qianxi.baidu.com/?from=shoubai#city=0)：大数据;

[新型肺炎-相同行程查询工具网站](https://rl.inews.qq.com/h5/trip?from=newsapp&ADTAG=tgi.wx.share.message)：疫情数据;

[新型肺炎-小区查询](https://ncov.html5.qq.com/community?channelid=1&from=singlemessage&isappinstalled=0)：疫情数据;

[商业特许经营信息管理网站](http://txjy.syggs.mofcom.gov.cn/)：市场数据;

[慈善中国网站](http://cishan.chinanpo.gov.cn/platform/login.html)：慈善数据;


[百度指数](http://index.baidu.com/v2/main/index.html)：百度指数数据;

[谷歌指数](https://trends.google.com/trends/?geo=US)：谷歌趋势指数数据;

[申万指数](http://www.swsindex.com/idx0120.aspx?columnid=8832)：行业指数数据;

[AQI空气质量数据](https://www.aqistudy.cn/)：空气质量数据;

[财富网站](http://www.fortunechina.com/)：财富企业世界500强数据;

[猫眼电影](https://maoyan.com/board/1)：实时票房数据;

[Expatistan网站](https://www.expatistan.com/cost-of-living)：世界各大城市生活成本数据;

[国家金融与发展实验室网站](http://www.nifd.cn/)：宏观杠杆率;

[北京市碳排放权电子交易平台](https://www.bjets.com.cn/article/jyxx/)：碳排放行情数据;

[IT桔子](https://www.itjuzi.com)：投融资数据;


更多数据上线中.....




## 交流与联系

您可以关注我们的微信公众号来获取最新的信息:

![](http://dt-share.com/img/weixin.png)

也欢迎加入官方QQ群交流: **1072948998**

![](http://dt-share.com/img/dtshare_qq.png)

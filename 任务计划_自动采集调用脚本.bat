D:
cd D:\spider\fb_sporrtery

rem 采集14场
scrapy crawl spd_sporttery_14match

rem 采集竞彩比赛
scrapy crawl spd_sporttery_JCmatch

rem 采集竞彩支持率
scrapy crawl spd_sporttery_JCmatchSupport

rem 采集奖金对比页面
scrapy crawl spd_sporttery_JCBonus

rem 采集固定奖金页面
scrapy crawl spd_sporttery_JCFixationBonus

rem 采集竞彩网比赛信息
scrapy crawl spd_sporttery_JCMatchInfo

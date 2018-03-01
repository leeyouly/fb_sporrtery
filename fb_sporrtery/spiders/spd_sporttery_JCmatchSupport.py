# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Spider
from fb_sporrtery.items import Football_sporttery_JCMatchSupportItem
import time, datetime
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
last_update_date = datetime.datetime.now() - datetime.timedelta(days=1)

class Sporttery_JCmatchSupport(Spider):
    name = "spd_sporttery_JCmatchSupport"
    start_urls = (
        'http://info.sporttery.cn/football/hhad_list.php',
    )
    ignore_page_incremental = True

    def parse(self, response):
        self.crawler.stats.set_value('spiderlog/source_name', u'T_SPORTTERY_JCMATCHSUPPORT')
        self.crawler.stats.set_value('spiderlog/target_tables', ['T_SPORTTERY_JCMATCHSUPPORT'])
        url = 'http://i.sporttery.cn/odds_calculator/get_proportion?i_format=json&pool[]=had&pool[]=hhad&i_callback=getReferData1&_=1510980021272'
        request = scrapy.http.Request(url, callback=self.parse_sporttery_content)
        yield request

    def parse_sporttery_content(self, response):
        content = response.body
        #得到第一个Id值
        matchId = int(re.findall("_(.+?)\":", content)[0])
        re.findall('getReferData1(\s\S+)',content)
        data_dict = eval(re.findall('getReferData1(.+);',content)[0])
        data_dict_len = len(data_dict['data'])
        for oddskey in ['had','hhad']:
            for row in range(data_dict_len):
                item = Football_sporttery_JCMatchSupportItem()
                if oddskey == 'had':
                    #判断oddskey是否存在，因为当此场比赛为开售时，则无赔率指标
                    if oddskey in data_dict['data'][data_dict['data'].keys()[row]].keys() :
                        item['win'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['win']
                        item['draw'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['draw']
                        item['lose'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['lose']
                        item['mid'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['mid']
                        item['num'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['num']
                        item['pre_draw'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['pre_draw']
                        item['pre_lose'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['pre_lose']
                        item['pre_win'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['pre_win']
                        item['total'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['total']
                        item['ctype'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['type']
                    else:
                        #当因为停售或者其他原因，取不到had这个key时，默认用hhad的mid来保证记录的完整性
                        item['mid'] = data_dict['data'][data_dict['data'].keys()[row]]['hhad']['mid']
                        item['ctype'] = 'had'
                elif oddskey == 'hhad':
                    # 判断oddskey是否存在，因为当此场比赛为开售时，则无赔率指标
                    if oddskey in data_dict['data'][data_dict['data'].keys()[row]].keys() :
                        item['win'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['win']
                        item['draw'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['draw']
                        item['lose'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['lose']
                        item['mid'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['mid']
                        item['num'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['num']
                        item['pre_draw'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['pre_draw']
                        item['pre_lose'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['pre_lose']
                        item['pre_win'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['pre_win']
                        item['total'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['total']
                        item['ctype'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['type']
                    else:
                        # 当因为停售或者其他原因，取不到had这个key时，默认用had的mid来保证记录的完整性
                        item['mid'] = data_dict['data'][data_dict['data'].keys()[row]]['had']['mid']
                        item['ctype'] = 'hhad'
                yield item

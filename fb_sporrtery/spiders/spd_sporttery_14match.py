# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Spider
from fb_sporrtery.items import Football_sporttery_14MatchItem,Football_sporttery_loseMatchId
import time, datetime
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
last_update_date = datetime.datetime.now() - datetime.timedelta(days=1)

class Sporttery_14match(Spider):
    name = "spd_sporttery_14match"
    start_urls = (
        'http://info.sporttery.cn/football/hhad_list.php',
    )
    ignore_page_incremental = True

    def parse(self, response):
        self.crawler.stats.set_value('spiderlog/source_name', u'spd_sporttery_14match')
        self.crawler.stats.set_value('spiderlog/target_tables', ['spd_sporttery_14match'])

        for row in range(1,196,1):
            url = 'http://i.sporttery.cn/wap/fb_lottery/fb_lottery_match?key=wilo&num='+str(17000 + row)+'&f_callback=getDataBack&_=1510996740996'
            request = scrapy.http.Request(url, callback=self.parse_sporttery_content)
            request.meta['term'] = str(17000 + row)
            yield request

    def parse_sporttery_content(self, response):
        term = response.meta['term']
        #得到第一个Id值
        if 'getDataBack();' == response.body:
            item = Football_sporttery_loseMatchId()
            item['matchid'] = None
            item['spidername'] = 'spd_sporttery_14match'
            item['tablename'] = 'T_SPORTTERY_14MATCH'
            item['url'] = response.url
            item['losereason'] = u'此matchId无数据返回，可能是此Id本身没有比赛，或者此Id过大，还未绑定比赛'
            yield item
        else:
            data_dict = eval(re.findall('getDataBack(.+);',response.body)[0])
            data_dict_len = len(data_dict['result'])
            for row in range(data_dict_len):
                item = Football_sporttery_14MatchItem()
                item['term']     = term
                if [data_dict['result'].keys()[row]]<>[]:
                    item['id']     = str([data_dict['result'].keys()[row]][0])
                    if 'mid' in data_dict['result'][data_dict['result'].keys()[row]].keys() :
                        item['mid']     = str(data_dict['result'][data_dict['result'].keys()[row]]['mid'])
                    item['home_team']    = data_dict['result'][data_dict['result'].keys()[row]]['h_cn'].decode("unicode_escape")
                    item['guest_team']    = data_dict['result'][data_dict['result'].keys()[row]]['a_cn'].decode("unicode_escape")
                    item['league_name']    = data_dict['result'][data_dict['result'].keys()[row]]['league'].decode("unicode_escape")

                    item['odds_win']    = data_dict['result'][data_dict['result'].keys()[row]]['h']
                    item['odds_draw']    = data_dict['result'][data_dict['result'].keys()[row]]['d']
                    item['odds_lose']    = data_dict['result'][data_dict['result'].keys()[row]]['a']
                    item['full']    = data_dict['result'][data_dict['result'].keys()[row]]['full']
                    item['result']    = str(data_dict['result'][data_dict['result'].keys()[row]]['result'])

                    item['time']    = data_dict['result'][data_dict['result'].keys()[row]]['date'] +' '+ data_dict['result'][data_dict['result'].keys()[row]]['time']
                    yield item

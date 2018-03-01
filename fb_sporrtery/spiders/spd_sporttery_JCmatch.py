# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Spider
from fb_sporrtery.items import Football_sporttery_JCItem,Football_sporttery_loseMatchId
import time, datetime
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
last_update_date = datetime.datetime.now() - datetime.timedelta(days=1)

class Sporttery_JCmatch(Spider):
    name = "spd_sporttery_JCmatch"
    start_urls = (
        'http://info.sporttery.cn/football/hhad_list.php',
    )
    ignore_page_incremental = True

    def parse(self, response):
        self.crawler.stats.set_value('spiderlog/source_name', u'T_SPORTTERY_JCMATCH')
        self.crawler.stats.set_value('spiderlog/target_tables', ['T_SPORTTERY_JCMATCH'])
        url = 'http://i.sporttery.cn/odds_calculator/get_odds?i_format=json&i_callback=getData&poolcode[]=hhad&poolcode[]=had&_=1510991344376'
        request = scrapy.http.Request(url, callback=self.parse_sporttery_content)
        yield request

    def parse_sporttery_content(self, response):
        content = response.body
        #得到第一个Id值
        matchid = int(re.findall("_(.+?)\":", content)[0])
        dataStrList = re.findall('getData(.+)',content)

        if dataStrList <> []:
            data_dict = eval(re.findall('getData(.+);',content)[0])
            data_dict_len = len(data_dict['data'])
            for oddskey in ['had','hhad']:
                for row in range(data_dict_len):
                    item = Football_sporttery_JCItem()
                    item['id']     = data_dict['data'][data_dict['data'].keys()[row]]['id']
                    item['num']     = data_dict['data'][data_dict['data'].keys()[row]]['num'].decode("unicode_escape")[2:5]
                    item['home_team']    = data_dict['data'][data_dict['data'].keys()[row]]['h_cn'].decode("unicode_escape")
                    item['home_team_order']    = data_dict['data'][data_dict['data'].keys()[row]]['h_order'].decode("unicode_escape")
                    item['guest_team']    = data_dict['data'][data_dict['data'].keys()[row]]['a_cn'].decode("unicode_escape")
                    item['guest_team_order']    = data_dict['data'][data_dict['data'].keys()[row]]['a_order'].decode("unicode_escape")
                    item['league_name']    = data_dict['data'][data_dict['data'].keys()[row]]['l_cn'].decode("unicode_escape")
                    item['b_date']  = data_dict['data'][data_dict['data'].keys()[row]]['b_date']
                    item['week']    = data_dict['data'][data_dict['data'].keys()[row]]['num'].decode("unicode_escape")[0:2]
                    if 'weather' in data_dict['data'][data_dict['data'].keys()[row]]:
                        item['weather'] = data_dict['data'][data_dict['data'].keys()[row]]['weather'].decode("unicode_escape")
                    else:
                        item['weather'] = u'未知'
                    item['time']    = data_dict['data'][data_dict['data'].keys()[row]]['date'] +' '+ data_dict['data'][data_dict['data'].keys()[row]]['time']
                    if oddskey == 'had':
                        #判断oddskey是否存在，因为当此场比赛为开售时，则无赔率指标
                        if oddskey in data_dict['data'][data_dict['data'].keys()[row]].keys() :
                            #让球指标 had中的该指标为空
                            # if data_dict['data'][data_dict['data'].keys()[row]][oddskey]['fixedodds'] == "":
                            item['fixedodds'] = "0"
                            item['odds_win'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['h']
                            item['odds_draw'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['d']
                            item['odds_lose'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['a']
                        else:
                            item['fixedodds'] = "0"
                    else:
                        # 判断oddskey是否存在，因为当此场比赛为开售时，则无赔率指标
                        if oddskey in data_dict['data'][data_dict['data'].keys()[row]].keys() :
                            #让球指标 had中的该指标为空
                            item['fixedodds'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['fixedodds']
                            item['odds_win'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['h']
                            item['odds_draw'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['d']
                            item['odds_lose'] = data_dict['data'][data_dict['data'].keys()[row]][oddskey]['a']
                        else:
                            item['fixedodds'] = 'UNKNOW'
                    yield item

        else:
            item = Football_sporttery_loseMatchId()
            item['matchid'] = matchid
            item['spidername'] = 'spd_sporttery_JCmatch'
            item['tablename'] = 'T_SPORTTERY_JCMATCH'
            item['url'] = response.url
            item['losereason'] = u'正则表达式未解析到dict数据,也可能是网络请求过快'
            yield item
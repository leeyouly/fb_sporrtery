# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Spider
from fb_sporrtery.items import Football_sporttery_JCBonusItem,Football_sporttery_loseMatchId
import time, datetime
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
last_update_date = datetime.datetime.now() - datetime.timedelta(days=1)

class JCmatch_310(Spider):
    name = "spd_sporttery_JCBonus"
    start_urls = (
        'http://info.sporttery.cn/football/hhad_list.php',
    )
    ignore_page_incremental = True

    def parse(self, response):

        for matchid in range(100000,103350,1):
            #mid = 95000 + mid
            url = 'http://i.sporttery.cn/api/fb_match_info/get_odds/?mid='+str(matchid)+'&f_callback=sportteryOdds&_=1512043006293'
            request = scrapy.http.Request(url, callback=self.parse_sporttery_content)
            request.meta['matchid'] = str(matchid)
            yield request

    def parse_sporttery_content(self, response):
        content = response.body
        data_dict = eval(re.findall('sportteryOdds(.+);',content)[0])
        matchid = response.meta['matchid']
        #先判断dict中是否存在result这个key 存在才继续
        if data_dict.has_key('result') :
            # 以下到第一个for循环为不让球胜平负
            if data_dict['result'].has_key('had'):
                had_win_per = data_dict['result']['had']['vote']['win_per']
                had_draw_per = data_dict['result']['had']['vote']['draw_per']
                had_lose_per = data_dict['result']['had']['vote']['lose_per']

                for data_list in data_dict['result']['had']['list']:
                    item = Football_sporttery_JCBonusItem()
                    item['matchid'] = matchid
                    item['id'] = data_list['id']
                    item['win'] = data_list['h']
                    item['draw'] = data_list['d']
                    item['lose'] = data_list['a']
                    item['win_ratio'] = data_list['h_ratio']
                    item['draw_ratio'] = data_list['d_ratio']
                    item['lose_ratio'] = data_list['a_ratio']
                    item['win_per'] = had_win_per
                    item['draw_per'] = had_draw_per
                    item['lose_per'] = had_lose_per
                    item['bonus_type'] = 'had'
                    item['deploytime'] = data_list['date'] + ' ' + data_list['time']
                    yield item

                # 以下到第一个for循环为让球胜平负
                had_win_per = data_dict['result']['hhad']['vote']['win_per']
                had_draw_per = data_dict['result']['hhad']['vote']['draw_per']
                had_lose_per = data_dict['result']['hhad']['vote']['lose_per']
                #让球数
                goalline = data_dict['result']['hhad']['odds']['goalline']
                for data_list in data_dict['result']['hhad']['list']:
                    item = Football_sporttery_JCBonusItem()
                    item['matchid'] = matchid
                    item['id'] = data_list['id']
                    item['win'] = data_list['h']
                    item['draw'] = data_list['d']
                    item['lose'] = data_list['a']
                    item['win_ratio'] = data_list['h_ratio']
                    item['draw_ratio'] = data_list['d_ratio']
                    item['lose_ratio'] = data_list['a_ratio']
                    item['win_per'] = had_win_per
                    item['draw_per'] = had_draw_per
                    item['lose_per'] = had_lose_per
                    item['bonus_type'] = goalline
                    item['deploytime'] = data_list['date'] + ' ' + data_list['time']
                    yield item
        else:
            item = Football_sporttery_loseMatchId()
            item['matchid'] = matchid
            item['spidername'] = 'spd_sporttery_JCBonus'
            item['tablename'] = 'T_SPORTTERY_JCBONUS'
            item['url'] = response.url
            item['losereason'] = u'此matchId无数据返回，可能是此Id本身没有比赛，或者此Id过大，还未绑定比赛'
            yield item
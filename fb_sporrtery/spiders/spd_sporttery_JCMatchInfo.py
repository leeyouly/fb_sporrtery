# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Spider
from fb_sporrtery.items import Football_sporttery_JCMatchInfoItem,Football_sporttery_loseMatchId
import time, datetime
import re
import sys
import fb_sporrtery.settings as settings
import cx_Oracle
reload(sys)
sys.setdefaultencoding('utf8')
last_update_date = datetime.datetime.now() - datetime.timedelta(days=1)

null = ''

class JCmatch_310(Spider):
    name = "spd_sporttery_JCMatchInfo"
    start_urls = (
        'http://info.sporttery.cn/football/hhad_list.php',
    )
    ignore_page_incremental = True

    def parse(self, response):

        # 链接数据库，拿到当前最大的matchId
        conn = cx_Oracle.connect(settings.dbusername, settings.dbpassword, settings.dbconnect)
        cursor = conn.cursor()
        findsql = "select max(t.matchid) from T_SPORTTERY_JCMATCH t"
        cursor.execute(findsql)
        max_matchId_list = cursor.fetchall()
        cursor.close()
        conn.close()

        max_matchId = max_matchId_list[0][0]
        # 取最大的matchId-300和matchId作为区间范围增量抓取数据
        for matchid in range(max_matchId - 300, max_matchId + 1, 1):
            #mid = 95000 + mid
            url = 'http://i.sporttery.cn/api/fb_match_info/get_match_info?mid='+str(matchid)+'&f_callback=getMatchInfo&_=1517315440768'
            # url = 'http://i.sporttery.cn/api/fb_match_info/get_match_info?mid=103350&f_callback=getMatchInfo&_=1517315440768'
            request = scrapy.http.Request(url, callback=self.parse_sporttery_content)
            request.meta['matchid'] = str(matchid)
            # request.meta['matchid'] = str(11)
            yield request

    def parse_sporttery_content(self, response):
        content = response.body
        data_dict_str = re.findall('getMatchInfo(.+);',content)
        if data_dict_str <> []:
            data_dict = eval(data_dict_str[0])
            #先判断dict中是否存在result这个key 存在才继续
            if data_dict['result']['a_id_dc'] <> 0 :
                result_dict = data_dict['result']
                item = Football_sporttery_JCMatchInfoItem()
                item['matchid'] = response.meta['matchid']
                item['home_teamid'] = result_dict['h_id_dc']
                item['home_team'] = result_dict['h_cn'].decode("unicode_escape")
                item['home_team_order'] = result_dict['table_h']
                item['guest_teamid'] = result_dict['a_id_dc']
                item['guest_team'] = result_dict['a_cn'].decode("unicode_escape")
                item['guest_team_order'] = result_dict['table_a']
                item['league_id'] = result_dict['l_id_dc']
                item['league_name'] = result_dict['l_cn'].decode("unicode_escape")
                item['league_names'] = result_dict['l_cn_abbr'].decode("unicode_escape")
                item['season'] = result_dict['s_cn']
                item['matchtime'] =  result_dict['date_cn'] + ' ' + result_dict['time_cn']
                item['s_num'] = result_dict['s_num'].decode("unicode_escape")
                item['match_type'] = result_dict['r_cn'].decode("unicode_escape")
                item['weather'] = result_dict['weather'].decode("unicode_escape")
                item['update_dt'] = time.strftime("%Y/%m/%d %X", time.localtime())
                item['source'] = response.url
                yield item
            else:
                item = Football_sporttery_loseMatchId()
                item['matchid'] = response.meta['matchid']
                item['spidername'] = 'spd_sporttery_JCMatchInfo'
                item['tablename'] = 'T_SPORTTERY_JCMatchInfo'
                item['url'] = response.url
                item['losereason'] = u'此matchId无数据返回，可能是此Id本身没有比赛，或者此Id过大，还未绑定比赛'
                item['update_dt'] = time.strftime("%Y-%m-%d %X", time.localtime())
                yield item
        else:
            print u'可能是请求过快---> ' + response.body
            item = Football_sporttery_loseMatchId()
            item['matchid'] = response.meta['matchid']
            item['spidername'] = 'spd_sporttery_JCMatchInfo'
            item['tablename'] = 'T_SPORTTERY_JCMatchInfo'
            item['url'] = response.url
            item['losereason'] = u'未找到数据，可能是请求速度过快导致'
            item['update_dt'] = time.strftime("%Y-%m-%d %X", time.localtime())
            yield item
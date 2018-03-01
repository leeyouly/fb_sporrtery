# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Spider
from fb_sporrtery.items import Football_sporttery_JCFixationBonusItem1,Football_sporttery_JCFixationBonusItem2,\
    Football_sporttery_JCFixationBonusItem4,Football_sporttery_JCFixationBonusItem5, \
    Football_sporttery_JCFixationBonusItem6,Football_sporttery_loseMatchId
import time, datetime
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
last_update_date = datetime.datetime.now() - datetime.timedelta(days=1)

class JCmatch_310(Spider):
    name = "spd_sporttery_JCFixationBonus"
    start_urls = (
        # 'http://info.sporttery.cn/football/hhad_list.php',
        'http://info.sporttery.cn/football/pool_result.php?id=102268',
    )
    ignore_page_incremental = True

    def parse(self, response):
        for matchid in range(80001,103350,1):
        # for matchid in range(112680,112681,1):
            url = 'http://i.sporttery.cn/api/fb_match_info/get_pool_rs/?f_callback=pool_prcess&mid='+str(matchid)+'&_=1514786127888'
            request = scrapy.http.Request(url, callback=self.parse_sporttery_content)
            request.meta['matchid'] = str(matchid)
            yield request

    def parse_sporttery_content(self, response):
        matchid = response.meta['matchid']
        content = response.body
        dataStrDict = re.findall('pool_prcess(.+);',content)
        #通过正则表达式截取，看截取部分的数据是否返回为空，有时请求过快，网页可能不会返回数据。如果网页没有返回数据，
        #那么这个id应该被写入数据库记录下来，表示这是一个采集失败的记录
        if dataStrDict <> []:
            data_dict = eval(re.findall('pool_prcess(.+);',content)[0])
            if 'result' in data_dict:
                lotteryResult = data_dict['result']['pool_rs']
                if lotteryResult <> []:
                    item = Football_sporttery_JCFixationBonusItem1()
                    if 'had' in lotteryResult:
                        item['matchid'] = matchid
                        item['playways'] = u'胜平负'
                        item['lotteryresult'] = lotteryResult['had']['prs_name'].decode("unicode_escape")
                        item['bonus'] = lotteryResult['had']['odds']
                        yield item
                    if 'hhad' in lotteryResult:
                        item['matchid'] = matchid
                        item['playways'] = u'让球胜平负'
                        item['lotteryresult'] = '(' + lotteryResult['hhad']['goalline'] + ')' + lotteryResult['hhad']['prs_name'].decode("unicode_escape")
                        item['bonus'] = lotteryResult['hhad']['odds']
                        yield item
                    if 'crs' in lotteryResult:
                        item['matchid'] = matchid
                        item['playways'] = u'比分'
                        item['lotteryresult'] = lotteryResult['crs']['prs_name'].decode("unicode_escape")
                        item['bonus'] = lotteryResult['crs']['odds']
                        yield item
                    if 'ttg' in lotteryResult:
                        item['matchid'] = matchid
                        item['playways'] = u'总进球'
                        item['lotteryresult'] = lotteryResult['ttg']['prs_name'].decode("unicode_escape")
                        item['bonus'] = lotteryResult['ttg']['odds']
                        yield item
                    if 'hafu' in lotteryResult:
                        item['matchid'] = matchid
                        item['playways'] = u'半全场胜平负'
                        item['lotteryresult'] = lotteryResult['hafu']['prs_name'].decode("unicode_escape")
                        item['bonus'] = lotteryResult['hafu']['odds']
                        yield item

                lotteryProcess = data_dict['result']['odds_list']
                if 'had' in lotteryProcess:
                    lotteryHadList = lotteryProcess['had']['odds']
                    for orderLine in lotteryHadList:
                        item = Football_sporttery_JCFixationBonusItem2()
                        item['matchid'] = matchid
                        item['deploytime'] = orderLine['date'] + ' ' + orderLine['time']
                        #goalline等于0为不让球
                        item['goalline'] = '0'
                        item['win'] = orderLine['h']
                        item['draw'] = orderLine['d']
                        item['lose'] = orderLine['a']
                        yield item

                if 'hhad' in lotteryProcess:
                    lotteryHHadList = lotteryProcess['hhad']['odds']
                    for orderLine in lotteryHHadList:
                        item = Football_sporttery_JCFixationBonusItem2()
                        item['matchid'] = matchid
                        item['deploytime'] = orderLine['date'] + ' ' + orderLine['time']
                        # goalline从网页中取值，为让球书
                        item['goalline'] = orderLine['goalline']
                        item['win'] = orderLine['h']
                        item['draw'] = orderLine['d']
                        item['lose'] = orderLine['a']
                        yield item

                if 'ttg' in lotteryProcess:
                    lotteryTtgList = lotteryProcess['ttg']['odds']
                    for orderLine in lotteryTtgList:
                        item = Football_sporttery_JCFixationBonusItem4()
                        item['matchid'] = matchid
                        item['deploytime'] = orderLine['date'] + ' ' + orderLine['time']
                        item['s0'] = orderLine['s0']
                        item['s1'] = orderLine['s1']
                        item['s2'] = orderLine['s2']
                        item['s3'] = orderLine['s3']
                        item['s4'] = orderLine['s4']
                        item['s5'] = orderLine['s5']
                        item['s6'] = orderLine['s6']
                        item['s7'] = orderLine['s7']
                        item['trend'] = orderLine['trend']
                        yield item

                if 'hafu' in lotteryProcess:
                    lotteryTtgList = lotteryProcess['hafu']['odds']
                    for orderLine in lotteryTtgList:
                        item = Football_sporttery_JCFixationBonusItem5()
                        item['matchid'] = matchid
                        item['deploytime'] = orderLine['date'] + ' ' + orderLine['time']
                        item['winwin'] = orderLine['hh']
                        item['windraw'] = orderLine['hd']
                        item['winlose'] = orderLine['ha']
                        item['drawwin'] = orderLine['dh']
                        item['drawdraw'] = orderLine['dd']
                        item['drawlose'] = orderLine['da']
                        item['losewin'] = orderLine['ah']
                        item['losedraw'] = orderLine['ad']
                        item['loselose'] = orderLine['aa']
                        yield item

                if 'crs' in lotteryProcess:
                    lotteryTtgList = lotteryProcess['crs']['odds']
                    for orderLine in lotteryTtgList:
                        item = Football_sporttery_JCFixationBonusItem6()
                        item['matchid'] = matchid
                        item['deploytime'] = orderLine['date'] + ' ' + orderLine['time']
                        item['win0100'] = orderLine['0100']
                        item['win0200'] = orderLine['0200']
                        item['win0201'] = orderLine['0201']
                        item['win0300'] = orderLine['0300']
                        item['win0301'] = orderLine['0301']
                        item['win0302'] = orderLine['0302']
                        item['win0400'] = orderLine['0400']
                        item['win0401'] = orderLine['0401']
                        item['win0402'] = orderLine['0402']
                        item['win0500'] = orderLine['0500']
                        item['win0501'] = orderLine['0501']
                        item['win0502'] = orderLine['0502']
                        item['win_other'] = orderLine['-1-h']

                        item['draw0000'] = orderLine['0000']
                        item['draw0101'] = orderLine['0101']
                        item['draw0202'] = orderLine['0202']
                        item['draw0303'] = orderLine['0303']
                        item['draw_other'] = orderLine['-1-d']

                        item['lose0001'] = orderLine['0001']
                        item['lose0002'] = orderLine['0002']
                        item['lose0102'] = orderLine['0102']
                        item['lose0003'] = orderLine['0003']
                        item['lose0103'] = orderLine['0103']
                        item['lose0203'] = orderLine['0203']
                        item['lose0004'] = orderLine['0004']
                        item['lose0104'] = orderLine['0104']
                        item['lose0204'] = orderLine['0204']
                        item['lose0005'] = orderLine['0005']
                        item['lose0105'] = orderLine['0105']
                        item['lose0205'] = orderLine['0205']
                        item['lose_other'] = orderLine['-1-a']
                        item['trend'] = orderLine['trend']
                        yield item

            elif data_dict['status']['code'] == 20002:
                item = Football_sporttery_loseMatchId()
                item['matchid'] = matchid
                item['spidername'] = 'spd_sporttery_JCFixationBonus'
                item['tablename'] = ''
                item['url'] = response.url
                item['losereason'] = u'此matchId无数据返回，可能是此Id本身没有比赛，或者此Id过大，还未绑定比赛'
                yield item

        #对应第一个if，当采集失败，则把失败的matchid插入到数据库中
        else:
            item = Football_sporttery_loseMatchId()
            item['matchid'] = matchid
            item['spidername'] = 'spd_sporttery_JCFixationBonus'
            item['tablename'] = 'T_SPORTTERY_JCFIXATIONBONUS 1-6'
            item['url'] = response.url
            item['losereason'] = u'正则表达式未解析到dict数据,也可能是网络请求过快'
            yield item

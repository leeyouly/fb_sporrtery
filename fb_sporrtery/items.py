# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FbSporrteryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass



class Football_sporttery_JCItem(scrapy.Item):
    matchid     = scrapy.Field()
    num     = scrapy.Field()
    home_teamid = scrapy.Field()
    home_team    = scrapy.Field()
    home_team_order    = scrapy.Field()
    guest_teamid    = scrapy.Field()
    guest_team    = scrapy.Field()
    guest_team_order    = scrapy.Field()
    league_id    = scrapy.Field()
    league_name    = scrapy.Field()
    match_info = scrapy.Field()
    b_date  = scrapy.Field()
    time    = scrapy.Field()
    week    = scrapy.Field()
    weather = scrapy.Field()
    fixedodds    = scrapy.Field()
    odds_win    = scrapy.Field()
    odds_draw    = scrapy.Field()
    odds_lose    = scrapy.Field()
    update_dt = scrapy.Field()


class Football_sporttery_JCMatchInfoItem(scrapy.Item):
    matchid  = scrapy.Field()
    home_teamid = scrapy.Field()
    home_team = scrapy.Field()
    home_team_order = scrapy.Field()
    guest_teamid = scrapy.Field()
    guest_team = scrapy.Field()
    guest_team_order = scrapy.Field()
    league_id = scrapy.Field()
    league_name = scrapy.Field()
    league_names = scrapy.Field()
    season = scrapy.Field()
    matchtime = scrapy.Field()
    s_num = scrapy.Field()
    match_type = scrapy.Field()
    weather = scrapy.Field()
    update_dt = scrapy.Field()
    source = scrapy.Field()



class Football_sporttery_JCMatchSupportItem(scrapy.Item):
    mid = scrapy.Field()
    win = scrapy.Field()
    pre_win = scrapy.Field()
    draw = scrapy.Field()
    pre_draw = scrapy.Field()
    lose = scrapy.Field()
    pre_lose = scrapy.Field()
    total = scrapy.Field()
    ctype = scrapy.Field()
    num = scrapy.Field()
    update_dt = scrapy.Field()

class Football_sporttery_14MatchItem(scrapy.Item):
    odds_win = scrapy.Field()
    odds_draw = scrapy.Field()
    odds_lose = scrapy.Field()
    id = scrapy.Field()
    mid = scrapy.Field()
    home_team = scrapy.Field()
    guest_team = scrapy.Field()
    league_name = scrapy.Field()
    full = scrapy.Field()
    result = scrapy.Field()
    time = scrapy.Field()
    update_dt = scrapy.Field()
    term = scrapy.Field()


class Football_sporttery_JCBonusItem(scrapy.Item):
    win     = scrapy.Field()
    draw    = scrapy.Field()
    lose    = scrapy.Field()
    win_ratio    = scrapy.Field()
    draw_ratio  = scrapy.Field()
    lose_ratio    = scrapy.Field()
    # mid为该场比赛Id
    matchid = scrapy.Field()
    # id为这次比赛某一条奖金的Id
    id = scrapy.Field()
    deploytime    = scrapy.Field()
    win_per    = scrapy.Field()
    draw_per = scrapy.Field()
    lose_per    = scrapy.Field()
    bonus_type = scrapy.Field()
    update_dt = scrapy.Field()


#以下为竞彩网固定奖金页面Item
class Football_sporttery_JCFixationBonusItem1(scrapy.Item):
    matchid     = scrapy.Field()
    playways    = scrapy.Field()
    lotteryresult    = scrapy.Field()
    bonus    = scrapy.Field()
    update_dt = scrapy.Field()

class Football_sporttery_JCFixationBonusItem2(scrapy.Item):
    matchid     = scrapy.Field()
    deploytime  = scrapy.Field()
    goalline  = scrapy.Field()
    win    = scrapy.Field()
    draw   = scrapy.Field()
    lose   = scrapy.Field()
    update_dt = scrapy.Field()

class Football_sporttery_JCFixationBonusItem4(scrapy.Item):
    matchid = scrapy.Field()
    deploytime     = scrapy.Field()
    s0  = scrapy.Field()
    s1  = scrapy.Field()
    s2    = scrapy.Field()
    s3   = scrapy.Field()
    s4   = scrapy.Field()
    s5   = scrapy.Field()
    s6   = scrapy.Field()
    s7   = scrapy.Field()
    trend   = scrapy.Field()
    update_dt = scrapy.Field()

class Football_sporttery_JCFixationBonusItem5(scrapy.Item):
    matchid = scrapy.Field()
    deploytime     = scrapy.Field()
    winwin  = scrapy.Field()
    windraw  = scrapy.Field()
    winlose  = scrapy.Field()
    drawwin  = scrapy.Field()
    drawdraw  = scrapy.Field()
    drawlose  = scrapy.Field()
    losewin  = scrapy.Field()
    losedraw  = scrapy.Field()
    loselose  = scrapy.Field()
    update_dt = scrapy.Field()


class Football_sporttery_JCFixationBonusItem6(scrapy.Item):
    matchid = scrapy.Field()
    deploytime     = scrapy.Field()
    win0100  = scrapy.Field()
    win0200  = scrapy.Field()
    win0201  = scrapy.Field()
    win0300  = scrapy.Field()
    win0301  = scrapy.Field()
    win0302  = scrapy.Field()
    win0400  = scrapy.Field()
    win0401  = scrapy.Field()
    win0402  = scrapy.Field()
    win0500  = scrapy.Field()
    win0501  = scrapy.Field()
    win0502  = scrapy.Field()
    win_other  = scrapy.Field()

    draw0000  = scrapy.Field()
    draw0101  = scrapy.Field()
    draw0202  = scrapy.Field()
    draw0303  = scrapy.Field()
    draw_other  = scrapy.Field()

    lose0001  = scrapy.Field()
    lose0002  = scrapy.Field()
    lose0102  = scrapy.Field()
    lose0003  = scrapy.Field()
    lose0103  = scrapy.Field()
    lose0203  = scrapy.Field()
    lose0004  = scrapy.Field()
    lose0104  = scrapy.Field()
    lose0204  = scrapy.Field()
    lose0005  = scrapy.Field()
    lose0105  = scrapy.Field()
    lose0205  = scrapy.Field()
    lose_other  = scrapy.Field()
    trend  = scrapy.Field()
    update_dt = scrapy.Field()


#采集失败的matchid专门存储的表
class Football_sporttery_loseMatchId(scrapy.Item):
    matchid = scrapy.Field()
    spidername = scrapy.Field()
    tablename = scrapy.Field()
    url = scrapy.Field()
    losereason = scrapy.Field()
    update_dt = scrapy.Field()

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from fb_sporrtery.data import ImportFootball_JCMatchStorage,ImportFootball_SportJCBonusStorage,\
    ImportFootball_JCMatchSupportStorage,ImportFootball_14MatchStorage,ImportFootball_SportFixaBonus1Storage,\
    ImportFootball_SportFixaBonus2Storage,ImportFootball_SportFixaBonus4Storage,ImportFootball_SportFixaBonus5Storage,\
    ImportFootball_SportFixaBonus6Storage, ImportFootball_SportloseMatchId,ImportFootball_JCMatchInfoStorage
from fb_sporrtery.items import Football_sporttery_JCItem,Football_sporttery_JCMatchSupportItem,\
    Football_sporttery_14MatchItem,Football_sporttery_JCFixationBonusItem1,Football_sporttery_JCFixationBonusItem2,\
    Football_sporttery_JCFixationBonusItem4,Football_sporttery_JCFixationBonusItem5,\
    Football_sporttery_JCFixationBonusItem6,Football_sporttery_loseMatchId,Football_sporttery_JCBonusItem,\
    Football_sporttery_JCMatchInfoItem
from scrapy.utils.project import get_project_settings



class FbSporrteryPipeline(object):
    def process_item(self, item, spider):
        return item


class ImportFootball_JCMatchSave(object):
    def __init__(self):
        self.storage = ImportFootball_JCMatchStorage(get_project_settings().get('DATABASE'))

    def process_item(self, item, spider):
        if isinstance(item, Football_sporttery_JCItem):
            # if not self.storage.exist(item):
                self.storage.save_or_update(item)
                spider.crawler.stats.inc_value('spiderlog/save_count')
        return item
        

class ImportFootball_JCMatchSupportSave(object):
    def __init__(self):
        self.storage = ImportFootball_JCMatchSupportStorage(get_project_settings().get('DATABASE'))

    def process_item(self, item, spider):
        if isinstance(item, Football_sporttery_JCMatchSupportItem):
            # if not self.storage.exist(item):
                self.storage.save_or_update(item)
                spider.crawler.stats.inc_value('spiderlog/save_count')
        return item



class ImportFootball_JCMatchInfoSave(object):
    def __init__(self):
        self.storage = ImportFootball_JCMatchInfoStorage(get_project_settings().get('DATABASE'))

    def process_item(self, item, spider):
        if isinstance(item, Football_sporttery_JCMatchInfoItem):
            # if not self.storage.exist(item):
                self.storage.save_or_update(item)
                spider.crawler.stats.inc_value('spiderlog/save_count')
        return item


class ImportFootball_14MatchSave(object):
    def __init__(self):
        self.storage = ImportFootball_14MatchStorage(get_project_settings().get('DATABASE'))

    def process_item(self, item, spider):
        if isinstance(item, Football_sporttery_14MatchItem):
            # if not self.storage.exist(item):
                self.storage.save_or_update(item)
                spider.crawler.stats.inc_value('spiderlog/save_count')
        return item


#竞彩官网 固定奖金页面 例如 http://info.sporttery.cn/football/pool_result.php?id=102268
class ImportFootball_SportFixaBonus1Save(object):
    def __init__(self):
        self.storage = ImportFootball_SportFixaBonus1Storage(get_project_settings().get('DATABASE'))

    def process_item(self, item, spider):
        if isinstance(item, Football_sporttery_JCFixationBonusItem1):
            if not self.storage.exist(item):
                self.storage.save_or_update(item)
                spider.crawler.stats.inc_value('spiderlog/save_count')
        return item

class ImportFootball_SportFixaBonus2Save(object):
    def __init__(self):
        self.storage = ImportFootball_SportFixaBonus2Storage(get_project_settings().get('DATABASE'))

    def process_item(self, item, spider):
        if isinstance(item, Football_sporttery_JCFixationBonusItem2):
            if not self.storage.exist(item):
                self.storage.save_or_update(item)
                spider.crawler.stats.inc_value('spiderlog/save_count')
        return item

class ImportFootball_SportFixaBonus4Save(object):
    def __init__(self):
        self.storage = ImportFootball_SportFixaBonus4Storage(get_project_settings().get('DATABASE'))

    def process_item(self, item, spider):
        if isinstance(item, Football_sporttery_JCFixationBonusItem4):
            if not self.storage.exist(item):
                self.storage.save_or_update(item)
                spider.crawler.stats.inc_value('spiderlog/save_count')
        return item

class ImportFootball_SportFixaBonus5Save(object):
    def __init__(self):
        self.storage = ImportFootball_SportFixaBonus5Storage(get_project_settings().get('DATABASE'))

    def process_item(self, item, spider):
        if isinstance(item, Football_sporttery_JCFixationBonusItem5):
            if not self.storage.exist(item):
                self.storage.save_or_update(item)
                spider.crawler.stats.inc_value('spiderlog/save_count')
        return item

class ImportFootball_SportFixaBonus6Save(object):
    def __init__(self):
        self.storage = ImportFootball_SportFixaBonus6Storage(get_project_settings().get('DATABASE'))

    def process_item(self, item, spider):
        if isinstance(item, Football_sporttery_JCFixationBonusItem6):
            if not self.storage.exist(item):
                self.storage.save_or_update(item)
                spider.crawler.stats.inc_value('spiderlog/save_count')
        return item

class ImportFootball_SportJCBonusSave(object):
    def __init__(self):
        self.storage = ImportFootball_SportJCBonusStorage(get_project_settings().get('DATABASE'))

    def process_item(self, item, spider):
        if isinstance(item, Football_sporttery_JCBonusItem):
            if not self.storage.exist(item):
                self.storage.save_or_update(item)
                spider.crawler.stats.inc_value('spiderlog/save_count')
        return item

#竞彩网采集失败的matchid
class ImportFootball_SportLoseMatchId(object):
    def __init__(self):
        self.storage = ImportFootball_SportloseMatchId(get_project_settings().get('DATABASE'))

    def process_item(self, item, spider):
        if isinstance(item, Football_sporttery_loseMatchId):
            # if not self.storage.exist(item):
                self.storage.save_or_update(item)
                spider.crawler.stats.inc_value('spiderlog/save_count')
        return item        
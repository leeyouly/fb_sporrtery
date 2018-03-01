from spiderlib.data import DataStorage
import PyDB

class ImportFootball_JCMatchStorage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 't_sporttery_jcmatch'
        self.db.set_metadata(self.table_name, [
            PyDB.StringField("matchid",is_key=True),
            PyDB.StringField("num"),
            PyDB.StringField("home_teamid"),
            PyDB.StringField("home_team"),
            PyDB.StringField("home_team_order"),
            PyDB.StringField("guest_teamid"),
            PyDB.StringField("guest_team"),
            PyDB.StringField("guest_team_order"),
            PyDB.StringField("league_id"),
            PyDB.StringField("league_name"),
            PyDB.StringField("match_info"),
            PyDB.DateField("b_date"),
            PyDB.DateField("time"),
            PyDB.StringField("week"),
            PyDB.StringField("weather"),
            PyDB.StringField("fixedodds",is_key=True),
            PyDB.StringField("odds_win"),
            PyDB.StringField("odds_draw"),
            PyDB.StringField("odds_lose"),
            PyDB.DateField("update_dt"),
        ])

    def save_or_update(self, item):
        self.db.save_or_update(self.table_name, item)
        self.db.commit()


class ImportFootball_JCMatchSupportStorage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_SPORTTERY_JCMATCHSUPPORT'
        self.db.set_metadata(self.table_name, [
            PyDB.StringField("mid",is_key=True),
            PyDB.StringField("win"),
            PyDB.StringField("pre_win"),
            PyDB.StringField("draw"),
            PyDB.StringField("pre_draw"),
            PyDB.StringField("lose"),
            PyDB.StringField("pre_lose"),
            PyDB.StringField("total"),
            PyDB.StringField("ctype",is_key=True),
            PyDB.DateField("num"),
            PyDB.DateField("update_dt"),
        ])

    def save_or_update(self, item):
        self.db.save_or_update(self.table_name, item)
        self.db.commit()


class ImportFootball_JCMatchInfoStorage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_SPORTTERY_JCMATCHINFO'
        self.db.set_metadata(self.table_name, [
            PyDB.IntField("matchid",is_key=True),
            PyDB.IntField("home_teamid"),
            PyDB.StringField("home_team"),
            PyDB.StringField("home_team_order"),
            PyDB.IntField("guest_teamid"),
            PyDB.StringField("guest_team"),
            PyDB.StringField("guest_team_order"),
            PyDB.IntField("league_id"),
            PyDB.StringField("league_name"),
            PyDB.StringField("league_names"),
            PyDB.StringField("matchtime"),
            PyDB.StringField("s_sum"),
            PyDB.StringField("match_type"),
            PyDB.StringField("weather"),
            PyDB.DatetimeField("update_dt"),
            PyDB.StringField("source"),
        ])

    def save_or_update(self, item):
        self.db.save_or_update(self.table_name, item)
        self.db.commit()



class ImportFootball_14MatchStorage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_SPORTTERY_14Match'
        self.db.set_metadata(self.table_name, [
            PyDB.StringField("id",is_key=True),
            PyDB.StringField("mid"),
            PyDB.StringField("odds_win"),
            PyDB.StringField("odds_draw"),
            PyDB.StringField("odds_lose"),
            PyDB.StringField("home_team"),
            PyDB.StringField("guest_team"),
            PyDB.StringField("league_name"),
            PyDB.StringField("full"),
            PyDB.StringField("result"),
            PyDB.StringField("term"),
            PyDB.DateField("update_dt"),
            PyDB.DateField("time"),
        ])

    def save_or_update(self, item):
        self.db.save_or_update(self.table_name, item)
        self.db.commit()


#
class ImportFootball_SportFixaBonus1Storage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_SPORTTERY_JCFIXATIONBONUS1'
        self.db.set_metadata(self.table_name, [
            PyDB.StringField("matchid",is_key=True),
            PyDB.StringField("playways",is_key=True),
            PyDB.StringField("lotteryresult"),
            PyDB.StringField("bonus"),
            PyDB.DateField("update_dt"),
        ])

    def save_or_update(self, item):
        # self.db.save_or_update(self.table_name, item)
        self.db.save(self.table_name, item)
        self.db.commit()

class ImportFootball_SportFixaBonus2Storage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_SPORTTERY_JCFIXATIONBONUS2'
        self.db.set_metadata(self.table_name, [
            PyDB.StringField("matchid",is_key=True),
            PyDB.DatetimeField("deploytime",is_key=True),
            PyDB.StringField("goalline"),
            PyDB.StringField("win"),
            PyDB.StringField("draw"),
            PyDB.StringField("lose"),
            PyDB.DateField("update_dt"),
        ])

    def save_or_update(self, item):
        self.db.save_or_update(self.table_name, item)
        # self.db.save(self.table_name, item)
        self.db.commit()


class ImportFootball_SportFixaBonus4Storage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_SPORTTERY_JCFIXATIONBONUS4'
        self.db.set_metadata(self.table_name, [
            PyDB.IntField("matchid",is_key=True),
            PyDB.DatetimeField("deploytime",is_key=True),
            PyDB.StringField("s0"),
            PyDB.StringField("s1"),
            PyDB.StringField("s2"),
            PyDB.StringField("s3"),
            PyDB.StringField("s4"),
            PyDB.StringField("s5"),
            PyDB.StringField("s6"),
            PyDB.StringField("s7"),
            PyDB.StringField("trend"),
            PyDB.DateField("update_dt"),
        ])

    def save_or_update(self, item):
        # self.db.save_or_update(self.table_name, item)
        self.db.save(self.table_name, item)
        self.db.commit()

class ImportFootball_SportFixaBonus5Storage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_SPORTTERY_JCFIXATIONBONUS5'
        self.db.set_metadata(self.table_name, [
            PyDB.IntField("matchid",is_key=True),
            PyDB.DatetimeField("deploytime",is_key=True),
            PyDB.StringField("winwin"),
            PyDB.StringField("windraw"),
            PyDB.StringField("winlose"),
            PyDB.StringField("drawwin"),
            PyDB.StringField("drawdraw"),
            PyDB.StringField("drawlose"),
            PyDB.StringField("losewin"),
            PyDB.StringField("losedraw"),
            PyDB.StringField("loselose"),
            PyDB.DateField("update_dt"),
        ])

    def save_or_update(self, item):
        # self.db.save_or_update(self.table_name, item)
        self.db.save(self.table_name, item)
        self.db.commit()

class ImportFootball_SportFixaBonus6Storage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_SPORTTERY_JCFIXATIONBONUS6'
        self.db.set_metadata(self.table_name, [
            PyDB.IntField("matchid",is_key=True),
            PyDB.DatetimeField("deploytime",is_key=True),
            PyDB.StringField("win0100"),
            PyDB.StringField("win0200"),
            PyDB.StringField("win0201"),
            PyDB.StringField("win0300"),
            PyDB.StringField("win0301"),
            PyDB.StringField("win0302"),
            PyDB.StringField("win0400"),
            PyDB.StringField("win0401"),
            PyDB.StringField("win0402"),
            PyDB.StringField("win0500"),
            PyDB.StringField("win0501"),
            PyDB.StringField("win0502"),
            PyDB.StringField("win_other"),

            PyDB.StringField("draw0000"),
            PyDB.StringField("draw0101"),
            PyDB.StringField("draw0202"),
            PyDB.StringField("draw0303"),
            PyDB.StringField("draw_other"),

            PyDB.StringField("lose0001"),
            PyDB.StringField("lose0002"),
            PyDB.StringField("lose0102"),
            PyDB.StringField("lose0003"),
            PyDB.StringField("lose0103"),
            PyDB.StringField("lose0203"),
            PyDB.StringField("lose0004"),
            PyDB.StringField("lose0104"),
            PyDB.StringField("lose0204"),
            PyDB.StringField("lose0005"),
            PyDB.StringField("lose0105"),
            PyDB.StringField("lose0205"),
            PyDB.StringField("lose_other"),
            PyDB.StringField("trend"),
            PyDB.DateField("update_dt"),
        ])

    def save_or_update(self, item):
        # self.db.save_or_update(self.table_name, item)
        self.db.save(self.table_name, item)
        self.db.commit()


class ImportFootball_SportJCBonusStorage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_SPORTTERY_JCBONUS'
        self.db.set_metadata(self.table_name, [
            PyDB.StringField("id", is_key=True),
            PyDB.IntField("matchid", is_key=True),
            PyDB.DatetimeField("deploytime", is_key=True),
            PyDB.StringField("win"),
            PyDB.StringField("draw"),
            PyDB.StringField("lose"),
            PyDB.StringField("win_ratio"),
            PyDB.StringField("draw_ratio"),
            PyDB.StringField("lose_ratio"),
            PyDB.StringField("win_per"),
            PyDB.StringField("draw_per"),
            PyDB.StringField("lose_per"),
            PyDB.StringField("bonus_type"),
            PyDB.DateField("update_dt"),
        ])

    def save_or_update(self, item):
        # self.db.save_or_update(self.table_name, item)
        self.db.save(self.table_name, item)
        self.db.commit()


class ImportFootball_SportloseMatchId(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_SPORTTERY_LOSEMATCHID'
        self.db.set_metadata(self.table_name, [
            PyDB.IntField("matchid"),
            PyDB.StringField("spidername"),
            PyDB.StringField("tablename"),
            PyDB.StringField("url"),
            PyDB.StringField("losereason"),
            PyDB.DateField("update_dt"),
        ])

    def save_or_update(self, item):
        self.db.save(self.table_name, item)
        self.db.commit()
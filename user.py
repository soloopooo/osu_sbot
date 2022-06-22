from io import TextIOWrapper
import json
from os import getcwd


class User():
    qqid: int = None
    uid: int = None
    name: str = None
    score_ranked: int = None
    score_all: int = None
    play_count: int = None
    pp: float = None
    acc: float = None
    ranking_global: int = None
    ranking_country: int = None
    country: dict = None
    join_date: str = None
    is_online: bool = None
    is_supporter: bool = None
    has_supported: bool = None
    cover_url: str = None
    grade: dict = None
    avatar_url: str = None
    total_hits: int = None
    max_combo: int = None
    level: int = None
    level_progress: int = None
    play_time: int = None
    mode: int = None
    monthly_playcounts: dict = None

    def __init__(
        self,
        avatar_url: str=avatar_url,
        has_supported: bool=has_supported,
        play_count: int=play_count,
        qqid: int=qqid,
        ranking_country: int=ranking_country,
        pp: float=pp,
        grade: dict=grade,
        is_online: bool=is_online,
        is_supporter: bool=is_supporter,
        cover_url: str=cover_url,
        join_date: str=join_date,
        country: dict=country,
        uid: int=uid,
        name: str=name,
        score_ranked: int=score_ranked,
        score_all: int=score_all,
        acc: float=acc,
        ranking_global: int=ranking_global,
        total_hits: int=total_hits,
        max_combo: int=max_combo,
        level: int=level,
        level_progress: int=level_progress,
        play_time: int=play_time,
        mode: int=mode,
        monthly_playcounts: dict=monthly_playcounts,
    ) -> None:
        self.uid = uid
        self.name = name
        self.score_ranked = score_ranked
        self.score_all = score_all
        self.acc = acc
        self.ranking_global = ranking_global
        self.ranking_country = ranking_country
        self.country = country
        self.join_date = join_date
        self.is_online = is_online
        self.is_supporter = is_supporter
        self.cover_url = cover_url
        self.qqid = qqid
        self.pp = pp
        self.play_count = play_count
        self.grade = grade
        self.has_supported = has_supported
        self.avatar_url = avatar_url
        self.total_hits = total_hits
        self.max_combo = max_combo
        self.level = level
        self.level_progress = level_progress
        self.play_time = play_time
        self.mode = mode
        self.monthly_playcounts = monthly_playcounts


def load_from_api(json_resp: dict, mode: int,qqid: int, ) -> User:
    stat = json_resp.get("statistics")
    if stat != None:
        u = User(
            mode=mode,
            avatar_url=json_resp.get("avatar_url"),
            has_supported=json_resp.get("has_supported"),
            play_count=stat.get("play_count"),
            qqid=qqid,
            play_time=stat.get("play_time"),
            ranking_country=stat.get("country_rank"),
            ranking_global=stat.get("global_rank"),
            grade=stat.get("grade_counts"),
            level=stat.get("level").get("current"),
            level_progress=stat.get("level").get("progress"),
            pp=stat.get("pp"),
            is_online=json_resp.get("is_online"),
            is_supporter=json_resp.get("is_supporter"),
            cover_url=json_resp.get("cover_url"),
            join_date=json_resp.get("join_date"),
            country=json_resp.get("country"),
            uid=json_resp.get("id"),
            name=json_resp.get("username"),
            score_ranked=stat.get("ranked_score"),
            score_all=stat.get("total_score"),
            max_combo=stat.get("maximum_combo"),
            acc=stat.get("hit_accuracy"),
            total_hits=stat.get("total_hits"),
            monthly_playcounts=json_resp.get("monthly_playcounts"),
        )
    else:
        u=User(
            mode=mode,
            avatar_url=json_resp.get("avatar_url"),
            has_supported=json_resp.get("has_supported"),
            qqid=qqid,
            is_online=json_resp.get("is_online"),
            is_supporter=json_resp.get("is_supporter"),
            cover_url=json_resp.get("cover_url"),
            join_date=json_resp.get("join_date"),
            country=json_resp.get("country"),
            uid=json_resp.get("id"),
            name=json_resp.get("username"),
            monthly_playcounts=json_resp.get("monthly_playcounts"),
            
        )
    return u


def load_from_json(jsonfile: dict) -> User:
    u = User(
        avatar_url=jsonfile.get("avatar_url"),
        has_supported=jsonfile.get("has_supported"),
        play_count=jsonfile.get("play_count"),
        qqid=jsonfile.get("qqid"),
        ranking_country=jsonfile.get("ranking_country"),
        pp=jsonfile.get("pp"),
        grade=jsonfile.get("grade"),
        is_online=jsonfile.get("is_online"),
        is_supporter=jsonfile.get("is_supporter"),
        cover_url=jsonfile.get("cover_url"),
        join_date=jsonfile.get("join_date"),
        country=jsonfile.get("country"),
        uid=jsonfile.get("uid"),
        name=jsonfile.get("name"),
        score_ranked=jsonfile.get("score_ranked"),
        score_all=jsonfile.get("score_all"),
        acc=jsonfile.get("acc"),
        ranking_global=jsonfile.get("ranking_global"),
        total_hits=jsonfile.get("total_hits"),
        max_combo=jsonfile.get("max_combo"),
        level=jsonfile.get("level"),
        level_progress=jsonfile.get("level_progress"),
        play_time=jsonfile.get("play_time"),
        mode=jsonfile.get("mode"),
        monthly_playcounts=jsonfile.get("monthly_playcounts"),
    )
    return u


def save_to_json(u: User, file: TextIOWrapper) -> None:
    l = u.__dict__
    json.dump(l, file)


cwd = getcwd()


class Qqid_to_uid:
    def qqid_save_to_json(u: User) -> None:
        qqid_file = cwd + "/mains/plugins\\osu_sbot\\json\\qq\\" + str(u.qqid) + ".json"
        l = {}
        l["uid"] = u.uid
        with open(qqid_file, "w+", encoding="utf-8") as jsonfile:
            json.dump(l, jsonfile)

    def qqid_load(qqid) -> int:
        try:
            qqid_file = cwd + "/mains/plugins\\osu_sbot\\json\\qq\\" + str(qqid) + ".json"
            with open(qqid_file, "r") as jsonfile:
                j:dict = json.load(jsonfile)
            return int(j.get("uid"))
        except:
            return None

from mains.plugins.osu_sbot.beatmap import Beatmap, BeatmapSet, beatmap_dict_to_class
from mains.plugins.osu_sbot.user import User, load_from_json


class Score:
    id: int = None
    best_id: int = None
    user_id: int = None
    accuracy: float = None
    mods: list = None
    score: int = None
    max_combo: int = None
    perfect: bool = False
    statistics: dict = None
    passed: bool = None
    pp: float = None
    rank: str = None
    created_at: str = None
    mode: str = None
    mode_int: int = None
    replay: bool = None
    beatmap: Beatmap = Beatmap()
    beatmapset: BeatmapSet = BeatmapSet()
    user: User = User()


    def __init__(
        self,
        id: int=id,
        best_id: int=best_id,
        user_id: int=user_id,
        accuracy: float=accuracy,
        mods: list=mods,
        score: int=score,
        max_combo: int=max_combo,
        perfect: bool=perfect,
        statistics: dict=statistics,
        passed: bool=passed,
        pp: float=pp,
        rank: str=rank,
        created_at: str=created_at,
        mode: str=mode,
        mode_int: str=mode_int,
        replay: bool=replay,
        beatmap: Beatmap=beatmap,
        beatmapset: BeatmapSet=beatmapset,
        user: User=user,
    ) -> None:
        self.id = id
        self.best_id = best_id
        self.user_id = user_id
        self.accuracy = accuracy
        self.mods = mods
        self.score = score
        self.max_combo = max_combo
        self.perfect = perfect
        self.statistics = statistics
        self.passed = passed
        self.pp = pp
        self.rank = rank
        self.created_at = created_at
        self.mode = mode
        self.mode_int = mode_int
        self.replay = replay
        self.beatmap = beatmap
        self.beatmapset = beatmapset
        self.user = user


def score_data_to_score(scoredata: dict) -> Score:
    user = load_from_json(scoredata.get("user"))
    beatmap, beatmapset = beatmap_dict_to_class(
        scoredata.get("beatmap"),scoredata.get("beatmapset")
    )

    s = Score(
        id=scoredata.get("id"),
        best_id=scoredata.get("best_id"),
        user_id=scoredata.get("user_id"),
        accuracy=scoredata.get("accuracy"),
        mods=scoredata.get("mods"),
        score=scoredata.get("score"),
        max_combo=scoredata.get("max_combo"),
        perfect=scoredata.get("perfect"),
        statistics=scoredata.get("statistics"),
        passed=scoredata.get("passed"),
        pp=scoredata.get("pp"),
        rank=scoredata.get("rank"),
        created_at=scoredata.get("created_at"),
        mode=scoredata.get("mode"),
        mode_int=scoredata.get("mode_int"),
        replay=scoredata.get("replay"),
        beatmap=beatmap,
        beatmapset=beatmapset,
        user=user,
    )

    return s

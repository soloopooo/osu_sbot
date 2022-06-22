class Beatmap:
    accuracy: float = None
    ar: float = None
    beatmapset_id: int = None
    bpm: float = None
    convert: bool = None
    count_circles: int = None
    count_sliders: int = None
    count_spinners: int = None
    cs: float = None
    deleted_at: str = None
    drain: float = None
    hit_length: int = None
    is_scoreable: bool = None
    last_updated: str = None
    mode_int: int = None  # may be deprecated soon
    mode: str = None
    passcount: int = None
    playcount: int = None
    ranked: int = None
    url: str = None
    beatmapset: dict = None
    difficulty_rating: float = None
    version: str = None
    id: int = None
    ar: int = None

    def __init__(
        self,
        ar: int = ar,
        accuracy: float = accuracy,
        beatmapset_id: int = beatmapset_id,
        bpm: float = bpm,
        convert: bool = convert,
        count_circles: int = count_circles,
        count_sliders: int = count_sliders,
        count_spinners: int = count_spinners,
        cs: float = cs,
        deleted_at: str = deleted_at,
        drain: float = drain,
        hit_length: int = hit_length,
        is_scoreable: bool = is_scoreable,
        last_updated: str = last_updated,
        mode_int: int = mode_int,
        mode: str = mode,
        passcount: int = passcount,
        playcount: int = playcount,
        ranked: int = ranked,
        url: str = url,
        beatmapset: dict = beatmapset,
        difficulty_rating: float = difficulty_rating,
        version: str = version,
        id: int = id,
    ) -> None:
        self.accuracy = accuracy
        self.beatmapset_id = beatmapset_id
        self.bpm = bpm
        self.convert = convert
        self.count_circles = count_circles
        self.count_sliders = count_sliders
        self.count_spinners = count_spinners
        self.cs = cs
        self.deleted_at = deleted_at
        self.drain = drain
        self.hit_length = hit_length
        self.is_scoreable = is_scoreable
        self.last_updated = last_updated
        self.mode_int = mode_int
        self.mode = mode
        self.passcount = passcount
        self.playcount = playcount
        self.ranked = ranked
        self.url = url
        self.beatmapset = beatmapset
        self.difficulty_rating = difficulty_rating
        self.version = version
        self.id = id
        self.ar = ar


class BeatmapSet:
    artist: str = None
    artist_unicode: str = None
    bpm: int = None
    covers: dict = None
    creator: str = None
    favorite_count: int = None
    id: int = None  # Same as Beatmap.beatmapset_id
    is_scoreable: bool = False
    last_updated: str = None
    nsfw: bool = False
    play_count: int = None
    preview_url: str = None
    ranked: int = None
    ranked_date: str = None
    ratings: dict = None
    source: str = None
    status: str = None
    storyboard: bool = None
    submitted_date: str = None
    tags: str = None
    title: str = None
    title_unicode: str = None
    track_id: int = None
    user_id: int = None
    video: bool = None

    def __init__(
        self,
        artist: str = artist,
        artist_unicode: str = artist_unicode,
        bpm: int = bpm,
        covers: dict = covers,
        creator: str = creator,
        favorite_count: int = favorite_count,
        id: int = id,
        is_scoreable: bool = is_scoreable,
        last_updated: str = last_updated,
        nsfw: bool = nsfw,
        play_count: int = play_count,
        preview_url: str = preview_url,
        ranked: int = ranked,
        ranked_date: str = ranked_date,
        ratings: dict = ratings,
        source: str = source,
        status: str = status,
        storyboard: bool = storyboard,
        submitted_date: str = submitted_date,
        tags: str = tags,
        title: str = title,
        title_unicode: str = title_unicode,
        track_id: int = track_id,
        user_id: int = user_id,
        video: bool = video,
    ) -> None:
        self.artist = artist
        self.artist_unicode = artist_unicode
        self.bpm = bpm
        self.covers = covers
        self.creator = creator
        self.favorite_count = favorite_count
        self.id = id
        self.is_scoreable = is_scoreable
        self.last_updated = last_updated
        self.nsfw = nsfw
        self.play_count = play_count
        self.preview_url = preview_url
        self.ranked = ranked
        self.ranked_date = ranked_date
        self.ratings = ratings
        self.source = source
        self.status = status
        self.storyboard = storyboard
        self.submitted_date = submitted_date
        self.tags = tags
        self.title = title
        self.title_unicode = title_unicode
        self.track_id = track_id
        self.user_id = user_id
        self.video = video


def beatmap_dict_to_class(
    beatmapdict: dict, beatmapsetdict: dict
) -> "tuple[Beatmap,BeatmapSet]":
    bm = None
    bmset = None
    if beatmapdict != None:
        bm = Beatmap(
            accuracy=beatmapdict.get("accuracy"),
            beatmapset_id=beatmapdict.get("beatmapset_id"),
            bpm=beatmapdict.get("bpm"),
            convert=beatmapdict.get("convert"),
            count_circles=beatmapdict.get("count_circles"),
            count_sliders=beatmapdict.get("count_sliders"),
            count_spinners=beatmapdict.get("count_spinners"),
            cs=beatmapdict.get("cs"),
            deleted_at=beatmapdict.get("deleted_at"),
            drain=beatmapdict.get("drain"),
            hit_length=beatmapdict.get("hit_length"),
            is_scoreable=beatmapdict.get("is_scoreable"),
            last_updated=beatmapdict.get("last_updated"),
            mode=beatmapdict.get("mode"),
            mode_int=beatmapdict.get("mode_int"),
            passcount=beatmapdict.get("passcount"),
            playcount=beatmapdict.get("playcount"),
            ranked=beatmapdict.get("ranked"),
            url=beatmapdict.get("url"),
            beatmapset=beatmapdict.get("beatmapset"),
            difficulty_rating=beatmapdict.get("difficulty_rating"),
            version=beatmapdict.get("version"),
            id=beatmapdict.get("id"),
            ar=beatmapdict.get("ar"),
        )

        if beatmapsetdict == None:
            beatmapsetdict = beatmapdict.get("beatmapset")
    if beatmapsetdict != None:
        bmset = BeatmapSet(
            artist=beatmapsetdict.get("artist"),
            artist_unicode=beatmapsetdict.get("artist_unicode"),
            bpm=beatmapsetdict.get("bpm"),
            covers=beatmapsetdict.get("covers"),
            creator=beatmapsetdict.get("creator"),
            favorite_count=beatmapsetdict.get("favorite_count"),
            id=beatmapsetdict.get("id"),
            is_scoreable=beatmapsetdict.get("is_scoreable"),
            last_updated=beatmapsetdict.get("last_updated"),
            nsfw=beatmapsetdict.get("nsfw"),
            play_count=beatmapsetdict.get("play_count"),
            preview_url=beatmapsetdict.get("preview_url"),
            ranked=beatmapsetdict.get("ranked"),
            ranked_date=beatmapsetdict.get("ranked_date"),
            ratings=beatmapsetdict.get("ratings"),
            source=beatmapsetdict.get("source"),
            status=beatmapsetdict.get("status"),
            storyboard=beatmapsetdict.get("storyboard"),
            submitted_date=beatmapsetdict.get("submitted_date"),
            tags=beatmapsetdict.get("tags"),
            title=beatmapsetdict.get("title"),
            title_unicode=beatmapsetdict.get("title_unicode"),
            track_id=beatmapsetdict.get("track_id"),
            user_id=beatmapsetdict.get("user_id"),
            video=beatmapsetdict.get("video"),
        )
    return bm, bmset


def beatmap_to_beatmapset(beatmap: Beatmap) -> BeatmapSet:
    bs = beatmap.beatmapset

    bs_b = beatmap_dict_to_class(None, bs)
    return bs_b

    # DONE: GetBeatmapSet

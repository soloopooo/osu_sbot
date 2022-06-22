from mains.plugins.osu_sbot.exceptions import IDNotFoundException
from mains.plugins.osu_sbot.user import Qqid_to_uid
from mains.plugins.osu_sbot.score import Score
from mains.plugins.osu_sbot.load_data import Load_osu_data


async def get_recent(
    authkey:str,
    uid: int = None,
    qqid: int = None,
    ispass: bool = False,
    offset: int = 0,
    limit: int = 1,
    mode: int = 0,
) -> 'list[Score]':
    '''
    returns a list of specific user's recent score.
    
    uid and qqid must have one available.
    
    ispass: show the score that passed or not passed.
    offset: show the #offset score of the list.
    limit: limit the amount of score.
    mode: 0=osu, 1=fruits, 2=taiko, 3=mania
    '''
    async def __get_recent_score(uid: int) -> 'list[Score]':
        include_fails = 0 if ispass else 1
        return (await Load_osu_data.load_score(
            authkey=authkey,
            uid=uid,
            mode=mode,
            limit=limit,
            offset=offset,
            include_fails=include_fails,
            type=2,
        ))

    if qqid == None:
        if uid == None:
            raise IDNotFoundException
        else:
            return  (await __get_recent_score(uid=uid))

    else:
        if uid == None:
            uid = Qqid_to_uid.qqid_load(qqid=qqid)
            return  (await __get_recent_score(uid=uid))

async def get_bp(
    authkey:str,
    uid: int = None,
    qqid: int = None,
    offset: int = 0,
    limit: int = 1,
    mode: int = 0,
) -> 'list[Score]':
    '''
    like get_recent, but is for best play.
    
    use offset and limit parameters to fill the user's need.
    
    bp -n 1 : offset = 0 
    '''
    async def __get_bp_score(uid: int) -> 'list[Score]':
        include_fails = 0
        return (await Load_osu_data.load_score(
            authkey=authkey,
            uid=uid,
            mode=mode,
            limit=limit,
            offset=offset,
            include_fails=include_fails,
            type=0,
        ))

    if qqid == None:
        if uid == None:
            raise IDNotFoundException
        else:
            return (await __get_bp_score(uid=uid))

    else:
        if uid == None:
            uid = Qqid_to_uid.qqid_load(qqid=qqid)
            return (await __get_bp_score(uid=uid))



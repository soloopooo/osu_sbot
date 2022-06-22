from mains.plugins.osu_sbot.user import Qqid_to_uid, User
from mains.plugins.osu_sbot.load_data import Load_osu_data
from mains.plugins.osu_sbot.stor_json import JsonStorage

async def binding(authkey:str,qqid:int,uid:int)->User:
    '''
    Needs to try_catch at FRONT
    '''
    u=(await Load_osu_data.load_user(authkey=authkey,uid=uid,qqid=qqid,))
    JsonStorage.stor(u)
    Qqid_to_uid.qqid_save_to_json(u)
    return u
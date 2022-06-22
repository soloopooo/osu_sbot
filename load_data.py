import json
from os import getcwd
from mains.plugins.osu_sbot.beatmap import Beatmap, BeatmapSet, beatmap_dict_to_class
from mains.plugins.osu_sbot.score import Score, score_data_to_score
from mains.plugins.osu_sbot.user import User, load_from_api
from mains.plugins.osu_sbot.exceptions import *
import time
import asyncio
import aiohttp

legacyapiurl = "https://osu.ppy.sh/api/"
apiurl = "https://osu.ppy.sh/api/v2/"
oauth_url = "https://osu.ppy.sh/oauth/token"
cwd = getcwd()


class Auth_data:
    async def get_auth_code(
        client_id: int, client_secret: str, grant_type: str = "client_credentials"
    ) -> dict:
        """
        in dict:
        token_type:	string,	The type of token, this should always be Bearer.
        expires_in:	number,	The number of seconds the token will be valid for.
        access_token:	string,	The access token.
        """
        auth_file = cwd + "/mains/plugins/osu_sbot/json/auth/auth.json"
        t = time.time()
        time_now = int(t)

        async def __save_auth(data: str) -> None:
            with open(auth_file, mode="w", encoding="utf-8") as file:
                json.dump(data, file)

        async def __get_auth(client_id, client_secret) -> str:
            url = oauth_url
            data = {
                "client_id": client_id,
                "client_secret": client_secret,
                "grant_type": grant_type,
                "scope": "public",
            }
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
            async with aiohttp.ClientSession() as session:
                async with session.post(url,json=data,headers=headers) as rep:
                    #rep = requests.post(url, json=data, headers=headers)
                    l = json.loads((await rep.text()))
                    l["expires_in"] = time_now + int(l["expires_in"])
            return json.dumps(l)

        async def __load_auth() -> dict:
            try:
                with open(auth_file, "r") as file:
                    jsondata = json.loads(json.load(file))
                    if jsondata["expires_in"] < time_now:
                        l = (await __get_auth(client_id=client_id, client_secret=client_secret))
                        await __save_auth(l)
                        jsondata = (await __load_auth())
                        return jsondata
                    else:
                        return jsondata
            except:
                l = (await __get_auth(client_id=client_id, client_secret=client_secret))
                await __save_auth(l)
                await __load_auth()

        return (await __load_auth())


class Load_osu_data:
    def type_convert(type: int) -> str:
        """
        0=best,1=firsts,2=recent
        """
        type_str = ["best", "firsts", "recent"]
        return type_str[type]

    def mode_convert(mode: int) -> str:
        """
        0=std,1=ctb,2=taiko,3=mania
        """
        mode_str = ["osu", "fruits", "taiko", "mania"]
        return mode_str[mode]

    async def get_api(url:str, authkey:str, params: dict = {}, apiversion=2)->'(dict|list)':
        """
        base method of get datas of osu's api.
        url: api's url
        authkey:...
        params: Params to get.
        apiversion: default is 2. apiversion 1 can have some problems.
        """
        if apiversion == 1:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
            }
            url = url + "&k=" + authkey
        elif apiversion == 2:
            headers = {
                "Authorization": "Bearer " + authkey,
                "Content-Type": "application/json",
                "Accept": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
            }
        async with aiohttp.ClientSession() as session_api:
            async with session_api.get(url=url,headers=headers,params=params) as resp:
                if resp.status == 200:
                    content = (await resp.text())
                    json_dict = json.loads(content)
                    return json_dict
                else:
                    raise APIGetException(code=resp.status)
        #resp = requests.get(url, headers=headers, params=params)

    async def load_user(authkey: str, uid: int, qqid: int=None, mode: int = 0) -> User:
        """
        load_user: Load users data FOR SAVING, Requires: OAUTHV2.
        Params:
        mode: 0=osu, 1=fruits, 2=taiko,3=mania
        """
        modec = Load_osu_data.mode_convert(mode)
        url = apiurl + "users/" + str(uid) + "/" + modec + "?key=id"
        json_resp = (await Load_osu_data.get_api(authkey=authkey, apiversion=2, url=url))
        u = load_from_api(json_resp=json_resp, qqid=qqid, mode=mode)
        return u

    async def load_score(
        authkey,
        uid,
        mode: int,
        limit: int,
        offset: int,
        include_fails: int,
        type: int,
    ) -> 'list[Score]':
        """
        load a user's score.
        Params:
        mode: 0=osu, 1=fruits, 2=taiko,3=mania
        limit: controls the score(s)' number
        offset: the scores' offset
        include_fails: include fail scores.
        type: 0=best, 1=firsts, 2=recent
        """
        if uid == None:
            raise IDNotFoundException(reason="Please give us a valid uid.")
        url = (
            apiurl
            + "users/"
            + str(uid)
            + "/scores/"
            + Load_osu_data.type_convert(type=type)
        )
        params = {
            "include_fails": include_fails,
            "mode": Load_osu_data.mode_convert(mode),
            "limit": limit,
            "offset": offset,
        }
        json_data = (await Load_osu_data.get_api(url=url, params=params, authkey=authkey))
        s=[]
        for i in json_data:
            s.append(score_data_to_score(scoredata=i))
        return s

    async def load_beatmap(
        authkey,
        bmid:int
    )->'tuple[Beatmap,BeatmapSet]':
        url = apiurl + "beatmaps/" + str(bmid)
        bmjson = (await Load_osu_data.get_api(url,authkey))
        bm,bms = beatmap_dict_to_class(bmjson,None)
        return bm,bms
        
        
    async def load_mps(authkey: str, mpid: int):
        #TODO
        if mpid == None:
            raise IDNotFoundException(reason="Please give us a valid multi match id.")

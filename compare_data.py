from mains.plugins.osu_sbot.user import User
from mains.plugins.osu_sbot.stor_json import JsonStorage
import asyncio


class Compare:
    """
    Compare scores,etc. to local data. Auto save user's attribute after this function,
    so Re-Saving is not necessary.
    """

    async def compare_user(u: User) -> dict:
        async def compare_user_l(u: User) -> dict:
            uid = u.uid
            u_from_json = JsonStorage.load_user(uid=uid, mode=u.mode)
            diff = {}
            diff_keys = [
                "score_all",
                "total_hits",
                "score_ranked",
                "pp",
                "level",
                "level_progress",
                "max_combo",
                "acc",
                "ranking_country",
                "ranking_global",
                "play_count",
            ]
            for diff_key in diff_keys:
                try:
                    diff[diff_key] = u.__dict__[diff_key] - u_from_json.__dict__[diff_key]
                except:
                    diff[diff_key] = 0
            diff["grade"] = {}
            diff_grade_keys = ["ss", "ssh", "s", "sh", "a"]
            for diff_grade_key in diff_grade_keys:
                diff["grade"][diff_grade_key] = (
                    u.grade[diff_grade_key] - u_from_json.grade[diff_grade_key]
                )
            JsonStorage.stor(u)
            return diff

        try:
            return await compare_user_l(u=u)
        except:
            JsonStorage.stor(u)
            await compare_user_l(u)
            # raise NoMoreDataException

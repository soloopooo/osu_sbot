from mains.plugins.osu_sbot.user import User, load_from_json, save_to_json,Qqid_to_uid
import json
import os
cwd = os.getcwd()

class JsonStorage:
    def stor(user:User):
        json_file = cwd + "/mains/plugins/osu_sbot/json/osu/"+str(user.uid)+"m"+str(user.mode)+".json"
        with open(json_file,"w+",encoding="utf-8") as file:
            save_to_json(user,file)
        Qqid_to_uid.qqid_save_to_json(user)
        
    def load_user(uid:int,mode:int)->User:
        try:
            json_file = cwd+"/mains/plugins/osu_sbot/json/osu/"+str(uid)+"m"+str(mode)+".json"
            with open(json_file,"r") as file:
                json_str = json.load(file)
            u_new = load_from_json(json_str)
            return u_new
        except:
            return User(
                uid=uid,
                score_all=0,
                total_hits=0,
                score_ranked=0,
                pp=0,
                level=0,
                level_progress=0,
                max_combo=0,
                acc=0,
                ranking_country=0,
                ranking_global=0,
                play_count=0,
                grade={
                    "ss":0,
                    "ssh":0,
                    "s":0,
                    "sh":0,
                    "a":0
                }
            )

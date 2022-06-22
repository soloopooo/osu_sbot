from datetime import datetime, timedelta
from genericpath import getsize
import os
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
from mains.plugins.osu_sbot.beatmap import Beatmap, BeatmapSet
from mains.plugins.osu_sbot.load_data import Load_osu_data
from mains.plugins.osu_sbot.score import Score
from mains.plugins.osu_sbot.user import User
from io import BytesIO
import aiohttp

cwd = os.getcwd()
BOT_TEMPLATE_USER_INFO_IMG = (
    cwd + "/mains/plugins/osu_sbot/data/images/bot_template_user_info.png"
)
SCORE_MINI = cwd + "/mains/plugins/osu_sbot/data/images/score_template_small.png"
BOT_IMG_DIR = cwd + "/mains/plugins/osu_sbot/data/images/"
BOT_SCORE_BIG = cwd + "/mains/plugins/osu_sbot/data/images/bot_template_score_big.png"
BOT_SCORE_SKIN_DIR = cwd + "/mains/plugins/osu_sbot/data/images/score_skin"
agencyfb_font = cwd + "/mains/plugins/osu_sbot/data/fonts/AGENCYR.TTF"
sarasa_font = cwd + "/mains/plugins/osu_sbot/data/fonts/sarasa-ui-sc-regular.ttf"
cataneo_font = cwd + "/mains/plugins/osu_sbot/data/fonts/TT0952M_.TTF"

userpanel_name_rgb = (54, 199, 199)
userpanel_pp_rgb = (182, 211, 60)

infopanel_plus_rgb = (238, 22, 101)
infopanel_reduce_rgb = (46, 197, 221)
infopanel_ranking_rgb = (198, 229, 234)
infopanel_other_rgb = (229, 217, 191)

userpanel_avatar_leftup = 35, 43
userpanel_name_center = 232, 72
userpanel_pp_center = 185, 111
userpanel_mode_rightdown = 365, 182

infopanel_acc_rightup = 492, 60
infopanel_acc_addon_leftup = 502, 60
infopanel_playcount_rightup = 750, 60
infopanel_playcount_addon_leftup = 760, 60
infopanel_ranked_score_rightup = 1065, 60
infopanel_ranked_score_addon_leftup = 1075, 60
infopanel_world_ranking_rightup = 1418, 60
infopanel_world_ranking_addon_leftup = 1428, 60
infopanel_pp_rightup = 492, 130
infopanel_pp_addon_leftup = 502, 130
infopanel_total_hits_rightup = 750, 130
infopanel_total_hits_addon_leftup = 760, 130
infopanel_total_score_rightup = 1065, 130
infopanel_total_score_addon_leftup = 1075, 130
infopanel_local_ranking_rightup = 1418, 130
infopanel_local_ranking_addon_leftup = 1428, 130


# 0: recent score 1: best score
infopanel_score_center = [(480, 460), (1430, 460)]
infopanel_score_leftup = [(25, 265), (985, 265)]

scorepanel_mini_title_and_artist_rgb = (234, 186, 110)
scorepanel_mini_info_basic_rgb = (210, 222, 155)
scorepanel_mini_difficulty_rgb = (230, 201, 37)
scorepanel_mini_pp_rgb = (210, 222, 155)
scorepanel_mini_info_time_rgb = (233, 232, 174)
scorepanel_mini_mods_rgb = (189, 228, 151)
scorepanel_mini_difficulty_stars_rgb = (60, 210, 241)
scorepanel_mini_ranking_rgba = {
    "xh": (219, 217, 208, 72),
    "sh": (219, 217, 208, 72),
    "ss": (230, 201, 37, 72),
    "s": (230, 201, 37, 72),
    "a": (102, 255, 0, 72),
    "b": (0, 162, 255, 72),
    "c": (231, 159, 223, 72),
    "d": (231, 159, 166, 72),
    "f": (0, 0, 0, 72),
    "XH": (219, 217, 208, 72),
    "SH": (219, 217, 208, 72),
    "X": (230, 201, 37, 72),
    "SS": (230, 201, 37, 72),
    "S": (230, 201, 37, 72),
    "A": (102, 255, 0, 72),
    "B": (0, 162, 255, 72),
    "C": (231, 159, 223, 72),
    "D": (231, 159, 166, 72),
    "F": (0, 0, 0, 72),
}
scorepanel_mini_stats_rgb = {
    "count_300": (60, 210, 241),
    "count_geki": (30, 242, 195),
    "count_katu": (60, 241, 60),
    "count_200": (60, 241, 60),
    "count_100": (129, 237, 129),
    "count_50": (231, 215, 39),
    "count_0": (234, 142, 161),
    "count_miss": (234, 142, 161),
}

scorepanel_mini_title_leftup = 15, 14
scorepanel_mini_title_x_max = 160
scorepanel_mini_artist_title_leftup = 15, 29
scorepanel_mini_artist_title_x_max = 140
scorepanel_mini_difficulty_leftup = 16, 113
scorepanel_mini_difficulty_x_max = 120
scorepanel_mini_score_leftup = 55, 50
scorepanel_mini_acc_leftup = 48, 73
scorepanel_mini_pp_leftup = 48, 95
scorepanel_mini_ymd_rightup = 293, 5
scorepanel_mini_hms_rightup = 293, 24
scorepanel_mini_difficulty_stars_rightup = 239, 25
scorepanel_mini_mods_rightup = 293, 45
scorepanel_statistics_right_x = 293
scorepanel_statistics_initial_y = 68
scorepanel_statistics_left_x = 172
scorepanel_statistics_y_add = 18
scorepanel_mini_ranking_center = 70, 70
scorepanel_mini_ranking_right = 130
scorepanel_mini_ranking_up = 15
scorepanel_mini_maxcombo_rightup = 216, 5

playcountpanel_monthly_playcount_rightup = 1880, 715
playcountpanel_grade_center_dict = {
    "XH": (1065, 875),
    "SH": (1177, 875),
    "X": (1285, 875),
    "S": (1390, 875),
    "A": (1493, 875),
    "ssh": (1065, 875),
    "sh": (1177, 875),
    "ss": (1285, 875),
    "s": (1390, 875),
    "a": (1493, 875),
}
playcountpanel_max_combo_leftup = 1140, 722
playcountpanel_play_time_leftup = 1120, 935
playcountpanel_level_leftup = 1067, 1019
playcountpanel_joined_at_leftup = 1115, 977
playcountpanel_rgb = (229, 217, 191)

font_agency_100 = ImageFont.truetype(agencyfb_font, size=100)
font_agency_32 = ImageFont.truetype(agencyfb_font, size=32)
font_agency_28 = ImageFont.truetype(agencyfb_font, size=28)
font_agency_18 = ImageFont.truetype(agencyfb_font, size=18)
font_agency_16 = ImageFont.truetype(agencyfb_font, size=16)
font_agency_12 = ImageFont.truetype(agencyfb_font, size=12)
font_sarasa_40 = ImageFont.truetype(sarasa_font, size=40)
font_sarasa_18 = ImageFont.truetype(sarasa_font, size=18)
font_sarasa_14 = ImageFont.truetype(sarasa_font, size=14)
font_sarasa_13 = ImageFont.truetype(sarasa_font, size=13)
font_sarasa_11 = ImageFont.truetype(sarasa_font, size=11)
font_sarasa_9 = ImageFont.truetype(sarasa_font, size=9)
font_cataneo_85 = ImageFont.truetype(cataneo_font, size=85)
font_cataneo_53 = ImageFont.truetype(cataneo_font, size=53)
font_cataneo_48 = ImageFont.truetype(cataneo_font, size=48)


async def __adj_weight(
    text: str,
    weight_limit: int,
    font: ImageFont.FreeTypeFont = ...,
    text_adj: str = None,
) -> str:
    """
    adjust the text by calculating font_weight.
    """

    def __text_width_adjust(text: str) -> "tuple[str, str]":
        text_end = text[text.__len__() - 3 :]
        text_start = text[0 : (text.__len__() - 4)]
        return (text_start, text_end)

    if text_adj == None:
        text_adj = text
    weight, height = font.getsize(text=text)
    if weight > weight_limit:
        text_start, text_end = __text_width_adjust(text=text_adj)
        text_0 = text_start + text_end
        text_1 = text_start + "..." + text_end
        text = await __adj_weight(
            text=text_1,
            font=font,
            weight_limit=weight_limit,
            text_adj=text_0,
        )
    else:
        return text
    return text


async def __draw_userpanel_info(
    user: User, info_img: Image.Image, mode: int
) -> Image.Image:
    async def __getavatar(avatar_url: str) -> BytesIO:
        async with aiohttp.ClientSession() as session_avatar:
            async with session_avatar.get(avatar_url) as avatar_img_get:
                avatar_byte = BytesIO((await avatar_img_get.read()))
                return avatar_byte

    # 0 Draw Userpanel.Info
    # 0.0 Draw avatar
    avatar_url = user.avatar_url
    avatar_byte = await __getavatar(avatar_url=avatar_url)
    avatar_image = Image.open(avatar_byte).convert(mode="RGBA")
    avatar_image = avatar_image.resize((98, 98))
    info_img.paste(avatar_image, box=(36, 43, 134, 141))
    info_draw = ImageDraw.Draw(info_img)
    # 0.1 Draw username
    name_adj = await __adj_weight(text=user.name, weight_limit=207, font=font_sarasa_18)
    info_draw.text(
        userpanel_name_center,
        text=name_adj,
        fill=userpanel_name_rgb,
        anchor="mm",
        font=font_sarasa_18,
    )
    # 0.2 Draw pp
    info_draw.text(
        userpanel_pp_center,
        text=str(user.pp) + "pp",
        fill=userpanel_pp_rgb,
        anchor="mm",
        font=font_sarasa_13,
    )
    # 0.3 Draw mode
    mode_list = ["osu!", "ctb", "taiko", "mania"]
    mode_str = mode_list[mode]
    info_draw.text(
        xy=userpanel_mode_rightdown,
        anchor="rb",
        font=font_sarasa_40,
        fill=userpanel_name_rgb,
        text=mode_str,
    )
    return info_img


async def draw_info(
    user: User,
    compare_data: dict,
    recent_score: "list[Score]",
    bp_score: "list[Score]",
    mode: int = 0,
) -> "BytesIO":
    template_info = Image.open(BOT_TEMPLATE_USER_INFO_IMG)
    template_score = Image.open(SCORE_MINI)

    async def __get_score_cover(score_list: "list[Score]") -> "dict[str,Image.Image]":
        """get score's cover pic.

        Args:
            score_list (list[Score]):

        Returns:
            dict[str,Image.Image]:
        """
        dict_images: dict[str, Image.Image] = {}
        try:
            for score in score_list:
                try_times = 2
                try:
                    async def trying_get():
                        async with aiohttp.ClientSession() as session_get_score:
                            async with session_get_score.get(
                                url=score.beatmapset.covers.get("card")
                            ) as card:
                                cardBuffer = BytesIO(initial_bytes=(await card.read()))
                                dict_images.update(
                                    {
                                        score.id: Image.open(cardBuffer).convert(
                                            mode="RGBA"
                                        )
                                    }
                                )

                    await trying_get()
                except:
                    try_times -= 1
                    if try_times > 0:
                        await trying_get()
                    else:
                        dict_images.update({score.id: None})
        except:
            return None
        return dict_images

    def __ranking_convert(rank: str) -> str:
        rank_dict = {
            "xh": "X+",
            "x": "X",
            "sh": "S+",
            "ss": "X",
            "s": "S",
            "a": "A",
            "b": "B",
            "c": "C",
            "d": "D",
            "f": "F",
            "XH": "X+",
            "X": "X",
            "SH": "S+",
            "SS": "X",
            "S": "S",
            "A": "A",
            "B": "B",
            "C": "C",
            "D": "D",
            "F": "F",
        }
        return rank_dict.get(rank)

    # define a func to draw easier cuz plus and reduce...
    async def __draw_stats(
        xy_origin: "tuple[int,int]",
        xy_change: "tuple[int,int]",
        text_origin: str,
        image_draw: ImageDraw.ImageDraw,
        nums_change: "int | float" = None,
        isrank: bool = False,
        isacc: bool = False,
        origin_anchor: str = "rt",
        change_anchor: str = "lt",
        font: ImageFont.FreeTypeFont = font_agency_28,
    ) -> None:
        image_draw.text(
            xy=xy_origin,
            text=text_origin,
            fill=(infopanel_ranking_rgb if isrank else infopanel_other_rgb),
            font=font,
            anchor=origin_anchor,
        )
        if nums_change == None:
            return None
        parser = (
            "-"
            if (isrank and nums_change > 0) or ((not isrank) and nums_change < 0)
            else "+"
            if (isrank and nums_change < 0) or ((not isrank) and nums_change > 0)
            else ""
        )
        color_change = (
            infopanel_plus_rgb
            if (isrank and nums_change < 0) or ((not isrank) and nums_change > 0)
            else infopanel_reduce_rgb
        )

        nums_change_abs = abs(nums_change)
        text_change = (
            parser + "{:.4f}%".format((nums_change_abs))
            if isacc
            else parser + "#{:,}".format(nums_change_abs)
            if isrank
            else parser + "{:,}".format(nums_change_abs)
            if isinstance(nums_change_abs, int)
            else parser + "{:,.4f}".format(nums_change_abs)
        )

        image_draw.text(
            xy=xy_change,
            text=text_change,
            fill=color_change,
            anchor=change_anchor,
            font=font,
        )

    async def __score_mini_drawing(
        score_list: "list[Score]",
    ) -> "dict[int,Image.Image]":
        """
        Returns a dict of drawed mini score images.
        """
        if score_list == None or score_list.__len__() == 0:
            return None
        dict_score_cover = await __get_score_cover(score_list=score_list)
        dict_score_img: dict[str, Image.Image] = {}

        for score in score_list:
            converted_rank = __ranking_convert(score.rank)
            score_cover = dict_score_cover.get(score.id)
            if score_cover != None:
                score_cover_resized = score_cover.resize(
                    size=template_score.size,
                    box=(50, 0, score_cover.size[0], score_cover.size[1]),
                )
                # 0. Brightness adjust.
                brightness = 0.45
                score_cover_resized_enh = ImageEnhance.Brightness(score_cover_resized)
                score_cover_resized = score_cover_resized_enh.enhance(brightness)
                # 0. Blend cover and template.
                score_image = Image.alpha_composite(score_cover_resized, template_score)
                score_draw = ImageDraw.Draw(score_image)
            else:
                score_image = template_score
                score_draw = ImageDraw.Draw(score_image)

            # 1. Draw Ranking.
            tmp_txt = Image.new(
                mode="RGBA", size=template_score.size, color="#00000000"
            )
            t = ImageDraw.Draw(tmp_txt)
            t.text(
                scorepanel_mini_ranking_center,
                converted_rank,
                fill=scorepanel_mini_ranking_rgba.get(score.rank),
                font=font_agency_100,
                anchor="mm",
            )
            score_image = Image.alpha_composite(score_image, tmp_txt)
            score_draw = ImageDraw.Draw(score_image)

            # 2. Draw Score.
            score_draw.text(
                scorepanel_mini_score_leftup,
                str("{:,}".format(score.score)),
                fill=scorepanel_mini_info_basic_rgb,
                font=font_agency_18,
                anchor="lt",
            )
            # 3. Draw Acc.
            score_draw.text(
                scorepanel_mini_acc_leftup,
                str("%.2f" % (score.accuracy * 100)) + "%",
                fill=scorepanel_mini_info_basic_rgb,
                font=font_agency_18,
                anchor="lt",
            )
            # 4. Draw PP.
            score_draw.text(
                scorepanel_mini_pp_leftup,
                str("{:,.4f}".format(0.000 if score.pp == None else score.pp)),
                fill=scorepanel_mini_pp_rgb,
                anchor="lt",
                font=font_agency_18,
            )
            # Plus: Draw max combo
            score_draw.text(
                scorepanel_mini_maxcombo_rightup,
                "{:,}x".format(score.max_combo),
                fill=scorepanel_mini_info_basic_rgb,
                font=font_agency_18,
                anchor="rt",
            )
            # 5. Draw title, artist, and difficulty.

            score_title = score.beatmapset.title_unicode
            score_artist = score.beatmapset.artist_unicode
            score_difficulty = score.beatmap.version
            score_title_adj = await __adj_weight(
                text=score_title,
                font=font_sarasa_14,
                weight_limit=scorepanel_mini_title_x_max
                - scorepanel_mini_title_leftup[0],
                text_adj=None,
            )
            score_artist_adj = await __adj_weight(
                text=score_artist,
                weight_limit=scorepanel_mini_artist_title_x_max
                - scorepanel_mini_artist_title_leftup[0],
                font=font_sarasa_11,
                text_adj=None,
            )
            score_difficulty_adj = await __adj_weight(
                text="[" + score_difficulty + "]",
                weight_limit=scorepanel_mini_difficulty_x_max
                - scorepanel_mini_difficulty_leftup[0],
                font=font_sarasa_9,
                text_adj=None,
            )
            score_draw.text(
                scorepanel_mini_title_leftup,
                text=score_title_adj,
                fill=scorepanel_mini_title_and_artist_rgb,
                anchor="lt",
                font=font_sarasa_14,
            )
            score_draw.text(
                scorepanel_mini_artist_title_leftup,
                text=score_artist_adj,
                fill=scorepanel_mini_title_and_artist_rgb,
                anchor="lt",
                font=font_sarasa_11,
            )
            score_draw.text(
                scorepanel_mini_difficulty_leftup,
                text=score_difficulty_adj,
                font=font_sarasa_9,
                fill=scorepanel_mini_difficulty_rgb,
                anchor="lt",
            )

            # 6. Draw Time.
            time_str = score.created_at
            time_score = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S+00:00")
            time_score_8 = time_score + timedelta(hours=8)

            time_str_ymd = time_score_8.strftime("%Y-%m-%d")
            time_str_hms = time_score_8.strftime("%H:%M:%S")

            score_draw.text(
                xy=scorepanel_mini_ymd_rightup,
                text=time_str_ymd,
                fill=scorepanel_mini_info_time_rgb,
                anchor="rt",
                font=font_agency_16,
            )
            score_draw.text(
                xy=scorepanel_mini_hms_rightup,
                text=time_str_hms,
                fill=scorepanel_mini_info_time_rgb,
                font=font_agency_16,
                anchor="rt",
            )

            # 7. Draw Stars.
            score_draw.text(
                scorepanel_mini_difficulty_stars_rightup,
                anchor="rt",
                text=str(score.beatmap.difficulty_rating) + "*",
                fill=scorepanel_mini_difficulty_stars_rgb,
                font=font_agency_18,
            )
            # 8. Draw Mods.
            mod_str = ""
            for mod in score.mods:
                mod_str = mod_str + mod
            mod_str_upper = mod_str.upper()
            score_draw.text(
                scorepanel_mini_mods_rightup,
                anchor="rt",
                fill=scorepanel_mini_mods_rgb,
                text=mod_str_upper,
                font=font_agency_18,
            )
            # 9. Draw statistics.
            count = 0
            scorepanel_statistics_y = (
                scorepanel_statistics_initial_y - scorepanel_statistics_y_add
            )

            def __conv_stat(stat_key: str) -> str:
                stat_dic = {
                    "count_300": "300",
                    "count_geki": "300g",
                    "count_katu": "100k",
                    "count_200": "200",
                    "count_100": "100",
                    "count_50": "50",
                    "count_0": "0",
                    "count_miss": "0",
                }
                return stat_dic.get(stat_key)

            # stat_list: do sort.
            stat_list = [
                "count_300",
                "count_geki",
                "count_200",
                "count_100",
                "count_katu",
                "count_50",
                "count_miss",
            ]
            for stat_key in stat_list:
                if score.statistics.get(stat_key) == None:
                    continue
                count += 1
                stat_key_conv = __conv_stat(stat_key)
                color = scorepanel_mini_stats_rgb.get(stat_key)

                if count % 2 != 0:
                    scorepanel_statistics_y = (
                        scorepanel_statistics_y + scorepanel_statistics_y_add
                    )
                    score_draw.text(
                        anchor="lt",
                        xy=(scorepanel_statistics_left_x, scorepanel_statistics_y),
                        text=stat_key_conv + ":" + str(score.statistics.get(stat_key)),
                        fill=color,
                        font=font_agency_16,
                    )
                if count % 2 == 0:
                    score_draw.text(
                        anchor="rt",
                        xy=(scorepanel_statistics_right_x, scorepanel_statistics_y),
                        font=font_agency_16,
                        fill=color,
                        text=stat_key_conv + ":" + str(score.statistics.get(stat_key)),
                    )

            # score_image.show()  # DEBUG
            dict_score_img.update({score.id: score_image})
        return dict_score_img

    async def __info_panel_drawing(
        user: User, compare_dict: dict, mode: int, info_img: Image.Image
    ) -> Image.Image:
        # 0 info
        info_img_x = await __draw_userpanel_info(
            user=user, info_img=info_img, mode=mode
        )
        info_draw = ImageDraw.Draw(info_img_x)
        # 1 Draw Infopanel.Stats
        # 1.0 Draw Acc
        await __draw_stats(
            xy_origin=infopanel_acc_rightup,
            xy_change=infopanel_acc_addon_leftup,
            text_origin="{:.4f}%".format(user.acc),
            nums_change=compare_dict.get("acc"),
            isacc=True,
            image_draw=info_draw,
        )
        # 1.1 Draw PP(Infopanel.Stats)
        await __draw_stats(
            xy_origin=infopanel_pp_rightup,
            xy_change=infopanel_pp_addon_leftup,
            text_origin="{:,}".format(user.pp),
            nums_change=compare_dict.get("pp"),
            image_draw=info_draw,
        )
        # 1.2 Draw Playcount
        await __draw_stats(
            xy_origin=infopanel_playcount_rightup,
            xy_change=infopanel_playcount_addon_leftup,
            text_origin="{:,}".format(user.play_count),
            nums_change=compare_dict.get("play_count"),
            image_draw=info_draw,
        )
        # 1.3 Draw Totalhits
        await __draw_stats(
            xy_origin=infopanel_total_hits_rightup,
            xy_change=infopanel_total_hits_addon_leftup,
            text_origin="{:,}".format(user.total_hits),
            nums_change=compare_dict.get("total_hits"),
            image_draw=info_draw,
        )
        # 1.4 Draw RankedScore
        await __draw_stats(
            xy_origin=infopanel_ranked_score_rightup,
            xy_change=infopanel_ranked_score_addon_leftup,
            text_origin="{:,}".format(user.score_ranked),
            nums_change=compare_dict.get("score_ranked"),
            image_draw=info_draw,
        )
        # 1.5 Draw TotalScore
        await __draw_stats(
            xy_origin=infopanel_total_score_rightup,
            xy_change=infopanel_total_score_addon_leftup,
            text_origin="{:,}".format(user.score_all),
            nums_change=compare_dict.get("score_all"),
            image_draw=info_draw,
        )
        # 1.6 Draw WorldRanking
        await __draw_stats(
            xy_origin=infopanel_world_ranking_rightup,
            xy_change=infopanel_world_ranking_addon_leftup,
            text_origin="#{:,}".format(user.ranking_global),
            nums_change=compare_dict.get("ranking_global"),
            image_draw=info_draw,
            isrank=True,
        )
        # 1.7 Draw LocalRanking
        await __draw_stats(
            xy_origin=infopanel_local_ranking_rightup,
            xy_change=infopanel_local_ranking_addon_leftup,
            text_origin="#{:,}".format(user.ranking_country),
            nums_change=compare_dict.get("ranking_country"),
            image_draw=info_draw,
            isrank=True,
        )
        return info_img_x

    async def __info_score_drawing(
        score_img_dict: "dict[int,Image.Image]",
        info_image: Image.Image,
        type_score: int,
    ) -> Image.Image:
        """
        type:
        0: recent score
        1: best score
        """
        xy_center: "tuple[int,int]" = infopanel_score_center[type_score]
        xy_leftup: "tuple[int,int]" = infopanel_score_leftup[type_score]
        xy_using_list = list(xy_leftup)
        count = 0
        info_draw = ImageDraw.Draw(info_image)
        if score_img_dict == None:
            info_draw.text(
                xy_center, text="No Data Available...", font=font_sarasa_40, anchor="mm"
            )
        else:
            for images_key in score_img_dict:
                image_score = score_img_dict.get(images_key)
                count += 1
                if count > 9:
                    break
                elif count % 3 == 1 and count != 1:
                    xy_using_list[0] += image_score.size[0] + 7
                    xy_using_list[1] -= 3 * image_score.size[1]
                    xy_using_list[1] -= 15
                    info_image.paste(image_score, box=tuple(xy_using_list))
                    xy_using_list[1] += image_score.size[1]
                    xy_using_list[1] += 5
                else:
                    info_image.paste(image_score, box=tuple(xy_using_list))
                    xy_using_list[1] += image_score.size[1]
                    xy_using_list[1] += 5
        return info_image

    async def __pp_plus_drawing(pp_plus: dict):
        pass

    async def __play_count_info_drawing(
        play_count: dict,
        grade: dict,
        grade_diff: dict,
        max_combo: int,
        join_date: str,
        info_image: Image.Image,
        level: int,
        level_progress: int,
        play_time: int,
    ) -> Image.Image:
        info_draw = ImageDraw.Draw(info_image)
        # 0 Draw MaxCombo
        info_draw.text(
            playcountpanel_max_combo_leftup,
            text="{:,}".format(max_combo),
            font=font_agency_32,
            fill=playcountpanel_rgb,
            anchor="lt",
        )
        # 1 Draw Grade Counts
        for grad in grade:
            xy = playcountpanel_grade_center_dict.get(grad)
            xy_diff = list(xy)
            xy_diff[1] = xy_diff[1] + 28

            await __draw_stats(
                xy_origin=xy,
                xy_change=tuple(xy_diff),
                origin_anchor="mm",
                change_anchor="mm",
                image_draw=info_draw,
                text_origin=str(grade.get(grad)),
                nums_change=grade_diff.get(grad),
                font=font_agency_28,
            )
            # info_image.show()

        # 2 Draw join Date
        time_str = join_date
        timel = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S+00:00")
        timel_8 = timel + timedelta(hours=8)
        time_str_conv = datetime.strftime(timel_8, format="%Y-%m-%d %H:%M:%S")
        info_draw.text(
            xy=playcountpanel_joined_at_leftup,
            anchor="lt",
            text=time_str_conv,
            font=font_agency_32,
            fill=playcountpanel_rgb,
        )
        # 3 Draw monthly play
        monthly_num_count = 0
        xy_list = list(playcountpanel_monthly_playcount_rightup)
        for monthly_count in reversed(play_count):
            monthly_num_count += 1
            if monthly_num_count > 9:
                break
            else:
                play_count_time_string = monthly_count.get("start_date")[
                    : len(monthly_count.get("start_date")) - 3
                ]
                play_count_string = str(monthly_count.get("count"))
                end_string = play_count_time_string + ":  " + play_count_string
                info_draw.text(
                    xy=tuple(xy_list),
                    text=end_string,
                    fill=playcountpanel_rgb,
                    anchor="rt",
                    font=font_agency_32,
                )
                xy_list[1] += 32

        # 4 Draw Level
        info_draw.text(
            xy=playcountpanel_level_leftup,
            anchor="lt",
            text=str(level) + "[" + str(level_progress) + "%]",
            fill=playcountpanel_rgb,
            font=font_agency_32,
        )
        # 5 Draw play time
        playtime_str = "{}D {}h{}m{}s".format(
            (play_time // (3600 * 24)),
            (play_time // 3600) % 24,
            (play_time // 60) % 60,
            play_time % 60,
        )
        info_draw.text(
            playcountpanel_play_time_leftup,
            text=playtime_str,
            fill=playcountpanel_rgb,
            anchor="lt",
            font=font_agency_32,
        )
        # info_image.show()

        return info_image

    # main
    if compare_data == None:
        compare_data = {}
    info_img = template_info.copy()
    info_img = await __info_panel_drawing(
        user=user, compare_dict=compare_data, mode=mode, info_img=info_img
    )
    info_img = await __info_score_drawing(
        (await __score_mini_drawing(bp_score)), info_image=info_img, type_score=1
    )
    info_img = await __info_score_drawing(
        (await __score_mini_drawing(recent_score)), info_image=info_img, type_score=0
    )
    info_img = await __play_count_info_drawing(
        play_count=user.monthly_playcounts,
        grade=user.grade,
        max_combo=user.max_combo,
        level=user.level,
        level_progress=user.level_progress,
        join_date=user.join_date,
        info_image=info_img,
        play_time=user.play_time,
        grade_diff=compare_data.get("grade"),
    )
    info_save = BytesIO()
    info_img.save(info_save, format="PNG")
    return info_save


# Constant for drawing score
bigscorepanel_infoX_leftup = 398, 25
bigscorepanel_infoX_rgb = infopanel_other_rgb
bigscorepanel_score_rightup = 1887, 235
bigscorepanel_combo_rightup = 1887, 429
bigscorepanel_combo_rgb = (255, 255, 255)
bigscorepanel_score_rgb = (255, 255, 255)
bigscorepanel_pp_rightup = 1887, 345
bigscorepanel_pp_rgb = (255, 255, 255)
bigscorepanel_rank_leftup = 1632, 800
bigscorepanel_stat_leftup = 42, 240
bigscorepanel_stat_rgb = (255, 255, 255)
bigscorepanel_stroke_rgb = {
    "300": (101, 181, 217),
    "geki": (101, 181, 217),
    "100": (76, 177, 52),
    "katu": (76, 177, 52),
    "50": (181, 179, 50),
    "miss": (236, 24, 109),
}
bigscorepanel_stroke_mania_rgb = {
    "300": (215, 157, 31),
    "geki": (155, 74, 152),
    "100": (27, 110, 147),
    "katu": (76, 177, 52),
    "50": (136, 136, 136),
    "miss": (236, 24, 109),
}
bigscorepanel_stat_osu_size = 184, 102
bigscorepanel_stat_mania_size = 299, 111
bigscorepanel_stat_taiko_size = 150, 150
bigscorepanel_fruit_size = 184, 102
bigscorepanel_mods_rightup = 1887, 485
bigscorepanel_mods_size = 140, 140


async def draw_score(
    user: User,
    score: Score,
) -> BytesIO:
    template_score_big = Image.open(BOT_SCORE_BIG)

    async def __score_info_drawing(
        score: Score,
        user: User,
        score_img: Image.Image,
    ) -> Image.Image:
        # 0 Userpanel
        score_img_x = await __draw_userpanel_info(
            user=user, info_img=score_img, mode=score.mode_int
        )
        # 0.1
        async def __get_score_cover_big(score:Score) -> BytesIO:
            try_times = 2
            try:
                async def trying_get():
                    async with aiohttp.ClientSession() as session_get_score:
                        async with session_get_score.get(
                            url=score.beatmapset.covers.get("cover@2x")
                        ) as cover:
                            coverBuffer = BytesIO(initial_bytes=(await cover.read()))
                            return coverBuffer
                        
                cv = (await trying_get())
                return cv
            except:
                try_times -= 1
                if try_times > 0:
                    cv = (await trying_get())
                    return cv
                else:
                    return Image.new("RGBA",(1920,1080),(0,0,0,255)).save(cv,format="PNG")
        
        async def __circle_corner(img:Image.Image, radii:'int|float')->Image.Image:  #把原图片变成圆角，这个函数是从网上找的，原址 https://www.pyget.cn/p/185266
            """
            圆角处理
            :param img: 源图象。
            :param radii: 半径，如：30。
            :return: 返回一个圆角处理后的图象。
            """
        
            # 画圆（用于分离4个角）
            circle = Image.new('L', (radii * 2, radii * 2), 0)  # 创建一个黑色背景的画布
            draw = ImageDraw.Draw(circle)
            draw.ellipse((0, 0, radii * 2, radii * 2), fill=255)  # 画白色圆形
        
            # 原图
            img = img.convert("RGBA")
            w, h = img.size
       
            # 画4个角（将整圆分离为4个部分）
            alpha = Image.new('L', img.size, 255)
            alpha.paste(circle.crop((0, 0, radii, radii)), (0, 0))  # 左上角
            alpha.paste(circle.crop((radii, 0, radii * 2, radii)), (w - radii, 0))  # 右上角
            alpha.paste(circle.crop((radii, radii, radii * 2, radii * 2)), (w - radii, h - radii))  # 右下角
            alpha.paste(circle.crop((0, radii, radii, radii * 2)), (0, h - radii))  # 左下角
            # alpha.show()
            img.putalpha(alpha)  # 白色区域透明可见，黑色区域不可见
            return img
        
        # open score cover
        score_cover = Image.open((await __get_score_cover_big(score=score))).convert("RGBA")
        # resize to less
        score_cover = score_cover.resize((int(score_cover.size[0]/2),int(score_cover.size[1]/2)))
        # gaussian blur
        score_cover = score_cover.filter(ImageFilter.GaussianBlur(radius = 4.5))
        # bright enhancement(decrease)
        score_cover_enh = ImageEnhance.Brightness(score_cover)
        score_cover_enh.enhance(0.55)
        # round corner
        score_cover = (await __circle_corner(score_cover,15))
        score_cover_draw = ImageDraw.Draw(score_cover)
        # adj weight for more
        text_artist = (await __adj_weight(text=score.beatmapset.artist_unicode,weight_limit=int((score_cover.size[0]-5)),font=font_sarasa_40))
        text_title = (await __adj_weight(text=score.beatmapset.title_unicode,weight_limit=int((score_cover.size[0]-5)),font=font_sarasa_40))
        # draw
        score_cover_draw.text(
            (int(score_cover.size[0]/2),int((score_cover.size[1]/5)*2)),text=text_artist,fill=(255,255,255),anchor='mm',font=font_sarasa_40,stroke_fill=(0,0,0),stroke_width=2
        )
        score_cover_draw.text(
            (int(score_cover.size[0]/2),int((score_cover.size[1]/5)*3)),text=text_title,fill=(255,255,255),anchor='mm',font=font_sarasa_40,stroke_fill=(0,0,0),stroke_width=2
        )
        # combine
        score_img_x.alpha_composite(score_cover,dest=(460,520))
        # 1 Infopanel
        score_draw = ImageDraw.Draw(score_img_x)
        timel = datetime.strptime(score.created_at, "%Y-%m-%dT%H:%M:%S+00:00")
        timel_8 = timel + timedelta(hours=8)
        time_str_conv = datetime.strftime(timel_8, format="%Y-%m-%d %H:%M:%S")
        score_info_artist = score.beatmapset.artist
        score_info_title = score.beatmapset.title
        score_info_version = score.beatmap.version
        h, score_info_artist_weight = font_agency_28.getsize(score_info_artist)
        h, score_info_title_weight = font_agency_28.getsize(score_info_title)
        h, score_info_version_weight = font_agency_28.getsize(
            "[" + score_info_version + "]"
        )
        h, score_info_co_weight = font_agency_28.getsize(" - ")
        # TODO
        def adj_score_title(
            wa: int,
            wt: int,
            wv: int,
            wc: int,
            t: str,
            a: str,
            v: str,
            font: ImageFont.FreeTypeFont,
            wlo: int = 1151,
            wvo: int = 300,
            wao: int = 300,
            wto: int = 550,
        ) -> "tuple[str,str,str]":
            # wa: max 300
            # wt: max 500
            # wv: max 300
            if wa + wt + wv + wc > wlo:
                if wt > wto:
                    t = __adj_weight(t, wto, font)
                    h, wt = font.getsize(t)
                    adj_score_title(wa, wt, wv, wc, t, a, v, font, wlo, wvo, wao, wto)
                elif wa > wao:
                    a = __adj_weight(a, wao, font)
                    h, wa = font.getsize(a)
                    adj_score_title(wa, wt, wv, wc, t, a, v, font, wlo, wvo, wao, wto)
                elif wv > wvo:
                    v = __adj_weight(v, wvo, font)
                    h, wv = font, getsize("[" + v + "]")
                    adj_score_title(wa, wt, wv, wc, t, a, v, font, wlo, wvo, wao, wto)
            return a, t, v

        a, t, v = adj_score_title(
            score_info_artist_weight,
            score_info_title_weight,
            score_info_version_weight,
            score_info_co_weight,
            score_info_title,
            score_info_artist,
            score_info_version,
            font_agency_28,
        )
        score_info_text = "Played by {} at {}.\n {} - {}[{}]\n CS: {:.2f} AR: {:.2f} HP: {:.2f} OD: {:.2f}     {:.2f}*".format(
            user.name,
            time_str_conv,
            a,
            t,
            v,
            score.beatmap.cs,
            score.beatmap.ar,
            score.beatmap.drain,
            score.beatmap.accuracy,
            score.beatmap.difficulty_rating,
        )

        score_draw.text(
            # anchor="lt",
            align="left",
            text=score_info_text,
            fill=bigscorepanel_infoX_rgb,
            xy=bigscorepanel_infoX_leftup,
            font=font_agency_32,
        )
        # 2 Score main
        # 2.1 Score
        score_draw.text(
            xy=bigscorepanel_score_rightup,
            anchor="rt",
            font=font_cataneo_85,
            text="{:,}".format(score.score),
            fill=bigscorepanel_score_rgb,
        )
        # 2.2 Ranking
        ranking_picture = Image.open(
            BOT_SCORE_SKIN_DIR + "/ranking-{}@2x.png".format(score.rank)
        ).convert(mode="RGBA")
        ranking_picture = ranking_picture.resize((256, 256))
        score_img_x.alpha_composite(ranking_picture, dest=bigscorepanel_rank_leftup)
        # 2.3 Stat

        if score.mode == "osu":
            # For std:
            stat_list = ["300", "geki", "100", "katu", "50", "miss"]
            list_ranking_xy = list(bigscorepanel_stat_leftup)
            for r in stat_list:
                rank_img = Image.open(
                    BOT_SCORE_SKIN_DIR + "/hit{}@2x.png".format(r)
                ).convert("RGBA")
                rank_img = rank_img.resize(bigscorepanel_stat_osu_size)
                stat_text = "{:,}".format(score.statistics.get("count_" + r))
                score_img_x.alpha_composite(rank_img, tuple(list_ranking_xy))
                list_ranking_xy[0] += rank_img.size[0] + 10
                list_ranking_xy_en = list_ranking_xy[0],list_ranking_xy[1]+15
                score_draw.text(
                    tuple(list_ranking_xy_en),
                    text=stat_text,
                    fill=bigscorepanel_stat_rgb,
                    font=font_cataneo_48,
                    stroke_fill=bigscorepanel_stroke_rgb.get(r),
                    stroke_width=5,
                    anchor="la",
                )
                list_ranking_xy[0] -= rank_img.size[0] + 10
                list_ranking_xy[1] += rank_img.size[1] + 20
                if list_ranking_xy[1] > 1005:
                    list_ranking_xy[1] = bigscorepanel_stat_leftup[1]
                    list_ranking_xy[0] += 600

        elif score.mode == "fruits":
            # For ctb:
            stat_list = ["300","geki","100", "katu", "50", "miss"]
            list_ranking_xy = list(bigscorepanel_stat_leftup)
            for r in stat_list:
                rank_img = Image.open(
                    BOT_SCORE_SKIN_DIR + "/hit{}@2x.png".format(r)
                ).convert("RGBA")
                
                rank_img = rank_img.resize(bigscorepanel_stat_osu_size)
                stat_text = "{:,}".format(score.statistics.get("count_" + r))
                score_img_x.alpha_composite(rank_img, tuple(list_ranking_xy))
                list_ranking_xy[0] += rank_img.size[0] + 10
                list_ranking_xy_en = list_ranking_xy[0],list_ranking_xy[1]+15
                score_draw.text(
                    tuple(list_ranking_xy_en),
                    text=stat_text,
                    fill=bigscorepanel_stat_rgb,
                    font=font_cataneo_48,
                    stroke_fill=bigscorepanel_stroke_rgb.get(r),
                    stroke_width=5,
                    anchor="la",
                )
                list_ranking_xy[0] -= rank_img.size[0] + 10
                list_ranking_xy[1] += rank_img.size[1] + 20
                if list_ranking_xy[1] > 1005:
                    list_ranking_xy[1] = bigscorepanel_stat_leftup[1]
                    list_ranking_xy[0] += 600

        elif score.mode == "taiko":
            # For taiko:
            stat_list = ["300", "geki", "100", "katu", "50", "miss"]
            list_ranking_xy = list(bigscorepanel_stat_leftup)
            for r in stat_list:
                rank_img = Image.open(
                    BOT_SCORE_SKIN_DIR + "/taiko-hit{}@2x.png".format(r)
                ).convert("RGBA")
                rank_img = rank_img.resize(bigscorepanel_stat_taiko_size)
                stat_text = "{:,}".format(score.statistics.get('count_'+r))
                score_img_x.alpha_composite(rank_img, tuple(list_ranking_xy))
                list_ranking_xy[0] += rank_img.size[0] + 10
                list_ranking_xy_en = list_ranking_xy[0],list_ranking_xy[1]+15
                score_draw.text(
                    tuple(list_ranking_xy_en),
                    text=stat_text,
                    fill=bigscorepanel_stat_rgb,
                    font=font_cataneo_48,
                    stroke_fill=bigscorepanel_stroke_rgb.get(r),
                    stroke_width=5,
                    anchor="la",
                )
                list_ranking_xy[0] -= rank_img.size[0] + 10
                list_ranking_xy[1] += rank_img.size[1] + 20
                if list_ranking_xy[1] > 1005:
                    list_ranking_xy[1] = bigscorepanel_stat_leftup[1]
                    list_ranking_xy[0] += 600

        elif score.mode == "mania":
            # For mania:
            stat_list = ["geki","300", "katu","100","50", "miss"]
            list_ranking_xy = list(bigscorepanel_stat_leftup)
            for r in stat_list:
                rank_img = Image.open(
                    BOT_SCORE_SKIN_DIR + "/mania-hit{}@2x.png".format(r)
                ).convert("RGBA")
                rank_img = rank_img.resize(bigscorepanel_stat_mania_size)
                stat_text = "{:,}".format(score.statistics.get("count_"+r))
                score_img_x.alpha_composite(rank_img, tuple(list_ranking_xy))
                list_ranking_xy[0] += rank_img.size[0] + 10
                list_ranking_xy_en = list_ranking_xy[0],list_ranking_xy[1]+15
                score_draw.text(
                    tuple(list_ranking_xy_en),
                    text=stat_text,
                    fill=bigscorepanel_stat_rgb,
                    font=font_cataneo_48,
                    stroke_fill=bigscorepanel_stroke_mania_rgb.get(r),
                    stroke_width=5,
                    anchor="la",
                )
                list_ranking_xy[0] -= rank_img.size[0] + 10
                list_ranking_xy[1] += rank_img.size[1] + 20
                if list_ranking_xy[1] > 1005:
                    list_ranking_xy[1] = bigscorepanel_stat_leftup[1]
                    list_ranking_xy[0] += 600
        # 2.4 Combo and ACC
        combo_text = "{:.3f}%   {:,}×".format((score.accuracy*100),score.max_combo)
        score_draw.text(
            xy=bigscorepanel_combo_rightup,
            fill=bigscorepanel_combo_rgb,
            text=combo_text,
            anchor="rt",
            font=font_cataneo_53,
        )
        # 2.5 PP
        if score.pp == None:
            score.pp = 0
        score_draw.text(
            text="PP: {:,.3f}".format(score.pp),
            xy=bigscorepanel_pp_rightup,
            anchor="rt",
            fill=bigscorepanel_pp_rgb,
            font=font_cataneo_53,
        )
        # 2.6 Mods
        mods_dict = {
            "EZ": "easy",
            "HD": "hidden",
            "HR": "hardrock",
            "FI": "fadein",
            "FL": "flashlight",
            "HT": "halftime",
            "1K": "key1",
            "2K": "key2",
            "3K": "key3",
            "4K": "key4",
            "5K": "key5",
            "6K": "key6",
            "7K": "key7",
            "8K": "key8",
            "9K": "key9",
            "CO": "keycoop",
            "MR": "mirror",
            "NC": "nightcore",
            "NF": "nofail",
            "PF": "perfect",
            "RD": "random",
            "RX": "relax",
            "AP": "relax2",
            "V2": "scorev2",
            "SO": "spunout",
            "SD": "suddendeath",
            "TP": "target",
            "TD": "touchdevice",
            "DT": "doubletime",
        }
        mods = reversed(score.mods)
        mod_xy = list(bigscorepanel_mods_rightup)
        if mods != {}:
            for mod in mods:
                mod_img = Image.open(
                    BOT_SCORE_SKIN_DIR
                    + "/selection-mod-{}@2x.png".format(mods_dict.get(mod))
                ).convert("RGBA")
                mod_img = mod_img.resize(size=bigscorepanel_mods_size)
                mod_xy_leftup = (mod_xy[0] - mod_img.size[0], mod_xy[1])
                score_img_x.alpha_composite(mod_img, tuple(mod_xy_leftup))
                mod_xy[0] -= mod_img.size[0] + 5
                if mod_xy[0] < 1400:
                    mod_xy[0] = bigscorepanel_mods_rightup[0]
                    mod_xy[1] += mod_img.szie[1] + 10

        return score_img_x

    # main

    score_img = template_score_big.copy()
    score_img = await __score_info_drawing(score=score, user=user, score_img=score_img)
    score_img_save = BytesIO()
    score_img.save(score_img_save, format="PNG")
    return score_img_save

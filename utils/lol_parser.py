from time import sleep
from loguru import logger
from utils.request_harvester import request_harvester
from bs4 import BeautifulSoup


def get_all_perso_from_lol():
    try:
        all_perso_page = request_harvester(
            "get",
            "https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control": "max-age=0",
                "priority": "u=0, i",
                "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "cross-site",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            },
        )
        if all_perso_page is not None:
            html = BeautifulSoup(all_perso_page["response"].text, "html.parser")
            champion_spans = html.find_all("span", class_="grid-icon champion-icon")
            champions = [span.get("data-champion") for span in champion_spans]
            perso_dict = []
            for champion_name in champions:
                perso_dict.append(find_lol_perso_by_name(champion_name))

            return perso_dict
    except Exception as e:
        logger.error(e)


def find_lol_perso_by_name(name: str):
    try:
        perso_page = request_harvester(
            "get",
            "https://leagueoflegends.fandom.com/api.php",
            headers={
                "accept": "application/json, text/javascript, */*; q=0.01",
                "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
                "priority": "u=1, i",
                "referer": "https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki",
                "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
                "x-requested-with": "XMLHttpRequest",
            },
            params={
                "format": "json",
                "action": "parse",
                "disablelimitreport": "true",
                "prop": "text",
                "title": "League_of_Legends_Wiki",
                "maxage": "600",
                "smaxage": "600",
                "text": "{{Tooltip/Champion|champion="
                + name
                + "|skin=|variant=|game=lol}}",
            },
        )
        if perso_page is not None:
            html = BeautifulSoup(
                perso_page["response"].json()["parse"]["text"]["*"], "html.parser"
            )
            champion_name = html.find(
                "td",
                class_="tooltip-header",
                style="height:20px;line-height:20px;padding:0 5px 0 0;text-align:left;font-size:20px;font-weight:bold;",
            ).text.strip()
            abilities = [
                div["data-ability"]
                for div in html.find_all("div", class_="grid-image ability-icon")
            ]
            stats_keys = [
                "Health",
                "Health Regen.",
                "Manaless",
                "Range",
                "Attack Damage",
                "Attack Speed",
                "Armor",
                "Magic Res.",
                "Move. Speed",
            ]

            stats_table = {}

            for key in stats_keys:
                stat_label = html.find("td", string=lambda text: text and key in text)
                if stat_label:
                    stat_value = stat_label.find_next("td")
                    if stat_value:
                        stats_table[key] = "".join(stat_value.stripped_strings)
                    else:
                        stats_table[key] = None
                else:
                    stats_table[key] = None

            return {
                "name": champion_name,
                "abilities": ",".join(abilities),
                "stats": stats_table,
                "image": html.find("img", {"class": "thumbborder"})["src"],
            }

    except Exception as e:
        logger.error(e)

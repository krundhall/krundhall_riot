import requests
import urllib.parse

api_key = "RGAPI-6f9070f0-18b2-4559-8b82-b417ec4072ac"


def get_puuid(riot_id: str) -> str:
    ### split into gameName and tagLine, then encode
    game_name, tag_line = riot_id.split("#")
    game_name = urllib.parse.quote(game_name)
    tag_line = urllib.parse.quote(tag_line)
    ### build url
    url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    ### request
    request_puuid = requests.get(url, headers={"X-Riot-Token": api_key})
    data = request_puuid.json()
    return data["puuid"]

def get_summonerid(puuid: str) -> str:
    url = f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}"
    request_summonerid = requests.get(url, headers={"X-Riot-Token": api_key})
    data = request_summonerid.json()
    return data["id"]

def get_rankedStats(puuid: str) -> dict:
    url = f"https://euw1.api.riotgames.com/lol/league/v4/entries/by-puuid/{puuid}"
    request_rankedStats = requests.get(url, headers={"X-Riot-Token": api_key})
    data = request_rankedStats.json()
    for i in data:
        if i["queueType"] == "RANKED_SOLO_5x5":
            return i
    return None

def winrate(solo_list: dict) -> float:
    wi = solo_list["wins"]
    lo = solo_list["losses"]
    wr = wi / (wi+lo) * 100 
    print(f"Winrate: {wr:.2f}%")
    return wr

def rank_status(puuid: str) -> str:
    url = f"https://euw1.api.riotgames.com/lol/league/v4/entries/by-puuid/{puuid}"
    requests_rankedStats = requests.get(url, headers={"X-Riot-Token": api_key})
    data = requests_rankedStats.json()
    
    for i in data:
        if i["queueType"] == "RANKED_SOLO_5x5":
            tier = i["tier"]
            rank = i["rank"]
            lp = i["leaguePoints"]
            return f"{tier} {rank} {lp} LP"
    return "Play some SoloQ shitter"
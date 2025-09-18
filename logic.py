import requests
import urllib.parse

api_key = "RGAPI-065fb448-0a61-4018-9539-037ecf04ca7c"

def get_puuid(riot_id: str) -> str:
    ### split into gameName and tagLine
    game_name, tag_line = riot_id.split("#")

    ### encode, urllib
    game_name = urllib.parse.quote(game_name)
    tag_line = urllib.parse.quote(tag_line)

    ### build url
    url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    
    ### get and index for ppuid
    request_puuid = requests.get(url, headers={"X-Riot-Token": api_key})
    data = request_puuid.json()
    puuid = data["puuid"]
    return puuid
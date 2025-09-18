from logic import get_puuid


print("Hi and welcome to Riot ID Fetcher")
riot_id = input("Enter name:\nex. 'Kevin Egg#EUW'\n>>> ")
puuid = get_puuid(riot_id)
from logic import get_puuid, get_rankedStats, winrate, rank_status

stop = False
while not stop:
    print("Hi : ^)\nWelcome to RAKOE\nWhat can I do you for?")
    print("1) Winrate")
    print("2) Rank")
    print("q) Quit")

    menu_choice = input(">>> ")

    if menu_choice == "q":
        print("Bye, bye - welcome back!")
        stop = True
    
    elif menu_choice == "1":
        riot_id = input("Enter name:\nex. 'Kevin Egg#EUW'\n>>> ")
        puuid = get_puuid(riot_id)
        solo_stats = get_rankedStats(puuid)
        if solo_stats:
            winrate(solo_stats)

    elif menu_choice == "2":
        riot_id = input("Enter name:\nex. 'Kevin Egg#EUW'\n>>> ")
        puuid = get_puuid(riot_id)
        print(rank_status(puuid))

    else:
        print("Not a valid menu choice\nTry again!")
    
    if not stop:
        input("\nPress Enter to continue...")
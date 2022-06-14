
LOGGING = True

team: list[dict] = [
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "John", "age": 20, "number": 1},
    {"name": "Cavin", "age": 17, "number": 12},
]


def repr_players(players: list[dict], par_sort=False, key_sort="number"):

    if par_sort:
        players.sort(key=lambda x: x[key_sort])

    print("TEAM:")
    for pla in players:
        print(f"\t{pla['number']} " f"Name: {pla['name']}, Age: {pla['age']}")
    print("\n")


def log(message: str):
    print(f"-> -> -> {message} <- <- <- ***")


def add_player(players):

    player_Num = input_number(True)

    if player_Num == 0:
        return

    while True:
        player_Nane = input("Enter the player names\n").replace("\n", "")

        if len(player_Nane) == 0:
            UserAnser = input(
                "The player names was entered incorrectly, try againe? (y/n): "
            )
            if UserAnser == "n":
                return
        else:
            break

    while True:

        player_AgeSt = input("Enter the age player\n").replace("\n", "")

        try:
            player_Age = int(player_AgeSt)
        except ValueError:
            player_Age = 0

        if player_Age == 0:

            UserAnser = input("Age entered incorrectly, try againe?(y/n): ")
            if UserAnser == "n":
                return
            else:
                continue
        else:
            break

    player = {"name": player_Nane, "number": player_Num, "age": player_Age}
    players.append(player)
    log(message=f"Adding {player['name']}")


def remove_player(players: list[dict]):

    player_Num = input_number(False)

    if player_Num == 0:
        return

    for index, player in enumerate(players):
        if player["number"] == player_Num:
            player_name = player["name"]
            del players[index]
            log(message=f"Deleting {player_name}")


def search_by_number(player_Num: int, player_NumSt: str):
    for index, player in enumerate(team):
        if player["number"] == player_Num:

            return input(
                "Our team already has a player with a number "
                + player_NumSt
                + ", try againe? (y/n): \n"
            )

    return "ok"


def input_number(sear_N: bool):

    while True:

        player_NumSt = input("Enter the player number\n").replace("\n", "")

        try:
            player_Num = int(player_NumSt)

        except ValueError:
            UserAnser = input("Bad player number, try againe? (y/n): ")
            if UserAnser == "n":
                return 0

        if sear_N:
            res_s = search_by_number(player_Num, player_NumSt)

            if res_s == "ok":
                break
            elif res_s == "n":
                return 0

        else:
            break

    return player_Num


def change_player_number(players):

    log("information about the old player number")
    player_Num_Old = input_number(False)

    if player_Num_Old == 0:
        return

    log("information about the new player number")
    player_Num_New = input_number(False)

    if player_Num_New == 0:
        return
    elif player_Num_New == player_Num_Old:
        log("old number = new number")
        return

    for index, player in enumerate(players):
        if player["number"] == player_Num_Old:
            player["number"] = player_Num_New
            player_name = player["name"]
            log(message=f"Player {player_name} change numger ")


def sortet_team(players):

    Var_sort = input(
        "How to sort list (anser: 1, 2, 3)?\n\t1.Number\n\t2.Name\n\t3.Age\n"
    )

    if Var_sort == "2":
        key_sort = "name"
    elif Var_sort == "3":
        key_sort = "age"
    else:
        key_sort = "number"

    repr_players(players=team, par_sort=True, key_sort=key_sort)


def main():

    repr_players(team)
    main_qutions = "Option team list (anser: 1,2,3,4)?\n\t"
    first_option = "1. Add new player\n\t"
    sec_option = "2. Delete player\n\t"
    tree_option = "3. Change player number \n\t"
    four_option = "4. Sorted team list\n"
    Var_Act = input(
        main_qutions+first_option+sec_option+tree_option+four_option
    )

    if Var_Act == "1":
        add_player(players=team)
    elif Var_Act == "2":
        remove_player(players=team)
    elif Var_Act == "3":
        change_player_number(players=team)
    elif Var_Act == "4":
        sortet_team(team)
        return
    else:
        log("bad choice, no option")

    # add_player(num=17, name="Cris", age=31)
    # add_player(num=17, name="Bob", age=39)1
    #

    repr_players(team)


if __name__ == "__main__":
    main()
else:
    raise SystemExit("This module in only for running")

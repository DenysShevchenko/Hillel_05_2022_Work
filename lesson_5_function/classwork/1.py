# from pprint import pprint as print

LOGGING = True

team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 17, "number": 12},
]


def repr_players(players: list[dict]) -> None:
    print("TEAM:")
    for player in players:
        print(f"\t{player['number']} " f"Name: {player['name']}, Age: {player['age']}")
    print("\n")


def log(message: str) -> None:
    print(f"-> -> -> {message} <- <- <- ***")


def add_player(num: int, name: str, age: int) -> None:
    player = {"name": name, "number": num, "age": age}
    team.append(player)
    log(message=f"Adding {player['name']}")


def remove_player(players: list[dict], num: int) -> None:
    for index, player in enumerate(players):
        if player["number"] == num:
            player_name = player["name"]
            del players[index]
            log(message=f"Deleting {player_name}")


def main():
    repr_players(team)

    add_player(num=17, name="Cris", age=31)
    add_player(num=17, name="Bob", age=39)
    remove_player(players=team, num=17)

    repr_players(team)


if __name__ == "__main__":
    main()
else:
    raise SystemExit("This module in only for running")

from pprint import pprint

team = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 17, "number": 12},
]


# def only_18_plus(player: dict) -> bool:
#     return player["age"] > 18


results = filter(lambda x: x["age"] > 18, team)

# pprint([player for player in team if player["age"] > 18])
# pprint(list(results))
# pprint(sorted(team, key=lambda x: x["age"], reverse=True))
team.sort(key=lambda x: x["age"])
pprint(team)

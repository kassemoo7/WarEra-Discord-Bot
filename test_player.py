from warera_api import get_player

user_id = "69df61ad6e69016f87379e5e"

player = get_player(user_id)

print(player["username"])
print(player["leveling"]["level"])
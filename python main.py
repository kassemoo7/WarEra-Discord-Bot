from warera_api import search_player, get_player

player_ids = search_player("don")

print("IDs:")
print(player_ids)

print("\nFirst Player:")
player = get_player(player_ids[0])
print(player)
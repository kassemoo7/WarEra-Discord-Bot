from warera_api import search_player

player = input("Player name: ")

user_id = search_player(player)

if user_id:
    print(f"\nUser ID: {user_id}")
else:
    print("\nPlayer not found.")
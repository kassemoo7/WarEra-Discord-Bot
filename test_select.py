from warera_api import search_player, get_player

player_name = input("Player name: ")

user_ids = search_player(player_name)

if not user_ids:
    print("Player not found.")
    exit()

players = []

for user_id in user_ids:
    player = get_player(user_id)
    players.append(player)

print("\n=== Search Results ===\n")

for i, player in enumerate(players, start=1):
    print(
        f"{i}. {player['username']} "
        f"(Level {player['leveling']['level']})"
    )

choice = int(input("\nChoose player number: ")) - 1

selected = players[choice]

print("\n========================")
print("Selected Player")
print("========================")

print("Username :", selected["username"])
print("Level    :", selected["leveling"]["level"])
print("User ID  :", selected["_id"])

print("\nWar Skills")
print("----------------")

print("Attack            :", selected["skills"]["attack"]["value"])
print("Precision         :", selected["skills"]["precision"]["value"])
print("Critical Chance   :", selected["skills"]["criticalChance"]["value"])
print("Critical Damage   :", selected["skills"]["criticalDamages"]["value"])
print("Armor             :", selected["skills"]["armor"]["value"])
print("Health            :", selected["skills"]["health"]["value"])

print("\nEco Skills")
print("----------------")

print("Energy            :", selected["skills"]["energy"]["value"])
print("Production        :", selected["skills"]["production"]["value"])
print("Entrepreneurship  :", selected["skills"]["entrepreneurship"]["value"])
print("Companies         :", selected["skills"]["companies"]["value"])
print("Management        :", selected["skills"]["management"]["value"])

print("\nAvailable Points :", selected["leveling"]["availableSkillPoints"])
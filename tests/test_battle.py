from warera_api import get_active_battles, get_battle_data
from pprint import pprint

battle_id = get_active_battles()[0]

print("Battle:", battle_id)
print()

data = get_battle_data(battle_id)

pprint(data, width=180)
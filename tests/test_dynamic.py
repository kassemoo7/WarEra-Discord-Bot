from warera_api import get_map_data
from pprint import pprint

data = get_map_data()

print(type(data["dynamicData"]))
print()

pprint(data["dynamicData"], width=150)
from pprint import pprint
from warera_api import get_map_data

data = get_map_data()

from pprint import pprint

print(type(data["dynamicData"]))
print(data["dynamicData"].keys())

pprint(data["dynamicData"], width=180)
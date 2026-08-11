from pprint import pprint
from warera_api import get_battle_info

data = get_battle_info("6a758c2863cc1fac315ccc10")

pprint(data, width=180)
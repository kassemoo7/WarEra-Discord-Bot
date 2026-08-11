from pprint import pprint
from warera_api import get_active_battles

battles = get_active_battles()

pprint(battles)
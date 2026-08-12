import requests
import os
from dotenv import load_dotenv

load_dotenv()

jwt = os.getenv("JWT")

if not jwt:
    raise ValueError("JWT not found in .env")

URL_ACTIVE = "https://api3.warera.io/trpc/battle.getSortedActiveBattles?batch=1"
URL_BATTLE = "https://api3.warera.io/trpc/battle.getLiveBattleData?batch=1"
URL_MAP = "https://api3.warera.io/trpc/map.getMapData?batch=1"

headers = {
    "accept": "*/*",
    "content-type": "application/json",
    "origin": "https://app.warera.io",
    "referer": "https://app.warera.io/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "x-gr": "ANGLE (NVIDIA, NVIDIA GeForce RTX 4050 Laptop GPU (0x000028E1) Direct3D11 vs_5_0 ps_5_0, D3D11)",
    "x-vid": "3327229d19910b26dc4c845b9b8a2276",
}

cookies = {
    "jwt": jwt
}


def get_active_battles():
    payload = {
        "0": {
            "filter": "all"
        }
    }

    response = requests.post(
        URL_ACTIVE,
        headers=headers,
        cookies=cookies,
        json=payload
    )

    response.raise_for_status()

    data = response.json()

    return data[0]["result"]["data"]


def get_battle_data(battle_id):
    payload = [
        {
            "battleId": battle_id
        }
    ]

    response = requests.post(
        URL_BATTLE,
        headers=headers,
        cookies=cookies,
        json=payload
    )

    response.raise_for_status()

    data = response.json()

    return data[0]["result"]["data"]


def get_countries():
    payload = {
        "0": None
    }

    response = requests.post(
        "https://api3.warera.io/trpc/user.getMe,country.getAllCountries,region.getRegionsObject?batch=1",
        headers=headers,
        cookies=cookies,
        json=payload
    )

    response.raise_for_status()

    data = response.json()

    countries = {}

    for country in data[1]["result"]["data"]:
        countries[country["_id"]] = {
            "name": country["name"],
            "code": country["code"] 
        }

    return countries


def get_map_data():
    payload = {
        "0": None
    }

    response = requests.post(
        URL_MAP,
        headers=headers,
        cookies=cookies,
        json=payload
    )

    response.raise_for_status()

    data = response.json()

    return data[0]["result"]["data"]


def get_battle_info(battle_id):
    response = requests.post(
        "https://api3.warera.io/trpc/battle.getById?batch=1",
        headers=headers,
        cookies=cookies,
        json=[{"battleId": battle_id}]
    )

    response.raise_for_status()

    return response.json()

URL_SEARCH = "https://api3.warera.io/trpc/search.searchAnything?batch=1"


def search_player(name):
    payload = {
        "0": {
            "searchText": name
        }
    }

    response = requests.post(
        URL_SEARCH,
        headers=headers,
        cookies=cookies,
        json=payload
    )

    response.raise_for_status()

    data = response.json()
    
    user_ids = data[0]["result"]["data"]["userIds"]

    if not user_ids:
        return []

    return user_ids

URL_PLAYER = "https://api3.warera.io/trpc/user.getUserLite?batch=1"


def get_player(user_id):
    payload = {
        "0": {
            "userId": user_id
        }
    }

    response = requests.post(
        URL_PLAYER,
        headers=headers,
        cookies=cookies,
        json=payload
    )

    response.raise_for_status()

    data = response.json()
    
    return data[0]["result"]["data"]

def get_players_lite(user_ids):
    payload = {}

    for i, user_id in enumerate(user_ids):
        payload[str(i)] = {
            "userId": user_id
        }

    

    response = requests.post(
        URL_PLAYER,
        headers=headers,
        cookies=cookies,
        json=payload
    )

    response.raise_for_status()

    data = response.json()

    players = []

    for item in data:
        if "result" in item:
            players.append(item["result"]["data"])

    return players

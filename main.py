import discord
from discord.ext import commands
from discord.ui import Select, View

from config import TOKEN
from warera_api import search_player, get_player, get_countries

intents = discord.Intents.default()
intents.message_content = True

RANKS = {
    1: "مبتدئ",
    2: "مبتدئ 1★",
    3: "مبتدئ 2★",
    4: "مبتدئ 3★",
    5: "متدرب",
    6: "متدرب 1★",
    7: "متدرب 2★",
    8: "متدرب 3★",
    9: "مجند",
    10: "مجند 1★",
    11: "مجند 2★",
    12: "مجند 3★",
    13: "طالب عسكري",
    14: "طالب عسكري 1★",
    15: "طالب عسكري 2★",
    16: "طالب عسكري 3★",
    17: "جندي",
    18: "جندي 1★",
    19: "جندي 2★",
    20: "جندي 3★",
    21: "جندي مشاة",
    22: "جندي مشاة 1★",
    23: "جندي مشاة 2★",
    24: "جندي مشاة 3★",

    25: "فني متخصص",
    26: "فني متخصص 1★",
    27: "فني متخصص 2★",
    28: "فني متخصص 3★",

    29: "عريف",
    30: "عريف 1★",
    31: "عريف 2★",
    32: "عريف 3★",

    33: "رقيب",
    34: "رقيب 1★",
    35: "رقيب 2★",
    36: "رقيب 3★",

    37: "طليعي",
    38: "طليعي 1★",
    39: "طليعي 2★",
    40: "طليعي 3★",

    41: "عميل",
    42: "عميل 1★",
    43: "عميل 2★",
    44: "عميل 3★",

    45: "ضابط صف",
    46: "ضابط صف 1★",
    47: "ضابط صف 2★",
    48: "ضابط صف 3★",

    49: "رئيس",
    50: "رئيس 1★",
    51: "رئيس 2★",
    52: "رئيس 3★",

    53: "ضابط أمر",
    54: "ضابط أمر 1★",
    55: "ضابط أمر 2★",
    56: "ضابط أمر 3★",

    57: "ملازم",
    58: "ملازم بحري 1★",
    59: "ملازم بحري 2★",
    60: "ملازم بحري 3★",

    61: "ملازم",
    62: "ملازم أول",
    63: "ملازم أول 2★",
    64: "ملازم أول 3★",

    65: "نقيب",
    66: "نقيب 1★",
    67: "نقيب 2★",
    68: "نقيب 3★",

    69: "رائد",
    70: "رائد 1★",
    71: "رائد 2★",
    72: "رائد 3★",

    73: "مقدم",
    74: "مقدم 1★",
    75: "مقدم 2★",
    76: "مقدم 3★",

    77: "عقيد",
    78: "عقيد 1★",
    79: "عقيد 2★",
    80: "عقيد 3★",

    81: "عميد",
    82: "عميد 1★",
    83: "عميد 2★",
    84: "عميد 3★",

    85: "مهيب بحري",
    86: "مهيب بحري 1★",
    87: "مهيب بحري 2★",
    88: "مهيب بحري 3★",

    89: "مشير",
    90: "مشير 1★",
    91: "مشير 2★",
    92: "مشير 3★",

    93: "لواء بحري",
    94: "لواء بحري 1★",
    95: "لواء بحري 2★",
    96: "لواء بحري 3★",

    97: "نائب أدميرال",
    98: "فريق بحري 1★",
    99: "فريق بحري 2★",
    100: "فريق بحري 3★",

    101: "أدميرال",
    102: "أدميرال 1★",
    103: "أدميرال 2★",
    104: "أدميرال 3★",

    105: "فريق",
    106: "فريق 1★",
    107: "فريق 2★",
    108: "فريق 3★",
    109: "فريق 4★",
    110: "فريق 5★",

    111: "جنرال",
    112: "جنرال 1★",
    113: "جنرال 2★",
    114: "جنرال 3★",
    115: "جنرال 4★",
    116: "جنرال 5★",

    117: "قائد",
    118: "قائد أعلى",
    119: "القائد العام",
    120: "القائد الأعلى"
}

bot = commands.Bot(command_prefix="!", intents=intents)

countries = get_countries()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


def country_flag(code):
    if not code:
        return "🌍"

    code = code.upper()
    return chr(ord(code[0]) + 127397) + chr(ord(code[1]) + 127397)

class PlayerSelect(Select):
    def __init__(self, players):

        options = []

        for player in players:
            options.append(
                discord.SelectOption(
                    label=player["username"][:100],
                    description=f"Level {player['leveling']['level']}",
                    value=player["_id"]
                )
            )

        super().__init__(
            placeholder="Select a player...",
            min_values=1,
            max_values=1,
            options=options
        )

        self.players = players

    async def callback(self, interaction: discord.Interaction):

     selected_id = self.values[0]

     player = next(
        p for p in self.players
        if p["_id"] == selected_id
    )

     country_id = player.get("country")

     country_name = "Unknown"

     if country_id in countries:
        country_name = countries[country_id]["name"]

     country_code = countries[country_id]["code"]
     flag = country_flag(country_code)

     embed = discord.Embed(
        title=f"{player['username']} | {flag} {country_name}",
        color=discord.Color.green()
    )

     embed.add_field(
        name="⭐ Level",
        value=player["leveling"]["level"],
        inline=True
    )

     rank_num = player.get("militaryRank", 0)
     rank_name = RANKS.get(rank_num, "غير معروف")

     embed.add_field(
        name="🎖 Military Rank",
        value=f"{rank_name} ({rank_num})",
        inline=True
    )

     if player.get("infos", {}).get("congressMemberOf"):
        embed.add_field(
            name="🏛 Congress Member",
            value=" ",
            inline=False
        )

     if player.get("infos", {}).get("presidentOf"):
        embed.add_field(
            name="👑 President",
            value=" ",
            inline=False
        )

     if player.get("infos", {}).get("vicePresidentOf"):
        embed.add_field(
            name="⭐ Vice President",
            value=" ",
            inline=False
        )

     if player.get("infos", {}).get("minOfDefenseOf"):
        embed.add_field(
            name="🛡️ Minister of Defense",
            value=" ",
            inline=False
        )

     if player.get("infos", {}).get("minOfEconomyOf"):
        embed.add_field(
            name="📈 Minister of Economy",
            value=" ",
            inline=False
        )

     if player.get("infos", {}).get("minOfForeignAffairsOf"):
        embed.add_field(
            name="🌍 Minister of Foreign Affairs",
            value=" ",
            inline=False
        )

     available_points = player["leveling"]["availableSkillPoints"]
     total_points = player["leveling"]["totalSkillPoints"]

     embed.add_field(
            name="📚 Skill Points",
            value=f"📖 {available_points} / {total_points}",
            inline=False
        )
     
     embed.add_field(
            name="⚔️ Fight Skills",
            value="──────────",
            inline=False
        )

     skills = player.get("skills", {})

     embed.add_field(
            name="⚔️ Attack",
            value=skills.get("attack", {}).get("level", 0),
            inline=True
        )

     embed.add_field(
            name="🎯 Precision",
            value=skills.get("precision", {}).get("level", 0),
            inline=True
        )

     embed.add_field(
            name="💥 Crit Chance",
            value=skills.get("criticalChance", {}).get("level", 0),
            inline=True
        )

     embed.add_field(
            name="🔥 Crit Damage",
            value=skills.get("criticalDamages", {}).get("level", 0),
            inline=True
        )

     embed.add_field(
            name="🛡️ Armor",
            value=skills.get("armor", {}).get("level", 0),
            inline=True
        )

     embed.add_field(
            name="🌀 Dodge",
            value=skills.get("dodge", {}).get("level", 0),
            inline=True
        )

     embed.add_field(
            name="❤️ Health",
            value=skills.get("health", {}).get("level", 0),
            inline=True
        )

     embed.add_field(
            name="💰 Loot",
            value=skills.get("lootChance", {}).get("level", 0),
            inline=True
        )

     embed.add_field(
            name="🍖 Hunger",
            value=skills.get("hunger", {}).get("level", 0),
            inline=True
        )

     embed.add_field(
            name="🏭 Economy Skills",
            value="━━━━━━━━━━━━",
            inline=False
        )

     embed.add_field(
            name="💼 Entre",
            value=skills.get("entrepreneurship", {}).get("level", 0),
            inline=True
        )

     embed.add_field(
            name="⚡ Energy",
            value=skills.get("energy", {}).get("level", 0),
            inline=True
        )

     embed.add_field(
            name="🏗️ Production",
            value=skills.get("production", {}).get("level", 0),
            inline=True
        )

     embed.add_field(
            name="🏢 Companies",
            value=skills.get("companies", {}).get("level", 0),
            inline=True
        )

     embed.add_field(
            name="👥 Management",
            value=skills.get("management", {}).get("level", 0),
            inline=True
        )

     if player.get("avatarUrl"):
        embed.set_thumbnail(url=player["avatarUrl"])

     await interaction.response.edit_message(
        content=None,
        embed=embed,
        view=OptimizeView()
    )


class PlayerView(View):
    def __init__(self, players):
        super().__init__(timeout=60)
        self.add_item(PlayerSelect(players))

class OptimizeView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)

    @discord.ui.button(
        label="War Skills",
        emoji="⚔️",
        style=discord.ButtonStyle.danger
    )
    async def war_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "⚔️ War Skills Optimization Coming Soon",
            ephemeral=True
        )

    @discord.ui.button(
        label="Eco Skills",
        emoji="💰",
        style=discord.ButtonStyle.success
    )
    async def eco_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "💰 Eco Skills Optimization Coming Soon",
            ephemeral=True
        )

@bot.command(name="skills")
async def skills(ctx, *, player_name):

    player_ids = search_player(player_name)

    print(player_ids)
    print(len(player_ids))

    if not player_ids:
        await ctx.send("❌ Player not found.")
        return

    players = []

    for user_id in player_ids:
        player = get_player(user_id)

        if player:
            players.append(player)

    exact_players = [
        p for p in players
        if p["username"].lower() == player_name.lower()
    ]

    if exact_players:
        players = exact_players

    if not players:
        await ctx.send("❌ No player data found.")
        return

    # لاعب واحد فقط
    if len(players) == 1:

        player = players[0]
        print(player.get("avatarUrl"))
        import pprint
        pprint.pprint(player)

        country_id = player.get("country")

        country_name = "Unknown"
        if country_id in countries:
            country_name = countries[country_id]["name"]

        flag = ""
        if country_id in countries:
         flag = country_flag(countries[country_id]["code"])

        embed = discord.Embed(
            title=f"{player['username']} | {flag} {country_name}",
            color=discord.Color.green()
        )

        embed.add_field(
            name="⭐ Level",
            value=player["leveling"]["level"],
            inline=True
        )


        rank_num = player.get("militaryRank", 0)
        rank_name = RANKS.get(rank_num, "غير معروف")

        embed.add_field(
            name="🎖 Military Rank",
            value=f"{rank_name} ({rank_num})",
            inline=True
        )

        if player.get("infos", {}).get("congressMemberOf"):
            embed.add_field(
            name="🏛 Congress Member",
            value=" ",
            inline=False 
        )

        if player.get("infos", {}).get("presidentOf"):
         embed.add_field(
        name="👑 President",
        value="",
        inline=False
        )

        if player.get("infos", {}).get("vicePresidentOf"):
         embed.add_field(
                name="⭐ Vice President",
                value=" ",
                inline=False
       )

        if player.get("infos", {}).get("minOfDefenseOf"):
         embed.add_field(
                name="🛡️ Minister of Defense",
                value="",
                inline=False
        )

        if player.get("infos", {}).get("minOfEconomyOf"):
         embed.add_field(
                 name="📈 Minister of Economy",
                 value="",
                 inline=False
        )

        if player.get("infos", {}).get("minOfForeignAffairsOf"):
         embed.add_field(
                 name="🌍 Minister of Foreign Affairs",
                 value="",
                 inline=False
       )


        available_points = player["leveling"]["availableSkillPoints"]
        total_points = player["leveling"]["totalSkillPoints"]

        embed.add_field(
            name="📚 Skill Points",
            value=f"📖 {available_points} / {total_points}",
            inline=False
        )

        embed.add_field(
        name="⚔️ Fight Skills",
        value="──────────",
        inline=False
        )

        skills = player.get("skills", {})

        embed.add_field(
        name="⚔️ Attack",
        value=skills.get("attack", {}).get("level", 0),
        inline=True
        )

        embed.add_field(
        name="🎯 Precision",
        value=skills.get("precision", {}).get("level", 0),
        inline=True
        )

        embed.add_field(
        name="💥 Crit Chance",
        value=skills.get("criticalChance", {}).get("level", 0),
        inline=True
        )

        embed.add_field(
        name="🔥 Crit Damage",
        value=skills.get("criticalDamages", {}).get("level", 0),
        inline=True
        )

        embed.add_field(
        name="🛡️ Armor",
        value=skills.get("armor", {}).get("level", 0),
        inline=True
        )

        embed.add_field(
        name="🌀 Dodge",
        value=skills.get("dodge", {}).get("level", 0),
        inline=True
        )

        embed.add_field(
        name="❤️ Health",
        value=skills.get("health", {}).get("level", 0),
        inline=True
        )

        embed.add_field(
        name="💰 Loot",
        value=skills.get("lootChance", {}).get("level", 0),
        inline=True
        )

        embed.add_field(
        name="🍖 Hunger",
        value=skills.get("hunger", {}).get("level", 0),
        inline=True
        )

        embed.add_field(
        name="🏭 Economy Skills",
        value="━━━━━━━━━━━━",
        inline=False
        )

        embed.add_field(
        name="💼 Entre",
        value=skills.get("entrepreneurship", {}).get("level", 0),
        inline=True
        )

        embed.add_field(
        name="⚡ Energy",
        value=skills.get("energy", {}).get("level", 0),
        inline=True
        )

        embed.add_field(
        name="🏗️ Production",
        value=skills.get("production", {}).get("level", 0),
        inline=True
        )

        embed.add_field(
        name="🏢 Companies",
        value=skills.get("companies", {}).get("level", 0),
        inline=True
        )

        embed.add_field(
        name="👥 Management",
        value=skills.get("management", {}).get("level", 0),
        inline=True
        )
                
        if player.get("avatarUrl"):
                embed.set_thumbnail(url=player["avatarUrl"])

        await ctx.send(
            embed=embed,
            view=OptimizeView()
        )
        return

    # أكثر من لاعب
    await ctx.send(
        "Select a player:",
        view=PlayerView(players)
    )


bot.run(TOKEN)
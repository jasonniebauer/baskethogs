from datetime import datetime, date
import dash
from dash import html
import dash_mantine_components as dmc


dash.register_page(__name__, path="/", name="Home", title="BasketHogs")

ARKANSAS_RED = "#9D2235"
BLACK = "#000000"
SPOOFER_STONE = "#424242"
TODAY = date.today()

TOTAL_GAMES_PLAYED = 12
TOTAL_WINS = 9
WINNING_PERCENT = f"{round((TOTAL_WINS / TOTAL_GAMES_PLAYED) * 100)}%"
WIN_STREAK = "L1"
AVG_POINTS_PER_GAME = 90
AVG_FIELD_GOALS = 31
AVG_3_POINTERS = 9
AVG_FREE_THROWS = 19
AVG_ASSISTS_PER_GAME = 18
AVG_TURNOVERS_PER_GAME = 10
AVG_STEALS_PER_GAME = 8

DF_GAME_STATS = [
    {
        "date": "Southern",
        "Arkansas": 109,
        "Opponent": 77,
        "Field Goals": 37,
        "Count 3-Pointers": 10,
        "Count Free Throws": 25,
        "Count 2-Pointers": 27,
        "Assists": 23,
        "Turnovers": 9,
        "Steals": 10,
    },
    {
        "date": "Michigan State",
        "Arkansas": 66,
        "Opponent": 69,
        "Field Goals": 22,
        "Count 3-Pointers": 7,
        "Count Free Throws": 15,
        "Count 2-Pointers": 15,
        "Assists": 16,
        "Turnovers": 14,
        "Steals": 11,
    },
    {
        "date": "Central Arkansas",
        "Arkansas": 93,
        "Opponent": 56,
        "Field Goals": 31,
        "Count 3-Pointers": 13,
        "Count Free Throws": 18,
        "Count 2-Pointers": 18,
        "Assists": 17,
        "Turnovers": 8,
        "Steals": 5,
    },
    {
        "date": "Samford",
        "Arkansas": 79,
        "Opponent": 75,
        "Field Goals": 28,
        "Count 3-Pointers": 6,
        "Count Free Throws": 17,
        "Count 2-Pointers": 22,
        "Assists": 13,
        "Turnovers": 9,
        "Steals": 5,
    },
    {
        "date": "Winthrop",
        "Arkansas": 84,
        "Opponent": 83,
        "Field Goals": 29,
        "Count 3-Pointers": 6,
        "Count Free Throws": 20,
        "Count 2-Pointers": 23,
        "Assists": 13,
        "Turnovers": 9,
        "Steals": 5,
    },
    {
        "date": "Jackson State",
        "Arkansas": 115,
        "Opponent": 61,
        "Field Goals": 39,
        "Count 3-Pointers": 9,
        "Count Free Throws": 28,
        "Count 2-Pointers": 30,
        "Assists": 24,
        "Turnovers": 6,
        "Steals": 14,
    },
    {
        "date": "Duke",
        "Arkansas": 71,
        "Opponent": 80,
        "Field Goals": 36,
        "Count 3-Pointers": 10,
        "Count Free Throws": 9,
        "Count 2-Pointers": 16,
        "Assists": 17,
        "Turnovers": 12,
        "Steals": 8,
    },
    {
        "date": "Louisville",
        "Arkansas": 89,
        "Opponent": 80,
        "Field Goals": 28,
        "Count 3-Pointers": 6,
        "Count Free Throws": 27,
        "Count 2-Pointers": 22,
        "Assists": 14,
        "Turnovers": 10,
        "Steals": 5,
    },
    {
        "date": "Fresno State",
        "Arkansas": 82,
        "Opponent": 58,
        "Field Goals": 24,
        "Count 3-Pointers": 11,
        "Count Free Throws": 11,
        "Count 2-Pointers": 19,
        "Assists": 17,
        "Turnovers": 8,
        "Steals": 11,
    },
    {
        "date": "Texas Tech",
        "Arkansas": 93,
        "Opponent": 86,
        "Field Goals": 33,
        "Count 3-Pointers": 10,
        "Count Free Throws": 17,
        "Count 2-Pointers": 23,
        "Assists": 18,
        "Turnovers": 7,
        "Steals": 6,
    },
    {
        "date": "Queens",
        "Arkansas": 108,
        "Opponent": 80,
        "Field Goals": 36,
        "Count 3-Pointers": 14,
        "Count Free Throws": 22,
        "Count 2-Pointers": 22,
        "Assists": 26,
        "Turnovers": 14,
        "Steals": 13,
    },
    {
        "date": "Houston",
        "Arkansas": 85,
        "Opponent": 94,
        "Field Goals": 28,
        "Count 3-Pointers": 8,
        "Count Free Throws": 21,
        "Count 2-Pointers": 20,
        "Assists": 13,
        "Turnovers": 12,
        "Steals": 3,
    },
    {
        "date": "James Madison",
        "Arkansas": 103,
        "Opponent": 74,
        "Field Goals": 34,
        "Count 3-Pointers": 15,
        "Count Free Throws": 20,
        "Count 2-Pointers": 19,
        "Assists": 24,
        "Turnovers": 6,
        "Steals": 7,
    },
    {
        "date": "Tennessee",
        "Arkansas": 86,
        "Opponent": 75,
        "Field Goals": 25,
        "Count 3-Pointers": 7,
        "Count Free Throws": 29,
        "Count 2-Pointers": 18,
        "Assists": 7,
        "Turnovers": 14,
        "Steals": 8,
    },
    {
        "date": "Ole Miss",
        "Arkansas": 94,
        "Opponent": 87,
        "Field Goals": 31,
        "Count 3-Pointers": 10,
        "Count Free Throws": 22,
        "Count 2-Pointers": 21,
        "Assists": 19,
        "Turnovers": 11,
        "Steals": 7,
    },
    {
        "date": "Auburn",
        "Arkansas": 73,
        "Opponent": 95,
        "Field Goals": 25,
        "Count 3-Pointers": 8,
        "Count Free Throws": 15,
        "Count 2-Pointers": 17,
        "Assists": 9,
        "Turnovers": 11,
        "Steals": 7,
    },
    {
        "date": "South Carolina",
        "Arkansas": 108,
        "Opponent": 74,
        "Field Goals": 43,
        "Count 3-Pointers": 8,
        "Count Free Throws": 14,
        "Count 2-Pointers": 35,
        "Assists": 27,
        "Turnovers": 4,
        "Steals": 12,
    },
    {
        "date": "Georgia",
        "Arkansas": 76,
        "Opponent": 90,
        "Field Goals": 29,
        "Count 3-Pointers": 5,
        "Count Free Throws": 13,
        "Count 2-Pointers": 24,
        "Assists": 13,
        "Turnovers": 18,
        "Steals": 11,
    },
    {
        "date": "Vanderbilt",
        "Arkansas": 93,
        "Opponent": 68,
        "Field Goals": 37,
        "Count 3-Pointers": 9,
        "Count Free Throws": 10,
        "Count 2-Pointers": 28,
        "Assists": 25,
        "Turnovers": 7,
        "Steals": 5,
    },
    {
        "date": "LSU",
        "Arkansas": 85,
        "Opponent": 81,
        "Field Goals": 34,
        "Count 3-Pointers": 10,
        "Count Free Throws": 7,
        "Count 2-Pointers": 24,
        "Assists": 18,
        "Turnovers": 8,
        "Steals": 7,
    },
    {
        "date": "Oklahoma",
        "Arkansas": 83,
        "Opponent": 79,
        "Field Goals": 35,
        "Count 3-Pointers": 2,
        "Count Free Throws": 11,
        "Count 2-Pointers": 33,
        "Assists": 17,
        "Turnovers": 6,
        "Steals": 4,
    },
    {
        "date": "Kentucky",
        "Arkansas": 77,
        "Opponent": 85,
        "Field Goals": 29,
        "Count 3-Pointers": 3,
        "Count Free Throws": 16,
        "Count 2-Pointers": 26,
        "Assists": 10,
        "Turnovers": 4,
        "Steals": 2,
    },
    {
        "date": "Mississippi State",
        "Arkansas": 88,
        "Opponent": 68,
        "Field Goals": 36,
        "Count 3-Pointers": 8,
        "Count Free Throws": 8,
        "Count 2-Pointers": 47,
        "Assists": 22,
        "Turnovers": 7,
        "Steals": 5,
    },
    {
        "date": "LSU",
        "Arkansas": 91,
        "Opponent": 62,
        "Field Goals": 35,
        "Count 3-Pointers": 3,
        "Count Free Throws": 18,
        "Count 2-Pointers": 32,
        "Assists": 10,
        "Turnovers": 10,
        "Steals": 7,
    },
    {
        "date": "Auburn",
        "Arkansas": 88,
        "Opponent": 75,
        "Field Goals": 35,
        "Count 3-Pointers": 8,
        "Count Free Throws": 10,
        "Count 2-Pointers": 27,
        "Assists": 19,
        "Turnovers": 5,
        "Steals": 6,
    },
    {
        "date": "Alabama",
        "Arkansas": 115,
        "Opponent": 117,
        "Field Goals": 43,
        "Count 3-Pointers": 13,
        "Count Free Throws": 16,
        "Count 2-Pointers": 30,
        "Assists": 15,
        "Turnovers": 7,
        "Steals": 6,
    },
    {
        "date": "Missouri",
        "Arkansas": 94,
        "Opponent": 86,
        "Field Goals": 32,
        "Count 3-Pointers": 8,
        "Count Free Throws": 22,
        "Count 2-Pointers": 24,
        "Assists": 20,
        "Turnovers": 5,
        "Steals": 5,
    },
    {
        "date": "Texas A&M",
        "Arkansas": 99,
        "Opponent": 84,
        "Field Goals": 33,
        "Count 3-Pointers": 4,
        "Count Free Throws": 29,
        "Count 2-Pointers": 29,
        "Assists": 18,
        "Turnovers": 9,
        "Steals": 9,
    },
    {
        "date": "Florida",
        "Arkansas": 77,
        "Opponent": 111,
        "Field Goals": 30,
        "Count 3-Pointers": 4,
        "Count Free Throws": 13,
        "Count 2-Pointers": 26,
        "Assists": 10,
        "Turnovers": 9,
        "Steals": 7,
    },
    {
        "date": "Texas",
        "Arkansas": 105,
        "Opponent": 85,
        "Field Goals": 35,
        "Count 3-Pointers": 11,
        "Count Free Throws": 24,
        "Count 2-Pointers": 24,
        "Assists": 21,
        "Turnovers": 10,
        "Steals": 8,
    },
    {
        "date": "Missouri",
        "Arkansas": 88,
        "Opponent": 84,
        "Field Goals": 33,
        "Count 3-Pointers": 8,
        "Count Free Throws": 14,
        "Count 2-Pointers": 25,
        "Assists": 13,
        "Turnovers": 11,
        "Steals": 8,
    },
    # {
    #     "date": "",
    #     "Arkansas": ,
    #     "Opponent": ,
    #     "Field Goals": ,
    #     "Count 3-Pointers": ,
    #     "Count Free Throws": ,
    #     "Count 2-Pointers": ,
    #     "Assists": ,
    #     "Turnovers": ,
    #     "Steals": ,
    # },
]

# Loop over each game to calculate stats
for game in DF_GAME_STATS:
    # Set averages for multiple stats
    game['Field Goal Avg.'] = AVG_FIELD_GOALS
    game['3-Pointer Avg.'] = AVG_3_POINTERS
    game['Free Throw Avg.'] = AVG_FREE_THROWS
    game['Assist Avg.'] = AVG_ASSISTS_PER_GAME
    game['Turnover Avg.'] = AVG_TURNOVERS_PER_GAME
    game['Steal Avg.'] = AVG_STEALS_PER_GAME

    # Get the difference in points between each team
    game['Point Gap'] = abs(game['Arkansas'] - game['Opponent'])

    # Get the total number of 3-Pointer points made
    game['3-Pointers'] = game['Count 3-Pointers'] * 3
    # Get the total number of 3-Pointer points made
    game['Free Throws'] = game['Count Free Throws'] * 1
    # Get the total number of 3-Pointer points made
    game['2-Pointers'] = game['Count 2-Pointers'] * 2

    # Get the percent of 3-Pointers made of the total points per game
    game['3-Pointers %'] = round(
        (game['3-Pointers'] / game['Arkansas']) * 100, 1
    )
    # Get the percent of Free Throws made of the total points per game
    game['Free Throws %'] = round(
        (game['Free Throws'] / game['Arkansas']) * 100, 1
    )
    # Get the percent of 2-Pointers made of the total points per game
    game['2-Pointers %'] = round(
        (game['2-Pointers'] / game['Arkansas']) * 100, 1
    )

jaden_karuletwa_stats = {
    "Name": "Jaden Karuletwa",
    "Position": "Guard",
    "Year": "Sophomore",
    "Height": "6' 4\"",
    "Weight": "195",
    "Birthdate": "1/1/2006",
    "Number": "0",
    "Season High": "5",
    "Games Played": "3",
    "PPG": "2",
    "FG%": "0",
    "3P%": "0",
    "FT%": "100%",
}

jaden_karuletwa_radar = [
    {"stat": "Field Goals", "count": 1},
    {"stat": "3-Pointers", "count": 1},
    {"stat": "Free Thows", "count": 2},
    {"stat": "Off. Rebounds", "count": 0},
    {"stat": "Def. Rebounds", "count": 1},
    {"stat": "Assists", "count": 1},
    {"stat": "Turnovers", "count": 0},
    {"stat": "Steals", "count": 1},
]

meleek_thomas_stats = {
    "Name": "Meleek Thomas",
    "Position": "Forward",
    "Year": "Freshman",
    "Height": "6' 5\"",
    "Weight": "185",
    "Birthdate": "8/6/2006",
    "Number": "1",
    "Season High": "26",
    "Games Played": "12",
    "PPG": "14",
    "FG%": "37",
    "3P%": "33",
    "FT%": "84",
}

meleek_thomas_radar = [
    {"stat": "Field Goals", "count": 5},
    {"stat": "3-Pointers", "count": 2},
    {"stat": "Free Thows", "count": 4},
    {"stat": "Off. Rebounds", "count": 2},
    {"stat": "Def. Rebounds", "count": 3},
    {"stat": "Assists", "count": 3},
    {"stat": "Turnovers", "count": 2},
    {"stat": "Steals", "count": 2},
]

amere_brown_stats = {
    "Name": "Amere Brown",
    "Position": "Guard",
    "Year": "Freshman",
    "Height": "5' 9\"",
    "Weight": "180",
    "Birthdate": "5/22/2006",
    "Number": "2",
    "Season High": "1",
    "Games Played": "3",
    "PPG": "0",
    "FG%": "0",
    "3P%": "0",
    "FT%": "50",
}

amere_brown_radar = [
    {"stat": "Field Goals", "count": 0},
    {"stat": "3-Pointers", "count": 0},
    {"stat": "Free Thows", "count": 1},
    {"stat": "Off. Rebounds", "count": 0},
    {"stat": "Def. Rebounds", "count": 0},
    {"stat": "Assists", "count": 0},
    {"stat": "Turnovers", "count": 0},
    {"stat": "Steals", "count": 0},
]

darius_acuff_jr_stats = {
    "Name": "Darius Acuff Jr.",
    "Position": "Guard",
    "Year": "Freshman",
    "Height": "6' 3\"",
    "Weight": "190",
    "Birthdate": "11/16/2006",
    "Number": "5",
    "Season High": "27",
    "Games Played": "12",
    "PPG": "19",
    "FG%": "49",
    "3P%": "44",
    "FT%": "73",
}

darius_acuff_jr_radar = [
    {"stat": "Field Goals", "count": 7},
    {"stat": "3-Pointers", "count": 3},
    {"stat": "Free Thows", "count": 4},
    {"stat": "Off. Rebounds", "count": 1},
    {"stat": "Def. Rebounds", "count": 3},
    {"stat": "Assists", "count": 6},
    {"stat": "Turnovers", "count": 2},
    {"stat": "Steals", "count": 2},
]

trevon_brazile_stats = {
    "Name": "Trevon Brazile",
    "Position": "Forward",
    "Year": "Senior",
    "Height": "6' 10\"",
    "Weight": "230",
    "Birthdate": "1/7/2003",
    "Number": "7",
    "Season High": "26",
    "Games Played": "11",
    "PPG": "14",
    "FG%": "55",
    "3P%": "46",
    "FT%": "80",
}

trevon_brazile_radar = [
    {"stat": "Field Goals", "count": 5},
    {"stat": "3-Pointers", "count": 3},
    {"stat": "Free Thows", "count": 3},
    {"stat": "Off. Rebounds", "count": 2},
    {"stat": "Def. Rebounds", "count": 6},
    {"stat": "Assists", "count": 2},
    {"stat": "Turnovers", "count": 2},
    {"stat": "Steals", "count": 2},
]

karter_knox_stats = {
    "Name": "Karter Knox",
    "Position": "Wing",
    "Year": "Sophomore",
    "Height": "6' 6\"",
    "Weight": "220",
    "Birthdate": "5/16/2005",
    "Number": "1",
    "Season High": "20",
    "Games Played": "11",
    "PPG": "9",
    "FG%": "45",
    "3P%": "47",
    "FT%": "81",
}

karter_knox_radar = [
    {"stat": "Field Goals", "count": 3},
    {"stat": "3-Pointers", "count": 2},
    {"stat": "Free Thows", "count": 3},
    {"stat": "Off. Rebounds", "count": 1},
    {"stat": "Def. Rebounds", "count": 4},
    {"stat": "Assists", "count": 2},
    {"stat": "Turnovers", "count": 2},
    {"stat": "Steals", "count": 1},
]

malique_ewin_stats = {
    "Name": "Malique Ewin",
    "Position": "Forward",
    "Year": "Senior",
    "Height": "6' 10\"",
    "Weight": "240",
    "Birthdate": "1/1/2003",
    "Number": "12",
    "Season High": "21",
    "Games Played": "12",
    "PPG": "9",
    "FG%": "65",
    "3P%": "100",
    "FT%": "71",
}

malique_ewin_radar = [
    {"stat": "Field Goals", "count": 3},
    {"stat": "3-Pointers", "count": 1},
    {"stat": "Free Thows", "count": 3},
    {"stat": "Off. Rebounds", "count": 3},
    {"stat": "Def. Rebounds", "count": 2},
    {"stat": "Assists", "count": 1},
    {"stat": "Turnovers", "count": 1},
    {"stat": "Steals", "count": 1},
]

ayden_kelley_stats = {
    "Name": "Ayden Kelley",
    "Position": "Guard",
    "Year": "Sophomore",
    "Height": "5' 10\"",
    "Weight": "170",
    "Birthdate": "4/9/2006",
    "Number": "14",
    "Season High": "1",
    "Games Played": "3",
    "PPG": "0",
    "FG%": "0",
    "3P%": "0",
    "FT%": "50",
}

ayden_kelley_radar = [
    {"stat": "Field Goals", "count": 0},
    {"stat": "3-Pointers", "count": 0},
    {"stat": "Free Thows", "count": 1},
    {"stat": "Off. Rebounds", "count": 0},
    {"stat": "Def. Rebounds", "count": 0},
    {"stat": "Assists", "count": 0},
    {"stat": "Turnovers", "count": 0},
    {"stat": "Steals", "count": 0},
]

elmir_dzafic_stats = {
    "Name": "Elmir Dzafic",
    "Position": "Center",
    "Year": "Freshman",
    "Height": "7' 0\"",
    "Weight": "285",
    "Birthdate": "1/1/2005",
    "Number": "15",
    "Season High": "1",
    "Games Played": "2",
    "PPG": "1",
    "FG%": "0",
    "3P%": "0",
    "FT%": "50",
}

elmir_dzafic_radar = [
    {"stat": "Field Goals", "count": 0},
    {"stat": "3-Pointers", "count": 0},
    {"stat": "Free Thows", "count": 1},
    {"stat": "Off. Rebounds", "count": 0},
    {"stat": "Def. Rebounds", "count": 0},
    {"stat": "Assists", "count": 0},
    {"stat": "Turnovers", "count": 2},
    {"stat": "Steals", "count": 1},
]

dj_wagner_stats = {
    "Name": "D.J. Wagner",
    "Position": "Guard",
    "Year": "Junior",
    "Height": "6' 4\"",
    "Weight": "190",
    "Birthdate": "5/4/2005",
    "Number": "21",
    "Season High": "16",
    "Games Played": "12",
    "PPG": "8",
    "FG%": "41",
    "3P%": "35",
    "FT%": "78",
}

dj_wagner_radar = [
    {"stat": "Field Goals", "count": 3},
    {"stat": "3-Pointers", "count": 2},
    {"stat": "Free Thows", "count": 2},
    {"stat": "Off. Rebounds", "count": 0},
    {"stat": "Def. Rebounds", "count": 2},
    {"stat": "Assists", "count": 3},
    {"stat": "Turnovers", "count": 1},
    {"stat": "Steals", "count": 2},
]

nick_pringle_stats = {
    "Name": "Nick Pringle",
    "Position": "Forward",
    "Year": "Gr. Senior",
    "Height": "6' 10\"",
    "Weight": "230",
    "Birthdate": "9/16/2001",
    "Number": "23",
    "Season High": "14",
    "Games Played": "12",
    "PPG": "5",
    "FG%": "68",
    "3P%": "0",
    "FT%": "61",
}

nick_pringle_radar = [
    {"stat": "Field Goals", "count": 3},
    {"stat": "3-Pointers", "count": 0},
    {"stat": "Free Thows", "count": 3},
    {"stat": "Off. Rebounds", "count": 2},
    {"stat": "Def. Rebounds", "count": 4},
    {"stat": "Assists", "count": 2},
    {"stat": "Turnovers", "count": 1},
    {"stat": "Steals", "count": 2},
]

billy_richmond_stats = {
    "Name": "Billy Richmond III",
    "Position": "Wing",
    "Year": "Junior",
    "Height": "6' 6\"",
    "Weight": "205",
    "Birthdate": "4/11/2006",
    "Number": "24",
    "Season High": "15",
    "Games Played": "12",
    "PPG": "9",
    "FG%": "57",
    "3P%": "35",
    "FT%": "77",
}

billy_richmond_radar = [
    {"stat": "Field Goals", "count": 3},
    {"stat": "3-Pointers", "count": 1},
    {"stat": "Free Thows", "count": 2},
    {"stat": "Off. Rebounds", "count": 2},
    {"stat": "Def. Rebounds", "count": 3},
    {"stat": "Assists", "count": 2},
    {"stat": "Turnovers", "count": 2},
    {"stat": "Steals", "count": 2},
]

isaiah_sealy_stats = {
    "Name": "Isaiah Sealy",
    "Position": "Wing",
    "Year": "Freshman",
    "Height": "6' 7\"",
    "Weight": "195",
    "Birthdate": "1/1/2007",
    "Number": "30",
    "Season High": "12",
    "Games Played": "7",
    "PPG": "5",
    "FG%": "50",
    "3P%": "0",
    "FT%": "81",
}

isaiah_sealy_radar = [
    {"stat": "Field Goals", "count": 3},
    {"stat": "3-Pointers", "count": 0},
    {"stat": "Free Thows", "count": 3},
    {"stat": "Off. Rebounds", "count": 1},
    {"stat": "Def. Rebounds", "count": 3},
    {"stat": "Assists", "count": 2},
    {"stat": "Turnovers", "count": 1},
    {"stat": "Steals", "count": 1},
]

karim_rtail_stats = {
    "Name": "Karim Rtail",
    "Position": "Wing",
    "Year": "Freshman",
    "Height": "6' 7\"",
    "Weight": "205",
    "Birthdate": "3/23/2004",
    "Number": "35",
    "Season High": "0",
    "Games Played": "0",
    "PPG": "0",
    "FG%": "0",
    "3P%": "0",
    "FT%": "0",
}

karim_rtail_radar = [
    {"stat": "Field Goals", "count": 0},
    {"stat": "3-Pointers", "count": 0},
    {"stat": "Free Thows", "count": 0},
    {"stat": "Off. Rebounds", "count": 0},
    {"stat": "Def. Rebounds", "count": 0},
    {"stat": "Assists", "count": 0},
    {"stat": "Turnovers", "count": 0},
    {"stat": "Steals", "count": 0},
]

paulo_semedo_stats = {
    "Name": "Paulo Semedo",
    "Position": "Forward",
    "Year": "Freshman",
    "Height": "7' 1\"",
    "Weight": "225",
    "Birthdate": "6/12/2006",
    "Number": "99",
    "Season High": "0",
    "Games Played": "0",
    "PPG": "0",
    "FG%": "0",
    "3P%": "0",
    "FT%": "0",
}

paulo_semedo_radar = [
    {"stat": "Field Goals", "count": 0},
    {"stat": "3-Pointers", "count": 0},
    {"stat": "Free Thows", "count": 0},
    {"stat": "Off. Rebounds", "count": 0},
    {"stat": "Def. Rebounds", "count": 0},
    {"stat": "Assists", "count": 0},
    {"stat": "Turnovers", "count": 0},
    {"stat": "Steals", "count": 0},
]

def scoreboard_stat_card(value, title, subtitle):
    return dmc.GridCol(
        mb="xl",  # Margin bottom
        children=[
            dmc.Title(
                value,  # Stat value
                order=1,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                c="black",  # Color utility
                ta="center",  # Text align
                fz="6rem",  # Font size
                lh=1.0,  # Line height
                fw="800",  # Font weight
                ff="Oxanium, sans-serif",  # Font family
            ),
            dmc.Title(
                title,  # Stat title
                order=4,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                c="black",  # Color utility
                ta="center",  # Text align
                tt="uppercase",  # Uppercase text
                lh=1.0,  # Line height
                fw="800",  # Font weight
            ),
            dmc.Title(
                subtitle,  # Stat subtitle
                order=6,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                c="#9D2235",  # Color utility
                ta="center",  # Text align
                fw="600",  # Font weight
            ),
        ],
        span={"base": 6, "sm": 6, "md": 3},  # Grid column width at different viewpoints
    )

scoreboard = dmc.Grid(
    pt="7rem",
    pb="5rem",
    justify="center",
    gutter="sm",
    children=[
        scoreboard_stat_card(TOTAL_GAMES_PLAYED, "Total Games", "2025-2026 Season"),
        scoreboard_stat_card(TOTAL_WINS, "Total Wins", "2025-2026 Season"),
        scoreboard_stat_card(WIN_STREAK, "Streak", "2025-2026 Season"),
        scoreboard_stat_card(WINNING_PERCENT, "Winning Percent", "Win to Loss Ratio"),
        scoreboard_stat_card(AVG_POINTS_PER_GAME, "Avg. Points", "Per Game"),
        scoreboard_stat_card(AVG_FIELD_GOALS, "Avg. Field Goals", "Per Game"),
        scoreboard_stat_card(AVG_3_POINTERS, "Avg. 3-Pointers", "Per Game"),
        scoreboard_stat_card(AVG_FREE_THROWS, "Avg. Free Throws", "Per Game"),
    ]
)

team_stats_headline = dmc.Title(
    "Team Stats",
    order=1,
    ta="center",
    py="2rem",
)

# team = dmc.AvatarGroup([
#     dmc.Tooltip(
#         dmc.Avatar(src="/assets/players/Meleek-Thomas.jpg", size="xl", radius="md"),
#         label="Meleek Thomas",
#         position="bottom",
#     ),
#     dmc.Avatar(src="/assets/players/Dj-Wagner.jpg", size="xl", radius="md"),
# ])

# df_total_wins_over_time = [
#   {"date": "Southern", "Total Wins": 1},
#   {"date": "Michigan State", "Total Wins": 1},
# ]

# total_wins_over_time = dmc.Card(
#     radius="md",
#     bd="1px solid #C7C8CA",
#     mb="5rem",
#     children=[
#         dmc.Title(
#             "Total Wins Over Time",
#             order=1,
#             mb="xl",
#         ),
#         dmc.LineChart(
#             h=300,
#             dataKey="date",
#             data=df_total_wins_over_time,
#             series = [
#                 {"name": "Total Wins", "color": ARKANSAS_RED},
#             ],
#             curveType="Linear",
#             tickLine="y",
#             # withXAxis=False,
#             mb="sm",
#             pr="1rem",
#         ),
#     ]
# )

total_points_over_time = dmc.Card(
    radius="md",
    bd="1px solid #C7C8CA",
    mb="5rem",
    children=[
        dmc.Title(
            "Total Points",
            order=1,
        ),
        dmc.Title(
            "The total points scored per game.",
            order=5,
            mb="xl",
            fw="500",
        ),
        dmc.AreaChart(
            h=300,
            dataKey="date",
            data=DF_GAME_STATS,
            series = [
                {"name": "Arkansas", "color": ARKANSAS_RED},
                {"name": "Opponent", "color": SPOOFER_STONE},
            ],
            curveType="linear",
            tickLine="y",
            mb="sm",
            pr="1rem",
            withLegend=True,
        ),
    ]
)

# leaderboard_total_points = dmc.Card(
#     radius="md",
#     bd="1px solid #C7C8CA",
#     mb="5rem",
#     h="100%",
#     children=[
#         dmc.Title(
#             "Total Points Leaderboard",
#             order=1,
#         ),
#         dmc.Title(
#             "The top 5 players by total points for the season.",
#             order=5,
#             mb="xl",
#             fw="500",
#         ),
#         dmc.Table(
#             striped=True,
#             data={
#                 "head": ["Rank", "Player", "Total Points"],
#                 "body": [
#                     [1, "Meleek Thomas", 97],
#                     [1, "Darius Acuff Jr.", 91],
#                     [3, "Trevon Brazile", 57],
#                     [4, "D.J. Wagner", 40],
#                     [5, "Nick Pringle", 36],
#                 ],
#             },
#         )
#     ]
# )

# total_points = dmc.Grid(
#     align="stretch",  # Default; explicitly set for clarity
#     children=[
#     dmc.GridCol(
#         span={"base": 12, "sm": 12, "md": 8},
#         children=total_points_over_time,
#     ),
#     dmc.GridCol(
#         span={"base": 12, "sm": 12, "md": 4},
#         style={"display": "flex", "flexDirection": "column"},  # Optional: Ensures inner content stretches
#         children=leaderboard_total_points,
#     ),
# ])

count_points_by_type = dmc.Card(
    radius="md",
    bd="1px solid #C7C8CA",
    mb="5rem",
    children=[
        dmc.Title(
            "Number of Points",
            order=1,
        ),
        dmc.Title(
            "The total number of points by type.",
            order=5,
            mb="xl",
            fw="500",
        ),
        dmc.BarChart(
            h=300,
            dataKey="date",
            data=DF_GAME_STATS,
            series=[
                {"name": "Count 3-Pointers", "label": "3-Pointers", "color": SPOOFER_STONE},
                {"name": "Count Free Throws", "label": "Free Throws", "color": "#C7C8CA"},
                {"name": "Count 2-Pointers", "label": "2-Pointers", "color": ARKANSAS_RED},
            ],
            withLegend=True,
            tickLine="none",
            gridAxis="x",
            withXAxis=True,
            withYAxis=True,
            mb="sm",
            pr="1rem",
        ),
    ]
)

totals_points_by_type = dmc.Card(
    radius="md",
    bd="1px solid #C7C8CA",
    mb="5rem",
    children=[
        dmc.Title(
            "Total Points by Type",
            order=1,
        ),
        dmc.Title(
            "The total points scored by point type.",
            order=5,
            mb="xl",
            fw="500",
        ),
        dmc.BarChart(
            h=300,
            dataKey="date",
            data=DF_GAME_STATS,
            type="stacked",
            series=[
                {"name": "3-Pointers", "color": SPOOFER_STONE},
                {"name": "Free Throws", "color": "#C7C8CA"},
                {"name": "2-Pointers", "color": ARKANSAS_RED},
            ],
            withLegend=True,
            tickLine="none",
            gridAxis="x",
            withXAxis=True,
            withYAxis=True,
            mb="sm",
            pr="1rem",
        ),
    ]
)

point_type_by_percent_of_total = dmc.Card(
    radius="md",
    bd="1px solid #C7C8CA",
    mb="5rem",
    children=[
        dmc.Title(
            "Point Type of Total Points",
            order=1,
        ),
        dmc.Title(
            "The percentage of total points scored per point type.",
            order=5,
            mb="xl",
            fw="500",
        ),
        dmc.BarChart(
            h=300,
            dataKey="date",
            data=DF_GAME_STATS,
            type="percent",
            series=[
                {"name": "3-Pointers %", "color": SPOOFER_STONE},
                {"name": "Free Throws %", "color": "#C7C8CA"},
                {"name": "2-Pointers %", "color": ARKANSAS_RED},
            ],
            withLegend=True,
            tickLine="none",
            gridAxis="x",
            withXAxis=True,
            withYAxis=True,
            mb="sm",
            pr="1rem",
        )
    ]
)

points_gap_over_time = dmc.Card(
    radius="md",
    bd="1px solid #C7C8CA",
    mb="5rem",
    children=[
        dmc.Title(
            "Point Gap Over Time",
            order=1,
            # mb="sm",
        ),
        dmc.Title(
            "The difference between the total points of each team per game.",
            order=5,
            mb="xl",
            fw="500",
        ),
        dmc.AreaChart(
            h=300,
            dataKey="date",
            data=DF_GAME_STATS,
            series = [
                {"name": "Point Gap", "color": ARKANSAS_RED},
            ],
            curveType="linear",
            tickLine="y",
            # withXAxis=False,
            mb="sm",
            pr="1rem",
        ),
    ]
)

# def get_player_age(birthdate_string):
#     # Convert the player's birthdate string to a date
#     birthdate = datetime.strptime(birthdate_string, "%m/%d/%Y").date()
#     # Get the player's age based on their date of birth
#     return TODAY.year - birthdate.year - ((TODAY.month, TODAY.day) < (birthdate.month, birthdate.day))

# players_and_birthdates = [
#     {"Name": "Isaiah Sealy", "Birthdate": "1/1/2007"},
#     {"Name": "Darius Acuff Jr.", "Birthdate": "11/16/2006"},
#     {"Name": "Meleek Thomas", "Birthdate": "8/6/2006"},
#     {"Name": "Paulo Semedo", "Birthdate": "6/12/2006"},
#     {"Name": "Amere Brown", "Birthdate": "5/22/2006"},
#     {"Name": "Billy Richmond III", "Birthdate": "4/11/2006"},
#     {"Name": "Ayden Kelley", "Birthdate": "4/9/2006"},
#     {"Name": "Jaden Karuletwa", "Birthdate": "1/1/2006"},
#     {"Name": "Karter Knox", "Birthdate": "5/16/2005"},
#     {"Name": "D.J. Wagner", "Birthdate": "5/4/2005"},
#     {"Name": "Elmir Dzafic", "Birthdate": "1/1/2005"},
#     {"Name": "Karim Rtail", "Birthdate": "3/23/2004"},
#     {"Name": "Trevon Brazile", "Birthdate": "1/7/2003"},
#     {"Name": "Malique Ewin", "Birthdate": "1/1/2003"},
#     {"Name": "Nick Pringle", "Birthdate": "9/16/2001"},
# ]

df_players_by_age = [
    # {"Age": "Age 18", "Total": 0},
    {"Age": "Age 19", "Total": 7},
    {"Age": "Age 20", "Total": 3},
    {"Age": "Age 21", "Total": 2},
    {"Age": "Age 22", "Total": 0},
    {"Age": "Age 23", "Total": 2},
    {"Age": "Age 24", "Total": 1}
]

# for player in players_and_birthdates:
#     age = get_player_age(player['Birthdate'])
#     if age == 18:
#         df_players_by_age[0]["Total"] += 1
#     elif age == 19:
#         df_players_by_age[1]["Total"] += 1
#     elif age == 20:
#         df_players_by_age[2]["Total"] += 1
#     elif age == 21:
#         df_players_by_age[3]["Total"] += 1
#     elif age == 22:
#         df_players_by_age[4]["Total"] += 1
#     elif age == 23:
#         df_players_by_age[5]["Total"] += 1
#     elif age == 24:
#         df_players_by_age[6]["Total"] += 1

df_players_by_year = [
    {"Year": "Freshman", "Total": 7},
    {"Year": "Sophomore", "Total": 3},
    {"Year": "Junior", "Total": 2},
    {"Year": "Senior", "Total": 2},
    {"Year": "Gr. Senior", "Total": 1},
]

players_by_age_and_year = dmc.Grid([
    dmc.GridCol(
        span={"base": 12, "sm": 12, "md": 6},
        children=dmc.Card(
            radius="md",
            bd="1px solid #C7C8CA",
            mb="4rem",  # subtract 1rem from bottom margin for extra margin added for stacked columns
            children=[
                dmc.Title(
                    "Players by Age",
                    order=1,
                ),
                dmc.Title(
                    "The total number of players grouped by their age.",
                    order=5,
                    mb="xl",
                    fw="500",
                ),
                dmc.BarChart(
                    h=300,
                    dataKey="Age",
                    data=df_players_by_age,
                    series=[
                        {"name": "Total", "color": ARKANSAS_RED}
                    ],
                    tickLine="none",
                    gridAxis="x",
                    withXAxis=True,
                    withYAxis=True,
                    mb="sm",
                    pr="1rem",
                ),
            ]
        )
    ),
    dmc.GridCol(
        span={"base": 12, "sm": 12, "md": 6},
        children=dmc.Card(
            radius="md",
            bd="1px solid #C7C8CA",
            mb="5rem",
            children=[
                dmc.Title(
                    "Players by Study Year",
                    order=1,
                ),
                dmc.Title(
                    "The total number of players grouped by year of study.",
                    order=5,
                    mb="xl",
                    fw="500",
                ),
                dmc.BarChart(
                    h=300,
                    dataKey="Year",
                    data=df_players_by_year,
                    series=[
                        {"name": "Total", "color": ARKANSAS_RED}
                    ],
                    tickLine="none",
                    gridAxis="x",
                    withXAxis=True,
                    withYAxis=True,
                    mb="sm",
                    pr="1rem",
                ),
            ]
        )
    ),
])

# df_player_weight_vs_height = [
#     {"Weight": 15, "Height": 76},  # Jaden Karuletwa
#     {"Weight": 185, "Height": 77},  # Meleek Thomas
#     {"Weight": 180, "Height": 69},  # Amere Brown
#     {"Weight": 190, "Height": 75},  # Darius Acuff Jr.
#     {"Weight": 230, "Height": 82},  # Trevon Brazile
#     {"Weight": 220, "Height": 78},  # Karter Knox
#     {"Weight": 240, "Height": 82},  # Malique Ewin
#     {"Weight": 170, "Height": 70},  # Ayden Kelley
#     {"Weight": 285, "Height": 84},  #Elmir Džafić
#     {"Weight": 190, "Height": 76},  # D.J. Wagner
#     {"Weight": 230, "Height": 82},  # Nick Pringle
#     {"Weight": 205, "Height": 78},  # Billy Richmond III
#     {"Weight": 195, "Height": 79},  # Isaiah Sealy
#     {"Weight": 205, "Height": 79},  # Karim Rtail
#     {"Weight": 225, "Height": 85},  # Paulo Semedo
# ]

# player_weight_vs_height = dmc.Card(
#     radius="md",
#     bd="1px solid #C7C8CA",
#     mb="5rem",
#     children=[
#         dmc.Title(
#             "Players by Weight & Height",
#             order=1,
#             mb="xl",
#         ),
#         dmc.ScatterChart(
#             h=300,
#             data=df_player_weight_vs_height,
#             dataKey={"x": "Weight", "y": "Height"},
#             xAxisLabel="Weight (lbs)",
#             yAxisLabel="Height (in)",
#             # style={"--mantine-primary-color": ARKANSAS_RED},
#         )
#     ]
# )

field_goals_over_time = dmc.Card(
    radius="md",
    bd="1px solid #C7C8CA",
    mb="5rem",
    children=[
        dmc.Title(
            "Field Goals Over Time",
            order=1,
        ),
        dmc.Title(
            "The total number of field goals made per game compared to the team's average.",
            order=5,
            mb="xl",
            fw="500",
        ),
        dmc.CompositeChart(
            h=300,
            data=DF_GAME_STATS,
            dataKey="date",
            curveType="Linear",
            gridAxis="x",
            withXAxis=True,
            withYAxis=True,
            withLegend=True,
            series=[
                {"name": "Field Goal Avg.", "label": "Field Goal Avg.", "color": "#C7C8CA", "type": "bar"},
                {"name": "Field Goals", "color": ARKANSAS_RED, "type": "line"},
            ]
        )
    ]
)

x3_pointers_over_time = dmc.Card(
    radius="md",
    bd="1px solid #C7C8CA",
    mb="5rem",
    children=[
        dmc.Title(
            "3-Pointers Over Time",
            order=1,
        ),
        dmc.Title(
            "The total number of 3-pointers made per game compared to the team's average.",
            order=5,
            mb="xl",
            fw="500",
        ),
        dmc.CompositeChart(
            h=300,
            data=DF_GAME_STATS,
            dataKey="date",
            curveType="Linear",
            gridAxis="x",
            withXAxis=True,
            withYAxis=True,
            withLegend=True,
            series=[
                {"name": "3-Pointer Avg.", "label": "3-Pointer Avg.", "color": "#C7C8CA", "type": "bar"},
                {"name": "Count 3-Pointers", "label": "3-Pointers", "color": ARKANSAS_RED, "type": "line"},
            ]
        )
    ]
)

free_throws_over_time = dmc.Card(
    radius="md",
    bd="1px solid #C7C8CA",
    mb="5rem",
    children=[
        dmc.Title(
            "Free Throws Over Time",
            order=1,
        ),
        dmc.Title(
            "The total number of free throws made per game compared to the team's average.",
            order=5,
            mb="xl",
            fw="500",
        ),
        dmc.CompositeChart(
            h=300,
            data=DF_GAME_STATS,
            dataKey="date",
            curveType="Linear",
            gridAxis="x",
            withXAxis=True,
            withYAxis=True,
            withLegend=True,
            series=[
                {"name": "Free Throw Avg.", "label": "Free Throw Avg.", "color": "#C7C8CA", "type": "bar"},
                {"name": "Count Free Throws", "label": "Free Throws", "color": ARKANSAS_RED, "type": "line"},
            ]
        )
    ]
)

assists_over_time = dmc.Card(
    radius="md",
    bd="1px solid #C7C8CA",
    mb="5rem",
    children=[
        dmc.Title(
            "Assists Over Time",
            order=1,
        ),
        dmc.Title(
            "The total number of assists per game compared to the team's average.",
            order=5,
            mb="xl",
            fw="500",
        ),
        dmc.CompositeChart(
            h=300,
            data=DF_GAME_STATS,
            dataKey="date",
            curveType="Linear",
            gridAxis="x",
            withXAxis=True,
            withYAxis=True,
            withLegend=True,
            series=[
                {"name": "Assist Avg.", "label": "Assist Avg.", "color": "#C7C8CA", "type": "bar"},
                {"name": "Assists", "color": ARKANSAS_RED, "type": "line"},
            ]
        )
    ]
)

turnovers_over_time = dmc.Card(
    radius="md",
    bd="1px solid #C7C8CA",
    mb="5rem",
    children=[
        dmc.Title(
            "Turnovers Over Time",
            order=1,
        ),
        dmc.Title(
            "The total number of turnovers per game compared to the team's average.",
            order=5,
            mb="xl",
            fw="500",
        ),
        dmc.CompositeChart(
            h=300,
            data=DF_GAME_STATS,
            dataKey="date",
            curveType="Linear",
            gridAxis="x",
            withXAxis=True,
            withYAxis=True,
            withLegend=True,
            series=[
                {"name": "Turnover Avg.", "label": "Turnover Avg.", "color": "#C7C8CA", "type": "bar"},
                {"name": "Turnovers", "color": ARKANSAS_RED, "type": "line"},
            ]
        )
    ]
)

steals_over_time = dmc.Card(
    radius="md",
    bd="1px solid #C7C8CA",
    mb="5rem",
    children=[
        dmc.Title(
            "Steals Over Time",
            order=1,
        ),
        dmc.Title(
            "The total number of steals per game compared to the team's average.",
            order=5,
            mb="xl",
            fw="500",
        ),
        dmc.CompositeChart(
            h=300,
            data=DF_GAME_STATS,
            dataKey="date",
            curveType="Linear",
            gridAxis="x",
            withXAxis=True,
            withYAxis=True,
            withLegend=True,
            series=[
                {"name": "Steal Avg.", "label": "Steal Avg.", "color": "#C7C8CA", "type": "bar"},
                {"name": "Steals", "color": ARKANSAS_RED, "type": "line"},
            ]
        )
    ]
)

df_team_by_position = [
    {"Position": "Guard", "Total": 6},
    {"Position": "Forward", "Total": 4},
    {"Position": "Wing", "Total": 4},
    {"Position": "Center", "Total": 1},
]

df_team_by_position_percentage = [
    {"positions": "Team Positions", "Guard": 6, "Forward": 4, "Wing": 4, "Center": 1},
]

team_by_positions = dmc.Grid([
    dmc.GridCol(
        span={"base": 12, "sm": 12, "md": 6},
        children=dmc.Card(
            radius="md",
            bd="1px solid #C7C8CA",
            mb="4rem",
            children=[
                dmc.Title(
                    "Total Positions",
                    order=1,
                ),
                dmc.Title(
                    "The total number of positions across the team.",
                    order=5,
                    mb="xl",
                    fw="500",
                ),
                dmc.BarChart(
                    h=300,
                    dataKey="Position",
                    data=df_team_by_position,
                    series=[
                        {"name": "Total", "color": ARKANSAS_RED}
                    ],
                    tickLine="none",
                    gridAxis="x",
                    withXAxis=True,
                    withYAxis=True,
                    mb="sm",
                    pr="1rem",
                ),
            ]
        )
    ),
    dmc.GridCol(
        span={"base": 12, "sm": 12, "md": 6},
        children=dmc.Card(
            radius="md",
            bd="1px solid #C7C8CA",
            mb="5rem",
            children=[
                dmc.Title(
                    "Position Total % of Team",
                    order=1,
                ),
                dmc.Title(
                    "The total position's percentage of the team's available positions.",
                    order=5,
                    mb="xl",
                    fw="500",
                ),
                dmc.BarChart(
                    h=300,
                    dataKey="positions",
                    data=df_team_by_position_percentage,
                    type="percent",
                    series=[
                        {"name": "Guard", "color": ARKANSAS_RED},
                        {"name": "Forward", "color": SPOOFER_STONE},
                        {"name": "Wing", "color": "#C7C8CA"},
                        {"name": "Center", "color": "black"},
                    ],
                    withLegend=True,
                    tickLine="none",
                    gridAxis="x",
                    withXAxis=True,
                    withYAxis=True,
                    mb="sm",
                    pr="1rem",
                ),
            ]
        )
    )
])

def player_card(player_stats_data, radar_data):
    # Remove space characters and periods
    name_formatted_for_headshot = player_stats_data['Name'].replace(" ", "-").replace(".", "")

    # Get player's age
    age = get_player_age(player_stats_data['Birthdate'])
    
    return dmc.GridCol(
        dmc.Card(
            radius="md",
            bd="1px solid #C7C8CA",
            children=[
                dmc.Flex(
                    justify="flex-start",
                    align="flex-start",
                    direction="row",
                    wrap="wrap",
                    mb="lg",
                    children=[
                        dmc.Flex(
                            justify="flex-start",
                            align="flex-start",
                            direction="row",
                            wrap="wrap",
                            children=[
                                dmc.Avatar(
                                    src=f"/assets/players/{name_formatted_for_headshot}.jpg",
                                    # size="lg",
                                    radius="sm",
                                    mr="0.5rem",
                                    h="70px",
                                    w="70px",
                                ),
                                dmc.Box(
                                    children=[
                                        dmc.Text(
                                            player_stats_data['Name'],
                                            fw="700",
                                            fz="1.125rem",
                                            lh=1.0,
                                            mb="1px",
                                        ),
                                        dmc.Text(
                                            f"{player_stats_data['Position']} - {player_stats_data['Year']}",
                                            fw="500",
                                            fz="0.825rem",
                                            lh=1.0,
                                            mb="5px",
                                        ),
                                        dmc.Text(
                                            f"Ht. {player_stats_data['Height']}",
                                            fw="500",
                                            fz="0.6875rem",
                                            lh=1.0,
                                        ),
                                        dmc.Text(
                                            f"Wt. {player_stats_data['Weight']}lbs",
                                            fw="500",
                                            fz="0.6875rem",
                                            lh=1.0,
                                        ),
                                        dmc.Text(
                                            f"Age {age}",
                                            fw="500",
                                            fz="0.6875rem",
                                            lh=1.0,
                                        ),
                                    ]
                                )
                            ]
                        ),
                        dmc.Title(
                            player_stats_data['Number'],
                            lh=1.0,
                            mt="-10px",
                            mb=0,
                            ml="auto",
                            fw=700,
                            fz="5.875rem",
                        )
                    ]
                ),
                dmc.RadarChart(
                    h=270,
                    pb="1.25rem",
                    data=radar_data,
                    dataKey="stat",
                    withPolarRadiusAxis=True,
                    series=[{"name": "count", "color": "#9D2235", "opacity": 0.2}],               # enable radial axis
                    # polarRadiusAxisProps={
                    #     "domain": [0, 10],  # radial scale: 0 to 100 (clamps data)
                    # },
                ),
                dmc.Table(
                    withTableBorder=True,
                    layout="fixed",
                    variant="vertical",
                    # horizontalSpacing="md",
                    # verticalSpacing="sm",
                    style={
                        "overflow": "hidden",  # ← crucial: clips table content to radius
                        "borderRadius": "0.25rem",
                        "border": "1px solid #C7C8CA",
                        "borderCollapse": "separate"
                    },
                    children=[
                        dmc.TableTbody([
                            dmc.TableTr([
                                dmc.TableTh(
                                    "Season High",
                                    style={
                                        "backgroundColor": "#F2F2F4",
                                        "borderRight": "1px solid #C7C8CA",
                                        "borderBottom": "1px solid #C7C8CA",
                                    }
                                ),
                                dmc.TableTd(
                                    player_stats_data['Season High'],
                                    ta="right",
                                    style={
                                        "borderBottom": "1px solid #C7C8CA",
                                    }
                                ),
                            ]),
                            dmc.TableTr([
                                dmc.TableTh(
                                    "Games Played",
                                    style={
                                        "backgroundColor": "#F2F2F4",
                                        "borderRight": "1px solid #C7C8CA",
                                        "borderBottom": "1px solid #C7C8CA",
                                    }
                                ),
                                dmc.TableTd(
                                    player_stats_data['Games Played'],
                                    ta="right",
                                    style={
                                        "borderBottom": "1px solid #C7C8CA",
                                    }
                                ),
                            ]),
                            dmc.TableTr([
                                dmc.TableTh(
                                    "Average PPG",
                                    style={
                                        "backgroundColor": "#F2F2F4",
                                        "borderRight": "1px solid #C7C8CA",
                                        "borderBottom": "1px solid #C7C8CA",
                                    }
                                ),
                                dmc.TableTd(
                                    player_stats_data['PPG'],
                                    ta="right",
                                    style={
                                        "borderBottom": "1px solid #C7C8CA",
                                    }
                                ),
                            ]),
                            dmc.TableTr([
                                dmc.TableTh(
                                    "Field Goal %",
                                    style={
                                        "backgroundColor": "#F2F2F4",
                                        "borderBottom": "1px solid #C7C8CA",
                                        "borderRight": "1px solid #C7C8CA",
                                    }
                                ),
                                dmc.TableTd(
                                    f"{player_stats_data['FG%']}%",
                                    ta="right",
                                    style={
                                        "borderBottom": "1px solid #C7C8CA",
                                    }
                                ),
                            ]),
                            dmc.TableTr([
                                dmc.TableTh(
                                    "3-Pointer %",
                                    style={
                                        "backgroundColor": "#F2F2F4",
                                        "borderRight": "1px solid #C7C8CA",
                                        "borderBottom": "1px solid #C7C8CA",
                                    }
                                ),
                                dmc.TableTd(
                                    f"{player_stats_data['3P%']}%",
                                    ta="right",
                                    style={
                                        "borderBottom": "1px solid #C7C8CA",
                                    }
                                ),
                            ]),
                            dmc.TableTr([
                                dmc.TableTh(
                                    "Free Throw %",
                                    style={
                                        "backgroundColor": "#F2F2F4",
                                        "borderRight": "1px solid #C7C8CA",
                                    }
                                ),
                                dmc.TableTd(
                                    f"{player_stats_data['FT%']}%",
                                    ta="right",
                                ),
                            ]),
                        ])
                    ]
                )
            ]
        ),
        span={"base": 12, "sm": 6, "md": 6, "lg": 4},
        mb="1.5rem",
    )


player_stats_headline = dmc.Title(
    "Player Stats",
    order=1,
    ta="center",
    py="2rem",
)

players = dmc.Grid(
    justify="center",
    gutter="md",
    mb="3.5rem",
    children=[
        player_card(
            player_stats_data=darius_acuff_jr_stats,
            radar_data=darius_acuff_jr_radar,
        ),
        player_card(
            player_stats_data=meleek_thomas_stats,
            radar_data=meleek_thomas_radar,
        ),
        player_card(
            player_stats_data=dj_wagner_stats,
            radar_data=dj_wagner_radar,
        ),
        player_card(
            player_stats_data=billy_richmond_stats,
            radar_data=billy_richmond_radar,
        ),
        player_card(
            player_stats_data=trevon_brazile_stats,
            radar_data=trevon_brazile_radar,
        ),
        player_card(
            player_stats_data=nick_pringle_stats,
            radar_data=nick_pringle_radar,
        ),
        player_card(
            player_stats_data=karter_knox_stats,
            radar_data=karter_knox_radar,
        ),
        player_card(
            player_stats_data=malique_ewin_stats,
            radar_data=malique_ewin_radar,
        ),
        player_card(
            player_stats_data=isaiah_sealy_stats,
            radar_data=isaiah_sealy_radar,
        ),
        player_card(
            player_stats_data=elmir_dzafic_stats,
            radar_data=elmir_dzafic_radar,
        ),
        player_card(
            player_stats_data=jaden_karuletwa_stats,
            radar_data=jaden_karuletwa_radar,
        ),
        player_card(
            player_stats_data=amere_brown_stats,
            radar_data=amere_brown_radar,
        ),
        player_card(
            player_stats_data=ayden_kelley_stats,
            radar_data=ayden_kelley_radar,
        ),
        player_card(
            player_stats_data=karim_rtail_stats,
            radar_data=karim_rtail_radar,
        ),
        player_card(
            player_stats_data=paulo_semedo_stats,
            radar_data=paulo_semedo_radar,
        ),
    ],
)

layout = dmc.Box(
    children=[
        # team,
        scoreboard,
        player_stats_headline,
        players,
        team_stats_headline,
        # total_wins_over_time,
        total_points_over_time,
        field_goals_over_time,
        x3_pointers_over_time,
        free_throws_over_time,
        assists_over_time,
        turnovers_over_time,
        steals_over_time,
        count_points_by_type,
        totals_points_by_type,
        point_type_by_percent_of_total,
        points_gap_over_time,
        players_by_age_and_year,
        team_by_positions,
        # player_weight_vs_height,
    ]
)

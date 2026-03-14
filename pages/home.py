from datetime import datetime, date
import dash
import dash_mantine_components as dmc
from data.game_stats import df_game_stats
from data.player_radar import (
    jaden_karuletwa_radar,
    meleek_thomas_radar,
    amere_brown_radar,
    darius_acuff_jr_radar,
    trevon_brazile_radar,
    karter_knox_radar,
    malique_ewin_radar,
    ayden_kelley_radar,
    elmir_dzafic_radar,
    dj_wagner_radar,
    nick_pringle_radar,
    billy_richmond_radar,
    isaiah_sealy_radar,
    karim_rtail_radar,
    paulo_semedo_radar
)
from data.player_stats import (
    jaden_karuletwa_stats,
    meleek_thomas_stats,
    amere_brown_stats,
    darius_acuff_jr_stats,
    trevon_brazile_stats,
    karter_knox_stats,
    malique_ewin_stats,
    ayden_kelley_stats,
    elmir_dzafic_stats,
    dj_wagner_stats,
    nick_pringle_stats,
    billy_richmond_stats,
    isaiah_sealy_stats,
    karim_rtail_stats,
    paulo_semedo_stats
)


dash.register_page(__name__, path="/", name="Home", title="BasketHogs")

ARKANSAS_RED = "#9D2235"
BLACK = "#000000"
SPOOFER_STONE = "#424242"
TODAY = date.today()

TOTAL_GAMES_PLAYED = 31
TOTAL_WINS = 23
WINNING_PERCENT = f"{round((TOTAL_WINS / TOTAL_GAMES_PLAYED) * 100)}%"
SEC_TOURNAMENT = "2nd"
AVG_POINTS_PER_GAME = 90
AVG_FIELD_GOALS = 32
AVG_3_POINTERS = 8
AVG_FREE_THROWS = 17
AVG_ASSISTS_PER_GAME = 17
AVG_TURNOVERS_PER_GAME = 9
AVG_STEALS_PER_GAME = 7

# Loop over each game to calculate stats
for game in df_game_stats:
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
        scoreboard_stat_card(SEC_TOURNAMENT, "SEC Tournament", "2025-2026 Season"),
        scoreboard_stat_card(TOTAL_GAMES_PLAYED, "Total Games", "2025-2026 Season"),
        scoreboard_stat_card(TOTAL_WINS, "Total Wins", "2025-2026 Season"),
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
            data=df_game_stats,
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
            data=df_game_stats,
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
            data=df_game_stats,
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
            data=df_game_stats,
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
            data=df_game_stats,
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

def get_player_age(birthdate_string):
    # Convert the player's birthdate string to a date
    birthdate = datetime.strptime(birthdate_string, "%m/%d/%Y").date()
    # Get the player's age based on their date of birth
    return TODAY.year - birthdate.year - ((TODAY.month, TODAY.day) < (birthdate.month, birthdate.day))

players_and_birthdates = [
    {"Name": "Isaiah Sealy", "Birthdate": "1/1/2007"},
    {"Name": "Darius Acuff Jr.", "Birthdate": "11/16/2006"},
    {"Name": "Meleek Thomas", "Birthdate": "8/6/2006"},
    {"Name": "Paulo Semedo", "Birthdate": "6/12/2006"},
    {"Name": "Amere Brown", "Birthdate": "5/22/2006"},
    {"Name": "Billy Richmond III", "Birthdate": "4/11/2006"},
    {"Name": "Ayden Kelley", "Birthdate": "4/9/2006"},
    {"Name": "Jaden Karuletwa", "Birthdate": "1/1/2006"},
    {"Name": "Karter Knox", "Birthdate": "5/16/2005"},
    {"Name": "D.J. Wagner", "Birthdate": "5/4/2005"},
    {"Name": "Elmir Dzafic", "Birthdate": "1/1/2005"},
    {"Name": "Karim Rtail", "Birthdate": "3/23/2004"},
    {"Name": "Trevon Brazile", "Birthdate": "1/7/2003"},
    {"Name": "Malique Ewin", "Birthdate": "1/1/2003"},
    {"Name": "Nick Pringle", "Birthdate": "9/16/2001"},
]

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
            data=df_game_stats,
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
            data=df_game_stats,
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
            data=df_game_stats,
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
            data=df_game_stats,
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
            data=df_game_stats,
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
            data=df_game_stats,
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

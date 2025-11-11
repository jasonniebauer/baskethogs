from datetime import datetime, date
import dash
from dash import html
import dash_mantine_components as dmc


dash.register_page(__name__, path="/", name="Home", title="BasketHogs")

ARKANSAS_RED = "#9D2235"
BLACK = "#000000"
TODAY = date.today()

scoreboard = dmc.Grid(
    pt="7rem",
    pb="5rem",
    justify="center",
    gutter="sm",
    children=[
        dmc.GridCol(
            dmc.Center([
                dmc.Card(
                    mb="xl",
                    children=[
                        dmc.Title(
                            "2",
                            order=1,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                            c="black",  # Color utility
                            ta="center",  # Text align, like .text-center
                            mb="0.25rem",  # Margin bottom
                            fz="6rem",
                            lh=1.0,
                            fw="800",
                        ),
                        dmc.Title(
                            "Total Games",
                            order=4,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                            c="black",  # Color utility
                            ta="center",  # Text align, like .text-center
                            tt="uppercase",  # Uppercase text
                            lh=1.0,
                            fw="800",
                        ),
                        dmc.Title(
                            "Non-Conference",
                            order=6,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                            c="#9D2235",  # Color utility
                            ta="center",  # Text align, like .text-center
                            fw="600",
                        ),
                    ],
                    miw="250",
                    radius="md",
                )
            ]),
            span={"base": 6, "sm": 6, "md": 3},
        ),
        dmc.GridCol(
            dmc.Center([
                dmc.Card(
                    mb="xl",
                    children=[
                        dmc.Title(
                            "1",
                            order=1,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                            c="black",  # Color utility
                            ta="center",  # Text align, like .text-center
                            mb="0.25rem",  # Margin bottom
                            fz="6rem",
                            lh=1.0,
                            fw="800",
                        ),
                        dmc.Title(
                            "Total Wins",
                            order=4,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                            c="black",  # Color utility
                            ta="center",  # Text align, like .text-center
                            tt="uppercase",  # Uppercase text
                            lh=1.0,
                            fw="800",
                        ),
                        dmc.Title(
                            "Non-Conference",
                            order=6,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                            c="#9D2235",  # Color utility
                            ta="center",  # Text align, like .text-center
                            fw="600",
                        ),
                    ],
                    # px="1.5rem",
                    miw="250",
                    radius="md",
                )
            ]),
            span={"base": 6, "sm": 6, "md": 3},
        ),
        dmc.GridCol(
            dmc.Center([
                dmc.Card(
                    mb="xl",
                    children=[
                        dmc.Title(
                            "50%",
                            order=1,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                            c="black",  # Color utility
                            ta="center",  # Text align, like .text-center
                            mb="0.25rem",  # Margin bottom
                            fz="6rem",
                            lh=1.0,
                            fw="800",
                        ),
                        dmc.Title(
                            "Winning Percent",
                            order=4,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                            c="black",  # Color utility
                            ta="center",  # Text align, like .text-center
                            tt="uppercase",  # Uppercase text
                            # mb="md",  # Margin bottom
                            lh=1.0,
                            fw="800",
                        ),
                        dmc.Title(
                            "Win to Loss Ratio",
                            order=6,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                            c="#9D2235",  # Color utility
                            ta="center",  # Text align, like .text-center
                            fw="600",
                        ),
                    ],
                    # px="1.5rem",
                    miw="250",
                    radius="md",
                )
            ]),
            span={"base": 6, "sm": 6, "md": 3},
        ),
        dmc.GridCol(
            dmc.Center([
                dmc.Card(
                    mb="xl",
                    children=[
                        dmc.Title(
                            "L1",
                            order=1,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                            c="black",  # Color utility
                            ta="center",  # Text align, like .text-center
                            mb="0.25rem",  # Margin bottom
                            fz="6rem",
                            lh=1.0,
                            fw="800",
                        ),
                        dmc.Title(
                            "Streak",
                            order=4,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                            c="black",  # Color utility
                            ta="center",  # Text align, like .text-center
                            tt="uppercase",  # Uppercase text
                            # mb="md",  # Margin bottom
                            lh=1.0,
                            fw="800",
                        ),
                        dmc.Title(
                            "Non-Conference",
                            order=6,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                            c="#9D2235",  # Color utility
                            ta="center",  # Text align, like .text-center
                            fw="600",
                        ),
                    ],
                    px="1.5rem",
                    miw="250",
                    radius="md",
                    # withBorder=True,
                )
            ]),
            span={"base": 6, "sm": 6, "md": 3},
        ),
        dmc.GridCol(
            dmc.Center([
                dmc.Card(
                    mb="xl",
                    children=[
                        dmc.Title(
                            "88",
                            order=1,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                            c="black",  # Color utility
                            ta="center",  # Text align, like .text-center
                            mb="0.25rem",  # Margin bottom
                            fz="6rem",
                            lh=1.0,
                            fw="800",
                        ),
                        dmc.Title(
                            "Avg. Points",
                            order=4,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                            c="black",  # Color utility
                            ta="center",  # Text align, like .text-center
                            tt="uppercase",  # Uppercase text
                            # mb="md",  # Margin bottom
                            lh=1.0,
                            fw="800",
                        ),
                        dmc.Title(
                            "Per Game",
                            order=6,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                            c="#9D2235",  # Color utility
                            ta="center",  # Text align, like .text-center
                            fw="600",
                        ),
                    ],
                    px="1.5rem",
                    miw="250",
                    radius="md",
                    # withBorder=True,
                )
            ]),
            span={"base": 6, "sm": 6, "md": 3},
        ),
        dmc.GridCol(
            dmc.Center([
                dmc.Card(
                    mb="xl",
                    children=[
                        dmc.Title(
                            "30",
                            order=1,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                            c="black",  # Color utility
                            ta="center",  # Text align, like .text-center
                            mb="0.25rem",  # Margin bottom
                            fz="6rem",
                            lh=1.0,
                            fw="800",
                        ),
                        dmc.Title(
                            "Avg. Field Goals",
                            order=4,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                            c="black",  # Color utility
                            ta="center",  # Text align, like .text-center
                            tt="uppercase",  # Uppercase text
                            fw="800",
                            # mb="md",  # Margin bottom
                            lh=1.0,
                        ),
                        dmc.Title(
                            "Per Game",
                            order=6,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                            c="#9D2235",  # Color utility
                            ta="center",  # Text align, like .text-center
                            fw="600",
                        ),
                    ],
                    px="1.5rem",
                    miw="250",
                    radius="md",
                )
            ]),
            span={"base": 6, "sm": 6, "md": 3},
        ),
        dmc.GridCol(
            dmc.Center([
                dmc.Card(
                    mb="xl",
                    children=[
                        dmc.Title(
                            "9",
                            order=1,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                            c="black",  # Color utility
                            ta="center",  # Text align, like .text-center
                            mb="0.25rem",  # Margin bottom
                            fz="6rem",
                            lh=1.0,
                            fw="800",
                        ),
                        dmc.Title(
                            "Avg. 3-Pointers",
                            order=4,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                            c="black",  # Color utility
                            ta="center",  # Text align, like .text-center
                            tt="uppercase",  # Uppercase text
                            fw="800",
                            # mb="md",  # Margin bottom
                            lh=1.0,
                        ),
                        dmc.Title(
                            "Per Game",
                            order=6,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                            c="#9D2235",  # Color utility
                            ta="center",  # Text align, like .text-center
                            fw="600",
                        ),
                    ],
                    px="1.5rem",
                    miw="250",
                    radius="md",
                )
            ]),
            span={"base": 6, "sm": 6, "md": 3},
        ),
        dmc.GridCol(
            dmc.Center([
                dmc.Card(
                    mb="xl",
                    children=[
                        dmc.Title(
                            "20",
                            order=1,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                            c="black",  # Color utility
                            ta="center",  # Text align, like .text-center
                            mb="0.25rem",  # Margin bottom
                            fz="6rem",
                            lh=1.0,
                            fw="800",
                        ),
                        dmc.Title(
                            "Avg. Free Throws",
                            order=4,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                            c="black",  # Color utility
                            ta="center",  # Text align, like .text-center
                            tt="uppercase",  # Uppercase text
                            fw="800",
                            # mb="md",  # Margin bottom
                            lh=1.0,
                        ),
                        dmc.Title(
                            "Per Game",
                            order=6,  # Largest: ~2.5rem, bold by default Large. Display Heading (order=1, like .display-1)
                            c="#9D2235",  # Color utility
                            ta="center",  # Text align, like .text-center
                            fw="600",
                        ),
                    ],
                    px="1.5rem",
                    miw="250",
                    radius="md",
                )
            ]),
            span={"base": 6, "sm": 6, "md": 3},
        ),
    ]
)

# scorecard_secondary = dmc.Grid(
#     justify="center",
#     gutter="md",
#     pb="5rem",
#     children=[
        
#     ]
# )

# df_total_wins_over_time = [
#   {"date": "Nov 3", "Total Wins": 1},
#   {"date": "Nov 8", "Total Wins": 1},
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

df_total_points_over_time = [
  {"date": "Nov 3", "Arkansas Points": 109, "Opponent Points": 77},
  {"date": "Nov 8", "Arkansas Points": 66, "Opponent Points": 69},
]

total_points_over_time = dmc.Card(
    radius="md",
    bd="1px solid #C7C8CA",
    mb="5rem",
    children=[
        dmc.Title(
            "Total Points Over Time",
            order=1,
            # mb="xl",
        ),
        dmc.Title(
            "The total points scored per game.",
            order=5,
            mb="xl",
            fw="500",
        ),
        dmc.LineChart(
            h=300,
            dataKey="date",
            data=df_total_points_over_time,
            series = [
                {"name": "Arkansas Points", "color": ARKANSAS_RED},
                {"name": "Opponent Points", "color": "#000000"},
            ],
            curveType="linear",
            tickLine="y",
            # withXAxis=False,
            mb="sm",
            pr="1rem",
            withLegend=True,
        ),
    ]
)

df_count_points_by_type = [
    {"date": "Nov 3", "2-Pointers": 27, "3-Pointers": 10, "Free Throws": 25},
    {"date": "Nov 8", "2-Pointers": 15, "3-Pointers": 7, "Free Throws": 15},
]

count_points_by_type = dmc.Card(
    radius="md",
    bd="1px solid #C7C8CA",
    mb="5rem",
    children=[
        dmc.Title(
            "Number of Points by Type",
            order=1,
            # mb="xl",
        ),
        dmc.Title(
            "The total number of points for each type.",
            order=5,
            mb="xl",
            fw="500",
        ),
        dmc.BarChart(
            h=300,
            dataKey="date",
            data=df_count_points_by_type,
            series=[
                {"name": "2-Pointers", "color": ARKANSAS_RED},
                {"name": "3-Pointers", "color": "black"},
                {"name": "Free Throws", "color": "#C7C8CA"}
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

df_totals_points_by_type = [
    {"date": "Nov 3", "2-Pointers": 54, "3-Pointers": 30, "Free Throws": 25},
    {"date": "Nov 8", "2-Pointers": 30, "3-Pointers": 21, "Free Throws": 15},
]

totals_points_by_type = dmc.Card(
    radius="md",
    bd="1px solid #C7C8CA",
    mb="5rem",
    children=[
        dmc.Title(
            "Total Points by Type",
            order=1,
            # mb="xl",
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
            data=df_totals_points_by_type,
            type="stacked",
            series=[
                {"name": "2-Pointers", "color": ARKANSAS_RED},
                {"name": "3-Pointers", "color": "black"},
                {"name": "Free Throws", "color": "#C7C8CA"}
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

df_point_type_by_percent_of_total = [
    {"date": "Nov 3", "2-Pointers": 49.5, "3-Pointers": 27.5, "Free Throws": 22.9},
    {"date": "Nov 8", "2-Pointers": 45.4, "3-Pointers": 31.8, "Free Throws": 22.7},
]

point_type_by_percent_of_total = dmc.Card(
    radius="md",
    bd="1px solid #C7C8CA",
    mb="5rem",
    children=[
        dmc.Title(
            "Point % of Total Points",
            order=1,
            # mb="xl",
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
            data=df_point_type_by_percent_of_total,
            type="percent",
            series=[
                {"name": "2-Pointers", "label": "2-Pointer %", "color": ARKANSAS_RED},
                {"name": "3-Pointers", "label": "3-Pointer %", "color": "black"},
                {"name": "Free Throws", "label": "Free Throw %", "color": "#C7C8CA"}
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

df_points_gap_over_time = [
  {"date": "Nov 3", "Point Gap": 32},
  {"date": "Nov 8", "Point Gap": 3},
]

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
        dmc.LineChart(
            h=300,
            dataKey="date",
            data=df_points_gap_over_time,
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

# df_player_age = [
#     {"Player": "Jaden Karuletwa", "Age": 19, "Year": "Sophomore"},
#     {"Player": "Meleek Thomas", "Age": 19, "Year": "Freshman"},
#     {"Player": "Amere Brown", "Age": 19, "Year": "Freshman"},
#     {"Player": "Darius Acuff Jr.", "Age": 18, "Year": "Freshman"},
#     {"Player": "Trevon Brazile", "Age": 22, "Year": "Senior"},
#     {"Player": "Karter Knox", "Age": 20, "Year": "Sophomore"},
#     {"Player": "Malique Ewin", "Age": 22, "Year": "Senior"},
#     {"Player": "Ayden Kelley", "Age": 19, "Year": "Sophomore"},
#     {"Player": "Elmir Džafić", "Age": 20, "Year": "Freshman"},
#     {"Player": "D.J. Wagner", "Age": 20, "Year": "Junior"},
#     {"Player": "Nick Pringle", "Age": 24, "Year": "Senior"},
#     {"Player": "Billy Richmond III", "Age": 19, "Year": "Junior"},
#     {"Player": "Isaiah Sealy", "Age": 18, "Year": "Freshman"},
#     {"Player": "Karim Rtail", "Age": 21, "Year": "Freshman"},
#     {"Player": "Paulo Semedo", "Age": 19, "Year": "Freshman"},
# ]

# player_age = dmc.Card(
#     radius="md",
#     bd="1px solid #C7C8CA",
#     mb="5rem",
#     children=[
#         dmc.Title(
#             "Total Wins Over Time",
#             order=1,
#             mb="xl",
#         ),
#         dmc.BubbleChart(
#             gridColor="gray.5",
#             textColor="gray.9",
#             h=60,
#             data=data,
#             range=[16, 225],
#             label="Sales/hour",
#             color="lime.6",
#             dataKey={"x": "hour", "y": "index", "z": "value"}
#         )
#     ]
# )

def player_card(player_stats_data, radar_data):
    # name, position, year, height, weight, age, number, 

    # Remove space characters and periods
    name_formatted_for_headshot = player_stats_data['Name'].replace(" ", "-").replace(".", "")

    # Convert the player's birthdate string to a date
    birthdate = datetime.strptime(player_stats_data['Birthdate'], "%m/%d/%Y").date()
    # Get the player's age based on their date of birth
    age = TODAY.year - birthdate.year - ((TODAY.month, TODAY.day) < (birthdate.month, birthdate.day))
    
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
                                    # mb="0.25rem",
                                    # style={"border": "2px solid #424242"}
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
                                    player_stats_data['FG'],
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
                                    player_stats_data['3P'],
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
                                    player_stats_data['FT'],
                                    ta="right",
                                ),
                            ]),
                        ])
                    ]
                )
            ]
        ),
        span={"base": 12, "sm": 6, "md": 6, "lg": 4},
        # miw="440",
        # maw="440",
    )

darius_acuff_jr_stats = {
    "Name": "Darius Acuff Jr.",
    "Position": "Guard",
    "Year": "Freshman",
    "Height": "6' 3\"",
    "Weight": "190",
    "Birthdate": "11/16/2006",
    "Number": "5",
    "Season High": "22",
    "Games Played": "2",
    "PPG": "19",
    "FG": "45",
    "3P": "39",
    "FT": "70",
}

darius_acuff_jr_radar = [
    {"stat": "Field Goals", "count": 7},
    {"stat": "3-Pointers", "count": 3},
    {"stat": "Free Thows", "count": 4},
    {"stat": "Off. Rebounds", "count": 1},
    {"stat": "Def. Rebounds", "count": 1},
    {"stat": "Assists", "count": 5},
    {"stat": "Turnovers", "count": 2},
    {"stat": "Steals", "count": 2},
]

meleek_thomas_stats = {
    "Name": "Meleek Thomas",
    "Position": "Forward",
    "Year": "Freshman",
    "Height": "6' 5\"",
    "Weight": "185",
    "Birthdate": "8/6/2006",
    "Number": "1",
    "Season High": "21",
    "Games Played": "2",
    "PPG": "19",
    "FG": "40",
    "3P": "32",
    "FT": "88",
}

meleek_thomas_radar = [
    {"stat": "Field Goals", "count": 6},
    {"stat": "3-Pointers", "count": 3},
    {"stat": "Free Thows", "count": 4},
    {"stat": "Off. Rebounds", "count": 3},
    {"stat": "Def. Rebounds", "count": 3},
    {"stat": "Assists", "count": 5},
    {"stat": "Turnovers", "count": 2},
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
    "Season High": "8",
    "Games Played": "2",
    "PPG": "7",
    "FG": "67",
    "3P": "0",
    "FT": "50",
}

nick_pringle_radar = [
    {"stat": "Field Goals", "count": 3},
    {"stat": "3-Pointers", "count": 0},
    {"stat": "Free Thows", "count": 1},
    {"stat": "Off. Rebounds", "count": 4},
    {"stat": "Def. Rebounds", "count": 4},
    {"stat": "Assists", "count": 1},
    {"stat": "Turnovers", "count": 1},
    {"stat": "Steals", "count": 1},
]

trevon_brazile_stats = {
    "Name": "Trevon Brazile",
    "Position": "Forward",
    "Year": "Senior",
    "Height": "6' 10\"",
    "Weight": "230",
    "Birthdate": "1/7/2003",
    "Number": "7",
    "Season High": "25",
    "Games Played": "2",
    "PPG": "14",
    "FG": "47",
    "3P": "20",
    "FT": "75",
}

trevon_brazile_radar = [
    {"stat": "Field Goals", "count": 5},
    {"stat": "3-Pointers", "count": 1},
    {"stat": "Free Thows", "count": 5},
    {"stat": "Off. Rebounds", "count": 1},
    {"stat": "Def. Rebounds", "count": 6},
    {"stat": "Assists", "count": 1},
    {"stat": "Turnovers", "count": 2},
    {"stat": "Steals", "count": 1},
]

karter_knox_stats = {
    "Name": "Karter Knox",
    "Position": "Wing",
    "Year": "Sophomore",
    "Height": "6' 6\"",
    "Weight": "220",
    "Birthdate": "5/16/2005",
    "Number": "1",
    "Season High": "0",
    "Games Played": "1",
    "PPG": "0",
    "FG": "0",
    "3P": "0",
    "FT": "0",
}

karter_knox_radar = [
    {"stat": "Field Goals", "count": 0},
    {"stat": "3-Pointers", "count": 0},
    {"stat": "Free Thows", "count": 0},
    {"stat": "Off. Rebounds", "count": 0},
    {"stat": "Def. Rebounds", "count": 4},
    {"stat": "Assists", "count": 4},
    {"stat": "Turnovers", "count": 4},
    {"stat": "Steals", "count": 1},
]

jaden_karuletwa_stats = {
    "Name": "Jaden Karuletwa",
    "Position": "Guard",
    "Year": "Sophomore",
    "Height": "6' 4\"",
    "Weight": "195",
    "Birthdate": "1/1/2006",
    "Number": "0",
    "Season High": "0",
    "Games Played": "1",
    "PPG": "0",
    "FG": "0",
    "3P": "0",
    "FT": "0",
}

jaden_karuletwa_radar = [
    {"stat": "Field Goals", "count": 0},
    {"stat": "3-Pointers", "count": 0},
    {"stat": "Free Thows", "count": 0},
    {"stat": "Off. Rebounds", "count": 0},
    {"stat": "Def. Rebounds", "count": 1},
    {"stat": "Assists", "count": 1},
    {"stat": "Turnovers", "count": 0},
    {"stat": "Steals", "count": 0},
]

amere_brown_stats = {
    "Name": "Amere Brown",
    "Position": "Guard",
    "Year": "Freshman",
    "Height": "5' 9\"",
    "Weight": "180",
    "Birthdate": "5/22/2006",
    "Number": "2",
    "Season High": "0",
    "Games Played": "1",
    "PPG": "0",
    "FG": "0",
    "3P": "0",
    "FT": "0",
}

amere_brown_radar = [
    {"stat": "Field Goals", "count": 0},
    {"stat": "3-Pointers", "count": 0},
    {"stat": "Free Thows", "count": 0},
    {"stat": "Off. Rebounds", "count": 0},
    {"stat": "Def. Rebounds", "count": 0},
    {"stat": "Assists", "count": 0},
    {"stat": "Turnovers", "count": 0},
    {"stat": "Steals", "count": 0},
]

malique_ewin_stats = {
    "Name": "Malique Ewin",
    "Position": "Forward",
    "Year": "Senior",
    "Height": "6' 10\"",
    "Weight": "240",
    "Birthdate": "1/1/2003",
    "Number": "12",
    "Season High": "6",
    "Games Played": "2",
    "PPG": "5",
    "FG": "67",
    "3P": "0",
    "FT": "100",
}

malique_ewin_radar = [
    {"stat": "Field Goals", "count": 2},
    {"stat": "3-Pointers", "count": 0},
    {"stat": "Free Thows", "count": 1},
    {"stat": "Off. Rebounds", "count": 3},
    {"stat": "Def. Rebounds", "count": 1},
    {"stat": "Assists", "count": 0},
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
    "Season High": "0",
    "Games Played": "1",
    "PPG": "0",
    "FG": "0",
    "3P": "0",
    "FT": "0",
}

ayden_kelley_radar = [
    {"stat": "Field Goals", "count": 0},
    {"stat": "3-Pointers", "count": 0},
    {"stat": "Free Thows", "count": 0},
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
    "Games Played": "1",
    "PPG": "1",
    "FG": "0",
    "3P": "0",
    "FT": "50",
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
    "Season High": "13",
    "Games Played": "2",
    "PPG": "11",
    "FG": "41",
    "3P": "36",
    "FT": "75",
}

dj_wagner_radar = [
    {"stat": "Field Goals", "count": 4},
    {"stat": "3-Pointers", "count": 2},
    {"stat": "Free Thows", "count": 2},
    {"stat": "Off. Rebounds", "count": 0},
    {"stat": "Def. Rebounds", "count": 3},
    {"stat": "Assists", "count": 5},
    {"stat": "Turnovers", "count": 2},
    {"stat": "Steals", "count": 3},
]

billy_richmond_stats = {
    "Name": "Billy Richmond III",
    "Position": "Wing",
    "Year": "Junior",
    "Height": "6' 6\"",
    "Weight": "205",
    "Birthdate": "4/11/2006",
    "Number": "24",
    "Season High": "8",
    "Games Played": "2",
    "PPG": "7",
    "FG": "42",
    "3P": "17",
    "FT": "75",
}

billy_richmond_radar = [
    {"stat": "Field Goals", "count": 3},
    {"stat": "3-Pointers", "count": 1},
    {"stat": "Free Thows", "count": 2},
    {"stat": "Off. Rebounds", "count": 1},
    {"stat": "Def. Rebounds", "count": 4},
    {"stat": "Assists", "count": 1},
    {"stat": "Turnovers", "count": 2},
    {"stat": "Steals", "count": 0},
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
    "Games Played": "2",
    "PPG": "6",
    "FG": "50",
    "3P": "0",
    "FT": "100",
}

isaiah_sealy_radar = [
    {"stat": "Field Goals", "count": 2},
    {"stat": "3-Pointers", "count": 0},
    {"stat": "Free Thows", "count": 3},
    {"stat": "Off. Rebounds", "count": 1},
    {"stat": "Def. Rebounds", "count": 1},
    {"stat": "Assists", "count": 1},
    {"stat": "Turnovers", "count": 0},
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
    "FG": "0",
    "3P": "0",
    "FT": "0",
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
    "FG": "0",
    "3P": "0",
    "FT": "0",
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

player_stats_headline = dmc.Title(
    "Player Stats",
    order=1,
    ta="center",
    py="2rem",
)

players = dmc.Grid(
    justify="center",
    gutter="md",
    mb="sm",
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
        scoreboard,
        # total_wins_over_time,
        total_points_over_time,
        count_points_by_type,
        totals_points_by_type,
        point_type_by_percent_of_total,
        points_gap_over_time,
        # player_age,
        player_stats_headline,
        players,
    ]
)

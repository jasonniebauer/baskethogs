import dash
from dash import html
import dash_mantine_components as dmc


dash.register_page(__name__, path="/about", name="About", title="About BasketHogs")

layout = dmc.Box(
    children=[
        dmc.Title(
            "About",
            order=1,
            ta="center",
            py="2rem",
        ),
        dmc.Text([
            "BasketHogs is a analytics hub for measuring the performance of the Arkansas Razorback men's basketball team across the 2025-2026 season. BasketHogs started as a weekend project by ",
            dmc.Anchor(
                "Jason Niebauer",
                href="https://www.linkedin.com/in/jasonniebauer/",
                target="_blank",
                c="#9D2235",
            ),
            " to track and chart performance, and soon grew to be a full website providing insights on the team's overall success as well as individual player stats.",
            html.Br(),
            html.Br(),
            "BasketHogs is updated after every game as soon as the data becomes available and is compiled. Charts will continue to grow and expand throughout the season, and player stats will become more balanced as the players spend time on the court.",
            html.Br(),
            html.Br(),
            "Follow ",
            dmc.Anchor(
                "BasketHogs on Twitter(X)",
                href="https://x.com/baskethogs",
                # target="_blank",
                c="#9D2235",
            ),
            " and subscribe for:",
            dmc.List(
                [
                    dmc.ListItem("Game day notifications"),
                    dmc.ListItem("Website updates"),
                    dmc.ListItem("If you're a fan of the Arkansas Razorbacks"),
                ]
            ),
            html.Br(),
            html.Br(),
            "Have questions or feedback? Send a message to ",
            dmc.Anchor(
                "BasketHogs on Twitter(X)",
                href="https://x.com/baskethogs",
                # target="_blank",
                c="#9D2235",
            ),
            ".",
            html.Br(),
            html.Br(),
            dmc.Text("Go Hogs!", fw=700)
        ],
        maw=670,
        mx="auto",
        ),
    ]
)

import dash
from dash import html
import dash_mantine_components as dmc
from dash_iconify import DashIconify


dash.register_page(__name__, path="/about", name="About", title="About BasketHogs")

ARKANSAS_RED = "#9D2235"

layout = dmc.Box(
    mb="5rem",
    children=[
        dmc.Title(
            "About",
            order=1,
            ta="center",
            py="2rem",
        ),
        dmc.Text([
            "BasketHogs is an analytics hub for measuring the performance of the Arkansas Razorback men's basketball team across the 2025-2026 season. BasketHogs started as a weekend project by ",
            dmc.Anchor(
                "Jason Niebauer",
                href="https://www.linkedin.com/in/jasonniebauer/",
                target="_blank",
                c=ARKANSAS_RED,
            ),
            " to track and chart performance in a spreadsheet, and soon grew to a full website providing insights on the team's overall success as well as individual player stats.",
            html.Br(),
            html.Br(),
            "BasketHogs is updated after every game as soon as the data becomes available and is compiled. Charts will continue to grow and expand throughout the season, and player stats will become more balanced as the players spend time on the court.",
            html.Br(),
            html.Br(),
            "Follow ",
            dmc.Anchor(
                "BasketHogs on Twitter(X)",
                href="https://x.com/baskethogs",
                c=ARKANSAS_RED,
            ),
            " and subscribe for:",
            dmc.List(
                [
                    dmc.ListItem("Game day notifications"),
                    dmc.ListItem("Website updates"),
                    dmc.ListItem("If you're a fan of the Arkansas Razorbacks"),
                ],
            ),
            html.Br(),
            dmc.Box(
                bg="#F2F2F4",
                bd="1px solid #C7C8CA",
                style={"borderRadius": "0.375rem"},
                p="1rem",
                ta="center",
                children=[
                dmc.Text("Want to support BasketHogs?", fw=500, mb="0.75rem", lh=1.0),
                dmc.Anchor(
                    dmc.Button(
                        "Buy me a coffee",
                        variant="filled",
                        color=ARKANSAS_RED,
                        size="sm",
                        radius="sm",
                        loading=False,
                        disabled=False,
                    ),
                    href="https://buymeacoffee.com/baskethogs",
                    c=ARKANSAS_RED,
                    target="_blank",
                    fw=500,
                ),
            ]),
            html.Br(),
            html.Br(),
            "Have questions or feedback? Send a message to ",
            dmc.Anchor(
                "BasketHogs on Twitter (X)",
                href="https://x.com/baskethogs",
                c=ARKANSAS_RED,
            ),
            html.Br(),
            html.Br(),
            html.Br(),
            dmc.Anchor(
                children=dmc.Group(
                    [
                        DashIconify(icon="mdi:arrow-left", width=18),  # Back arrow icon (Material Design Icons)
                        dmc.Text("Back to home"),  # The text after the icon
                    ],
                    gap="0.5rem",
                    align="center",
                ),
                href="/",
                c=ARKANSAS_RED,
            )
        ],
        maw=670,
        mx="auto",
        ),
    ]
)

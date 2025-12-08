from dash import Dash, html, page_container
import dash_mantine_components as dmc
from dash_iconify import DashIconify


# Google Analytics Measurement ID
GA_MEASUREMENT_ID = 'G-ZD0QG42GY9'

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&family=Oxanium:wght@200..800&display=swap",
        "rel": "stylesheet"
    },
    "custom.css",
]

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True, external_stylesheets=external_stylesheets)

APP_LAST_UPDATED = "Dec 7, 2025"

# Google analytics
app.index_string = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <!-- Global site tag (gtag.js) - Google Analytics -->
            <script async src="https://www.googletagmanager.com/gtag/js?id={GA_MEASUREMENT_ID}"></script>
            <script>
                window.dataLayer = window.dataLayer || [];
                function gtag(){{dataLayer.push(arguments);}}
                gtag('js', new Date());
                gtag('config', '{GA_MEASUREMENT_ID}');
            </script>
            {{%metas%}}
            <title>{{%title%}}</title>
            {{%favicon%}}
            {{%css%}}
            <script data-name="BMC-Widget" data-cfasync="false" src="https://cdnjs.buymeacoffee.com/1.0.0/widget.prod.min.js" data-id="baskethogs" data-description="Support me on Buy me a coffee!" data-message="" data-color="#FF813F" data-position="Right" data-x_margin="18" data-y_margin="18"></script>
        </head>
        <body>
            {{%app_entry%}}
            <footer>
                {{%config%}}
                {{%scripts%}}
                {{%renderer%}}
            </footer>
        </body>
    </html>
    """

navbar = dmc.Flex(
    justify="flex-start",
    align="center",
    direction="row",
    wrap="wrap",
    py="1.25rem",
    style={
        "backdropFilter": "blur(0.5px)",
    },
    children=[
        dmc.Flex(
            justify="flex-start",
            align="flex-start",
            direction="row",
            wrap="wrap",
            children=[
                dmc.Image(
                    h=37,
                    w="auto",
                    fit="contain",
                    src="/assets/basketball-icon128.png",
                    mr="0.375rem"
                ),
                dmc.Anchor(
                    href="/",
                    underline="never",
                    children=[
                        dmc.Title(
                            "BasketHogs",
                            order=1,
                            c="white",  # Color utility
                            mb=0,
                            lh=1.0,
                            style={
                                "textShadow": "1px 1px 3px black",
                            },
                        ),
                        dmc.Title(
                            "Fan-powered analytics hub",
                            order=6,
                            c="white",  # Color utility
                            fw=400,
                            fz="0.6875rem",
                            lh=0.96,
                            style={
                                "textShadow": "1px 1px 3px black",
                            },
                        ),
                    ]
                ),
            ]
        ),
        dmc.Flex(
            ml="auto",
            children=[
                dmc.Anchor(
                    dmc.Button(
                        "About",
                        variant="white",
                        color="black",
                        size="xs",
                        mr="1rem",
                        style={
                            "boxShadow": "5px 5px 10px 2px rgba(0, 0, 0, 0.6)"
                        }
                    ),
                    href="/about",
                    underline="never",
                ),
                dmc.Anchor(
                    dmc.Button(
                        "Twitter",
                        variant="white",
                        color="black",
                        size="xs",
                        rightSection=DashIconify(icon="logos:x"),
                        styles={
                            "section": {
                                "marginInlineStart": "0.375rem"
                            }
                        }
                    ),
                    href="https://x.com/baskethogs",
                    underline="never",
                ),
            ]
        )
        
    ]
)

header = dmc.Box(
    px="1rem",
    # mb="2rem",
    style={
        "backgroundImage": "linear-gradient(rgba(0, 0, 0, 0.375), rgba(0, 0, 0, 0.25)), url('/assets/bwa-packed-arena.png')",
        "backgroundSize": "cover",
        "backgroundPosition": "center center"
    },
    children=[
        navbar,
        dmc.Flex(
            justify="center",
            align="center",
            direction="column",
            wrap="wrap",
            pt={"base": "7rem", "lg": "10rem"},
            pb={"base": "3rem", "lg": "4rem"},
            style={
                "backdropFilter": "blur(0.5px)",
            },
            children=[
                dmc.Title(
                    "Arkansas Razorbacks",
                    order=1,
                    c="white",  # Color utility
                    ta="center",  # text align center
                    lh=1.0,  # line height 1
                    mb="sm",  # margin-bottom
                    fz={
                        "base": "4rem",  # mobile ≤576px
                        "sm": "5rem",  # ≥768px
                        "md": "7rem",  # ≥992px
                        "lg": "7rem",  # ≥1200px
                        "xl": "7rem"  # ≥1440px
                    },
                    style={
                        "textShadow": "1px 1px 47px black",
                    }
                ),
                dmc.Title(
                    f"Men's Basketball 2025-2026 • Last Updated {APP_LAST_UPDATED}",
                    order=6,
                    c="white",
                    fw=500,
                    bg="black",
                    p="0.375rem 0.75rem",
                    style={"borderRadius": "0.375rem"},
                    fz={"base": "0.75rem", "sm": "0.75rem", "md": "0.875rem"},
                ),
            ]
        )
    ]
)

footer = dmc.Group(
    align="center",   # vertical alignment
    pt="2.5rem",
    mb="1.25rem",
    justify="space-between",
    mt="auto",
    children=[
        dmc.Anchor(
            "Source",
            c="black",
            href="https://arkansasrazorbacks.com/sport/m-baskbl/",
            underline="never",
            fw=500
        ),
        dmc.Text(
            "© 2025 BasketHogs",
            # ml="auto",
        ),
    ]
)

app.layout = html.Div([
    # Favicon
    html.Link(
        rel="icon",
        href="/assets/favicon.ico",
        type="image/x-icon"
    ),
    dmc.MantineProvider(
        theme= {
        "fontFamily": 'Inter',
        "headings": { "fontFamily": "Inter, Arial, sans-serif" },
        },
        children=[
            header,
            dmc.Container(
                fluid=True,  # Makes it full-width
                style={
                    "minHeight": "100vh",
                    "display": "flex",          # Added: Enables flexbox
                    "flexDirection": "column",  # Added: Vertical stacking (page > footer)
                },
                children=[
                    # page_container,
                    # footer
                    # Main content (grows to fill space)
                    html.Div(
                        style={"flex": "1"},  # Added: Expands page_container
                        children=page_container,  # Dash injects multi-page content here
                    ),
                    footer,  # Pushed to bottom by flex:1 above
                ],
            ),
        ]
    )
])

if __name__ == "__main__":
    app.run(debug=True)


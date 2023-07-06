from textual.app import App, ComposeResult
from textual.widgets import Header, Footer


class QuoteaApp(App):
    """
    A Textual app to manage books & quotes.
    """

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()


if __name__ == "__main__":
    app = QuoteaApp()
    app.run()

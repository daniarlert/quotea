from textual.app import App, ComposeResult
from textual.widgets import Footer, Tabs, DataTable

BOOK_ROWS = [
    ("title", "author", "start_date", "end_date"),
    ("1984", "George Orwell", "1949-06-08", "1949-06-08"),
    ("To Kill a Mockingbird", "Harper Lee", "1960-07-11", "1960-07-11"),
    ("The Great Gatsby", "F. Scott Fitzgerald", "1925-04-10", "1925-04-10"),
    ("Pride and Prejudice", "Jane Austen", "1813-01-28", "1813-01-28"),
    ("The Catcher in the Rye", "J.D. Salinger", "1951-07-16", "1951-07-16"),
    ("Moby-Dick", "Herman Melville", "1851-10-18", "1851-10-18"),
    ("To the Lighthouse", "Virginia Woolf", "1927-05-05", "1927-05-05"),
    ("Brave New World", "Aldous Huxley", "1932-01-01", "1932-01-01"),
    ("The Lord of the Rings", "J.R.R. Tolkien", "1954-07-29", "1955-10-20"),
    ("The Chronicles of Narnia", "C.S. Lewis", "1950-10-16", "1956-01-04"),
]

QUOTE_ROWS = [
    ("book", "quote", "favorite"),
    ("1984", "Big Brother is watching you.", True),
    (
        "To Kill a Mockingbird",
        "You never really understand a person until you consider things from his point of view... Until you climb inside of his skin and walk around in it.",
        True,
    ),
    (
        "The Great Gatsby",
        "So we beat on, boats against the current, borne back ceaselessly into the past.",
        False,
    ),
    (
        "Pride and Prejudice",
        "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.",
        True,
    ),
    (
        "The Catcher in the Rye",
        "I'm sick of just liking people. I wish to God I could meet somebody I could respect.",
        False,
    ),
]


class QuoteaApp(App):
    """
    A Textual app to manage books & quotes.
    """

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Tabs("Books", "Quotes")
        yield DataTable()
        yield Footer()

    def on_mount(self) -> None:
        self.query_one(Tabs).focus()

    def on_tabs_tab_activated(self, event: Tabs.TabActivated) -> None:
        table = self.query_one(DataTable)
        if event.tab is None:
            table.visible = False
        else:
            table.clear()
            table.visible = True
            table.zebra_stripes = True
            table.cursor_type = "row"

            table.add_columns(*BOOK_ROWS[0])
            table.add_rows(BOOK_ROWS[1:])


if __name__ == "__main__":
    app = QuoteaApp()
    app.run()

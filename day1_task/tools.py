
"""Private book collection and tools for the Personal Library Assistant."""

BOOKS = [
    {"title": "The Hobbit", "author": "J.R.R. Tolkien",
     "genre": "Fantasy", "pages": 310, "status": "Read"},
    {"title": "A Game of Thrones", "author": "George R.R. Martin",
     "genre": "Fantasy", "pages": 694, "status": "Unread"},
    {"title": "The Name of the Wind", "author": "Patrick Rothfuss",
     "genre": "Fantasy", "pages": 662, "status": "Currently Reading"},
    {"title": "The Ocean at the End of the Lane", "author": "Neil Gaiman",
     "genre": "Fantasy", "pages": 181, "status": "Unread"},
    {"title": "The Midnight Library", "author": "Matt Haig",
     "genre": "Fiction", "pages": 288, "status": "Unread"},
    {"title": "The Silent Patient", "author": "Alex Michaelides",
     "genre": "Mystery", "pages": 336, "status": "Unread"},
    {"title": "Gone Girl", "author": "Gillian Flynn",
     "genre": "Mystery", "pages": 422, "status": "Read"},
    {"title": "Atomic Habits", "author": "James Clear",
     "genre": "Self-Help", "pages": 320, "status": "Currently Reading"},
]


def search_books(genre=None, max_pages=None, unread_only=False):
    """Search books by genre, page limit, and reading status."""
    results = BOOKS

    if genre:
        results = [
            b for b in results
            if genre.lower() in b["genre"].lower()
        ]

    if max_pages is not None:
        results = [b for b in results if b["pages"] <= max_pages]

    if unread_only:
        results = [b for b in results if b["status"] == "Unread"]

    if not results:
        return "No books matched those filters."

    return "\n".join(
        f'{b["title"]} by {b["author"]} | {b["genre"]} | '
        f'{b["pages"]} pages | {b["status"]}'
        for b in results
    )


def get_reading_status(title):
    """Look up a book's reading status."""
    for book in BOOKS:
        if book["title"].lower() == title.lower():
            return f'{book["title"]}: {book["status"]}'

    return f"Book not found: {title}"


def update_reading_status(title, status):
    """Update a book's reading status."""
    allowed = ["Unread", "Currently Reading", "Read"]

    if status not in allowed:
        return f"Invalid status. Choose from: {', '.join(allowed)}"

    for book in BOOKS:
        if book["title"].lower() == title.lower():
            book["status"] = status
            return f'Updated "{book["title"]}" to {status}.'

    return f"Book not found: {title}"


# Tool definitions provided to the LLM
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_books",
            "description": (
                "Search the private book collection by genre, "
                "maximum pages, or unread status."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "genre": {"type": "string"},
                    "max_pages": {"type": "integer"},
                    "unread_only": {"type": "boolean"}
                },
                "required": [],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_reading_status",
            "description": "Get the reading status of a specific book.",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"}
                },
                "required": ["title"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_reading_status",
            "description": "Update a book's reading status.",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "status": {
                        "type": "string",
                        "enum": ["Unread", "Currently Reading", "Read"]
                    }
                },
                "required": ["title", "status"],
                "additionalProperties": False
            }
        }
    }
]

TOOL_FUNCTIONS = {
    "search_books": search_books,
    "get_reading_status": get_reading_status,
    "update_reading_status": update_reading_status
}


if __name__ == "__main__":
    print("Unread fantasy books under 400 pages:")
    print(search_books(
        genre="Fantasy", max_pages=400, unread_only=True
    ))

    print("\nReading status:")
    print(get_reading_status("The Hobbit"))

    print("\nUpdating reading status:")
    print(update_reading_status(
        "The Midnight Library", "Currently Reading"
    ))
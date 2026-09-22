
from tools import (
    search_books,
    get_reading_status,
    update_reading_status,
    BOOKS,
)


def run_workflow(question):
    question_lower = question.lower()

    # Question 1: Check reading status
    if "read the hobbit" in question_lower:
        status = get_reading_status("The Hobbit")
        return f"The Hobbit reading status: {status}"

    # Question 2: Find an unread fantasy book under 400 pages
    elif "fantasy" in question_lower and "400" in question_lower:
        books = search_books(
            genre="Fantasy",
            max_pages=400,
            unread_only=True
        )

        if books:
            return f"Unread fantasy books under 400 pages: {books}"
        return "No matching books found."

    # Question 3: Mark The Midnight Library as currently reading
    elif "midnight library" in question_lower:
        result = update_reading_status(
            "The Midnight Library",
            "Currently Reading"
        )
        return result

    # Question 4: Find an unread mystery book and recommend one
    elif "mystery" in question_lower:
        books = search_books(
            genre="Mystery",
            unread_only=True
        )

        if books:
            return f"Unread mystery books: {books}. I recommend starting with The Silent Patient."

    else:
        return "Sorry, this workflow cannot handle that question."


if __name__ == "__main__":
    print("SYSTEM 2: RULE-BASED WORKFLOW\n")

    for question in [
        "Have I read The Hobbit?",
        "Find an unread fantasy book under 400 pages.",
        "Mark The Midnight Library as currently reading.",
        "Find an unread mystery book and recommend one."
    ]:
        print(f"\nQuestion: {question}")
        print(f"Answer: {run_workflow(question)}")
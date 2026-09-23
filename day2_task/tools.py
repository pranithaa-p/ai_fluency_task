"""Mock travel-data tools for the Switzerland trip."""

TRAVEL_DATA = {
    "flight": {
        "name": "Round-trip flight",
        "price": 45000,
        "unit": "per student"
    },
    "hotel": {
        "name": "Hotel accommodation",
        "price": 8000,
        "unit": "per student per night"
    },
    "food": {
        "name": "Food",
        "price": 2500,
        "unit": "per student per day"
    },
    "transport": {
        "name": "Local transport",
        "price": 12000,
        "unit": "per student for 7 days"
    }
}


def lookup_travel_cost(category):
    """Retrieve fictional travel cost data."""
    category = category.lower().strip()

    if category not in TRAVEL_DATA:
        return {"error": f"Unknown category: {category}"}

    return TRAVEL_DATA[category]


def calculate_trip_budget(
    students,
    days,
    flight,
    hotel_per_night,
    food_per_day,
    transport
):
    """Calculate individual and group trip costs."""

    hotel_total = hotel_per_night * days
    food_total = food_per_day * days

    per_student = (
        flight + hotel_total + food_total + transport
    )

    return {
        "hotel_total_per_student": hotel_total,
        "food_total_per_student": food_total,
        "total_per_student": per_student,
        "total_for_group": per_student * students
    }


TOOL_FUNCTIONS = {
    "lookup_travel_cost": lookup_travel_cost,
    "calculate_trip_budget": calculate_trip_budget
}
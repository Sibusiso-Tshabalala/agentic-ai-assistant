from api.hotel_api import search_hotels

def hotel_agent(params):
    print("[Hotel Agent] Searching for hotels...")
    city = params.get("destination", "CPT")
    checking = params.get("departure_date")
    checkout = params.get("return_date")

    hotels = search_hotels(city, checking, checkout)
    if hotels:
        selected = hotels[0]
        return {
            "status": "success",
            "hotel_details": selected
        }
    return {
        "status": "error",
        "message": "No hotels found"
    }

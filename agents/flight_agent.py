
from api.flight_api import search_flights

def flight_agent(params):
    print("[Flight Agent] Searching for flights...")
    flights = search_flights(
        origin=params['origin'],
        destination=params['destination'],
        departure_date=params['departure_date'],
        return_date=params.get('return_date')
    )
    if flights:
        best = flights[0]
        params['flight_details'] = best
        return params
    return {"status": "error", "message": "No flights found"}
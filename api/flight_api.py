from amadeus import Client, ResponseError
import os
from dotenv import load_dotenv

load_dotenv()

amadeus = Client(
    client_id=os.getenv("AMADEUS_API_KEY"),
    client_secret=os.getenv("AMADEUS_API_SECRET")
)

def search_flights(origin, destination, departure_date, return_date=None, adults=1):
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin,
            destinationLocationCode=destination,
            departureDate=departure_date,
            returnDate=return_date,
            adults=adults,
            max=1
        )
        return response.data
    except ResponseError as e:
        print("[Amadeus Error]", e)
        return []

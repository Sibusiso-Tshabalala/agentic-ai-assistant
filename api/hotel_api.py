def search_hotels(city, checking_date, checkout_date, stars=4, near=None):
    # Simulated hotel results
    dummy_hotels = [
        {
            "name": "Ocean View Hotel",
            "location": "Beachside",
            "stars": 4,
            "price_per_night": 1450,
            "total_price": 4350,
            "checking": checking_date,
            "checkout": checkout_date,
        },
        {
            "name": "City Center Lodge",
            "location": "Downtown",
            "stars": 3,
            "price_per_night": 950,
            "total_price": 2850,
            "checking": checking_date,
            "checkout": checkout_date,
        }
    ]
    return dummy_hotels

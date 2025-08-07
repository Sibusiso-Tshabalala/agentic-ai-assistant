def save_trip_to_file(destination, days, interests, plan):
    try:
        with open("trip_data.txt", "w", encoding='utf-8') as file:
            file.write(f"Destination: {destination}\n")
            file.write(f"Days: {days}\n")
            file.write(f"Interests: {interests}\n\n")
            file.write("Trip Plan:\n")
            file.write(plan)
        return True
    except Exception as e:
        return str(e)

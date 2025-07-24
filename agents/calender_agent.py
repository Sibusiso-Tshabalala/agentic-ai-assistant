from api.calender_api import add_to_calendar

def calendar_agent(params):
    print("[Calendar Agent] Scheduling event...")
    event = add_to_calendar(params)
    return {"status": "success", "calendar_event": event, **params}
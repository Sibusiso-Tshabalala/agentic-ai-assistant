from langgraph.graph import StateGraph
from agents.planner_agent import planner_agent
from agents.flight_agent import flight_agent
from agents.hotel_agent import hotel_agent
from agents.calender_agent import calendar_agent

def build_workflow():
    graph = StateGraph(   )
    graph.add_node("planner", planner_agent)
    graph.add_node("flight", flight_agent)
    graph.add_node("hotel", hotel_agent)
    graph.add_node("calendar", calendar_agent)

    graph.add_edge("planner", "flight")
    graph.add_edge("flight", "hotel")
    graph.add_edge("hotel", "calendar")
    graph.set_entry_point("planner")

    return graph

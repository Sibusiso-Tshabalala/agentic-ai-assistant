from core.langgraph_flow import build_workflow

if __name__ == "__main__":
    workflow = build_workflow()
    input_request = input("What do you want me to plan? ")
    result = workflow.run(input_request)
    print("🧠 Workflow Result:", result)

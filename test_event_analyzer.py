from ingestion.event_parser import load_windows_events
from engine.event_analyzer import analyze_event


events = load_windows_events(
    "sample_data/windows_events.json"
)

print("\n===== SECURITY EVENT ANALYSIS =====\n")

for event in events:
    result = analyze_event(event)

    print("Event ID:", result["event_id"])
    print("Event Type:", result["analysis"]["event_type"])
    print("Severity:", result["analysis"]["severity"])
    print("Meaning:", result["analysis"]["meaning"])
    print("-" * 50)
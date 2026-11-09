from ingestion.event_parser import load_windows_events
from engine.timeline import build_timeline


events = load_windows_events(
    "sample_data/windows_events.json"
)

timeline = build_timeline(events)

print("\n===== INCIDENT TIMELINE =====\n")

for event in timeline:
    print(
        event["timestamp"],
        "| Event ID:", event["event_id"],
        "| User:", event["username"],
        "| Description:", event["description"]
    )
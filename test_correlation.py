from ingestion.event_parser import load_windows_events
from engine.correlation import correlate_events

events = load_windows_events(
    "sample_data/windows_events.json"
)

findings = correlate_events(events)

print("\n===== INCIDENT CORRELATION RESULTS =====\n")

for finding in findings:
    print(finding)
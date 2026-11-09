from ingestion.event_parser import load_windows_events
from engine.correlation import correlate_events
from engine.confidence import calculate_confidence

events = load_windows_events(
    "sample_data/windows_events.json"
)

findings = correlate_events(events)

result = calculate_confidence(findings)

print("\n===== EVIDENCE CONFIDENCE REPORT =====\n")
print(result)
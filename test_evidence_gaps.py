from ingestion.event_parser import load_windows_events
from engine.evidence_gaps import detect_evidence_gaps

events = load_windows_events(
    "sample_data/windows_events.json"
)

result = detect_evidence_gaps(events)

print("\n===== INVESTIGATION EVIDENCE GAPS =====\n")
print("Available:", result["available_evidence"])
print("Missing:", result["missing_evidence"])
print("Warning:", result["warning"])
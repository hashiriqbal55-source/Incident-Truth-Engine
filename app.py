import streamlit as st
import pandas as pd

from ingestion.event_parser import load_windows_events
from engine.timeline import build_timeline
from engine.event_analyzer import analyze_event
from engine.correlation import correlate_events
from engine.confidence import calculate_confidence
from engine.evidence_gaps import detect_evidence_gaps
from evidence.verify_integrity import verify_evidence


st.set_page_config(
    page_title="Incident Truth Engine",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Incident Truth Engine")
st.caption("Evidence-driven Digital Forensics and Incident Reconstruction")

st.sidebar.header("Investigation")
case_id = st.sidebar.text_input("Case ID", "CASE-001")

if st.button("Run Incident Investigation", type="primary"):

    try:
        events = load_windows_events(
            "sample_data/windows_events.json"
        )

        timeline = build_timeline(events)

        findings = correlate_events(events)

        confidence = calculate_confidence(findings)

        gaps = detect_evidence_gaps(events)

        integrity = verify_evidence(
            "evidence/sample_evidence.txt",
            "evidence/evidence_manifest.json"
        )

        analyzed_events = [
            analyze_event(event) for event in events
        ]

        st.success("Investigation completed successfully!")

        st.subheader("Investigation Overview")

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Events", len(events))
        col2.metric("Findings", len(findings))
        col3.metric(
            "Signal Score",
            f"{confidence['confidence_score']}/100"
        )

        st.subheader("Evidence Confidence / Signal Assessment")
        st.write("Level:", confidence["confidence_level"])
        st.write("Reasons:", confidence.get("reasons", []))
        st.caption(
            "This is a heuristic signal score, not a probability "
            "that an attack occurred."
        )

        st.subheader("Incident Timeline")
        st.dataframe(
            pd.DataFrame(timeline),
            use_container_width=True
        )

        st.subheader("Security Event Analysis")
        for event in analyzed_events:
            st.write(
                f"Event ID: {event['event_id']} | "
                f"Type: {event['analysis']['event_type']} | "
                f"Severity: {event['analysis']['severity']}"
            )

        st.subheader("Incident Correlation Findings")
        st.json(findings)

        st.subheader("Investigation Evidence Gaps")
        st.write("Available:", gaps["available_evidence"])
        st.write("Missing:", gaps["missing_evidence"])
        st.warning(gaps["warning"])

        st.subheader("Evidence Integrity Verification")
        st.json(integrity)

        report = {
            "case_id": case_id,
            "total_events": len(events),
            "timeline": timeline,
            "findings": findings,
            "signal_assessment": confidence,
            "evidence_gaps": gaps,
            "integrity": integrity
        }

        st.download_button(
            "Download Investigation Report (JSON)",
            data=__import__("json").dumps(
                report, indent=4
            ),
            file_name=f"{case_id}_investigation_report.json",
            mime="application/json"
        )

    except Exception as error:
        st.error(f"Investigation error: {error}")
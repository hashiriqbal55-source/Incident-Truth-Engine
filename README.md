# Incident Truth Engine

**Evidence-driven digital forensics and incident reconstruction using Python.**

Incident Truth Engine is a small, modular cybersecurity investigation prototype. It ingests supplied Windows Security Event Log data, normalizes events, builds a chronological timeline, applies basic event-analysis and correlation rules, highlights evidence gaps, calculates a heuristic signal score, and checks the integrity of a sample evidence file using SHA-256.

The project includes a Streamlit dashboard and a JSON report export.

> **Important scope note:** This is a learning/portfolio prototype that processes the supplied sample JSON dataset. The included events and evidence are synthetic. It is not a production forensic platform, SIEM replacement, automated malware detector, or proof that an incident occurred.

## Features

- **Event ingestion:** loads Windows event records from JSON and normalizes common fields.
- **Event interpretation:** recognizes Windows Security Event IDs `4624` (successful logon), `4625` (failed logon), and `4688` (process creation).
- **Correlation rules:** flags three or more failed logons for the same username, mixed successful/failed logon activity, and process-creation activity.
- **Timeline reconstruction:** sorts normalized events by timestamp.
- **Heuristic signal assessment:** calculates a rule-based score from generated findings and assigns a confidence label.
- **Evidence-gap review:** compares supplied evidence sources with a small expected-source list.
- **Evidence integrity:** calculates and verifies a SHA-256 hash against a saved manifest.
- **Chain of custody:** appends a timestamped JSON Lines record for an evidence-handling action.
- **Dashboard and export:** presents the investigation in Streamlit and allows the report to be downloaded as JSON.

## Technology

- Python 3
- Streamlit
- pandas
- JSON / JSON Lines
- SHA-256 (`hashlib`)
- Python standard library (`datetime`, `collections`, `json`, `os`)

## Repository structure

```text
Incident-Truth-Engine/
├── app.py
├── ingestion/
│   └── event_parser.py
├── engine/
│   ├── confidence.py
│   ├── correlation.py
│   ├── event_analyzer.py
│   ├── evidence_gaps.py
│   └── timeline.py
├── evidence/
│   ├── chain_of_custody.jsonl
│   ├── chain_of_custody.py
│   ├── evidence_manifest.json
│   ├── hashing.py
│   ├── manifest.py
│   ├── sample_evidence.txt
│   └── verify_integrity.py
├── sample_data/
│   └── windows_events.json
├── docs/
│   ├── RESUME-PROJECT-DESCRIPTION.md
│   └── TECHNICAL-OVERVIEW.md
├── test_*.py
├── requirements.txt
└── README.md
```

## Run locally

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Incident-Truth-Engine
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Launch the dashboard

```bash
streamlit run app.py
```

Streamlit will print a local URL (usually `http://localhost:8501`). Open it in your browser and select **Run Incident Investigation**.

## Run the included checks

The original project contains standalone Python check scripts rather than tests built with `pytest` or `unittest`. Run them from the repository root:

```bash
python test_event_analyzer.py
python test_correlation.py
python test_confidence.py
python test_evidence_gaps.py
python test_timeline.py
python test_hash.py
```

These scripts exercise the sample dataset and print results to the terminal. They do not provide comprehensive automated coverage.

## Investigation workflow

1. Load the supplied Windows event JSON file.
2. Normalize event fields into a consistent internal structure.
3. Build a timestamp-ordered event timeline.
4. Analyze each event using the currently supported event-ID rules.
5. Correlate events using the project's basic detection rules.
6. Calculate a heuristic signal score from the findings.
7. list expected evidence sources that are absent from the supplied dataset.
8. Verify the sample evidence file against its SHA-256 manifest.
9. Display the results and offer a JSON report download.

See [Technical Overview](docs/TECHNICAL-OVERVIEW.md) for module responsibilities and [Resume Project Description](docs/RESUME-PROJECT-DESCRIPTION.md) for concise resume wording.

## Current limitations and responsible interpretation

- The dashboard currently reads fixed sample paths; it does not yet provide an upload workflow for arbitrary evidence files.
- Only three Windows event IDs are interpreted by explicit rules.
- The failed-logon rule uses a simple threshold of three events per username; it does not evaluate time windows, source IPs, logon types, or account context.
- The confidence score is a heuristic signal score, not a statistical probability or calibrated confidence measure.
- The evidence-source comparison is a basic presence/absence check. Missing evidence means it was not supplied to this run; it does not establish that activity did not happen.
- The SHA-256 check detects a mismatch against the stored manifest, but the manifest itself is not digitally signed or stored in an independently protected location.
- The chain-of-custody function appends records to a local JSONL file; it does not enforce authenticated identities, access controls, or tamper-proof storage.
- The sample data is synthetic and must not be represented as a real-world incident investigation.

## Potential future enhancements

- Add file upload and validation for event logs and evidence.
- Add unit tests with `pytest`, fixtures, and edge-case coverage.
- Add detection rules for source IP, logon type, account, host, and time-window context.
- Support EVTX parsing and additional telemetry sources.
- Add report metadata, analyst notes, and case-level evidence linking.
- Protect manifests and custody records with signatures and access-controlled storage.
- Add configurable rule thresholds and explainable rule results.

## Portfolio use

This project can demonstrate practical exposure to Python scripting, Windows security-event interpretation, basic event correlation, timeline reconstruction, evidence integrity concepts, and investigation reporting. Describe it as a **personal/lab project** unless it was completed in a professional environment.


**Chapter 1 — CyberTriageX**  
Based on: SIH1744 — Cyber triage tool for digital forensic investigation  
Skills Required: Digital forensics, Ethical hacking, VAPT, Python, Linux basics  

***

**Project Description**  
CyberTriageX is a hybrid DFIR + VAPT toolkit for rapid triage of suspected-compromised systems. It automates evidence collection, timeline construction, artifact parsing, basic memory and disk triage, and produces prioritized findings with suggested mitigations. An optional agentless vulnerability-scan module correlates detected vulnerabilities with compromise evidence.

**Tech Stack & Tools**  
-  Python (scripting, parsing)  
-  SleuthKit/Autopsy, Volatility (memory analysis)  
-  Plaso/Log2timeline (timeline construction)  
-  YARA (file-indicator scanning)  
-  Elasticsearch or SQLite (search & storage)  
-  Flask or FastAPI + React (dashboard UI)  
-  Nmap/OpenVAS (optional vulnerability correlation)  

***

## Week-Wise Roadmap (4 Weeks)

**Week 1 — Foundations & Evidence Collection**  
- Provision lab environment: create sanitized VM snapshots (Windows 10 and Ubuntu20.04).  
- Develop `collect.py` to gather:  
  -  System info (hostname, users, installed software)  
  -  Running processes and services  
  -  Autorun entries (registry keys, systemd units)  
  -  Network connections (netstat/lsof)  
  -  System logs (Windows Event Logs, /var/log)  
  -  Browser artifacts (history, cookies)  
- Export all artifacts into a timestamped JSON + tarball.  
- **Deliverable**: `collect.py` script + sample artifact bundle.

**Week 2 — Parsing & Timeline Generation**  
- Integrate Plaso or build custom parsers to extract timestamps from:  
  -  File metadata (MFT, inodes)  
  -  Event logs  
  -  Browser histories  
- Construct timeline generator producing CSV and a static HTML viewer.  
- Normalize parsed events into Elasticsearch or SQLite schema.  
- **Deliverable**: `timeline.py` + `timeline.html` viewer with zoom & filter.

**Week 3 — Memory & Disk Analysis + Correlation**  
- Integrate Volatility plugins for:  
  -  Process listing & hidden processes  
  -  Network socket analysis  
  -  Injected DLL detection  
- Run YARA rules against collected files for IOCs.  
- If vulnerability module is used: trigger Nmap/OpenVAS scan on target VM and ingest results.  
- Correlate exploitation artifacts (e.g., suspicious DLLs) with known CVEs from scan results.  
- **Deliverable**: `correlate.py` producing JSON report with scored findings.

**Week 4 — Dashboard & Reporting**  
- Build REST API (FastAPI) exposing case creation, artifact search, timeline, and correlation endpoints.  
- Develop React dashboard enabling:  
  -  New case initialization (upload bundle)  
  -  Artifact list and timeline view  
  -  Priority-scored findings table with remediation suggestions  
- Implement PDF AAR (After Action Report) generator using Jinja2 templates.  
- Package entire solution as Docker containers (collector, parser, analysis, UI).  
- **Deliverable**: Full demo showing end-to-end triage; sample PDF report.

***

## Testing & Final Deliverables

- Deploy demo VM with seeded compromise indicators.  
- Run `collect.py`, timeline and correlation modules, then view dashboard.  
- **Deliverables**:  
  -  Code repository with modular Python packages  
  -  Demo VM snapshot (sanitized)  
  -  Sample PDF AAR  
  -  Short video walkthrough (5-minute demo)  

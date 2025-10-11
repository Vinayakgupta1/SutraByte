### Chapter 8 — VulneraX  
**Based on:** SIH1684 — Agentless Vulnerability Scanner (NTRO)  
**Skills required:** VAPT, Network scanning, Python scripting, Security automation, Kali Linux  

***

#### Project Description  
VulneraX is an advanced agentless vulnerability scanner designed for rapid and scalable vulnerability detection across large networks. It builds on core network discovery and service fingerprinting, adding features like parallel scanning, differential detection, and integration with vulnerability databases. The tool automates vulnerability identification with minimal manual intervention and provides detailed, prioritized reports for security teams.

***

#### Tech Stack & Tools  
- Python (scan orchestration and scripting)  
- Nmap for network discovery and scanning  
- OpenVAS or alternative open-source vulnerability scanners  
- Elasticsearch or SQLite for storage and reporting  
- Flask/FastAPI for API backend  
- React or Vue for frontend dashboard  
- Kali Linux environment for testing and development  

***

#### Week-wise Roadmap (8 Weeks)

**Week 1 — Development Environment Setup & Network Discovery**  
- Set up Kali Linux and development tools.  
- Implement network host discovery and port scanning using Nmap.  
- Build host and service inventory management.  
- **Deliverable:** Network discovery tool producing inventory lists.

**Week 2 — Vulnerability Detection Module**  
- Integrate vulnerability data sources (NVD, CVE databases).  
- Map detected services to known vulnerabilities.  
- Develop vulnerability scanning orchestration with OpenVAS or other tools.  
- **Deliverable:** Vulnerability detection and mapping module.

**Week 3 — Parallel Scanning & Scheduling**  
- Enhance scanner with parallelism for faster scans against large asset pools.  
- Develop scheduled scan management and scan queueing.  
- **Deliverable:** Parallel scan engine with task scheduling.

**Week 4 — Differential Scan & Change Detection**  
- Implement differential scanning logic to detect new vulnerabilities or misconfigurations.  
- Build baseline snapshot capture and comparison features.  
- **Deliverable:** Differential scanner for change monitoring.

**Week 5 — Report Generation & Dashboard**  
- Develop backend reporting engine aggregating vulnerability data.  
- Build frontend dashboard for visualization of findings and risk prioritization.  
- **Deliverable:** Initial reporting module and dashboard UI.

**Week 6 — User Access & Role Management**  
- Integrate authentication and role-based access control.  
- Provide user management features and secure API access.  
- **Deliverable:** RBAC-enabled user management system.

**Week 7 — Integration & Notification System**  
- Add integrations for notification systems (email, Slack).  
- Enable export of vulnerability reports via API.  
- Implement webhook support for automation pipelines.  
- **Deliverable:** Notification and export features.

**Week 8 — Final Testing & Documentation**  
- Conduct comprehensive testing against known vulnerable environments.  
- Refine UI/UX and performance tuning.  
- Prepare user guides, developer documentation, and demo materials.  
- **Deliverable:** Complete tested system with documentation and demo.

***

#### Testing & Deliverables  
- Create VM lab with vulnerable targets (e.g., Metasploitable).  
- Validate scan accuracy, speed, and false positive rates.  
- Deliver source code repo, documented API, UI assets, and demo videos.

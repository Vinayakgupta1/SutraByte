# ✅ **Chapter 16: AI-Driven SOC Lab — Build Your Own AI-Augmented SOC Environment**

### *A complete hands-on guide to creating a personal AI-powered Security Operations Center at home*

---

# 📌 **Introduction**

Modern SOCs are no longer human-only.
They use:

* SIEM + AI
* EDR with behavioural ML
* Threat Intel + LLMs
* Automated IR playbooks (SOAR)
* Network anomaly detection (NDR AI)

But most students never get access to real SOC tools.
This chapter solves that by teaching you how to build a **fully working AI-powered SOC lab** using:

* free tools
* open-source ML models
* cloud-free setups
* your laptop or VM

This lab gives you:
✔ hands-on experience
✔ real logs and alerts
✔ AI-assisted investigation
✔ SOC automation workflows
✔ projects for your resume

Let’s build it step by step.

---

# 🧩 **1. SOC Lab Architecture (Simple Diagram)**

```
               +-------------------------+
               |   Attack Simulation     |
               |  (Caldera / AtomicRed) |
               +------------+------------+
                            |
                   Security Data Pipeline
                            |
        +-------------------+-----------------------+
        |                                           |
+-------v-------+                           +-------v-------+
|   Wazuh SIEM  | <-- Logs, Alerts -------> | Zeek NDR AI  |
+-------+-------+                           +-------+-------+
        |                                           |
        |                              ML Models (Anomaly, RF)
        |                                           |
+-------v-------+                           +-------v-------+
|  Shuffle SOAR | <------ AI Decisions ---- | LLM Assistant |
+---------------+                           +---------------+
```

This SOC includes:

* SIEM (Wazuh)
* NDR (Zeek ML)
* SOAR (Shuffle)
* LLM Assistant (ChatGPT locally or API)
* Attack tools (Caldera, Atomic Red Team)

---

# 🔧 **2. Tools You Will Use (All Free)**

## **1. Wazuh (SIEM + EDR Agent)**

Collects:

* system logs
* authentication logs
* file integrity events
* security alerts

---

## **2. Zeek (Network Detection Tool)**

Monitors:

* network flows
* DNS anomalies
* scans
* unusual behaviour

---

## **3. Shuffle SOAR**

Automates:

* alert triage
* enrichment
* response
* blocking actions

---

## **4. MITRE Caldera (Adversary Simulation)**

Generates friendly attacks:

* privilege escalation
* lateral movement
* credential theft

---

## **5. Atomic Red Team (TTP Testing)**

Runs individual tactics from MITRE ATT&CK.

---

## **6. LLM Assistant (Optional but recommended)**

Use:

* ChatGPT
* LM Studio + Llama
* Local Ollama

To generate:

* summaries
* IR recommendations
* Sigma rules
* detection logic

---

# 🏗️ **3. Step-by-Step Lab Setup Guide**

Below is the **exact setup** used by SOC teams for training.

---

## 🔹 **Step 1 — Install Wazuh (SIEM/EDR)**

### Option A: Use Wazuh Docker (recommended)

```bash
git clone https://github.com/wazuh/wazuh-docker
cd wazuh-docker
docker-compose up -d
```

Components installed:

* Wazuh Manager
* Wazuh Indexer
* Wazuh Dashboard

Access dashboard at:

```
https://localhost:5601
```

---

## 🔹 **Step 2 — Deploy Wazuh Agents**

Install agent on:

* Windows VM
* Linux VM
* Kali attack machine

Example:

```bash
curl -s https://packages.wazuh.com/install.sh | bash
```

Agent logs will now flow to the SIEM.

---

## 🔹 **Step 3 — Install Zeek for Network Monitoring**

Deploy Zeek on:

* Ubuntu VM
* Security gateway
* Proxmox / ESXi VM

Commands:

```bash
sudo apt install cmake make gcc g++ flex bison libpcap-dev python3
git clone --recursive https://github.com/zeek/zeek
cd zeek
./configure && make && sudo make install
```

Start Zeek:

```bash
sudo zeekctl deploy
```

Zeek generates:

* conn.log
* dns.log
* http.log
* weird.log (suspicious behaviour)

---

## 🔹 **Step 4 — Add ML to Zeek (Anomaly Detection)**

Install the **ML plugin for Zeek**:

```bash
git clone https://github.com/zeek/spicy-ml
```

This enables:

* behavioural anomaly detection
* DNS tunneling detection
* flow classification

---

## 🔹 **Step 5 — Install Shuffle SOAR**

Run Shuffle via Docker:

```bash
docker run -d -p 3001:3001 frikky/shuffle:latest
```

Access:

```
http://localhost:3001
```

In Shuffle, integrate:

* Wazuh API
* VirusTotal
* AbuseIPDB
* LLM Webhook

---

## 🔹 **Step 6 — Add LLM Assistant (Optional but powerful)**

You can use:

* ChatGPT API
* Claude API
* LM Studio (local)
* Ollama (local Llama)

Integrate via:

* Shuffle Webhook
* Python script
* Simple REST API

Now alerts can be sent to LLM → summarized → returned to SOAR.

---

## 🔹 **Step 7 — Install MITRE Caldera (Attack Simulation)**

```bash
git clone https://github.com/mitre/caldera
cd caldera
pip3 install -r requirements.txt
python3 server.py --insecure
```

Use Caldera to simulate:

* privilege escalation
* lateral movement
* credential extraction

These events will hit Wazuh + Zeek.

---

## 🔹 **Step 8 — Install Atomic Red Team**

```bash
git clone https://github.com/redcanaryco/atomic-red-team
```

Run specific ATT&CK tests:

```bash
Invoke-AtomicTest T1059
```

This generates realistic attack logs.

---

# 🔥 **4. Building the AI-Driven SOC Workflow**

Let’s design your alert flow.

---

## **Step A: Log Collection (Wazuh + Zeek)**

Wazuh collects:

* authentication logs
* Windows event logs
* file integrity alerts
* EDR behaviour logs

Zeek collects:

* DNS
* network flows
* HTTP
* SSL fingerprints

Together: 360° visibility.

---

## **Step B: AI Detection**

### AI models process:

* anomalies (Isolation Forest)
* clustering (DBSCAN)
* behaviour scoring

Add ML jobs using:

```python
from sklearn.ensemble import IsolationForest
```

Use Zeek logs as input.

---

## **Step C: SOAR Automation (Shuffle)**

Create playbooks:

* If malicious IP → auto block
* If suspicious PowerShell → isolate endpoint
* If login anomaly → disable user
* If ransomware detected → stop processes

Shuffle uses:

* triggers
* logic blocks
* enrichment steps
* responses

---

## **Step D: LLM-Assisted Alert Triage**

When Wazuh sends an alert:

1. Shuffle forwards it to LLM
2. LLM evaluates:

   * severity
   * threat behaviour
   * ATT&CK mapping
   * recommended actions
3. Shuffle parses LLM output
4. Executes automatic containment

Sample LLM prompt:

```
You are a SOC analyst.
Analyze this alert and map it to MITRE ATT&CK.
Provide severity and response steps.
Alert:
<alert JSON>
```

---

# 🕵️‍♂️ **5. SOC Attack Simulation (Red Team Testing)**

Use Caldera + Atomic Red Team.

### Example Attacks:

* Brute force (T1110)
* PowerShell malicious commands (T1059)
* Credential dumping (T1003)
* Lateral movement (T1021)

Logs flow into SIEM → ML detects anomalies → SOAR responds.

---

# 📊 **6. Visualizing Alerts & Dashboards**

Use Wazuh dashboard to see:

* attack timelines
* MITRE coverage
* endpoint alerts
* network events

Use Grafana + Zeek logs for:

* DNS anomalies
* cryptomining traffic
* botnet C2 patterns

---

# 🧪 **7. Hands-On Student Projects (Portfolio Ready)**

Here are projects you can publish:

---

### **Project 1: Build an ML-Based Anomaly Detector Using Zeek Logs**

Model: Isolation Forest
Input: conn.log
Output: suspicious flows

---

### **Project 2: Automated SOC Playbook (Shuffle SOAR)**

Example playbook:

* detect brute force
* enrich with VirusTotal
* auto-lock account

---

### **Project 3: LLM-Powered SOC Assistant**

Build a system that:

* summarizes alerts
* creates reports
* maps ATT&CK TTPs

---

### **Project 4: MITRE Red Team Attack Simulation Lab**

Run:

* T1059
* T1003
* T1021
  Analyze SIEM results.

---

### **Project 5: Cloud Attack Detection (Optional add-on)**

Feed AWS CloudTrail logs → Wazuh → ML scoring.

---

# 🛡️ **8. What Students Learn from This SOC Lab**

You gain experience in:

* SIEM
* NDR
* EDR
* SOAR automation
* LLM-driven triage
* ML anomaly detection
* threat intel
* MITRE ATT&CK

These skills are exactly what companies expect in:

* SOC Analyst
* Threat Hunter
* Red Team Intern
* Cloud Security Analyst
* Detection Engineer

---

# 📌 **Key Takeaways**

* You can build a real SOC with SIEM, EDR, NDR, SOAR, and AI on your laptop.
* AI helps analyze, triage, and respond to security events automatically.
* Zeek + Wazuh + Shuffle + LLM is a powerful open-source SOC stack.
* MITRE Caldera and Atomic Red Team let you simulate real attacks safely.
* This lab gives students hands-on, job-ready experience in modern defensive cybersecurity.

---
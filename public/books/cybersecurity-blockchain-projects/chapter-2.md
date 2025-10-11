### Chapter 2 — ShieldCloud  
**Based on:** SIH1649 — DDoS Protection for Cloud (Ministry of Defence)  
**Skills required:** Cybersecurity fundamentals, Network traffic analysis, Machine learning, Cloud computing, Python, Linux basics  

***

#### Project Description  
ShieldCloud is an AI-powered DDoS detection and mitigation system designed for cloud infrastructure. It continuously monitors network traffic patterns using scalable data ingestion pipelines and leverages machine learning to identify and differentiate legitimate traffic from attack traffic in real time. The system automatically triggers mitigation actions such as rate limiting, BGP blackholing, or firewall updates to maintain service availability. The dashboard provides operators with live traffic visualization, alerts, and incident response tools.

***

#### Tech Stack & Tools  
- Python (for data ingestion, ML models)  
- Kafka (real-time streaming ingestion)  
- Apache Flink/Spark (stream processing and feature extraction)  
- TensorFlow or PyTorch (machine learning models)  
- eBPF / iptables (mitigation enforcement)  
- Grafana/Prometheus (monitoring and dashboards)  
- Cloud APIs (AWS/GCP/Azure mitigation hooks)

***

#### Week-wise Roadmap (9 Weeks)  

**Week 1 — Setup and Data Collection**  
- Setup cloud lab environment: VMs/containers simulating cloud network traffic.  
- Implement network traffic capture utilising packet capture tools or flow exporters (sFlow/NetFlow).  
- Build Kafka ingestion pipeline for real-time traffic streaming.  
- **Deliverable:** Streaming pipeline ingesting real-time emulated network flow data.

**Week 2 — Feature Engineering**  
- Extract key traffic features: packet rate, byte rate, entropy measures, protocol distribution, SYN/ACK ratios.  
- Establish baseline traffic profiles and thresholds.  
- Build feature extraction module using Apache Flink or Spark.  
- **Deliverable:** Feature extraction pipeline with visualizations showing baseline traffic metrics.

**Week 3 — Machine Learning Model Development**  
- Develop anomaly detection ML models (Isolation Forest, LSTM, Autoencoders).  
- Train models on normal and simulated attack traffic.  
- Evaluate model accuracy, precision, recall.  
- **Deliverable:** Trained ML models and evaluation report.

**Week 4 — Automated Mitigation Framework**  
- Design automated response system integrating ML results with mitigation actions.  
- Implement mitigation policies including iptables rate limiting, BGP blackholing, or cloud firewall updates.  
- Build mitigation decision engine.  
- **Deliverable:** Working mitigation playbook triggered by ML alerts.

**Week 5 — WAF and False Positive Management**  
- Integrate Web Application Firewall configurations to block common attack patterns.  
- Develop false positive reduction heuristics and whitelist management.  
- Monitor and refine detection thresholds for production readiness.  
- **Deliverable:** Stable WAF ruleset and false positive management system.

**Week 6 — Real-time Dashboard and Alerting**  
- Build Grafana dashboards for traffic and alert monitoring.  
- Implement alert management and notification system for security operators.  
- Include incident logging and audit trails.  
- **Deliverable:** Interactive dashboard with real-time traffic and alert views.

**Week 7 — Stress Testing and Simulation**  
- Simulate various DDoS attack vectors to test detection and mitigation efficacy (SYN flood, UDP flood, HTTP flood).  
- Measure mitigation latency and system resilience.  
- Refine parameters and failover mechanisms.  
- **Deliverable:** Stress testing reports and system tuning adjustments.

**Week 8 — Deployment and Scaling**  
- Containerize components with Docker and orchestrate via Kubernetes for scalability.  
- Implement load balancing and horizontal scaling for streaming and ML inference modules.  
- Establish monitoring on scaling behaviors.  
- **Deliverable:** Scalable ShieldCloud deployment with documentation.

**Week 9 — Documentation and Final Testing**  
- Prepare comprehensive user manuals, runbooks, and deployment guides.  
- Conduct bug fixes and integration testing across all modules.  
- Provide final demo with simulated attack and operator response.  
- **Deliverable:** Final product documentation and demo video.

***

#### Testing and Deliverables  
- Deploy ShieldCloud in a controlled cloud lab environment.  
- Validate detection accuracy against known DDoS datasets.  
- Document performance metrics including detection latency and mitigation effectiveness.  
- Deliver full source code, deployment scripts, training datasets, architecture documentation, and demonstration records.

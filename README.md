
# Security Log Analysis & Incident Detection

## Overview
This project simulates the work of a cybersecurity analyst reviewing authentication logs to identify suspicious access patterns, indicators of compromise (IOCs), and potential account takeover activity. The analysis focuses on failed login behavior, targeted accounts, and high-risk authentication sequences commonly investigated in SOC and cyber risk roles.

---

## Key Files
- **Notebook (Analysis):** `analysis/log_analysis.ipynb`  
- **Rendered Notebook (HTML):** `analysis/log_analysis.html`  
- **Incident Report:** `reports/incident_summary.md`  
- **Log Generator Script:** `generate_logs.py`  
- **Dataset:** `data/auth_logs.csv`

---

## Dataset
Synthetic authentication logs generated for analysis, including:
- `timestamp`
- `username`
- `source_ip`
- `location`
- `device`
- `event_type` (SUCCESS / FAILED)

The dataset includes injected attack patterns to simulate real-world brute-force behavior.

---

## Analysis Performed
- Reviewed authentication activity to establish baseline behavior
- Identified IP addresses with excessive failed login attempts
- Analyzed targeted user accounts and privilege risk
- Detected high-risk patterns where a successful login followed repeated failures
- Visualized failed login activity over time to identify attack windows

---

## Key Findings
- A single external IP generated a high volume of failed login attempts
- A privileged account (`admin`) was repeatedly targeted
- A successful authentication occurred after multiple failed attempts, indicating a potential brute-force compromise
- Login activity originated from unusual locations and device fingerprints

---

## Incident Summary
Findings were documented in a formal incident report that includes:
- Indicators of Compromise (IOCs)
- Risk assessment and potential impact
- Recommended mitigations such as MFA enforcement, rate limiting, and alerting controls

See: `reports/incident_summary.md`

---

## Tools & Technologies
- Python (pandas, matplotlib)
- Jupyter Notebook
- Markdown documentation
- Git & GitHub

---

## Cybersecurity Relevance
Log analysis and incident documentation are foundational skills for SOC, cybersecurity risk, and fraud investigation roles. This project demonstrates the ability to analyze raw security telemetry, identify meaningful risk signals, and communicate findings with actionable mitigation recommendations.

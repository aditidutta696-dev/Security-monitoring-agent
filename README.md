"# Security-monitoring-agent" 
# 🛡️ AI Cyber-Agent SOC: Intelligent Log Analysis Pipeline

An automated Security Operations Center (SOC) system designed to process high-volume logs, identify brute-force attacks, and generate deduplicated security conclusions.

## 🌟 The Problem
Security analysts often face "Log Fatigue"—sifting through thousands of repetitive log entries to find a single threat. Manually inspecting 1,000+ logs to identify unique attackers is slow and prone to error.

## 🚀 The Solution
This project implements a multi-agent pipeline that:
1.  **Standardizes** varied log formats.
2.  **Compresses** repetitive data to reduce noise.
3.  **Analyzes** behavior in batches to identify threshold-crossing threats.
4.  **Reports** only the unique security conclusions, providing a clear "Verdict" and "Audit Trail."

---

## 🛠️ System Architecture

### 1. Log Analyzer Agent (`log_analyzer.py`)
Acts as the first line of defense. It normalizes incoming raw JSON data into a consistent format (Source IP, Action, Timestamp) while preparing it for high-speed inspection.

### 2. Threat Detector Agent (`threat_detector.py`)
The "brain" of the operation. It tracks login failure counts per IP address. Once a threshold (e.g., 5 failures) is met, it triggers a permanent block and generates a single, unique incident report.

### 3. FastAPI Coordinator (`main.py`)
The central hub that provides a REST API endpoint (`/ingest`). It orchestrates the flow of data between agents and returns a clean, non-hectic JSON summary to the user.
| Component | Responsibility | Key Logic |
| :--- | :--- | :--- |
| **main.py** | API Orchestration | Coordinates the handover between agents. |
| **log_analyzer.py** | Log Compression | Standardizes diverse keys (e.g., `ip` vs `src`). |
| **threat_detector.py** | Pattern Recognition | Stateful counting and unique incident filtering. |
| **Playbooks** | Automated Response | Maps threat types to specific firewall/ticketing actions. |
---

## 📊 Sample Conclusion Output
Instead of 1,000 logs, the user receives this:

```json
{
    "status": "Analysis Complete",
    "metadata": { "total_logs_analyzed": 1000, "unique_threats_found": 1 },
    "security_conclusions": [
        {
            "ip": "45.33.22.11",
            "incident": "Brute Force Attack",
            "reason": "Detected 5 failed attempts",
            "blocked_at": "2026-02-08 01:38:09",
            "verdict": "IP_PERMANENTLY_BLOCKED"
        }
    ]
}

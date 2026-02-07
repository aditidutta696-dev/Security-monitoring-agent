class ThreatDetectorAgent:
    def __init__(self):
        self.failure_counts = {}
        self.blocked_ips = set()

    def check_for_threats(self, normalized_logs):
        conclusions = []
        
        for log in normalized_logs:
            ip = log.get("src")
            action = log.get("act")
            timestamp = log.get("time")

            if action == "login_failed":
                self.failure_counts[ip] = self.failure_counts.get(ip, 0) + 1
                count = self.failure_counts[ip]

                # Lowering threshold to 3 to catch "stealthier" attackers
                if count >= 3 and ip not in self.blocked_ips:
                    self.blocked_ips.add(ip)
                    
                    # Calculate Risk Score (Simple logic: more attempts = higher risk)
                    risk_score = min(count * 2, 10) 
                    
                    conclusions.append({
                        "ip": ip,
                        "incident": "Brute Force Attack",
                        "count_at_block": count,
                        "risk_score": f"{risk_score}/10",
                        "blocked_at": timestamp,
                        "verdict": "IP_PERMANENTLY_BLOCKED"
                    })
        
        return conclusions
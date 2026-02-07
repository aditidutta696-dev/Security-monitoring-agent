import json
import random
from datetime import datetime, timedelta

def generate_test_data():
    logs = []
    start_time = datetime.now()
    
    # 4 Specific Attacker IPs
    attackers = [
        "192.168.1.50",   # Brute Force 1
        "10.0.0.15",      # Brute Force 2
        "45.33.22.11",    # Brute Force 3
        "172.16.0.5"      # Brute Force 4
    ]
    
    # Generate 1000 logs
    for i in range(1000):
        current_time = (start_time + timedelta(seconds=i)).strftime("%Y-%m-%d %H:%M:%S")
        
        # Every 10th log is an attack from one of the 4 attackers
        if i % 10 == 0 and len(attackers) > 0:
            attacker_ip = random.choice(attackers)
            logs.append({
                "time": current_time,
                "src": attacker_ip,
                "act": "login_failed",
                "lvl": "WARNING"
            })
        else:
            # Normal background traffic noise
            logs.append({
                "time": current_time,
                "src": f"192.168.1.{random.randint(100, 200)}",
                "act": "login_success",
                "lvl": "INFO"
            })

    with open("attack_logs.json", "w") as f:
        json.dump(logs, f, indent=4)
    print("Successfully generated attack_logs.json with 1000 entries.")

generate_test_data()
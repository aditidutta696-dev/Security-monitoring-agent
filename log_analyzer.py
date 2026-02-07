import hashlib

class LogAnalyzerAgent:
    def __init__(self):
        self.seen_hashes = set()

    def scaledown_compress(self, raw_log):
        # We process every log to ensure the counter works, 
        # but we keep the normalization clean.
        return self.normalize(raw_log)

    def normalize(self, log):
        return {
            "src": log.get("src", "0.0.0.0"),
            "act": log.get("act", "unknown"),
            "time": log.get("time", "No Timestamp Found")
        }
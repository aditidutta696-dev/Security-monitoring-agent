from fastapi import FastAPI, Body, HTTPException
from log_analyzer import LogAnalyzerAgent
from threat_detector import ThreatDetectorAgent
import uvicorn

app = FastAPI(title="AI SOC Final Conclusion")
analyzer = LogAnalyzerAgent()
detector = ThreatDetectorAgent()

@app.post("/ingest")
async def ingest_logs(raw_data: list = Body(...)): 
    try:
        # 1. Standardize logs
        cleaned_logs = [analyzer.scaledown_compress(l) for l in raw_data if l]
        
        # 2. Extract unique security conclusions
        summary_report = detector.check_for_threats(cleaned_logs)
        
        # 3. Present the professional summary
        return {
            "status": "Analysis Complete",
            "metadata": {
                "total_logs_analyzed": len(raw_data),
                "unique_threats_found": len(summary_report)
            },
            "security_conclusions": summary_report
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis Error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
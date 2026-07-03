import re

class DataNormalizer:
    def __init__(self):
        # Simulated raw, dirty payload stream (unstructured system logs)
        self.raw_payload = [
            "  DATA_NODE_01 // ACTIVE // temp:98.4C // status:clean  ",
            "DATA_NODE_02 // SYSTEM_ERR // temp:102.1C // status:friction",
            "   DATA_NODE_03 // LATENCY_WARN // temp:88.7C // status:static  ",
            "INVALID_STREAM_RECORD_NULL"
        ]

    def execute_normalization(self):
        cleaned_records = []
        print("🔧 RUNNING STREAM NORMALIZATION PARSER...")
        
        for record in self.raw_payload:
            stripped = record.strip()
            # Drop invalid/corrupted packet lines
            if "INVALID" in stripped or not stripped:
                continue
                
            # Break down the raw text delimiters
            parts = [part.strip() for part in stripped.split("//")]
            
            # Extract key-value parameters via simple matching
            node_id = parts[0]
            metric_state = parts[1]
            temperature = parts[2].split(":")[1] if ":" in parts[2] else "N/A"
            
            # Map into a structured data matrix
            structured_log = {
                "node_id": node_id,
                "state": metric_state,
                "metrics": {"temp": temperature},
                "validated": True
            }
            cleaned_records.append(structured_log)
            print(f"✅ SECURED NODE: [{node_id}] -> State: {metric_state}")
            
        return cleaned_records
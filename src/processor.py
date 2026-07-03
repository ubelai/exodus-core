import os
import json

class DataNormalizer:
    def __init__(self, input_filename="raw_logs.txt", output_filename="clean_telemetry.json"):
        self.input_path = input_filename
        self.output_path = output_filename

    def execute_normalization(self):
        cleaned_records = []
        print(f"📂 OPENING INGRESS TIER: {self.input_path}")
        
        # Guardrail: Check if the file physically exists before opening
        if not os.path.exists(self.input_path):
            print(f"❌ CRITICAL: Ingress target file missing at {self.input_path}")
            return cleaned_records

        # Physical Disk Ingress Phase
        with open(self.input_path, "r", encoding="utf-8") as file:
            raw_lines = file.readlines()

        print(f"⚙️  PROCESSING STREAM: Ingested {len(raw_lines)} raw data rows from disk.")
        
        for line in raw_lines:
            stripped = line.strip()
            # Drop invalid/corrupted structural noise
            if "INVALID" in stripped or not stripped:
                print(f"⚠️  PURGING CORRUPTED PACKET: '{stripped}'")
                continue
                
            # Parse out the delimiters
            parts = [part.strip() for part in stripped.split("//")]
            
            node_id = parts[0]
            metric_state = parts[1]
            temperature = parts[2].split(":")[1] if ":" in parts[2] else "N/A"
            
            # Construct the formal data matrix
            structured_log = {
                "node_id": node_id,
                "state": metric_state,
                "metrics": {"temp": temperature},
                "validated": True
            }
            cleaned_records.append(structured_log)
            print(f"   ✅ SECURED NODE: [{node_id}] -> State: {metric_state}")
            
        # Physical Disk Egress Phase (Writing JSON file to drive)
        print(f"💾 DEPLOYING EGRESS TIER: Writing clean matrix to {self.output_path}")
        with open(self.output_path, "w", encoding="utf-8") as output_file:
            json.dump(cleaned_records, output_file, indent=4)
            
        return cleaned_records
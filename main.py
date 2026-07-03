import os
from dotenv import load_dotenv
from src.processor import DataNormalizer

def initialize_pipeline():
    load_dotenv()
    
    project_name = os.getenv("PROJECT_NAME")
    env_mode = os.getenv("ENV_MODE")
    core_version = os.getenv("CORE_VERSION")
    
    print("\n" + "—" * 40)
    print(f"📡 CORE ENGINE LAUNCH MATRIX")
    print(f"DEPLOYMENT INSTANCE: {project_name}")
    print(f"SYSTEM VERSION:      v{core_version}")
    print(f"RUNNING MODE:        [{env_mode.upper()}]")
    print("—" * 40 + "\n")
    
    # Fire the automated logic sub-routine
    normalizer = DataNormalizer()
    structured_output = normalizer.execute_normalization()
    
    print("\n" + "—" * 40)
    print(f"📊 PIPELINE INGRESS COMPLETED. TARGET ROWS SECURED: {len(structured_output)}")
    print("—" * 40 + "\n")

if __name__ == "__main__":
    initialize_pipeline()
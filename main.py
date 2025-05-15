from generator import generate_document
from pipeline import run_pipeline
import os

def main():
    print("[MAIN] Starting pipeline...")
    run_pipeline()
    
    print("[MAIN] Generating documentation...")
    doc = generate_document()

    with open("generated_doc.md", "w") as f:
        f.write(doc)

    print("[MAIN] Document saved to 'generated_doc.md'.")

if __name__ == "__main__":
    main()
